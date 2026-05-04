# SchemaUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_entity_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.schema_update import SchemaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaUpdate from a JSON string
schema_update_instance = SchemaUpdate.from_json(json)
# print the JSON string representation of the object
print(SchemaUpdate.to_json())

# convert the object into a dict
schema_update_dict = schema_update_instance.to_dict()
# create an instance of SchemaUpdate from a dict
schema_update_from_dict = SchemaUpdate.from_dict(schema_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


