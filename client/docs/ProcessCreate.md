# ProcessCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**output_data_asset_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.process_create import ProcessCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessCreate from a JSON string
process_create_instance = ProcessCreate.from_json(json)
# print the JSON string representation of the object
print(ProcessCreate.to_json())

# convert the object into a dict
process_create_dict = process_create_instance.to_dict()
# create an instance of ProcessCreate from a dict
process_create_from_dict = ProcessCreate.from_dict(process_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


