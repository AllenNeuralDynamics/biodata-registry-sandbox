# DataAssetView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_asset_id** | **int** |  | [optional] 
**acquisition_id** | **int** |  | [optional] 
**process_id** | **int** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**acquisition_data** | **Dict[str, object]** |  | [optional] 
**processes_data** | **Dict[str, object]** |  | [optional] 
**instrument_name** | **str** |  | [optional] 
**instrument_data** | **Dict[str, object]** |  | [optional] 
**data_asset_location** | **str** |  | [optional] 
**data_asset_name** | **str** |  | [optional] 
**data_asset_data** | **Dict[str, object]** |  | [optional] 
**data_asset_external_links** | **Dict[str, object]** |  | [optional] 
**subjects** | **List[Optional[Dict[str, object]]]** |  | [optional] 
**subject_procedures** | **List[Optional[Dict[str, object]]]** |  | [optional] 
**quality_control_metrics** | **List[Optional[Dict[str, object]]]** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.data_asset_view import DataAssetView

# TODO update the JSON string below
json = "{}"
# create an instance of DataAssetView from a JSON string
data_asset_view_instance = DataAssetView.from_json(json)
# print the JSON string representation of the object
print(DataAssetView.to_json())

# convert the object into a dict
data_asset_view_dict = data_asset_view_instance.to_dict()
# create an instance of DataAssetView from a dict
data_asset_view_from_dict = DataAssetView.from_dict(data_asset_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


