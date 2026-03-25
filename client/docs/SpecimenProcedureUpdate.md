# SpecimenProcedureUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.specimen_procedure_update import SpecimenProcedureUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SpecimenProcedureUpdate from a JSON string
specimen_procedure_update_instance = SpecimenProcedureUpdate.from_json(json)
# print the JSON string representation of the object
print(SpecimenProcedureUpdate.to_json())

# convert the object into a dict
specimen_procedure_update_dict = specimen_procedure_update_instance.to_dict()
# create an instance of SpecimenProcedureUpdate from a dict
specimen_procedure_update_from_dict = SpecimenProcedureUpdate.from_dict(specimen_procedure_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


