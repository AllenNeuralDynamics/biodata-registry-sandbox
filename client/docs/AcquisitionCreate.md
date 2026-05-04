# AcquisitionCreate


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
from biodata_registry_api_client.models.acquisition_create import AcquisitionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionCreate from a JSON string
acquisition_create_instance = AcquisitionCreate.from_json(json)
# print the JSON string representation of the object
print(AcquisitionCreate.to_json())

# convert the object into a dict
acquisition_create_dict = acquisition_create_instance.to_dict()
# create an instance of AcquisitionCreate from a dict
acquisition_create_from_dict = AcquisitionCreate.from_dict(acquisition_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


