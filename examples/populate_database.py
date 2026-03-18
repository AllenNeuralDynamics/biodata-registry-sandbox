import argparse
import json
from pathlib import Path
from typing import Any

import requests


BASE_URL = "http://localhost:5000"
SCHEMA_DIR = Path(__file__).resolve().parent / "schema_definitions"
RECORDS_PATH = Path(__file__).resolve().parent / "records" / "docdb_records.json"
SCHEMA_VERSION_FALLBACKS = {
    "subject_procedures.json": "procedures_schema.json",
    "specimen_procedures.json": "procedures_schema.json",
}


def register(session: requests.Session, endpoint: str, **kwargs) -> Any:
    response = session.post(f"{BASE_URL}{endpoint}", **kwargs)
    print(response.status_code)
    response.raise_for_status()
    if not response.content:
        return None
    return response.json()


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


def get_schema_version(schema_filename: str) -> str:
    schema = load_schema(schema_filename)
    properties = schema.get("properties", {})
    schema_version = properties.get("schema_version", {}).get("const")
    if schema_version is not None:
        return str(schema_version)

    fallback_schema_filename = SCHEMA_VERSION_FALLBACKS.get(schema_filename)
    if fallback_schema_filename is None:
        raise ValueError(f"Could not determine schema version for {schema_filename}.")

    fallback_schema = load_schema(fallback_schema_filename)
    fallback_version = fallback_schema["properties"]["schema_version"]["const"]
    return str(fallback_version)


def get_schema_id(
    session: requests.Session,
    schema_name: str,
    schema_filename: str,
) -> int:
    schema_version = get_schema_version(schema_filename)
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


def canonicalize_data(data: dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True)


def register_documents(session: requests.Session, space_id: int = 1) -> None:
    subject_schema_id = get_schema_id(session, "subject", "subject_schema.json")
    data_asset_schema_id = get_schema_id(
        session,
        "data_description",
        "data_description_schema.json",
    )
    instrument_schema_id = get_schema_id(
        session,
        "instrument",
        "instrument_schema.json",
    )
    acquisition_schema_id = get_schema_id(
        session,
        "acquisition",
        "acquisition_schema.json",
    )
    subject_procedure_schema_id = get_schema_id(
        session,
        "subject_procedures",
        "subject_procedures.json",
    )
    existing_subject_procedures = get(
        session,
        "/subject_procedures",
        params={"schema_id": subject_procedure_schema_id},
    )
    registered_subject_procedures = {
        (row["subject_id"], canonicalize_data(row["data"]))
        for row in existing_subject_procedures
    }

    for record in load_docdb_records():
        subject = record.get("subject")
        subject_name: str | None = None
        subject_id: int | None = None
        if isinstance(subject, dict):
            raw_subject_name = subject.get("subject_id")
            if raw_subject_name:
                subject_name = str(raw_subject_name)
                existing_subjects = get(
                    session,
                    "/subjects",
                    params={"name": subject_name},
                )
                if existing_subjects:
                    subject_id = existing_subjects[0]["id"]
                else:
                    created_subjects = register(
                        session,
                        "/subjects",
                        params={
                            "schema_id": subject_schema_id,
                            "space_id": space_id,
                            "name": subject_name,
                        },
                        json=subject,
                    )
                    subject_id = created_subjects[0]["id"]

        data_asset = record.get("data_description")
        location = record.get("location")
        name = record.get("name") or (data_asset or {}).get("name")
        data_asset_id: int | None = None
        if isinstance(data_asset, dict) and location and name:
            data_asset_name = str(name)
            data_asset_location = str(location)
            existing_data_assets = get(
                session,
                "/data_assets",
                params={"location": data_asset_location},
            )
            matching_data_assets = [
                row
                for row in existing_data_assets
                if row["location"] == data_asset_location
                and row["name"] == data_asset_name
            ]
            if matching_data_assets:
                data_asset_id = matching_data_assets[0]["id"]
            else:
                created_data_assets = register(
                    session,
                    "/data_assets",
                    params={
                        "schema_id": data_asset_schema_id,
                        "space_id": space_id,
                        "name": data_asset_name,
                        "location": data_asset_location,
                    },
                    json=data_asset,
                )
                data_asset_id = created_data_assets[0]["id"]

        instrument = record.get("instrument")
        instrument_id: int | None = None
        if isinstance(instrument, dict):
            raw_instrument_name = instrument.get("instrument_id")
            if raw_instrument_name:
                instrument_name = str(raw_instrument_name)
                existing_instruments = get(
                    session,
                    "/instruments",
                    params={"name": instrument_name},
                )
                if existing_instruments:
                    instrument_id = existing_instruments[0]["id"]
                else:
                    created_instruments = register(
                        session,
                        "/instruments",
                        params={
                            "schema_id": instrument_schema_id,
                            "space_id": space_id,
                            "name": instrument_name,
                        },
                        json=instrument,
                    )
                    instrument_id = created_instruments[0]["id"]

        acquisition = record.get("acquisition")
        if (
            isinstance(acquisition, dict)
            and data_asset_id is not None
            and instrument_id is not None
            and subject_id is not None
        ):
            existing_acquisitions = get(
                session,
                "/acquisitions",
                params={"data_asset_id": data_asset_id},
            )
            if existing_acquisitions:
                acquisition_id = existing_acquisitions[0]["id"]
            else:
                created_acquisitions = register(
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
                acquisition_id = created_acquisitions[0]["id"]

            acquisition_subjects = get(
                session,
                "/acquisition_subjects",
                params={"acquisition_id": acquisition_id},
            )
            if not any(
                row["acquisition_id"] == acquisition_id
                and row["subject_id"] == subject_id
                for row in acquisition_subjects
            ):
                register(
                    session,
                    "/acquisition_subjects",
                    params={
                        "acquisition_id": acquisition_id,
                        "subject_id": subject_id,
                    },
                )

        procedures = record.get("procedures")
        if not isinstance(procedures, dict) or subject_id is None:
            continue

        for subject_procedure in procedures.get("subject_procedures", []):
            if not isinstance(subject_procedure, dict):
                continue

            payload_key = (subject_id, canonicalize_data(subject_procedure))
            if payload_key in registered_subject_procedures:
                continue

            register(
                session,
                "/subject_procedures",
                params={
                    "schema_id": subject_procedure_schema_id,
                    "space_id": space_id,
                    "subject_id": subject_id,
                },
                json=subject_procedure,
            )
            registered_subject_procedures.add(payload_key)


def register_specimen_procedures(
    session: requests.Session,
    space_id: int = 1,
) -> None:
    specimen_procedure_schema_id = get_schema_id(
        session,
        "specimen_procedures",
        "specimen_procedures.json",
    )
    existing_rows = get(
        session,
        "/specimen_procedures",
        params={"schema_id": specimen_procedure_schema_id},
    )
    existing_payloads = {
        canonicalize_data(row["data"])
        for row in existing_rows
    }
    records = load_docdb_records()
    unique_specimen_procedures: dict[str, dict[str, Any]] = {}

    for record in records:
        procedures = record.get("procedures")
        if not isinstance(procedures, dict):
            continue

        for specimen_procedure in procedures.get("specimen_procedures", []):
            if not isinstance(specimen_procedure, dict):
                continue

            unique_specimen_procedures.setdefault(
                canonicalize_data(specimen_procedure),
                specimen_procedure,
            )

    for payload_key, specimen_procedure in unique_specimen_procedures.items():
        if payload_key in existing_payloads:
            continue

        register(
            session,
            "/specimen_procedures",
            params={
                "schema_id": specimen_procedure_schema_id,
                "space_id": space_id,
            },
            json=specimen_procedure,
        )


def create_schemas(session: requests.Session) -> None:
    schema_definitions = [
        ("acquisition", "acquisition_schema.json", 1),
        ("data_description", "data_description_schema.json", 2),
        ("instrument", "instrument_schema.json", 3),
        ("subject_procedures", "subject_procedures.json", 4),
        ("specimen_procedures", "specimen_procedures.json", 5),
        ("processing", "processing_schema.json", 6),
        ("quality_control", "quality_control_schema.json", 7),
        ("subject", "subject_schema.json", 8),
    ]

    for name, schema_filename, schema_entity_id in schema_definitions:
        data = load_schema(schema_filename)
        register(
            session,
            "/schemas",
            params={
                "name": name,
                "version": get_schema_version(schema_filename),
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
        "subject_procedures",
        "specimen_procedures",
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

        register_documents(session, space_id=args.space_id)


if __name__ == "__main__":
    main()
