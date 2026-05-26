# QualityControls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**last_updated_by** | **int** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**data_asset_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.quality_controls import QualityControls

# TODO update the JSON string below
json = "{}"
# create an instance of QualityControls from a JSON string
quality_controls_instance = QualityControls.from_json(json)
# print the JSON string representation of the object
print(QualityControls.to_json())

# convert the object into a dict
quality_controls_dict = quality_controls_instance.to_dict()
# create an instance of QualityControls from a dict
quality_controls_from_dict = QualityControls.from_dict(quality_controls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


