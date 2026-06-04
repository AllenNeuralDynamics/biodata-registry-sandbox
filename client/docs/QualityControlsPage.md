# QualityControlsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]
**results** | [**List[QualityControls]**](QualityControls.md) |  | 

## Example

```python
from biodata_registry_api_client.models.quality_controls_page import QualityControlsPage

# TODO update the JSON string below
json = "{}"
# create an instance of QualityControlsPage from a JSON string
quality_controls_page_instance = QualityControlsPage.from_json(json)
# print the JSON string representation of the object
print(QualityControlsPage.to_json())

# convert the object into a dict
quality_controls_page_dict = quality_controls_page_instance.to_dict()
# create an instance of QualityControlsPage from a dict
quality_controls_page_from_dict = QualityControlsPage.from_dict(quality_controls_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


