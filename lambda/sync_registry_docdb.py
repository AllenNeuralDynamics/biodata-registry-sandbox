from typing import List, Dict
from collections import defaultdict
from elasticsearch.helpers import bulk

from kafka import KafkaConsumer
import psycopg
from psycopg.rows import dict_row
from pymongo import MongoClient, ReplaceOne
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
from elasticsearch import Elasticsearch
import uuid
import os
import json
from copy import deepcopy

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

KAFKA_SERVER=os.environ['KAFKA_SERVER']
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
ES_URL=os.environ["ES_URL"]
ES_INDEX=os.environ["ES_INDEX"]

PG_INFO=f"host={PG_HOST} port={PG_PORT} dbname={PG_DBNAME} user={PG_USER} password={PG_PASSWORD}"

print("Starting Kafka consumer...")

consumer = KafkaConsumer(
    *TOPICS,
    bootstrap_servers=[KAFKA_SERVER],
    auto_offset_reset='earliest',
    allow_auto_create_topics=False,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Kafka Consumer listening!")

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

def add_records_to_databases(d_collection, e_client, p_records):
    replace_requests = []
    es_actions = []
    for k_data_asset_id, p_records in p_records.items():
        mongo_db_record = flatten_data_asset_view_records(p_records)
        if mongo_db_record is not None:
            es_record = deepcopy(mongo_db_record)
            hashed_uuid = str(uuid.uuid5(namespace, str(k_data_asset_id)))
            mongo_db_record["_id"] = hashed_uuid
            replace_requests.append(
                ReplaceOne(
                    {"_id": hashed_uuid},
                    mongo_db_record,
                    upsert=True
                )
            )
            es_actions.append(
                {
                    "_op_type": "index",
                    "_index": ES_INDEX,
                    "_id": hashed_uuid,
                    "_source": es_record
                }
            )
    if replace_requests:
        d_collection.bulk_write(replace_requests)
    if es_actions:
        bulk(e_client, es_actions)


def handle_data_asset_change(d_collection, p_conn, e_client, k_data_asset_id):
    if k_data_asset_id is not None:
        p_record_groups = defaultdict(list)
        with p_conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM data_asset_view WHERE data_asset_id = %s;",
                (k_data_asset_id,)
            )
            for p_record in cur:
                p_record_groups[k_data_asset_id].append(p_record)
        add_records_to_databases(d_collection, e_client, p_record_groups)

def handle_subject_change(d_collection, p_conn, e_client, k_subject_id):
    if k_subject_id is not None:
        p_record_groups = defaultdict(list)
        with p_conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM data_asset_view WHERE subject_id = %s;",
                (k_subject_id,)
            )
            for p_record in cur:
                k_data_asset_id = p_record["data_asset_id"]
                p_record_groups[k_data_asset_id].append(p_record)
        add_records_to_databases(d_collection, e_client, p_record_groups)


def handle_specimen_change(k_message, d_collection, p_conn):
    pass

def handle_specimen_procedure_change(k_message, d_collection, p_conn):
    pass

def handle_instrument_change(d_collection, p_conn, e_client, k_instrument_id):
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
        add_records_to_databases(d_collection, e_client, p_record_groups)

try:
    pg_conn_info = PG_INFO
    namespace = uuid.NAMESPACE_DNS
    print("Setting up clients...")
    with (
        MongoClient(
            host=MONGO_HOST,
            port=MONGO_PORT,
            username=MONGO_USERNAME,
            password=MONGO_PASSWORD
        ) as mongodb_client,
        psycopg.connect(pg_conn_info, row_factory=dict_row) as conn,
        Elasticsearch(ES_URL) as es_client
    ):
        db = mongodb_client[MONGO_DBNAME]
        opts = CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
        collection = db.get_collection(MONGO_DB_COLLECTION, codec_options=opts)
        print("Clients for databases established!")
        for message in consumer:
            print(f"Handling message: {message.topic}")
            match message.topic:
                case "registry.public.data_assets":
                    data_asset_id = message.value["payload"]["after"].get("id")
                    handle_data_asset_change(collection, conn, es_client, data_asset_id)
                case "registry.public.subjects":
                    subject_id = message.value["payload"]["after"].get("id")
                    handle_subject_change(collection, conn, es_client, subject_id)
                case "registry.public.specimens":
                    handle_specimen_change(message, collection, conn)
                case "registry.specimen_procedures":
                    handle_specimen_procedure_change(message, collection, conn)
                case "registry.public.subject_procedures":
                    subject_id = message.value["payload"]["after"].get("subject_id")
                    handle_subject_change(collection, conn, es_client, subject_id)
                case "registry.public.instruments":
                    instrument_id = message.value["payload"]["after"].get("instrument_id")
                    handle_instrument_change(collection, conn, es_client, instrument_id)
                case "registry.public.acquisitions":
                    data_asset_id = message.value["payload"]["after"].get("data_asset_id")
                    handle_data_asset_change(collection, conn, es_client, data_asset_id)
                case "registry.public.quality_controls":
                    data_asset_id = message.value["payload"]["after"].get("data_asset_id")
                    handle_data_asset_change(collection, conn, es_client, data_asset_id)
                case "registry.public.processes":
                    data_asset_id = message.value["payload"]["after"].get("output_data_asset_id")
                    handle_data_asset_change(collection, conn, es_client, data_asset_id)
                case _:
                    print("Unknown topic")
except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    print("Closing consumer...")
    consumer.close()
