import argparse
import json
from pathlib import Path
from typing import Any

import requests

from api_helpers import (
    find_record,
    get,
    get_or_register_record,
    register,
)

SCHEMA_DIR = Path(__file__).resolve().parent / "schema_definitions"
RECORDS_PATH = Path(__file__).resolve().parent / "records" / "docdb_records.json"
SCHEMA_DEFINITIONS = {
    "acquisition": {
        "filename": "acquisition_schema.json",
        "version": "2.4.0",
        "schema_entity_id": 1,
    },
    "data_description": {
        "filename": "data_description_schema.json",
        "version": "2.3.3",
        "schema_entity_id": 2,
    },
    "instrument": {
        "filename": "instrument_schema.json",
        "version": "2.2.3",
        "schema_entity_id": 3,
    },
    "subject_procedures": {
        "filename": "subject_procedures.json",
        "version": "2.1.1",
        "schema_entity_id": 4,
    },
    "specimen_procedures": {
        "filename": "specimen_procedures.json",
        "version": "2.1.1",
        "schema_entity_id": 5,
    },
    "processing": {
        "filename": "processing_schema.json",
        "version": "2.2.5",
        "schema_entity_id": 6,
    },
    "quality_control": {
        "filename": "quality_control_schema.json",
        "version": "2.4.1",
        "schema_entity_id": 7,
    },
    "subject": {
        "filename": "subject_schema.json",
        "version": "2.2.1",
        "schema_entity_id": 8,
    },
}


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


def get_schema_definition(schema_name: str) -> dict[str, Any]:
    if schema_name not in SCHEMA_DEFINITIONS:
        raise ValueError(f"Unknown schema definition for {schema_name}.")
    return SCHEMA_DEFINITIONS[schema_name]


def get_schema_id(session: requests.Session, schema_name: str) -> int:
    schema_version = get_schema_definition(schema_name)["version"]
    schemas = get(session, "/schemas", params={"name": schema_name})

    for row in schemas:
        if row["name"] == schema_name and row["version"] == schema_version:
            return row["id"]

    raise ValueError(
        f"Could not find schema id for {schema_name} {schema_version}. "
        "Create schemas before registering records."
    )


def canonicalize_data(data: dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True)


def register_documents(session: requests.Session, space_id: int = 1) -> None:
    subject_schema_id = get_schema_id(session, "subject")
    data_asset_schema_id = get_schema_id(session, "data_description")
    instrument_schema_id = get_schema_id(session, "instrument")
    acquisition_schema_id = get_schema_id(session, "acquisition")
    subject_procedure_schema_id = get_schema_id(session, "subject_procedures")
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
        subject_id: int | None = None
        if isinstance(subject, dict):
            raw_subject_name = subject.get("subject_id")
            if raw_subject_name:
                subject_name = str(raw_subject_name)
                subject_row = get_or_register_record(
                    session,
                    endpoint="/subjects",
                    lookup_params={"name": subject_name},
                    match_fields={"name": subject_name},
                    create_params={
                        "schema_id": subject_schema_id,
                        "space_id": space_id,
                        "name": subject_name,
                    },
                    data=subject,
                )
                subject_id = subject_row["id"]

        data_asset = record.get("data_description")
        location = record.get("location")
        name = record.get("name") or (data_asset or {}).get("name")
        data_asset_id: int | None = None
        if isinstance(data_asset, dict) and location and name:
            data_asset_name = str(name)
            data_asset_location = str(location)
            data_asset_row = get_or_register_record(
                session,
                endpoint="/data_assets",
                lookup_params={"location": data_asset_location},
                match_fields={
                    "location": data_asset_location,
                    "name": data_asset_name,
                },
                create_params={
                    "schema_id": data_asset_schema_id,
                    "space_id": space_id,
                    "name": data_asset_name,
                    "location": data_asset_location,
                },
                data=data_asset,
            )
            data_asset_id = data_asset_row["id"]

        instrument = record.get("instrument")
        instrument_id: int | None = None
        if isinstance(instrument, dict):
            raw_instrument_name = instrument.get("instrument_id")
            if raw_instrument_name:
                instrument_name = str(raw_instrument_name)
                instrument_row = get_or_register_record(
                    session,
                    endpoint="/instruments",
                    lookup_params={"name": instrument_name},
                    match_fields={"name": instrument_name},
                    create_params={
                        "schema_id": instrument_schema_id,
                        "space_id": space_id,
                        "name": instrument_name,
                    },
                    data=instrument,
                )
                instrument_id = instrument_row["id"]

        acquisition = record.get("acquisition")
        if (
            isinstance(acquisition, dict)
            and data_asset_id is not None
            and instrument_id is not None
            and subject_id is not None
        ):
            acquisition_row = get_or_register_record(
                session,
                endpoint="/acquisitions",
                lookup_params={"data_asset_id": data_asset_id},
                match_fields={"data_asset_id": data_asset_id},
                create_params={
                    "schema_id": acquisition_schema_id,
                    "space_id": space_id,
                    "data_asset_id": data_asset_id,
                    "instrument_id": instrument_id,
                },
                data=acquisition,
            )
            acquisition_id = acquisition_row["id"]

            acquisition_subject_row = find_record(
                get(
                    session,
                    "/acquisition_subjects",
                    params={"acquisition_id": acquisition_id},
                ),
                acquisition_id=acquisition_id,
                subject_id=subject_id,
            )
            if acquisition_subject_row is None:
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
    specimen_procedure_schema_id = get_schema_id(session, "specimen_procedures")
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
    for name, schema_definition in SCHEMA_DEFINITIONS.items():
        data = load_schema(schema_definition["filename"])
        register(
            session,
            "/schemas",
            params={
                "name": name,
                "version": schema_definition["version"],
                "schema_entity_id": schema_definition["schema_entity_id"],
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
