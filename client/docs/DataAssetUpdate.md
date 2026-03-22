# DataAssetUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**external_links** | **Dict[str, object]** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.data_asset_update import DataAssetUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DataAssetUpdate from a JSON string
data_asset_update_instance = DataAssetUpdate.from_json(json)
# print the JSON string representation of the object
print(DataAssetUpdate.to_json())

# convert the object into a dict
data_asset_update_dict = data_asset_update_instance.to_dict()
# create an instance of DataAssetUpdate from a dict
data_asset_update_from_dict = DataAssetUpdate.from_dict(data_asset_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


