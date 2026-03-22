# OrganizationAdminCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.organization_admin_create import OrganizationAdminCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAdminCreate from a JSON string
organization_admin_create_instance = OrganizationAdminCreate.from_json(json)
# print the JSON string representation of the object
print(OrganizationAdminCreate.to_json())

# convert the object into a dict
organization_admin_create_dict = organization_admin_create_instance.to_dict()
# create an instance of OrganizationAdminCreate from a dict
organization_admin_create_from_dict = OrganizationAdminCreate.from_dict(organization_admin_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


