# SubjectUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.subject_update import SubjectUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectUpdate from a JSON string
subject_update_instance = SubjectUpdate.from_json(json)
# print the JSON string representation of the object
print(SubjectUpdate.to_json())

# convert the object into a dict
subject_update_dict = subject_update_instance.to_dict()
# create an instance of SubjectUpdate from a dict
subject_update_from_dict = SubjectUpdate.from_dict(subject_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


