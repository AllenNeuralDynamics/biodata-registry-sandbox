# Legacy code

# import requests
# import json
# from pathlib import Path
#
# # Add Users
# response = requests.post(
#     'http://localhost:5000/users',
#     params={'name': 'Joe Smith', 'contact': 'joe.smith@example.com'}
# )
# print(response.status_code)
#
# response = requests.post(
#     'http://localhost:5000/users',
#     params={'name': 'Anna Apple', 'contact': 'anna.apple@example.com'}
# )
# print(response.status_code)
#
#
# # Add Organizations
# response = requests.post(
#     'http://localhost:5000/organizations',
#     params={'name': 'AIND'}
# )
# print(response.status_code)
#
# response = requests.post(
#     'http://localhost:5000/organizations',
#     params={'name': 'AIBS'}
# )
# print(response.status_code)
#
#
# # Create Spaces
# response = requests.post(
#     'http://localhost:5000/spaces',
#     params={'name': 'Space1', 'organization_id': 1}
# )
# print(response.status_code)
#
#
# # Create Space Admins
# response = requests.post(
#     'http://localhost:5000/space_admins',
#     params={'user_id': 2, "space_id": 1}
# )
# print(response.status_code)
#
#
# # Create Organization Admins
# response = requests.post(
#     'http://localhost:5000/organization_admins',
#     params={'user_id': 2, "organization_id": 1}
# )
# print(response.status_code)
#
#
# # Create Collections
# response = requests.post(
#     'http://localhost:5000/collections',
#     params={'name': "test_collection", "description": "Test Collection", "owner_id": 1}
# )
# print(response.status_code)
#
#
# # Create Schema Entities
# response = requests.post(
#     'http://localhost:5000/schema_entities',
#     params={'name': "acquisition"}
# )
# print(response.status_code)
#
# response = requests.post(
#     'http://localhost:5000/schema_entities',
#     params={'name': "data_description"}
# )
# print(response.status_code)
#
# response = requests.post(
#     'http://localhost:5000/schema_entities',
#     params={'name': "instrument"}
# )
# print(response.status_code)
#
# response = requests.post(
#     'http://localhost:5000/schema_entities',
#     params={'name': "procedures"}
# )
# print(response.status_code)
#
# response = requests.post(
#     'http://localhost:5000/schema_entities',
#     params={'name': "processing"}
# )
# print(response.status_code)
#
# response = requests.post(
#     'http://localhost:5000/schema_entities',
#     params={'name': "quality_control"}
# )
# print(response.status_code)
#
# response = requests.post(
#     'http://localhost:5000/schema_entities',
#     params={'name': "subject"}
# )
# print(response.status_code)
#
#
# # Create Schemas
# with open(Path("schema_definitions") / "acquisition_schema.json", "r") as f:
#     data = json.load(f)
# response = requests.post(
#     'http://localhost:5000/schemas',
#     params={
#         'name': "acquisition",
#         "version": data["properties"]["schema_version"]["const"],
#         "schema_entity_id": 1
#     },
#     json=data
# )
# print(response.status_code)
#
# with open(Path("schema_definitions") / "data_description_schema.json", "r") as f:
#     data = json.load(f)
# response = requests.post(
#     'http://localhost:5000/schemas',
#     params={
#         'name': "data_description",
#         "version": data["properties"]["schema_version"]["const"],
#         "schema_entity_id": 2
#     },
#     json=data
# )
# print(response.status_code)
#
# with open(Path("schema_definitions") / "instrument_schema.json", "r") as f:
#     data = json.load(f)
# response = requests.post(
#     'http://localhost:5000/schemas',
#     params={
#         'name': "instrument",
#         "version": data["properties"]["schema_version"]["const"],
#         "schema_entity_id": 3
#     },
#     json=data
# )
# print(response.status_code)
#
# with open(Path("schema_definitions") / "procedures_schema.json", "r") as f:
#     data = json.load(f)
# response = requests.post(
#     'http://localhost:5000/schemas',
#     params={
#         'name': "procedures",
#         "version": data["properties"]["schema_version"]["const"],
#         "schema_entity_id": 4
#     },
#     json=data
# )
# print(response.status_code)
#
# with open(Path("schema_definitions") / "processing_schema.json", "r") as f:
#     data = json.load(f)
# response = requests.post(
#     'http://localhost:5000/schemas',
#     params={
#         'name': "processing",
#         "version": data["properties"]["schema_version"]["const"],
#         "schema_entity_id": 5
#     },
#     json=data
# )
# print(response.status_code)
#
# with open(Path("schema_definitions") / "quality_control_schema.json", "r") as f:
#     data = json.load(f)
# response = requests.post(
#     'http://localhost:5000/schemas',
#     params={
#         'name': "quality_control",
#         "version": data["properties"]["schema_version"]["const"],
#         "schema_entity_id": 6
#     },
#     json=data
# )
# print(response.status_code)
#
# with open(Path("schema_definitions") / "subject_schema.json", "r") as f:
#     data = json.load(f)
# response = requests.post(
#     'http://localhost:5000/schemas',
#     params={
#         'name': "subject",
#         "version": data["properties"]["schema_version"]["const"],
#         "schema_entity_id": 7
#     },
#     json=data
# )
# print(response.status_code)
