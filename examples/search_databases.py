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

subject_data = core_api.get_subject(id=1)
data_asset_view = views_api.get_data_asset_view(
    data_asset_name__ilike="behavior_774600",
    limit=10
)

# TODO: Write own paginate method in client library
all_rows = data_asset_view.results
while data_asset_view.has_more:
    data_asset_view = views_api.get_data_asset_view(
        data_asset_name__ilike="behavior_774600",
        next_token=data_asset_view.next_token,
        limit=10
    )
    all_rows.extend(data_asset_view.results)

for row in all_rows:
    print(row.data_asset_name)

# TODO: Put these behind the api in the future instead of allowing people
#  direct access

## Postgres
pg_conn_info=f"host=localhost port=5432 dbname=registry user=user password=password"

pg_results = defaultdict(list)
with psycopg.connect(pg_conn_info, row_factory=dict_row) as conn:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM data_asset_view WHERE data_asset_id = %s;",
            (1,)
        )
        for p_record in cur:
            k_data_asset_id = p_record["data_asset_id"]
            pg_results[k_data_asset_id].append(p_record)
pg_results = json.loads(json.dumps(pg_results))
print(pg_results)

## MongoDB
with MongoClient(
        host="localhost",
        port=27017,
        username="admin",
        password="admin_password"
    ) as mongodb_client:
    db = mongodb_client["metadata"]
    opts = CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
    collection = db.get_collection("data_assets", codec_options=opts)
    collection_count = collection.count_documents({})
    mongodb_results = collection.find({"data_asset_id": 2}).to_list()

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
