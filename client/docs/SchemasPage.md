# SchemasPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Schemas]**](Schemas.md) |  | 

## Example

```python
from biodata_registry_api_client.models.schemas_page import SchemasPage

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasPage from a JSON string
schemas_page_instance = SchemasPage.from_json(json)
# print the JSON string representation of the object
print(SchemasPage.to_json())

# convert the object into a dict
schemas_page_dict = schemas_page_instance.to_dict()
# create an instance of SchemasPage from a dict
schemas_page_from_dict = SchemasPage.from_dict(schemas_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


