# Instruments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**name** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.instruments import Instruments

# TODO update the JSON string below
json = "{}"
# create an instance of Instruments from a JSON string
instruments_instance = Instruments.from_json(json)
# print the JSON string representation of the object
print(Instruments.to_json())

# convert the object into a dict
instruments_dict = instruments_instance.to_dict()
# create an instance of Instruments from a dict
instruments_from_dict = Instruments.from_dict(instruments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


