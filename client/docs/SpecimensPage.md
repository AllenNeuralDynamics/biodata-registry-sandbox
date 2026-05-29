# SpecimensPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Specimens]**](Specimens.md) |  | 

## Example

```python
from biodata_registry_api_client.models.specimens_page import SpecimensPage

# TODO update the JSON string below
json = "{}"
# create an instance of SpecimensPage from a JSON string
specimens_page_instance = SpecimensPage.from_json(json)
# print the JSON string representation of the object
print(SpecimensPage.to_json())

# convert the object into a dict
specimens_page_dict = specimens_page_instance.to_dict()
# create an instance of SpecimensPage from a dict
specimens_page_from_dict = SpecimensPage.from_dict(specimens_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


