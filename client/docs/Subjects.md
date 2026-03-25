# Subjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.subjects import Subjects

# TODO update the JSON string below
json = "{}"
# create an instance of Subjects from a JSON string
subjects_instance = Subjects.from_json(json)
# print the JSON string representation of the object
print(Subjects.to_json())

# convert the object into a dict
subjects_dict = subjects_instance.to_dict()
# create an instance of Subjects from a dict
subjects_from_dict = Subjects.from_dict(subjects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


