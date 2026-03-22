# SchemaCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**schema_entity_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.schema_create import SchemaCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaCreate from a JSON string
schema_create_instance = SchemaCreate.from_json(json)
# print the JSON string representation of the object
print(SchemaCreate.to_json())

# convert the object into a dict
schema_create_dict = schema_create_instance.to_dict()
# create an instance of SchemaCreate from a dict
schema_create_from_dict = SchemaCreate.from_dict(schema_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


