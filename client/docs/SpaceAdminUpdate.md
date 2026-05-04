# SpaceAdminUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.space_admin_update import SpaceAdminUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceAdminUpdate from a JSON string
space_admin_update_instance = SpaceAdminUpdate.from_json(json)
# print the JSON string representation of the object
print(SpaceAdminUpdate.to_json())

# convert the object into a dict
space_admin_update_dict = space_admin_update_instance.to_dict()
# create an instance of SpaceAdminUpdate from a dict
space_admin_update_from_dict = SpaceAdminUpdate.from_dict(space_admin_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


