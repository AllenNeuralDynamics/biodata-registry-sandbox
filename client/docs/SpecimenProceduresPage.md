# SpecimenProceduresPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[SpecimenProcedures]**](SpecimenProcedures.md) |  | 

## Example

```python
from biodata_registry_api_client.models.specimen_procedures_page import SpecimenProceduresPage

# TODO update the JSON string below
json = "{}"
# create an instance of SpecimenProceduresPage from a JSON string
specimen_procedures_page_instance = SpecimenProceduresPage.from_json(json)
# print the JSON string representation of the object
print(SpecimenProceduresPage.to_json())

# convert the object into a dict
specimen_procedures_page_dict = specimen_procedures_page_instance.to_dict()
# create an instance of SpecimenProceduresPage from a dict
specimen_procedures_page_from_dict = SpecimenProceduresPage.from_dict(specimen_procedures_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


