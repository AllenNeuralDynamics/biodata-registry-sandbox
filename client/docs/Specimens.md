# Specimens


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**name** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**subject_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.specimens import Specimens

# TODO update the JSON string below
json = "{}"
# create an instance of Specimens from a JSON string
specimens_instance = Specimens.from_json(json)
# print the JSON string representation of the object
print(Specimens.to_json())

# convert the object into a dict
specimens_dict = specimens_instance.to_dict()
# create an instance of Specimens from a dict
specimens_from_dict = Specimens.from_dict(specimens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


