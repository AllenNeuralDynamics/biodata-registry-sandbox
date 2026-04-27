from pymongo import MongoClient
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
from biodata_registry_api_client import (
    Configuration,
    ApiClient,
    CoreApi,
    ViewsApi,
)
from elasticsearch import Elasticsearch
from sqlmodel import create_engine, text

## Using the API client

configuration = Configuration(
    host = "http://localhost:5000"
)

api_client = ApiClient(configuration)
core_api = CoreApi(api_client)
views_api = ViewsApi(api_client)

subject_data = core_api.get_subjects(limit=1)
data_asset_view = views_api.get_data_asset_view(limit=1)

# TODO: Put these behind the api in the future instead of allowing people
#  direct access

## Postgres

engine = create_engine(
    "postgresql://user:password@localhost:5432/registry",
    echo=True
)

pg_results = []
with engine.connect() as connection:
    query = text("SELECT * FROM data_asset_view LIMIT 5;")
    result = connection.execute(query)
    for row in result:
        pg_results.append(row)

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
    mongodb_results = collection.find().limit(1).to_list()

print(mongodb_results[0]["subjects"])

## ElasticSearch

es_client = Elasticsearch("http://localhost:9200")

es_response = es_client.search(
    index="data_assets",
    query={"match": {"instrument_name": "SmartSPIM1-7_2023-10-24"}},
    size=1
)

print(es_response)
