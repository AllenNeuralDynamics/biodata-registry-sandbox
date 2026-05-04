# QualityControlUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**data_asset_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.quality_control_update import QualityControlUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of QualityControlUpdate from a JSON string
quality_control_update_instance = QualityControlUpdate.from_json(json)
# print the JSON string representation of the object
print(QualityControlUpdate.to_json())

# convert the object into a dict
quality_control_update_dict = quality_control_update_instance.to_dict()
# create an instance of QualityControlUpdate from a dict
quality_control_update_from_dict = QualityControlUpdate.from_dict(quality_control_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


