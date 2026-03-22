# SpaceAdmins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.space_admins import SpaceAdmins

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceAdmins from a JSON string
space_admins_instance = SpaceAdmins.from_json(json)
# print the JSON string representation of the object
print(SpaceAdmins.to_json())

# convert the object into a dict
space_admins_dict = space_admins_instance.to_dict()
# create an instance of SpaceAdmins from a dict
space_admins_from_dict = SpaceAdmins.from_dict(space_admins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


