# ProcessesPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[Processes]**](Processes.md) |  | 

## Example

```python
from biodata_registry_api_client.models.processes_page import ProcessesPage

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessesPage from a JSON string
processes_page_instance = ProcessesPage.from_json(json)
# print the JSON string representation of the object
print(ProcessesPage.to_json())

# convert the object into a dict
processes_page_dict = processes_page_instance.to_dict()
# create an instance of ProcessesPage from a dict
processes_page_from_dict = ProcessesPage.from_dict(processes_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


