# biodata_registry_api_client.ViewsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_acquisition_view**](ViewsApi.md#get_acquisition_view) | **GET** /acquisition_view | Get Acquisition View
[**get_data_asset_view**](ViewsApi.md#get_data_asset_view) | **GET** /data_asset_view | Get Data Asset View


# **get_acquisition_view**
> List[AcquisitionView] get_acquisition_view(acquisition_id=acquisition_id, subject_id=subject_id, data_asset_name=data_asset_name, subject_name=subject_name, instrument_name=instrument_name, data_asset_location=data_asset_location, offset=offset, limit=limit)

Get Acquisition View

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.acquisition_view import AcquisitionView
from biodata_registry_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biodata_registry_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biodata_registry_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biodata_registry_api_client.ViewsApi(api_client)
    acquisition_id = 56 # int |  (optional)
    subject_id = 56 # int |  (optional)
    data_asset_name = 'data_asset_name_example' # str |  (optional)
    subject_name = 'subject_name_example' # str |  (optional)
    instrument_name = 'instrument_name_example' # str |  (optional)
    data_asset_location = 'data_asset_location_example' # str |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Acquisition View
        api_response = api_instance.get_acquisition_view(acquisition_id=acquisition_id, subject_id=subject_id, data_asset_name=data_asset_name, subject_name=subject_name, instrument_name=instrument_name, data_asset_location=data_asset_location, offset=offset, limit=limit)
        print("The response of ViewsApi->get_acquisition_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->get_acquisition_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acquisition_id** | **int**|  | [optional] 
 **subject_id** | **int**|  | [optional] 
 **data_asset_name** | **str**|  | [optional] 
 **subject_name** | **str**|  | [optional] 
 **instrument_name** | **str**|  | [optional] 
 **data_asset_location** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[AcquisitionView]**](AcquisitionView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_asset_view**
> List[DataAssetView] get_data_asset_view(data_asset_id=data_asset_id, acquisition_id=acquisition_id, subject_id=subject_id, data_asset_name=data_asset_name, subject_name=subject_name, instrument_name=instrument_name, data_asset_location=data_asset_location, offset=offset, limit=limit)

Get Data Asset View

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.data_asset_view import DataAssetView
from biodata_registry_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biodata_registry_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biodata_registry_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biodata_registry_api_client.ViewsApi(api_client)
    data_asset_id = 56 # int |  (optional)
    acquisition_id = 56 # int |  (optional)
    subject_id = 56 # int |  (optional)
    data_asset_name = 'data_asset_name_example' # str |  (optional)
    subject_name = 'subject_name_example' # str |  (optional)
    instrument_name = 'instrument_name_example' # str |  (optional)
    data_asset_location = 'data_asset_location_example' # str |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Data Asset View
        api_response = api_instance.get_data_asset_view(data_asset_id=data_asset_id, acquisition_id=acquisition_id, subject_id=subject_id, data_asset_name=data_asset_name, subject_name=subject_name, instrument_name=instrument_name, data_asset_location=data_asset_location, offset=offset, limit=limit)
        print("The response of ViewsApi->get_data_asset_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->get_data_asset_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_asset_id** | **int**|  | [optional] 
 **acquisition_id** | **int**|  | [optional] 
 **subject_id** | **int**|  | [optional] 
 **data_asset_name** | **str**|  | [optional] 
 **subject_name** | **str**|  | [optional] 
 **instrument_name** | **str**|  | [optional] 
 **data_asset_location** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[DataAssetView]**](DataAssetView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

