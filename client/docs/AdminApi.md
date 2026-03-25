# biodata_registry_api_client.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collection**](AdminApi.md#create_collection) | **POST** /collection | Create Collection
[**create_organization**](AdminApi.md#create_organization) | **POST** /organization | Create Organization
[**create_organization_admin**](AdminApi.md#create_organization_admin) | **POST** /organization_admin | Create Organization Admin
[**create_space**](AdminApi.md#create_space) | **POST** /space | Create Space
[**create_space_admin**](AdminApi.md#create_space_admin) | **POST** /space_admin | Create Space Admin
[**create_user**](AdminApi.md#create_user) | **POST** /user | Create User
[**delete_collection**](AdminApi.md#delete_collection) | **DELETE** /collection | Delete
[**delete_organization**](AdminApi.md#delete_organization) | **DELETE** /organization | Delete
[**delete_organization_admin**](AdminApi.md#delete_organization_admin) | **DELETE** /organization_admin | Delete
[**delete_space**](AdminApi.md#delete_space) | **DELETE** /space | Delete
[**delete_space_admin**](AdminApi.md#delete_space_admin) | **DELETE** /space_admin | Delete
[**delete_user**](AdminApi.md#delete_user) | **DELETE** /user | Delete
[**get_collection**](AdminApi.md#get_collection) | **GET** /collection | Get Collection
[**get_collections**](AdminApi.md#get_collections) | **GET** /collections | Get Collections
[**get_organization**](AdminApi.md#get_organization) | **GET** /organization | Get Organization
[**get_organization_admin**](AdminApi.md#get_organization_admin) | **GET** /organization_admin | Get Organization Admin
[**get_organization_admins**](AdminApi.md#get_organization_admins) | **GET** /organization_admins | Get Organization Admins
[**get_organizations**](AdminApi.md#get_organizations) | **GET** /organizations | Get Organizations
[**get_space**](AdminApi.md#get_space) | **GET** /space | Get Space
[**get_space_admin**](AdminApi.md#get_space_admin) | **GET** /space_admin | Get Space Admin
[**get_space_admins**](AdminApi.md#get_space_admins) | **GET** /space_admins | Get Space Admins
[**get_spaces**](AdminApi.md#get_spaces) | **GET** /spaces | Get Spaces
[**get_user**](AdminApi.md#get_user) | **GET** /user | Get User
[**get_users**](AdminApi.md#get_users) | **GET** /users | Get Users
[**update_collection**](AdminApi.md#update_collection) | **PUT** /collection | Update
[**update_organization**](AdminApi.md#update_organization) | **PUT** /organization | Update
[**update_organization_admin**](AdminApi.md#update_organization_admin) | **PUT** /organization_admin | Update
[**update_space**](AdminApi.md#update_space) | **PUT** /space | Update
[**update_space_admin**](AdminApi.md#update_space_admin) | **PUT** /space_admin | Update
[**update_user**](AdminApi.md#update_user) | **PUT** /user | Update


# **create_collection**
> Collections create_collection(collection_create)

Create Collection

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.collection_create import CollectionCreate
from biodata_registry_api_client.models.collections import Collections
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    collection_create = biodata_registry_api_client.CollectionCreate() # CollectionCreate | 

    try:
        # Create Collection
        api_response = api_instance.create_collection(collection_create)
        print("The response of AdminApi->create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_create** | [**CollectionCreate**](CollectionCreate.md)|  | 

### Return type

[**Collections**](Collections.md)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    organization_create = biodata_registry_api_client.OrganizationCreate() # OrganizationCreate | 

    try:
        # Create Organization
        api_response = api_instance.create_organization(organization_create)
        print("The response of AdminApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_organization: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    organization_admin_create = biodata_registry_api_client.OrganizationAdminCreate() # OrganizationAdminCreate | 

    try:
        # Create Organization Admin
        api_response = api_instance.create_organization_admin(organization_admin_create)
        print("The response of AdminApi->create_organization_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_organization_admin: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    space_create = biodata_registry_api_client.SpaceCreate() # SpaceCreate | 

    try:
        # Create Space
        api_response = api_instance.create_space(space_create)
        print("The response of AdminApi->create_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_space: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    space_admin_create = biodata_registry_api_client.SpaceAdminCreate() # SpaceAdminCreate | 

    try:
        # Create Space Admin
        api_response = api_instance.create_space_admin(space_admin_create)
        print("The response of AdminApi->create_space_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_space_admin: %s\n" % e)
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

# **create_user**
> Users create_user(user_create)

Create User

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.user_create import UserCreate
from biodata_registry_api_client.models.users import Users
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    user_create = biodata_registry_api_client.UserCreate() # UserCreate | 

    try:
        # Create User
        api_response = api_instance.create_user(user_create)
        print("The response of AdminApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**Users**](Users.md)

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

# **delete_collection**
> object delete_collection(id)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_collection(id)
        print("The response of AdminApi->delete_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_collection: %s\n" % e)
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

# **delete_organization**
> object delete_organization(id)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_organization(id)
        print("The response of AdminApi->delete_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_organization: %s\n" % e)
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

# **delete_organization_admin**
> object delete_organization_admin(id)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_organization_admin(id)
        print("The response of AdminApi->delete_organization_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_organization_admin: %s\n" % e)
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

# **delete_space**
> object delete_space(id)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_space(id)
        print("The response of AdminApi->delete_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_space: %s\n" % e)
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

# **delete_space_admin**
> object delete_space_admin(id)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_space_admin(id)
        print("The response of AdminApi->delete_space_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_space_admin: %s\n" % e)
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

# **delete_user**
> object delete_user(id)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_user(id)
        print("The response of AdminApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_user: %s\n" % e)
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

# **get_collection**
> Collections get_collection(id)

Get Collection

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.collections import Collections
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Get Collection
        api_response = api_instance.get_collection(id)
        print("The response of AdminApi->get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Collections**](Collections.md)

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

# **get_collections**
> List[Collections] get_collections(offset=offset, limit=limit)

Get Collections

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.collections import Collections
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Collections
        api_response = api_instance.get_collections(offset=offset, limit=limit)
        print("The response of AdminApi->get_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[Collections]**](Collections.md)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Get Organization
        api_response = api_instance.get_organization(id)
        print("The response of AdminApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_organization: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Get Organization Admin
        api_response = api_instance.get_organization_admin(id)
        print("The response of AdminApi->get_organization_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_organization_admin: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Organization Admins
        api_response = api_instance.get_organization_admins(offset=offset, limit=limit)
        print("The response of AdminApi->get_organization_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_organization_admins: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Organizations
        api_response = api_instance.get_organizations(offset=offset, limit=limit)
        print("The response of AdminApi->get_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_organizations: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Get Space
        api_response = api_instance.get_space(id)
        print("The response of AdminApi->get_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_space: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Get Space Admin
        api_response = api_instance.get_space_admin(id)
        print("The response of AdminApi->get_space_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_space_admin: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Space Admins
        api_response = api_instance.get_space_admins(offset=offset, limit=limit)
        print("The response of AdminApi->get_space_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_space_admins: %s\n" % e)
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Spaces
        api_response = api_instance.get_spaces(offset=offset, limit=limit)
        print("The response of AdminApi->get_spaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_spaces: %s\n" % e)
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

# **get_user**
> Users get_user(id)

Get User

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.users import Users
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 

    try:
        # Get User
        api_response = api_instance.get_user(id)
        print("The response of AdminApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Users**](Users.md)

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

# **get_users**
> List[Users] get_users(offset=offset, limit=limit)

Get Users

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.users import Users
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Users
        api_response = api_instance.get_users(offset=offset, limit=limit)
        print("The response of AdminApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[Users]**](Users.md)

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

# **update_collection**
> Collections update_collection(id, collection_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.collection_update import CollectionUpdate
from biodata_registry_api_client.models.collections import Collections
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 
    collection_update = biodata_registry_api_client.CollectionUpdate() # CollectionUpdate | 

    try:
        # Update
        api_response = api_instance.update_collection(id, collection_update)
        print("The response of AdminApi->update_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **collection_update** | [**CollectionUpdate**](CollectionUpdate.md)|  | 

### Return type

[**Collections**](Collections.md)

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

# **update_organization**
> Organizations update_organization(id, organization_update)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 
    organization_update = biodata_registry_api_client.OrganizationUpdate() # OrganizationUpdate | 

    try:
        # Update
        api_response = api_instance.update_organization(id, organization_update)
        print("The response of AdminApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_organization: %s\n" % e)
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

# **update_organization_admin**
> OrganizationAdmins update_organization_admin(id, organization_admin_update)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 
    organization_admin_update = biodata_registry_api_client.OrganizationAdminUpdate() # OrganizationAdminUpdate | 

    try:
        # Update
        api_response = api_instance.update_organization_admin(id, organization_admin_update)
        print("The response of AdminApi->update_organization_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_organization_admin: %s\n" % e)
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

# **update_space**
> Spaces update_space(id, space_update)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 
    space_update = biodata_registry_api_client.SpaceUpdate() # SpaceUpdate | 

    try:
        # Update
        api_response = api_instance.update_space(id, space_update)
        print("The response of AdminApi->update_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_space: %s\n" % e)
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

# **update_space_admin**
> SpaceAdmins update_space_admin(id, space_admin_update)

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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 
    space_admin_update = biodata_registry_api_client.SpaceAdminUpdate() # SpaceAdminUpdate | 

    try:
        # Update
        api_response = api_instance.update_space_admin(id, space_admin_update)
        print("The response of AdminApi->update_space_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_space_admin: %s\n" % e)
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

# **update_user**
> Users update_user(id, user_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.user_update import UserUpdate
from biodata_registry_api_client.models.users import Users
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
    api_instance = biodata_registry_api_client.AdminApi(api_client)
    id = 56 # int | 
    user_update = biodata_registry_api_client.UserUpdate() # UserUpdate | 

    try:
        # Update
        api_response = api_instance.update_user(id, user_update)
        print("The response of AdminApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**Users**](Users.md)

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

