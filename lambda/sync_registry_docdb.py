import json
from typing import List, Dict

from kafka import KafkaConsumer
import psycopg
from psycopg.rows import dict_row
from pymongo import MongoClient
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


def handle_data_asset(k_message, d_collection, p_conn):
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
                    handle_data_asset(message, collection, conn)
                case "registry.public.subjects":
                    print(message.topic)
                case "registry.public.specimens":
                    print(message.topic)
                case "registry.specimen_procedures":
                    print(message.topic)
                case "registry.public.subject_procedures":
                    print(message.topic)
                case "registry.public.instruments":
                    print(message.topic)
                case "registry.public.acquisitions":
                    print(message.topic)
                case "registry.public.quality_controls":
                    print(message.topic)
                case "registry.public.processes":
                    print(message.topic)
                case _:
                    print("Unknown topic")
except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    consumer.close()
