# SubjectCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.subject_create import SubjectCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectCreate from a JSON string
subject_create_instance = SubjectCreate.from_json(json)
# print the JSON string representation of the object
print(SubjectCreate.to_json())

# convert the object into a dict
subject_create_dict = subject_create_instance.to_dict()
# create an instance of SubjectCreate from a dict
subject_create_from_dict = SubjectCreate.from_dict(subject_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


