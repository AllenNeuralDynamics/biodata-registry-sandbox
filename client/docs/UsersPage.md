# UsersPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Users]**](Users.md) |  | 

## Example

```python
from biodata_registry_api_client.models.users_page import UsersPage

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPage from a JSON string
users_page_instance = UsersPage.from_json(json)
# print the JSON string representation of the object
print(UsersPage.to_json())

# convert the object into a dict
users_page_dict = users_page_instance.to_dict()
# create an instance of UsersPage from a dict
users_page_from_dict = UsersPage.from_dict(users_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


