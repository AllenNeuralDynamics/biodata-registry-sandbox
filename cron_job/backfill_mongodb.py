from typing import List, Dict, Iterator
from collections import defaultdict

import psycopg
from psycopg.rows import dict_row
from pymongo import MongoClient, ReplaceOne
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
import uuid
import os
import argparse

MONGO_HOST=os.environ['MONGO_HOST']
MONGO_PORT=int(os.environ['MONGO_PORT'])
MONGO_USERNAME=os.environ['MONGO_USERNAME']
MONGO_PASSWORD=os.environ['MONGO_PASSWORD']
MONGO_DBNAME=os.environ['MONGO_DBNAME']
MONGO_DB_COLLECTION=os.environ['MONGO_DB_COLLECTION']
PG_USER=os.environ['PG_USER']
PG_PASSWORD=os.environ['PG_PASSWORD']
PG_HOST=os.environ['PG_HOST']
PG_PORT=os.environ['PG_PORT']
PG_DBNAME=os.environ['PG_DBNAME']

PG_INFO=f"host={PG_HOST} port={PG_PORT} dbname={PG_DBNAME} user={PG_USER} password={PG_PASSWORD}"

def partition(lst: List, size: int) -> Iterator:
    """Partition a list"""
    for i in range(0, len(lst), size):
        yield lst[i : i + size]  # noqa: E203

def flatten_data_asset_view_records(p_records: List[Dict]):
    if len(p_records) > 0:
        p_subject_seen = set()
        p_subject_procedure_seen = set()
        p_quality_control_seen = set()
        p_subjects = dict()
        p_subject_procedures = defaultdict(list)
        p_quality_control = []
        p_record = dict()
        for p_record in p_records:
            _ = p_record.pop("subject_name", None)
            p_subject_id = str(p_record.pop("subject_id", None))
            p_subject_procedure_id = p_record.pop("subject_procedure_id", None)
            p_quality_control_id = p_record.pop("quality_control_id", None)
            p_subject_data = p_record.pop("subject_data", None)
            p_subject_procedure_data = p_record.pop("subject_procedures_data", None)
            p_quality_control_data = p_record.pop("quality_control_data", None)
            if p_subject_data is not None and p_subject_id not in p_subject_seen and p_subject_id is not None:
                p_subject_seen.add(p_subject_id)
                p_subjects[p_subject_id] = p_subject_data
            if p_subject_procedure_data is not None and p_subject_procedure_id not in p_subject_procedure_seen and p_subject_id is not None:
                p_subject_procedure_seen.add(p_subject_procedure_id)
                p_subject_procedures[p_subject_id].append(p_subject_procedure_data)
            if p_quality_control_data is not None and p_quality_control_id not in p_quality_control_seen:
                p_quality_control_seen.add(p_quality_control_id)
                p_quality_control.append(p_quality_control_data)
        p_record["subjects"] = p_subjects
        p_record["subject_procedures"] = p_subject_procedures
        p_record["quality_control"] = p_quality_control
        return p_record
    else:
        return None

def add_records_to_databases(d_collection, p_records):
    replace_requests = []
    for k_data_asset_id, p_records in p_records.items():
        mongo_db_record = flatten_data_asset_view_records(p_records)
        if mongo_db_record is not None:
            hashed_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(k_data_asset_id)))
            mongo_db_record["_id"] = hashed_uuid
            replace_requests.append(
                ReplaceOne(
                    {"_id": hashed_uuid},
                    mongo_db_record,
                    upsert=True
                )
            )
    if replace_requests:
        d_collection.bulk_write(replace_requests)


def handle_data_asset_changes(d_collection, p_conn, k_data_asset_ids):
    if k_data_asset_ids:
        p_record_groups = defaultdict(list)
        with p_conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM data_asset_view WHERE data_asset_id = ANY(%s);",
                (k_data_asset_ids,)
            )
            for p_record in cur:
                k_data_asset_id = p_record["data_asset_id"]
                p_record_groups[k_data_asset_id].append(p_record)
        add_records_to_databases(d_collection, p_record_groups)

def main(backfill_all: bool = False):
    # TODO add filter on last_modified when info is added
    pg_conn_info = PG_INFO
    with (
        MongoClient(
            host=MONGO_HOST,
            port=MONGO_PORT,
            username=MONGO_USERNAME,
            password=MONGO_PASSWORD
        ) as mongodb_client,
        psycopg.connect(pg_conn_info, row_factory=dict_row) as conn
    ):
        db = mongodb_client[MONGO_DBNAME]
        opts = CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
        collection = db.get_collection(MONGO_DB_COLLECTION, codec_options=opts)
        data_asset_ids = []
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM data_assets")
            for p_record in cur:
                data_asset_ids.append(p_record["id"])
        if backfill_all:
            missing_ids = data_asset_ids
        else:
            mongodb_ids = [
                row["data_asset_id"] for row in collection.find(
                    {},
                    projection={"data_asset_id": 1}
                ).to_list()
            ]
            missing_ids = list(set(data_asset_ids).difference(set(mongodb_ids)))
        print(f"Backfilling {len(missing_ids)} records")
        missing_ids.sort()
        pages = partition(missing_ids, 50)
        for page in pages:
            handle_data_asset_changes(collection, conn, page)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Run backfill.")
        parser.add_argument('--all', action='store_true', help="Migrate all data asset records.")
        args = parser.parse_args()
        main(args.all)
    except Exception as e:
        print(f"There was an exception running the script: {e}")
