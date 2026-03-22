# biodata_registry_api_client.SpacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_space**](SpacesApi.md#create_space) | **POST** /space | Create Space
[**delete**](SpacesApi.md#delete) | **DELETE** /space | Delete
[**get_space**](SpacesApi.md#get_space) | **GET** /space | Get Space
[**get_spaces**](SpacesApi.md#get_spaces) | **GET** /spaces | Get Spaces
[**update**](SpacesApi.md#update) | **PUT** /space | Update


# **create_space**
> Spaces create_space(space_create)

Create Space

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.space_create import SpaceCreate
from biodata_registry_api_client.models.spaces import Spaces
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
    api_instance = biodata_registry_api_client.SpacesApi(api_client)
    space_create = biodata_registry_api_client.SpaceCreate() # SpaceCreate | 

    try:
        # Create Space
        api_response = api_instance.create_space(space_create)
        print("The response of SpacesApi->create_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->create_space: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_create** | [**SpaceCreate**](SpaceCreate.md)|  | 

### Return type

[**Spaces**](Spaces.md)

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
    api_instance = biodata_registry_api_client.SpacesApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete(id)
        print("The response of SpacesApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->delete: %s\n" % e)
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

# **get_space**
> Spaces get_space(id)

Get Space

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.spaces import Spaces
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
    api_instance = biodata_registry_api_client.SpacesApi(api_client)
    id = 56 # int | 

    try:
        # Get Space
        api_response = api_instance.get_space(id)
        print("The response of SpacesApi->get_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->get_space: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Spaces**](Spaces.md)

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

# **get_spaces**
> List[Spaces] get_spaces(offset=offset, limit=limit)

Get Spaces

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.spaces import Spaces
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
    api_instance = biodata_registry_api_client.SpacesApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Spaces
        api_response = api_instance.get_spaces(offset=offset, limit=limit)
        print("The response of SpacesApi->get_spaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->get_spaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[Spaces]**](Spaces.md)

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
> Spaces update(id, space_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.space_update import SpaceUpdate
from biodata_registry_api_client.models.spaces import Spaces
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
    api_instance = biodata_registry_api_client.SpacesApi(api_client)
    id = 56 # int | 
    space_update = biodata_registry_api_client.SpaceUpdate() # SpaceUpdate | 

    try:
        # Update
        api_response = api_instance.update(id, space_update)
        print("The response of SpacesApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **space_update** | [**SpaceUpdate**](SpaceUpdate.md)|  | 

### Return type

[**Spaces**](Spaces.md)

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

