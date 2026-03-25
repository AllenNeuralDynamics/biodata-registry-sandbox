# SubjectProcedureCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**subject_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.subject_procedure_create import SubjectProcedureCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectProcedureCreate from a JSON string
subject_procedure_create_instance = SubjectProcedureCreate.from_json(json)
# print the JSON string representation of the object
print(SubjectProcedureCreate.to_json())

# convert the object into a dict
subject_procedure_create_dict = subject_procedure_create_instance.to_dict()
# create an instance of SubjectProcedureCreate from a dict
subject_procedure_create_from_dict = SubjectProcedureCreate.from_dict(subject_procedure_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


