import json
from typing import List, Dict
from collections import defaultdict

from kafka import KafkaConsumer
import psycopg
from psycopg.rows import dict_row
from pymongo import MongoClient, ReplaceOne
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
import uuid

TOPICS = [
    "registry.public.data_assets",
    "registry.public.subjects",
    "registry.public.specimens",
    "registry.public.specimen_procedures",
    "registry.public.subject_procedures",
    "registry.public.instruments",
    "registry.public.acquisitions",
    "registry.public.quality_controls",
    "registry.public.processes"
]

consumer = KafkaConsumer(
    *TOPICS,
    bootstrap_servers=['localhost:29092'],
    auto_offset_reset='earliest',
    allow_auto_create_topics=False,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def flatten_data_asset_view_records(p_records: List[Dict]):
    subjects = []
    if len(p_records) > 0:
        p_record = dict()
        for p_record in p_records:
            _ = p_record.pop("subject_name", None)
            subject_data = p_record.pop("subject_data", None)
            if subject_data is not None:
                subjects.append(subject_data)
        p_record["subjects"] = subjects
        return p_record
    else:
        return None


def handle_data_asset_change(k_message, d_collection, p_conn):
    k_data_asset_id = k_message.value["payload"]["after"].get("id")
    if k_data_asset_id is not None:
        with p_conn.cursor() as cur:
            p_records = []
            cur.execute(
                "SELECT * FROM data_asset_view WHERE data_asset_id = %s;",
                (k_data_asset_id,)
            )
            for p_record in cur:
                p_records.append(p_record)
        mongo_db_record = flatten_data_asset_view_records(p_records)
        if mongo_db_record is not None:
            hashed_uuid = uuid.uuid5(namespace, str(k_data_asset_id))
            mongo_db_record["_id"] = hashed_uuid
            d_collection.replace_one(
                {"_id": hashed_uuid}, mongo_db_record, upsert=True
            )

def handle_subject_change(k_message, d_collection, p_conn):
    k_subject_id = k_message.value["payload"]["after"].get("id")
    if k_subject_id is not None:
        with p_conn.cursor() as cur:
            p_record_groups = defaultdict(list)
            cur.execute(
                "SELECT * FROM data_asset_view WHERE subject_id = %s;",
                (k_subject_id,)
            )
            for p_record in cur:
                k_data_asset_id = p_record["data_asset_id"]
                p_record_groups[k_data_asset_id].append(p_record)
        replace_requests = []
        for k_data_asset_id, p_records in p_record_groups.items():
            mongo_db_record = flatten_data_asset_view_records(p_records)
            if mongo_db_record is not None:
                hashed_uuid = uuid.uuid5(namespace, str(k_data_asset_id))
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

def handle_subject_procedure_change(k_message, d_collection, p_conn):
    k_subject_id = k_message.value["payload"]["after"].get("subject_id")
    if k_subject_id is not None:
        with p_conn.cursor() as cur:
            p_record_groups = defaultdict(list)
            cur.execute(
                "SELECT * FROM data_asset_view WHERE subject_id = %s;",
                (k_subject_id,)
            )
            for p_record in cur:
                k_data_asset_id = p_record["data_asset_id"]
                p_record_groups[k_data_asset_id].append(p_record)
        replace_requests = []
        for k_data_asset_id, p_records in p_record_groups.items():
            mongo_db_record = flatten_data_asset_view_records(p_records)
            if mongo_db_record is not None:
                hashed_uuid = uuid.uuid5(namespace, str(k_data_asset_id))
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

def handle_instrument_change(k_message, d_collection, p_conn):
    k_instrument_id = k_message.value["payload"]["after"].get("instrument_id")
    if k_instrument_id is not None:
        with p_conn.cursor() as cur:
            p_record_groups = defaultdict(list)
            cur.execute(
                "SELECT * FROM data_asset_view WHERE k_instrument_id = %s;",
                (k_instrument_id,)
            )
            for p_record in cur:
                k_data_asset_id = p_record["data_asset_id"]
                p_record_groups[k_data_asset_id].append(p_record)
        replace_requests = []
        for k_data_asset_id, p_records in p_record_groups.items():
            mongo_db_record = flatten_data_asset_view_records(p_records)
            if mongo_db_record is not None:
                hashed_uuid = uuid.uuid5(namespace, str(k_data_asset_id))
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

def handle_acquisition_change(k_message, d_collection, p_conn):
    k_data_asset_id = k_message.value["payload"]["after"].get("data_asset_id")
    if k_data_asset_id is not None:
        with p_conn.cursor() as cur:
            p_records = []
            cur.execute(
                "SELECT * FROM data_asset_view WHERE data_asset_id = %s;",
                (k_data_asset_id,)
            )
            for p_record in cur:
                p_records.append(p_record)
        mongo_db_record = flatten_data_asset_view_records(p_records)
        if mongo_db_record is not None:
            hashed_uuid = uuid.uuid5(namespace, str(k_data_asset_id))
            mongo_db_record["_id"] = hashed_uuid
            d_collection.replace_one(
                {"_id": hashed_uuid}, mongo_db_record, upsert=True
            )

def handle_processes_change(k_message, d_collection, p_conn):
    k_data_asset_id = k_message.value["payload"]["after"].get("output_data_asset_id")
    if k_data_asset_id is not None:
        with p_conn.cursor() as cur:
            p_records = []
            cur.execute(
                "SELECT * FROM data_asset_view WHERE data_asset_id = %s;",
                (k_data_asset_id,)
            )
            for p_record in cur:
                p_records.append(p_record)
        mongo_db_record = flatten_data_asset_view_records(p_records)
        if mongo_db_record is not None:
            hashed_uuid = uuid.uuid5(namespace, str(k_data_asset_id))
            mongo_db_record["_id"] = hashed_uuid
            d_collection.replace_one(
                {"_id": hashed_uuid}, mongo_db_record, upsert=True
            )

def handle_quality_controls_change(k_message, d_collection, p_conn):
    k_data_asset_id = k_message.value["payload"]["after"].get("data_asset_id")
    if k_data_asset_id is not None:
        with p_conn.cursor() as cur:
            p_records = []
            cur.execute(
                "SELECT * FROM data_asset_view WHERE data_asset_id = %s;",
                (k_data_asset_id,)
            )
            for p_record in cur:
                p_records.append(p_record)
        mongo_db_record = flatten_data_asset_view_records(p_records)
        if mongo_db_record is not None:
            hashed_uuid = uuid.uuid5(namespace, str(k_data_asset_id))
            mongo_db_record["_id"] = hashed_uuid
            d_collection.replace_one(
                {"_id": hashed_uuid}, mongo_db_record, upsert=True
            )

try:
    pg_conn_info = "host=localhost port=5432 dbname=registry user=user password=password"
    namespace = uuid.NAMESPACE_DNS
    with (
        MongoClient(
            host="localhost",
            port=27017,
            username="admin",
            password="admin_password"
        ) as mongodb_client,
        psycopg.connect(pg_conn_info, row_factory=dict_row) as conn
    ):
        db = mongodb_client["metadata"]
        opts = CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
        collection = db.get_collection("data_assets", codec_options=opts)
        for message in consumer:
            match message.topic:
                case "registry.public.data_assets":
                    handle_data_asset_change(message, collection, conn)
                case "registry.public.subjects":
                    handle_subject_change(message, collection, conn)
                case "registry.public.specimens":
                    print(message.topic)
                case "registry.specimen_procedures":
                    print(message.topic)
                case "registry.public.subject_procedures":
                    handle_subject_procedure_change(message, collection, conn)
                case "registry.public.instruments":
                    handle_instrument_change(message, collection, conn)
                case "registry.public.acquisitions":
                    handle_acquisition_change(message, collection, conn)
                case "registry.public.quality_controls":
                    handle_quality_controls_change(message, collection, conn)
                case "registry.public.processes":
                    handle_processes_change(message, collection, conn)
                case _:
                    print("Unknown topic")
except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    consumer.close()
