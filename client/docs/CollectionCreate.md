# CollectionCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**owner_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.collection_create import CollectionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionCreate from a JSON string
collection_create_instance = CollectionCreate.from_json(json)
# print the JSON string representation of the object
print(CollectionCreate.to_json())

# convert the object into a dict
collection_create_dict = collection_create_instance.to_dict()
# create an instance of CollectionCreate from a dict
collection_create_from_dict = CollectionCreate.from_dict(collection_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


