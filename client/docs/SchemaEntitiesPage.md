# SchemaEntitiesPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[SchemaEntities]**](SchemaEntities.md) |  | 

## Example

```python
from biodata_registry_api_client.models.schema_entities_page import SchemaEntitiesPage

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaEntitiesPage from a JSON string
schema_entities_page_instance = SchemaEntitiesPage.from_json(json)
# print the JSON string representation of the object
print(SchemaEntitiesPage.to_json())

# convert the object into a dict
schema_entities_page_dict = schema_entities_page_instance.to_dict()
# create an instance of SchemaEntitiesPage from a dict
schema_entities_page_from_dict = SchemaEntitiesPage.from_dict(schema_entities_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


