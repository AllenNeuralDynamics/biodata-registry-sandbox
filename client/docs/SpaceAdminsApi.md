# biodata_registry_api_client.SpaceAdminsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_space_admin**](SpaceAdminsApi.md#create_space_admin) | **POST** /space_admin | Create Space Admin
[**delete**](SpaceAdminsApi.md#delete) | **DELETE** /space_admin | Delete
[**get_space_admin**](SpaceAdminsApi.md#get_space_admin) | **GET** /space_admin | Get Space Admin
[**get_space_admins**](SpaceAdminsApi.md#get_space_admins) | **GET** /space_admins | Get Space Admins
[**update**](SpaceAdminsApi.md#update) | **PUT** /space_admin | Update


# **create_space_admin**
> SpaceAdmins create_space_admin(space_admin_create)

Create Space Admin

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.space_admin_create import SpaceAdminCreate
from biodata_registry_api_client.models.space_admins import SpaceAdmins
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
    api_instance = biodata_registry_api_client.SpaceAdminsApi(api_client)
    space_admin_create = biodata_registry_api_client.SpaceAdminCreate() # SpaceAdminCreate | 

    try:
        # Create Space Admin
        api_response = api_instance.create_space_admin(space_admin_create)
        print("The response of SpaceAdminsApi->create_space_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceAdminsApi->create_space_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_admin_create** | [**SpaceAdminCreate**](SpaceAdminCreate.md)|  | 

### Return type

[**SpaceAdmins**](SpaceAdmins.md)

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
    api_instance = biodata_registry_api_client.SpaceAdminsApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete(id)
        print("The response of SpaceAdminsApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceAdminsApi->delete: %s\n" % e)
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

# **get_space_admin**
> SpaceAdmins get_space_admin(id)

Get Space Admin

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.space_admins import SpaceAdmins
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
    api_instance = biodata_registry_api_client.SpaceAdminsApi(api_client)
    id = 56 # int | 

    try:
        # Get Space Admin
        api_response = api_instance.get_space_admin(id)
        print("The response of SpaceAdminsApi->get_space_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceAdminsApi->get_space_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SpaceAdmins**](SpaceAdmins.md)

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

# **get_space_admins**
> List[SpaceAdmins] get_space_admins(offset=offset, limit=limit)

Get Space Admins

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.space_admins import SpaceAdmins
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
    api_instance = biodata_registry_api_client.SpaceAdminsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Space Admins
        api_response = api_instance.get_space_admins(offset=offset, limit=limit)
        print("The response of SpaceAdminsApi->get_space_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceAdminsApi->get_space_admins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[SpaceAdmins]**](SpaceAdmins.md)

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
> SpaceAdmins update(id, space_admin_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.space_admin_update import SpaceAdminUpdate
from biodata_registry_api_client.models.space_admins import SpaceAdmins
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
    api_instance = biodata_registry_api_client.SpaceAdminsApi(api_client)
    id = 56 # int | 
    space_admin_update = biodata_registry_api_client.SpaceAdminUpdate() # SpaceAdminUpdate | 

    try:
        # Update
        api_response = api_instance.update(id, space_admin_update)
        print("The response of SpaceAdminsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceAdminsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **space_admin_update** | [**SpaceAdminUpdate**](SpaceAdminUpdate.md)|  | 

### Return type

[**SpaceAdmins**](SpaceAdmins.md)

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

