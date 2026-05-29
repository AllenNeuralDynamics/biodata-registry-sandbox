# InstrumentsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Instruments]**](Instruments.md) |  | 

## Example

```python
from biodata_registry_api_client.models.instruments_page import InstrumentsPage

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentsPage from a JSON string
instruments_page_instance = InstrumentsPage.from_json(json)
# print the JSON string representation of the object
print(InstrumentsPage.to_json())

# convert the object into a dict
instruments_page_dict = instruments_page_instance.to_dict()
# create an instance of InstrumentsPage from a dict
instruments_page_from_dict = InstrumentsPage.from_dict(instruments_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


