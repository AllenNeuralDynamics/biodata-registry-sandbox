# biodata_registry_api_client.DataAssetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_asset**](DataAssetsApi.md#create_data_asset) | **POST** /data_asset | Create Data Asset
[**delete**](DataAssetsApi.md#delete) | **DELETE** /data_asset | Delete
[**get_data_asset**](DataAssetsApi.md#get_data_asset) | **GET** /data_asset | Get Data Asset
[**get_data_assets**](DataAssetsApi.md#get_data_assets) | **GET** /data_assets | Get Data Assets
[**update**](DataAssetsApi.md#update) | **PUT** /data_asset | Update


# **create_data_asset**
> DataAssets create_data_asset(data_asset_create)

Create Data Asset

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.data_asset_create import DataAssetCreate
from biodata_registry_api_client.models.data_assets import DataAssets
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
    api_instance = biodata_registry_api_client.DataAssetsApi(api_client)
    data_asset_create = biodata_registry_api_client.DataAssetCreate() # DataAssetCreate | 

    try:
        # Create Data Asset
        api_response = api_instance.create_data_asset(data_asset_create)
        print("The response of DataAssetsApi->create_data_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAssetsApi->create_data_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_asset_create** | [**DataAssetCreate**](DataAssetCreate.md)|  | 

### Return type

[**DataAssets**](DataAssets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete

### Example


```python
import biodata_registry_api_client
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
    api_instance = biodata_registry_api_client.DataAssetsApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete(id)
        print("The response of DataAssetsApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAssetsApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

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

# **get_data_asset**
> DataAssets get_data_asset(id)

Get Data Asset

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.data_assets import DataAssets
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
    api_instance = biodata_registry_api_client.DataAssetsApi(api_client)
    id = 56 # int | 

    try:
        # Get Data Asset
        api_response = api_instance.get_data_asset(id)
        print("The response of DataAssetsApi->get_data_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAssetsApi->get_data_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DataAssets**](DataAssets.md)

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

# **get_data_assets**
> List[DataAssets] get_data_assets(offset=offset, limit=limit)

Get Data Assets

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.data_assets import DataAssets
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
    api_instance = biodata_registry_api_client.DataAssetsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Data Assets
        api_response = api_instance.get_data_assets(offset=offset, limit=limit)
        print("The response of DataAssetsApi->get_data_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAssetsApi->get_data_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[DataAssets]**](DataAssets.md)

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

# **update**
> DataAssets update(id, data_asset_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.data_asset_update import DataAssetUpdate
from biodata_registry_api_client.models.data_assets import DataAssets
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
    api_instance = biodata_registry_api_client.DataAssetsApi(api_client)
    id = 56 # int | 
    data_asset_update = biodata_registry_api_client.DataAssetUpdate() # DataAssetUpdate | 

    try:
        # Update
        api_response = api_instance.update(id, data_asset_update)
        print("The response of DataAssetsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAssetsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **data_asset_update** | [**DataAssetUpdate**](DataAssetUpdate.md)|  | 

### Return type

[**DataAssets**](DataAssets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

