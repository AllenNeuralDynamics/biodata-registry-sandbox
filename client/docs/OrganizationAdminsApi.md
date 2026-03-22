# biodata_registry_api_client.OrganizationAdminsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_admin**](OrganizationAdminsApi.md#create_organization_admin) | **POST** /organization_admin | Create Organization Admin
[**delete**](OrganizationAdminsApi.md#delete) | **DELETE** /organization_admin | Delete
[**get_organization_admin**](OrganizationAdminsApi.md#get_organization_admin) | **GET** /organization_admin | Get Organization Admin
[**get_organization_admins**](OrganizationAdminsApi.md#get_organization_admins) | **GET** /organization_admins | Get Organization Admins
[**update**](OrganizationAdminsApi.md#update) | **PUT** /organization_admin | Update


# **create_organization_admin**
> OrganizationAdmins create_organization_admin(organization_admin_create)

Create Organization Admin

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.organization_admin_create import OrganizationAdminCreate
from biodata_registry_api_client.models.organization_admins import OrganizationAdmins
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
    api_instance = biodata_registry_api_client.OrganizationAdminsApi(api_client)
    organization_admin_create = biodata_registry_api_client.OrganizationAdminCreate() # OrganizationAdminCreate | 

    try:
        # Create Organization Admin
        api_response = api_instance.create_organization_admin(organization_admin_create)
        print("The response of OrganizationAdminsApi->create_organization_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAdminsApi->create_organization_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_admin_create** | [**OrganizationAdminCreate**](OrganizationAdminCreate.md)|  | 

### Return type

[**OrganizationAdmins**](OrganizationAdmins.md)

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
    api_instance = biodata_registry_api_client.OrganizationAdminsApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete(id)
        print("The response of OrganizationAdminsApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAdminsApi->delete: %s\n" % e)
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

# **get_organization_admin**
> OrganizationAdmins get_organization_admin(id)

Get Organization Admin

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.organization_admins import OrganizationAdmins
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
    api_instance = biodata_registry_api_client.OrganizationAdminsApi(api_client)
    id = 56 # int | 

    try:
        # Get Organization Admin
        api_response = api_instance.get_organization_admin(id)
        print("The response of OrganizationAdminsApi->get_organization_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAdminsApi->get_organization_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrganizationAdmins**](OrganizationAdmins.md)

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

# **get_organization_admins**
> List[OrganizationAdmins] get_organization_admins(offset=offset, limit=limit)

Get Organization Admins

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.organization_admins import OrganizationAdmins
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
    api_instance = biodata_registry_api_client.OrganizationAdminsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Organization Admins
        api_response = api_instance.get_organization_admins(offset=offset, limit=limit)
        print("The response of OrganizationAdminsApi->get_organization_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAdminsApi->get_organization_admins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[OrganizationAdmins]**](OrganizationAdmins.md)

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
> OrganizationAdmins update(id, organization_admin_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.organization_admin_update import OrganizationAdminUpdate
from biodata_registry_api_client.models.organization_admins import OrganizationAdmins
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
    api_instance = biodata_registry_api_client.OrganizationAdminsApi(api_client)
    id = 56 # int | 
    organization_admin_update = biodata_registry_api_client.OrganizationAdminUpdate() # OrganizationAdminUpdate | 

    try:
        # Update
        api_response = api_instance.update(id, organization_admin_update)
        print("The response of OrganizationAdminsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAdminsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **organization_admin_update** | [**OrganizationAdminUpdate**](OrganizationAdminUpdate.md)|  | 

### Return type

[**OrganizationAdmins**](OrganizationAdmins.md)

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

