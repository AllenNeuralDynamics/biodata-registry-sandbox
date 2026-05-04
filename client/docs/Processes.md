# Processes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**output_data_asset_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.processes import Processes

# TODO update the JSON string below
json = "{}"
# create an instance of Processes from a JSON string
processes_instance = Processes.from_json(json)
# print the JSON string representation of the object
print(Processes.to_json())

# convert the object into a dict
processes_dict = processes_instance.to_dict()
# create an instance of Processes from a dict
processes_from_dict = Processes.from_dict(processes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


