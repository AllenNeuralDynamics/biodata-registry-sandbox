# CollectionsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Collections]**](Collections.md) |  | 

## Example

```python
from biodata_registry_api_client.models.collections_page import CollectionsPage

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsPage from a JSON string
collections_page_instance = CollectionsPage.from_json(json)
# print the JSON string representation of the object
print(CollectionsPage.to_json())

# convert the object into a dict
collections_page_dict = collections_page_instance.to_dict()
# create an instance of CollectionsPage from a dict
collections_page_from_dict = CollectionsPage.from_dict(collections_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


