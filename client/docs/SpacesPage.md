# SpacesPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Spaces]**](Spaces.md) |  | 

## Example

```python
from biodata_registry_api_client.models.spaces_page import SpacesPage

# TODO update the JSON string below
json = "{}"
# create an instance of SpacesPage from a JSON string
spaces_page_instance = SpacesPage.from_json(json)
# print the JSON string representation of the object
print(SpacesPage.to_json())

# convert the object into a dict
spaces_page_dict = spaces_page_instance.to_dict()
# create an instance of SpacesPage from a dict
spaces_page_from_dict = SpacesPage.from_dict(spaces_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


