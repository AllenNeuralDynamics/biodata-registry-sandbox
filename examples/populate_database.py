import argparse
import json
from pathlib import Path
from typing import Any

import requests


BASE_URL = "http://localhost:5000"
SCHEMA_DIR = Path(__file__).resolve().parent / "schema_definitions"
RECORDS_PATH = Path(__file__).resolve().parent / "records" / "docdb_records.json"


def register(session: requests.Session, endpoint: str, **kwargs) -> None:
    response = session.post(f"{BASE_URL}{endpoint}", **kwargs)
    print(response.status_code)


def get(session: requests.Session, endpoint: str, **kwargs) -> Any:
    response = session.get(f"{BASE_URL}{endpoint}", **kwargs)
    response.raise_for_status()
    return response.json()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Populate aind-registry-sandbox with example records."
    )
    parser.add_argument(
        "--register-core-data",
        action="store_true",
        help=(
            "Also register users, organizations, spaces, collections, and "
            "non-subject schema metadata."
        ),
    )
    parser.add_argument(
        "--space-id",
        type=int,
        default=1,
        help="Space id to use when registering subjects.",
    )
    return parser.parse_args()


def load_schema(schema_filename: str) -> dict:
    with (SCHEMA_DIR / schema_filename).open("r", encoding="utf-8") as file:
        return json.load(file)


def load_docdb_records() -> list[dict[str, Any]]:
    with RECORDS_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_schema_id(
    session: requests.Session,
    schema_name: str,
    schema_filename: str,
) -> int:
    schema = load_schema(schema_filename)
    schema_version = schema["properties"]["schema_version"]["const"]
    schemas = get(session, "/schemas", params={"name": schema_name})

    for row in schemas:
        if (
            row["name"] == schema_name
            and row["version"] == schema_version
        ):
            return row["id"]

    raise ValueError(
        f"Could not find schema id for {schema_name} {schema_version}. "
        "Create schemas before registering records."
    )


def get_data_asset_id(
    session: requests.Session,
    *,
    location: str,
    name: str,
) -> int:
    data_assets = get(session, "/data_assets", params={"location": location})

    for row in data_assets:
        if row["location"] == location and row["name"] == name:
            return row["id"]

    raise ValueError(
        f"Could not find data asset for name={name} location={location}. "
        "Register data assets before acquisitions."
    )


def get_instrument_id(session: requests.Session, *, name: str) -> int:
    instruments = get(session, "/instruments", params={"name": name})

    for row in instruments:
        if row["name"] == name:
            return row["id"]

    raise ValueError(
        f"Could not find instrument for name={name}. "
        "Register instruments before acquisitions."
    )


def register_subjects(session: requests.Session, space_id: int = 1) -> None:
    subject_schema_id = get_schema_id(session, "subject", "subject_schema.json")
    records = load_docdb_records()
    unique_subjects: dict[str, dict[str, Any]] = {}

    for record in records:
        subject = record.get("subject")
        if not isinstance(subject, dict):
            continue

        subject_id = subject.get("subject_id")
        if not subject_id:
            continue

        unique_subjects.setdefault(str(subject_id), subject)

    for subject_id, subject in unique_subjects.items():
        existing_subjects = get(session, "/subjects", params={"name": subject_id})
        if existing_subjects:
            continue

        register(
            session,
            "/subjects",
            params={
                "schema_id": subject_schema_id,
                "space_id": space_id,
                "name": subject_id,
            },
            json=subject,
        )


def register_data_assets(session: requests.Session, space_id: int = 1) -> None:
    data_asset_schema_id = get_schema_id(
        session,
        "data_description",
        "data_description_schema.json",
    )
    records = load_docdb_records()
    unique_data_assets: dict[str, dict[str, Any]] = {}

    for record in records:
        data_description = record.get("data_description")
        if not isinstance(data_description, dict):
            continue

        location = record.get("location")
        name = record.get("name") or data_description.get("name")
        if not location or not name:
            continue

        unique_data_assets.setdefault(
            str(location),
            {
                "name": str(name),
                "location": str(location),
                "data": data_description,
            },
        )

    for data_asset in unique_data_assets.values():
        existing_data_assets = get(
            session,
            "/data_assets",
            params={"location": data_asset["location"]},
        )
        if any(
            row["location"] == data_asset["location"]
            and row["name"] == data_asset["name"]
            for row in existing_data_assets
        ):
            continue

        register(
            session,
            "/data_assets",
            params={
                "schema_id": data_asset_schema_id,
                "space_id": space_id,
                "name": data_asset["name"],
                "location": data_asset["location"],
            },
            json=data_asset["data"],
        )


def register_instruments(session: requests.Session, space_id: int = 1) -> None:
    instrument_schema_id = get_schema_id(
        session,
        "instrument",
        "instrument_schema.json",
    )
    records = load_docdb_records()
    unique_instruments: dict[str, dict[str, Any]] = {}

    for record in records:
        instrument = record.get("instrument")
        if not isinstance(instrument, dict):
            continue

        instrument_id = instrument.get("instrument_id")
        if not instrument_id:
            continue

        unique_instruments.setdefault(str(instrument_id), instrument)

    for instrument_id, instrument in unique_instruments.items():
        existing_instruments = get(
            session,
            "/instruments",
            params={"name": instrument_id},
        )
        if any(row["name"] == instrument_id for row in existing_instruments):
            continue

        register(
            session,
            "/instruments",
            params={
                "schema_id": instrument_schema_id,
                "space_id": space_id,
                "name": instrument_id,
            },
            json=instrument,
        )


def register_acquisitions(session: requests.Session, space_id: int = 1) -> None:
    acquisition_schema_id = get_schema_id(
        session,
        "acquisition",
        "acquisition_schema.json",
    )
    register_instruments(session, space_id=space_id)
    records = load_docdb_records()

    for record in records:
        acquisition = record.get("acquisition")
        if not isinstance(acquisition, dict):
            continue

        instrument_name = acquisition.get("instrument_id")
        if not instrument_name:
            continue

        location = record.get("location")
        name = record.get("name")
        if not location or not name:
            continue

        data_asset_id = get_data_asset_id(
            session,
            location=str(location),
            name=str(name),
        )
        instrument_id = get_instrument_id(session, name=str(instrument_name))
        existing_acquisitions = get(
            session,
            "/acquisitions",
            params={"data_asset_id": data_asset_id},
        )
        if any(row["data_asset_id"] == data_asset_id for row in existing_acquisitions):
            continue

        register(
            session,
            "/acquisitions",
            params={
                "schema_id": acquisition_schema_id,
                "space_id": space_id,
                "data_asset_id": data_asset_id,
                "instrument_id": instrument_id,
            },
            json=acquisition,
        )


def create_schemas(session: requests.Session) -> None:
    schema_definitions = [
        ("acquisition", "acquisition_schema.json", 1),
        ("data_description", "data_description_schema.json", 2),
        ("instrument", "instrument_schema.json", 3),
        ("procedures", "procedures_schema.json", 4),
        ("processing", "processing_schema.json", 5),
        ("quality_control", "quality_control_schema.json", 6),
        ("subject", "subject_schema.json", 7),
    ]

    for name, schema_filename, schema_entity_id in schema_definitions:
        data = load_schema(schema_filename)
        register(
            session,
            "/schemas",
            params={
                "name": name,
                "version": data["properties"]["schema_version"]["const"],
                "schema_entity_id": schema_entity_id,
            },
            json=data,
        )


def register_core_data(session: requests.Session) -> None:
    for params in [
        {"name": "Joe Smith", "contact": "joe.smith@example.com"},
        {"name": "Anna Apple", "contact": "anna.apple@example.com"},
    ]:
        register(session, "/users", params=params)

    for params in [{"name": "AIND"}, {"name": "AIBS"}]:
        register(session, "/organizations", params=params)

    register(
        session,
        "/spaces",
        params={"name": "Space1", "organization_id": 1},
    )

    register(
        session,
        "/space_admins",
        params={"user_id": 2, "space_id": 1},
    )

    register(
        session,
        "/organization_admins",
        params={"user_id": 2, "organization_id": 1},
    )

    register(
        session,
        "/collections",
        params={
            "name": "test_collection",
            "description": "Test Collection",
            "owner_id": 1,
        },
    )

    for schema_entity_name in [
        "acquisition",
        "data_description",
        "instrument",
        "procedures",
        "processing",
        "quality_control",
        "subject",
    ]:
        register(
            session,
            "/schema_entities",
            params={"name": schema_entity_name},
        )

    create_schemas(session)


def main() -> None:
    args = parse_args()

    with requests.Session() as session:
        if args.register_core_data:
            register_core_data(session)

        register_subjects(session, space_id=args.space_id)
        register_data_assets(session, space_id=args.space_id)
        register_acquisitions(session, space_id=args.space_id)


if __name__ == "__main__":
    main()
