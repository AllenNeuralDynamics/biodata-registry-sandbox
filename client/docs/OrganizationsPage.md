# OrganizationsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Organizations]**](Organizations.md) |  | 

## Example

```python
from biodata_registry_api_client.models.organizations_page import OrganizationsPage

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsPage from a JSON string
organizations_page_instance = OrganizationsPage.from_json(json)
# print the JSON string representation of the object
print(OrganizationsPage.to_json())

# convert the object into a dict
organizations_page_dict = organizations_page_instance.to_dict()
# create an instance of OrganizationsPage from a dict
organizations_page_from_dict = OrganizationsPage.from_dict(organizations_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


