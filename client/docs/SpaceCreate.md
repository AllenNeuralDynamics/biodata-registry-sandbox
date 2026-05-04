# SpaceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**organization_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.space_create import SpaceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceCreate from a JSON string
space_create_instance = SpaceCreate.from_json(json)
# print the JSON string representation of the object
print(SpaceCreate.to_json())

# convert the object into a dict
space_create_dict = space_create_instance.to_dict()
# create an instance of SpaceCreate from a dict
space_create_from_dict = SpaceCreate.from_dict(space_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


