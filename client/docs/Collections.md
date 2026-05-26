# Collections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**last_updated_by** | **int** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | 
**owner_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.collections import Collections

# TODO update the JSON string below
json = "{}"
# create an instance of Collections from a JSON string
collections_instance = Collections.from_json(json)
# print the JSON string representation of the object
print(Collections.to_json())

# convert the object into a dict
collections_dict = collections_instance.to_dict()
# create an instance of Collections from a dict
collections_from_dict = Collections.from_dict(collections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


