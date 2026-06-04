# SpecimenProcedures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.specimen_procedures import SpecimenProcedures

# TODO update the JSON string below
json = "{}"
# create an instance of SpecimenProcedures from a JSON string
specimen_procedures_instance = SpecimenProcedures.from_json(json)
# print the JSON string representation of the object
print(SpecimenProcedures.to_json())

# convert the object into a dict
specimen_procedures_dict = specimen_procedures_instance.to_dict()
# create an instance of SpecimenProcedures from a dict
specimen_procedures_from_dict = SpecimenProcedures.from_dict(specimen_procedures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


