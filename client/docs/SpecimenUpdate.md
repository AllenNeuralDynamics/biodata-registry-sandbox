# SpecimenUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**subject_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.specimen_update import SpecimenUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SpecimenUpdate from a JSON string
specimen_update_instance = SpecimenUpdate.from_json(json)
# print the JSON string representation of the object
print(SpecimenUpdate.to_json())

# convert the object into a dict
specimen_update_dict = specimen_update_instance.to_dict()
# create an instance of SpecimenUpdate from a dict
specimen_update_from_dict = SpecimenUpdate.from_dict(specimen_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


