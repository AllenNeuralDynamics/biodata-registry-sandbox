# SubjectProcedures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**data** | **List[Dict[str, object]]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**subject_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.subject_procedures import SubjectProcedures

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectProcedures from a JSON string
subject_procedures_instance = SubjectProcedures.from_json(json)
# print the JSON string representation of the object
print(SubjectProcedures.to_json())

# convert the object into a dict
subject_procedures_dict = subject_procedures_instance.to_dict()
# create an instance of SubjectProcedures from a dict
subject_procedures_from_dict = SubjectProcedures.from_dict(subject_procedures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


