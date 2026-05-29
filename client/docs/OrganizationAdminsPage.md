# OrganizationAdminsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[OrganizationAdmins]**](OrganizationAdmins.md) |  | 

## Example

```python
from biodata_registry_api_client.models.organization_admins_page import OrganizationAdminsPage

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAdminsPage from a JSON string
organization_admins_page_instance = OrganizationAdminsPage.from_json(json)
# print the JSON string representation of the object
print(OrganizationAdminsPage.to_json())

# convert the object into a dict
organization_admins_page_dict = organization_admins_page_instance.to_dict()
# create an instance of OrganizationAdminsPage from a dict
organization_admins_page_from_dict = OrganizationAdminsPage.from_dict(organization_admins_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


