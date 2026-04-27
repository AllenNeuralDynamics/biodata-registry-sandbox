import urllib.request
import urllib.error
import json
import os

print("Creating ElasticSearch Index")

ES_URL=os.environ['ES_INDEX_URL']

index_config = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "data_asset_id": {"type": "unsigned_long"},
            "acquisition_id": {"type": "unsigned_long"},
            "subject_id": {"type": "unsigned_long"},
            "process_id": {"type": "unsigned_long"},
            "subject_procedure_id": {"type": "unsigned_long"},
            "instrument_id": {"type": "unsigned_long"},
            "processes_data": {"type": "object", "dynamic": "false"},
            "acquisition_data": {"type": "object", "dynamic": "false"},
            "instrument_name": {"type": "text"},
            "instrument_data": {"type": "object", "dynamic": "false"},
            "data_asset_location": {"type": "text"},
            "data_asset_name": {"type": "text"},
            "data_asset_data": {"type": "object", "dynamic": "false"},
            "data_asset_external_links": {"type": "object", "dynamic": "false"},
            "subject_procedures_data": {"type": "object", "dynamic": "false"},
            "quality_control_data": {"type": "object", "dynamic": "false"},
            "subjects": {"type": "object", "dynamic": "false"},
        }
    }
}

headers = {"Content-Type": "application/json"}
req = urllib.request.Request(
    ES_URL,
    headers=headers,
    data=json.dumps(index_config).encode('utf-8'),
    method='PUT'
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode('utf-8'))
    print(result)

print("Finished creating ElasticSearch index!")
