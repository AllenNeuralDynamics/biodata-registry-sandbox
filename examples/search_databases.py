from pymongo import MongoClient
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
from biodata_registry_api_client import (
    Configuration,
    ApiClient,
    CoreApi,
    ViewsApi,
)
# from elasticsearch import Elasticsearch
import psycopg
from psycopg.rows import dict_row
from collections import defaultdict
import json

## Using the API client

configuration = Configuration(
    host = "http://localhost:5000"
)

api_client = ApiClient(configuration)
core_api = CoreApi(api_client)
views_api = ViewsApi(api_client)

subject_data = core_api.get_subjects(limit=1)
data_asset_view = views_api.get_data_asset_view(data_asset_id=1)

# TODO: Put these behind the api in the future instead of allowing people
#  direct access

## Postgres
pg_conn_info=f"host=localhost port=5432 dbname=registry user=user password=password"

pg_results = []
with psycopg.connect(pg_conn_info, row_factory=dict_row) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM data_asset_view;")
        for p_record in cur:
            pg_results.append(p_record)
pg_results = json.loads(json.dumps(pg_results))
print(pg_results)

with psycopg.connect(pg_conn_info) as conn:
    with conn.cursor() as cur:
        cur.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY data_asset_view;")

## MongoDB
with MongoClient(
        host="aind-biodata-registry",
        port=27017,
        username="admin",
        password="admin_password"
    ) as mongodb_client:
    db = mongodb_client["metadata"]
    opts = CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
    collection = db.get_collection("data_assets", codec_options=opts)
    mongodb_results = collection.count_documents({})
    # mongodb_results = collection.find().limit(1).to_list()

print(mongodb_results[0]["subjects"])

## ElasticSearch

# es_client = Elasticsearch("http://localhost:9200")
#
# es_response = es_client.search(
#     index="data_assets",
#     query={"match": {"instrument_name": "SmartSPIM1-7_2023-10-24"}},
#     size=1
# )
#
# print(es_response)
