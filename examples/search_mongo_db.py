from pymongo import MongoClient
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
from biodata_registry_api_client import (
    Configuration,
    ApiClient,
    CoreApi,
    ViewsApi,
)
configuration = Configuration(
    host = "http://localhost:5000"
)

api_client = ApiClient(configuration)
core_api = CoreApi(api_client)
views_api = ViewsApi(api_client)

with MongoClient(
        host="localhost",
        port=27017,
        username="admin",
        password="admin_password"
    ) as mongodb_client:
    db = mongodb_client["metadata"]
    opts = CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
    collection = db.get_collection("data_assets", codec_options=opts)
    results = collection.find().limit(1).to_list()

print(results[0]["subjects"])

