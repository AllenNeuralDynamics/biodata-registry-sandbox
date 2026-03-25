# Acquisitions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**data_asset_id** | **int** |  | [optional] 
**instrument_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.acquisitions import Acquisitions

# TODO update the JSON string below
json = "{}"
# create an instance of Acquisitions from a JSON string
acquisitions_instance = Acquisitions.from_json(json)
# print the JSON string representation of the object
print(Acquisitions.to_json())

# convert the object into a dict
acquisitions_dict = acquisitions_instance.to_dict()
# create an instance of Acquisitions from a dict
acquisitions_from_dict = Acquisitions.from_dict(acquisitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


