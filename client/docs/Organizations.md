# Organizations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**last_updated_by** | **int** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from biodata_registry_api_client.models.organizations import Organizations

# TODO update the JSON string below
json = "{}"
# create an instance of Organizations from a JSON string
organizations_instance = Organizations.from_json(json)
# print the JSON string representation of the object
print(Organizations.to_json())

# convert the object into a dict
organizations_dict = organizations_instance.to_dict()
# create an instance of Organizations from a dict
organizations_from_dict = Organizations.from_dict(organizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


