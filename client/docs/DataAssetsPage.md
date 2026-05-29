# DataAssetsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[DataAssets]**](DataAssets.md) |  | 

## Example

```python
from biodata_registry_api_client.models.data_assets_page import DataAssetsPage

# TODO update the JSON string below
json = "{}"
# create an instance of DataAssetsPage from a JSON string
data_assets_page_instance = DataAssetsPage.from_json(json)
# print the JSON string representation of the object
print(DataAssetsPage.to_json())

# convert the object into a dict
data_assets_page_dict = data_assets_page_instance.to_dict()
# create an instance of DataAssetsPage from a dict
data_assets_page_from_dict = DataAssetsPage.from_dict(data_assets_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


