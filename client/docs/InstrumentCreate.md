# InstrumentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.instrument_create import InstrumentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentCreate from a JSON string
instrument_create_instance = InstrumentCreate.from_json(json)
# print the JSON string representation of the object
print(InstrumentCreate.to_json())

# convert the object into a dict
instrument_create_dict = instrument_create_instance.to_dict()
# create an instance of InstrumentCreate from a dict
instrument_create_from_dict = InstrumentCreate.from_dict(instrument_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


