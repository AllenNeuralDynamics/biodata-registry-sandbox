# Spaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**name** | **str** |  | 
**organization_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.spaces import Spaces

# TODO update the JSON string below
json = "{}"
# create an instance of Spaces from a JSON string
spaces_instance = Spaces.from_json(json)
# print the JSON string representation of the object
print(Spaces.to_json())

# convert the object into a dict
spaces_dict = spaces_instance.to_dict()
# create an instance of Spaces from a dict
spaces_from_dict = Spaces.from_dict(spaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


