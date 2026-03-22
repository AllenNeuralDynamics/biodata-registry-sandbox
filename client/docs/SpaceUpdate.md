# SpaceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.space_update import SpaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceUpdate from a JSON string
space_update_instance = SpaceUpdate.from_json(json)
# print the JSON string representation of the object
print(SpaceUpdate.to_json())

# convert the object into a dict
space_update_dict = space_update_instance.to_dict()
# create an instance of SpaceUpdate from a dict
space_update_from_dict = SpaceUpdate.from_dict(space_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


