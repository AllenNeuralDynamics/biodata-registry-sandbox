# SchemaEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from biodata_registry_api_client.models.schema_entities import SchemaEntities

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaEntities from a JSON string
schema_entities_instance = SchemaEntities.from_json(json)
# print the JSON string representation of the object
print(SchemaEntities.to_json())

# convert the object into a dict
schema_entities_dict = schema_entities_instance.to_dict()
# create an instance of SchemaEntities from a dict
schema_entities_from_dict = SchemaEntities.from_dict(schema_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


