# AcquisitionView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisition_id** | **int** |  | [optional] 
**subject_id** | **int** |  | [optional] 
**acquisition_data** | **Dict[str, object]** |  | [optional] 
**instrument_name** | **str** |  | [optional] 
**instrument_data** | **Dict[str, object]** |  | [optional] 
**data_asset_location** | **str** |  | [optional] 
**data_asset_name** | **str** |  | [optional] 
**data_asset_data** | **Dict[str, object]** |  | [optional] 
**data_asset_external_links** | **Dict[str, object]** |  | [optional] 
**subject_name** | **str** |  | [optional] 
**subject_data** | **Dict[str, object]** |  | [optional] 
**quality_control_data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.acquisition_view import AcquisitionView

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionView from a JSON string
acquisition_view_instance = AcquisitionView.from_json(json)
# print the JSON string representation of the object
print(AcquisitionView.to_json())

# convert the object into a dict
acquisition_view_dict = acquisition_view_instance.to_dict()
# create an instance of AcquisitionView from a dict
acquisition_view_from_dict = AcquisitionView.from_dict(acquisition_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


