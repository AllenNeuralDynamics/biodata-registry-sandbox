# biodata_registry_api_client.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationsApi.md#create_organization) | **POST** /organization | Create Organization
[**delete**](OrganizationsApi.md#delete) | **DELETE** /organization | Delete
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /organization | Get Organization
[**get_organizations**](OrganizationsApi.md#get_organizations) | **GET** /organizations | Get Organizations
[**update**](OrganizationsApi.md#update) | **PUT** /organization | Update


# **create_organization**
> Organizations create_organization(organization_create)

Create Organization

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.organization_create import OrganizationCreate
from biodata_registry_api_client.models.organizations import Organizations
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
    api_instance = biodata_registry_api_client.OrganizationsApi(api_client)
    organization_create = biodata_registry_api_client.OrganizationCreate() # OrganizationCreate | 

    try:
        # Create Organization
        api_response = api_instance.create_organization(organization_create)
        print("The response of OrganizationsApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_create** | [**OrganizationCreate**](OrganizationCreate.md)|  | 

### Return type

[**Organizations**](Organizations.md)

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
    api_instance = biodata_registry_api_client.OrganizationsApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete(id)
        print("The response of OrganizationsApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete: %s\n" % e)
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

# **get_organization**
> Organizations get_organization(id)

Get Organization

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.organizations import Organizations
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
    api_instance = biodata_registry_api_client.OrganizationsApi(api_client)
    id = 56 # int | 

    try:
        # Get Organization
        api_response = api_instance.get_organization(id)
        print("The response of OrganizationsApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Organizations**](Organizations.md)

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

# **get_organizations**
> List[Organizations] get_organizations(offset=offset, limit=limit)

Get Organizations

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.organizations import Organizations
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
    api_instance = biodata_registry_api_client.OrganizationsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Organizations
        api_response = api_instance.get_organizations(offset=offset, limit=limit)
        print("The response of OrganizationsApi->get_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[Organizations]**](Organizations.md)

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
> Organizations update(id, organization_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.organization_update import OrganizationUpdate
from biodata_registry_api_client.models.organizations import Organizations
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
    api_instance = biodata_registry_api_client.OrganizationsApi(api_client)
    id = 56 # int | 
    organization_update = biodata_registry_api_client.OrganizationUpdate() # OrganizationUpdate | 

    try:
        # Update
        api_response = api_instance.update(id, organization_update)
        print("The response of OrganizationsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **organization_update** | [**OrganizationUpdate**](OrganizationUpdate.md)|  | 

### Return type

[**Organizations**](Organizations.md)

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

