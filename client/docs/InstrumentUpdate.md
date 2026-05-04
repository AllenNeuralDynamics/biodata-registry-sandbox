# InstrumentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.instrument_update import InstrumentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentUpdate from a JSON string
instrument_update_instance = InstrumentUpdate.from_json(json)
# print the JSON string representation of the object
print(InstrumentUpdate.to_json())

# convert the object into a dict
instrument_update_dict = instrument_update_instance.to_dict()
# create an instance of InstrumentUpdate from a dict
instrument_update_from_dict = InstrumentUpdate.from_dict(instrument_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


