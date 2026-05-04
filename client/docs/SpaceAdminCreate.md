# SpaceAdminCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.space_admin_create import SpaceAdminCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceAdminCreate from a JSON string
space_admin_create_instance = SpaceAdminCreate.from_json(json)
# print the JSON string representation of the object
print(SpaceAdminCreate.to_json())

# convert the object into a dict
space_admin_create_dict = space_admin_create_instance.to_dict()
# create an instance of SpaceAdminCreate from a dict
space_admin_create_from_dict = SpaceAdminCreate.from_dict(space_admin_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


