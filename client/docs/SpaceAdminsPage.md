# SpaceAdminsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[SpaceAdmins]**](SpaceAdmins.md) |  | 

## Example

```python
from biodata_registry_api_client.models.space_admins_page import SpaceAdminsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceAdminsPage from a JSON string
space_admins_page_instance = SpaceAdminsPage.from_json(json)
# print the JSON string representation of the object
print(SpaceAdminsPage.to_json())

# convert the object into a dict
space_admins_page_dict = space_admins_page_instance.to_dict()
# create an instance of SpaceAdminsPage from a dict
space_admins_page_from_dict = SpaceAdminsPage.from_dict(space_admins_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


