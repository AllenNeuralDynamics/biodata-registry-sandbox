# SubjectProcedureUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[Optional[Dict[str, object]]]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**subject_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.subject_procedure_update import SubjectProcedureUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectProcedureUpdate from a JSON string
subject_procedure_update_instance = SubjectProcedureUpdate.from_json(json)
# print the JSON string representation of the object
print(SubjectProcedureUpdate.to_json())

# convert the object into a dict
subject_procedure_update_dict = subject_procedure_update_instance.to_dict()
# create an instance of SubjectProcedureUpdate from a dict
subject_procedure_update_from_dict = SubjectProcedureUpdate.from_dict(subject_procedure_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


