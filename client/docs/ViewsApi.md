# biodata_registry_api_client.ViewsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_asset_view**](ViewsApi.md#get_data_asset_view) | **GET** /data_asset_view | Get Data Asset View


# **get_data_asset_view**
> DataAssetViewsPage get_data_asset_view(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, data_asset_id=data_asset_id, acquisition_id=acquisition_id, instrument_id=instrument_id, instrument_name__ilike=instrument_name__ilike, data_asset_name__ilike=data_asset_name__ilike, data_asset_location__ilike=data_asset_location__ilike)

Get Data Asset View

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.data_asset_views_page import DataAssetViewsPage
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
    next_token = 'next_token_example' # str |  (optional)
    limit = 10 # int |  (optional) (default to 10)
    created_at__gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_at__lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at__gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at__lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    data_asset_id = 56 # int |  (optional)
    acquisition_id = 56 # int |  (optional)
    instrument_id = 56 # int |  (optional)
    instrument_name__ilike = 'instrument_name__ilike_example' # str |  (optional)
    data_asset_name__ilike = 'data_asset_name__ilike_example' # str |  (optional)
    data_asset_location__ilike = 'data_asset_location__ilike_example' # str |  (optional)

    try:
        # Get Data Asset View
        api_response = api_instance.get_data_asset_view(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, data_asset_id=data_asset_id, acquisition_id=acquisition_id, instrument_id=instrument_id, instrument_name__ilike=instrument_name__ilike, data_asset_name__ilike=data_asset_name__ilike, data_asset_location__ilike=data_asset_location__ilike)
        print("The response of ViewsApi->get_data_asset_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->get_data_asset_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **created_at__gt** | **datetime**|  | [optional] 
 **created_at__lt** | **datetime**|  | [optional] 
 **created_at__gte** | **datetime**|  | [optional] 
 **created_at__lte** | **datetime**|  | [optional] 
 **updated_at__gt** | **datetime**|  | [optional] 
 **updated_at__lt** | **datetime**|  | [optional] 
 **updated_at__gte** | **datetime**|  | [optional] 
 **updated_at__lte** | **datetime**|  | [optional] 
 **data_asset_id** | **int**|  | [optional] 
 **acquisition_id** | **int**|  | [optional] 
 **instrument_id** | **int**|  | [optional] 
 **instrument_name__ilike** | **str**|  | [optional] 
 **data_asset_name__ilike** | **str**|  | [optional] 
 **data_asset_location__ilike** | **str**|  | [optional] 

### Return type

[**DataAssetViewsPage**](DataAssetViewsPage.md)

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

