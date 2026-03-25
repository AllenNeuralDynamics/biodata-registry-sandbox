# AcquisitionUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**data_asset_id** | **int** |  | [optional] 
**instrument_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.acquisition_update import AcquisitionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionUpdate from a JSON string
acquisition_update_instance = AcquisitionUpdate.from_json(json)
# print the JSON string representation of the object
print(AcquisitionUpdate.to_json())

# convert the object into a dict
acquisition_update_dict = acquisition_update_instance.to_dict()
# create an instance of AcquisitionUpdate from a dict
acquisition_update_from_dict = AcquisitionUpdate.from_dict(acquisition_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


