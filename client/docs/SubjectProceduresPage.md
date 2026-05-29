# SubjectProceduresPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[SubjectProcedures]**](SubjectProcedures.md) |  | 

## Example

```python
from biodata_registry_api_client.models.subject_procedures_page import SubjectProceduresPage

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectProceduresPage from a JSON string
subject_procedures_page_instance = SubjectProceduresPage.from_json(json)
# print the JSON string representation of the object
print(SubjectProceduresPage.to_json())

# convert the object into a dict
subject_procedures_page_dict = subject_procedures_page_instance.to_dict()
# create an instance of SubjectProceduresPage from a dict
subject_procedures_page_from_dict = SubjectProceduresPage.from_dict(subject_procedures_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


