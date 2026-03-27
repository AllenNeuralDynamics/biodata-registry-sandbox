# DataAssets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**external_links** | **Dict[str, object]** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.data_assets import DataAssets

# TODO update the JSON string below
json = "{}"
# create an instance of DataAssets from a JSON string
data_assets_instance = DataAssets.from_json(json)
# print the JSON string representation of the object
print(DataAssets.to_json())

# convert the object into a dict
data_assets_dict = data_assets_instance.to_dict()
# create an instance of DataAssets from a dict
data_assets_from_dict = DataAssets.from_dict(data_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


