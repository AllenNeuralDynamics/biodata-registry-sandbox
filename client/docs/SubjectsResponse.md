# SubjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | 
**has_more** | **bool** |  | 
**results** | [**List[Subjects]**](Subjects.md) |  | 

## Example

```python
from biodata_registry_api_client.models.subjects_response import SubjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectsResponse from a JSON string
subjects_response_instance = SubjectsResponse.from_json(json)
# print the JSON string representation of the object
print(SubjectsResponse.to_json())

# convert the object into a dict
subjects_response_dict = subjects_response_instance.to_dict()
# create an instance of SubjectsResponse from a dict
subjects_response_from_dict = SubjectsResponse.from_dict(subjects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


