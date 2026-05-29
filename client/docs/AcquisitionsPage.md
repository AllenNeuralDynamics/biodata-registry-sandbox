# AcquisitionsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Acquisitions]**](Acquisitions.md) |  | 

## Example

```python
from biodata_registry_api_client.models.acquisitions_page import AcquisitionsPage

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionsPage from a JSON string
acquisitions_page_instance = AcquisitionsPage.from_json(json)
# print the JSON string representation of the object
print(AcquisitionsPage.to_json())

# convert the object into a dict
acquisitions_page_dict = acquisitions_page_instance.to_dict()
# create an instance of AcquisitionsPage from a dict
acquisitions_page_from_dict = AcquisitionsPage.from_dict(acquisitions_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


