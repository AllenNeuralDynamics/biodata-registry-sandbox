# DataAssetViewsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[DataAssetView]**](DataAssetView.md) |  | 

## Example

```python
from biodata_registry_api_client.models.data_asset_views_page import DataAssetViewsPage

# TODO update the JSON string below
json = "{}"
# create an instance of DataAssetViewsPage from a JSON string
data_asset_views_page_instance = DataAssetViewsPage.from_json(json)
# print the JSON string representation of the object
print(DataAssetViewsPage.to_json())

# convert the object into a dict
data_asset_views_page_dict = data_asset_views_page_instance.to_dict()
# create an instance of DataAssetViewsPage from a dict
data_asset_views_page_from_dict = DataAssetViewsPage.from_dict(data_asset_views_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


