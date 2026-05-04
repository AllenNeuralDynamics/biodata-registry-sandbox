# SpecimenCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**schema_id** | **int** |  | [optional] 
**space_id** | **int** |  | [optional] 
**subject_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.specimen_create import SpecimenCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SpecimenCreate from a JSON string
specimen_create_instance = SpecimenCreate.from_json(json)
# print the JSON string representation of the object
print(SpecimenCreate.to_json())

# convert the object into a dict
specimen_create_dict = specimen_create_instance.to_dict()
# create an instance of SpecimenCreate from a dict
specimen_create_from_dict = SpecimenCreate.from_dict(specimen_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


