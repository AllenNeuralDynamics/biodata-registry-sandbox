# Schemas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**version** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**schema_entity_id** | **int** |  | [optional] 

## Example

```python
from biodata_registry_api_client.models.schemas import Schemas

# TODO update the JSON string below
json = "{}"
# create an instance of Schemas from a JSON string
schemas_instance = Schemas.from_json(json)
# print the JSON string representation of the object
print(Schemas.to_json())

# convert the object into a dict
schemas_dict = schemas_instance.to_dict()
# create an instance of Schemas from a dict
schemas_from_dict = Schemas.from_dict(schemas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


