# ProcessUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**output_data_asset_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.process_update import ProcessUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessUpdate from a JSON string
process_update_instance = ProcessUpdate.from_json(json)
# print the JSON string representation of the object
print(ProcessUpdate.to_json())

# convert the object into a dict
process_update_dict = process_update_instance.to_dict()
# create an instance of ProcessUpdate from a dict
process_update_from_dict = ProcessUpdate.from_dict(process_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


