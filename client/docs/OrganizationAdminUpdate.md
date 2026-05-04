# OrganizationAdminUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.organization_admin_update import OrganizationAdminUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAdminUpdate from a JSON string
organization_admin_update_instance = OrganizationAdminUpdate.from_json(json)
# print the JSON string representation of the object
print(OrganizationAdminUpdate.to_json())

# convert the object into a dict
organization_admin_update_dict = organization_admin_update_instance.to_dict()
# create an instance of OrganizationAdminUpdate from a dict
organization_admin_update_from_dict = OrganizationAdminUpdate.from_dict(organization_admin_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


