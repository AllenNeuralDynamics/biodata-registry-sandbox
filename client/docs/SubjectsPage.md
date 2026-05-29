# SubjectsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Subjects]**](Subjects.md) |  | 

## Example

```python
from biodata_registry_api_client.models.subjects_page import SubjectsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectsPage from a JSON string
subjects_page_instance = SubjectsPage.from_json(json)
# print the JSON string representation of the object
print(SubjectsPage.to_json())

# convert the object into a dict
subjects_page_dict = subjects_page_instance.to_dict()
# create an instance of SubjectsPage from a dict
subjects_page_from_dict = SubjectsPage.from_dict(subjects_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


