# QualityControlCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**data_asset_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.quality_control_create import QualityControlCreate

# TODO update the JSON string below
json = "{}"
# create an instance of QualityControlCreate from a JSON string
quality_control_create_instance = QualityControlCreate.from_json(json)
# print the JSON string representation of the object
print(QualityControlCreate.to_json())

# convert the object into a dict
quality_control_create_dict = quality_control_create_instance.to_dict()
# create an instance of QualityControlCreate from a dict
quality_control_create_from_dict = QualityControlCreate.from_dict(quality_control_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


