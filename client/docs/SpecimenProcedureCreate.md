# SpecimenProcedureCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.specimen_procedure_create import SpecimenProcedureCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SpecimenProcedureCreate from a JSON string
specimen_procedure_create_instance = SpecimenProcedureCreate.from_json(json)
# print the JSON string representation of the object
print(SpecimenProcedureCreate.to_json())

# convert the object into a dict
specimen_procedure_create_dict = specimen_procedure_create_instance.to_dict()
# create an instance of SpecimenProcedureCreate from a dict
specimen_procedure_create_from_dict = SpecimenProcedureCreate.from_dict(specimen_procedure_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


