# SchemaEntityCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from biodata_registry_api_client.models.schema_entity_create import SchemaEntityCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaEntityCreate from a JSON string
schema_entity_create_instance = SchemaEntityCreate.from_json(json)
# print the JSON string representation of the object
print(SchemaEntityCreate.to_json())

# convert the object into a dict
schema_entity_create_dict = schema_entity_create_instance.to_dict()
# create an instance of SchemaEntityCreate from a dict
schema_entity_create_from_dict = SchemaEntityCreate.from_dict(schema_entity_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


