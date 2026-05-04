from biodata_registry_api_client import (
    Configuration,
    AcquisitionCreate,
    ApiClient,
    AdminApi,
    CollectionCreate,
    CoreApi,
    ViewsApi,
    DataAssetCreate,
    OrganizationCreate,
    UserCreate,
    SpaceCreate,
    SchemaEntityCreate,
    CollectionUpdate,
    SpaceAdminCreate,
    SchemaCreate,
    InstrumentCreate,
    SubjectCreate,
    SubjectProcedureCreate,
    DataAssetCreate,
    QualityControlCreate,
    ProcessCreate
)
from pathlib import Path
import json
import gzip
import re

SCHEMA_DIR = Path("../examples/schema_definitions")
DOCDB_RECORDS_FILE = Path(
    "../examples/records/docdb_records_10_percent_sample.json.gz"
)
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
        "filename": "quality_control_metric_schema.json",
        "version": "2.4.1",
        "schema_entity_id": 7,
    },
    "subject": {
        "filename": "subject_schema.json",
        "version": "2.2.1",
        "schema_entity_id": 8,
    },
}

configuration = Configuration(
    host = "http://localhost:5000"
)

api_client = ApiClient(configuration)
admin_api = AdminApi(api_client)
core_api = CoreApi(api_client)
views_api = ViewsApi(api_client)

admin_api.create_user(
    UserCreate(name="Joe Smith", contact="joe.smith@example.com")
)

admin_api.create_user(
    UserCreate(name="Anna Apple", contact="anna.apple@example.com")
)

admin_api.create_organization(OrganizationCreate(name="AIND"))
admin_api.create_organization(OrganizationCreate(name="AIBS"))

admin_api.create_space(
    SpaceCreate(name="Space1", organization_id=1)
)

admin_api.create_space_admin(
    SpaceAdminCreate(space_id=1, user_id=1)
)

admin_api.create_collection(
    CollectionCreate(
        name="My Collection",
        description="My Collection description",
        owner_id=1,
    )
)

for schema_entity_name in [
    "acquisition",
    "data_description",
    "instrument",
    "subject_procedures",
    "specimen_procedures",
    "processing",
    "quality_control",
    "subject"
]:
    core_api.create_schema_entity(
        SchemaEntityCreate(name=schema_entity_name)
    )

for name, schema_definition in SCHEMA_DEFINITIONS.items():
    with open(SCHEMA_DIR / schema_definition["filename"], "r") as f:
        data = json.load(f)
    version = schema_definition["version"]
    schema_entity_id = schema_definition["schema_entity_id"]
    response = core_api.create_schema(
        SchemaCreate(
            name=name,
            version=version,
            data=data,
            schema_entity_id=schema_entity_id,
        )
    )

schemas = core_api.get_schemas()
schema_id_map = dict([(r.name, r.id) for r in schemas])

with gzip.open(DOCDB_RECORDS_FILE, 'rt', encoding='utf-8') as f:
    docdb_records = json.load(f)

names_seen = set()
filtered_records = []
for record in docdb_records:
    if ((
            record.get("subject") is not None and record["subject"].get("schema_version") == "2.2.1"
    ) and (
            record.get("data_description") is not None and record["data_description"].get("schema_version") == "2.3.3"
    ) and (
            record.get("quality_control") is None or record["quality_control"].get("schema_version") == "2.4.1"
    ) and (
            record.get("processing") is None or record["processing"].get("schema_version") == "2.2.5"
    ) and (
            record.get("acquisition") is None or record["acquisition"].get("schema_version") == "2.4.0"
    ) and (
            record.get("procedures") is None or record["procedures"].get("schema_version") == "2.1.1"
    ) and (
            record.get("instrument") is None or record["instrument"].get("schema_version") == "2.2.3"
    )):
        record_name = record["name"]
        dd_name = record["data_description"]["name"]
        if record_name == dd_name and record_name not in names_seen:
            names_seen.add(record_name)
            filtered_records.append(record)


subjects_seen = set()
instruments_seen = set()
counter = 0
total_records = len(filtered_records)
for record in filtered_records[0:400]:
    counter += 1
    if counter % 100 == 0:
        print(f"On {counter} of {total_records}")
    subject = record["subject"]
    subject_id = subject["subject_id"]
    instrument = record["instrument"]
    instrument_id = instrument["instrument_id"]
    instrument_modification_date = instrument["modification_date"]
    if bool(re.search(r'\d{8}$', instrument_id)):
        instrument_name = instrument_id[:-8] + instrument_modification_date
    elif not bool(re.search(r'\d{4}-\d{2}-\d{2}$', instrument_id)):
        instrument_name = instrument_id + "_" + instrument_modification_date
    else:
        instrument_name = instrument_id
    location = record["location"]
    external_links = record["other_identifiers"]
    data_description = record["data_description"]
    name = data_description["name"]
    acquisition = record["acquisition"]
    quality_controls = record["quality_control"]
    quality_control_metrics = [] if quality_controls is None else quality_controls.get("metrics", [])
    processes = record["processing"]
    procedures = record["procedures"]
    subject_procedures = [] if procedures is None else procedures.get("subject_procedures", [])
    if subject_id not in subjects_seen:
        subjects_seen.add(subject["subject_id"])
        registered_subject = core_api.create_subject(
            SubjectCreate(
                space_id=1,
                schema_id=schema_id_map["subject"],
                name=subject_id,
                data=subject
            )
        )
        for subject_procedure in subject_procedures:
            registered_subject_procedures = core_api.create_subject_procedure(
                SubjectProcedureCreate(
                    space_id=1,
                    schema_id=schema_id_map["subject_procedures"],
                    subject_id=registered_subject.id,
                    data=subject_procedures,
                )
            )
    else:
        # TODO: Cache things to avoid fetching from DB
        registered_subject = core_api.get_subjects(name=subject_id)[0]
    if instrument_name not in instruments_seen:
        instruments_seen.add(instrument_name)
        registered_instrument = core_api.create_instrument(
            InstrumentCreate(
                space_id=1,
                schema_id=schema_id_map["instrument"],
                name=instrument_name,
                data=instrument
            )
        )
    else:
        # TODO: Cache things to avoid fetching from DB
        registered_instrument = core_api.get_instruments(name=instrument_name)[0]
    registered_data_asset = core_api.create_data_asset(
        DataAssetCreate(
            space_id=1,
            schema_id=schema_id_map["data_description"],
            location=location,
            name=name,
            data=data_description
        )
    )
    registered_acquisition = core_api.create_acquisition(
        AcquisitionCreate(
            space_id=1,
            schema_id=schema_id_map["acquisition"],
            data_asset_id=registered_data_asset.id,
            instrument_id=registered_instrument.id,
            data=acquisition
        )
    )
    add_acquisition_response = core_api.put_acquisition_subject(
        id=registered_acquisition.id,
        subject_id=registered_subject.id,
    )
    for quality_control_metric in quality_control_metrics:
        registered_quality_control = core_api.create_quality_control(
            QualityControlCreate(
                space_id=1,
                schema_id=schema_id_map["quality_control"],
                data_asset_id=registered_data_asset.id,
                data=quality_control_metric
            )
        )
    registered_processes = core_api.create_process(
        ProcessCreate(
            space_id=1,
            schema_id=schema_id_map["processing"],
            output_data_asset_id=registered_data_asset.id,
            data=processes
        )
    )
