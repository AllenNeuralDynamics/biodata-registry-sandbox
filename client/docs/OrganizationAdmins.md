# OrganizationAdmins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.organization_admins import OrganizationAdmins

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAdmins from a JSON string
organization_admins_instance = OrganizationAdmins.from_json(json)
# print the JSON string representation of the object
print(OrganizationAdmins.to_json())

# convert the object into a dict
organization_admins_dict = organization_admins_instance.to_dict()
# create an instance of OrganizationAdmins from a dict
organization_admins_from_dict = OrganizationAdmins.from_dict(organization_admins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


