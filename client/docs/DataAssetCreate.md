# DataAssetCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**location** | **str** |  | 
**external_links** | **Dict[str, object]** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.data_asset_create import DataAssetCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DataAssetCreate from a JSON string
data_asset_create_instance = DataAssetCreate.from_json(json)
# print the JSON string representation of the object
print(DataAssetCreate.to_json())

# convert the object into a dict
data_asset_create_dict = data_asset_create_instance.to_dict()
# create an instance of DataAssetCreate from a dict
data_asset_create_from_dict = DataAssetCreate.from_dict(data_asset_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


