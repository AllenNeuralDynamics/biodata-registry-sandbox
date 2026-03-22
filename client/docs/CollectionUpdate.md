# CollectionUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.collection_update import CollectionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionUpdate from a JSON string
collection_update_instance = CollectionUpdate.from_json(json)
# print the JSON string representation of the object
print(CollectionUpdate.to_json())

# convert the object into a dict
collection_update_dict = collection_update_instance.to_dict()
# create an instance of CollectionUpdate from a dict
collection_update_from_dict = CollectionUpdate.from_dict(collection_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


