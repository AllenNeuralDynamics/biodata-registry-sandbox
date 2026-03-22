# biodata_registry_api_client.SchemasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schema**](SchemasApi.md#create_schema) | **POST** /schema | Create Schema
[**delete**](SchemasApi.md#delete) | **DELETE** /schema | Delete
[**get_schema**](SchemasApi.md#get_schema) | **GET** /schema | Get Schema
[**get_schemas**](SchemasApi.md#get_schemas) | **GET** /schemas | Get Schemas
[**update**](SchemasApi.md#update) | **PUT** /schema | Update


# **create_schema**
> Schemas create_schema(schema_create)

Create Schema

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schema_create import SchemaCreate
from biodata_registry_api_client.models.schemas import Schemas
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
    api_instance = biodata_registry_api_client.SchemasApi(api_client)
    schema_create = biodata_registry_api_client.SchemaCreate() # SchemaCreate | 

    try:
        # Create Schema
        api_response = api_instance.create_schema(schema_create)
        print("The response of SchemasApi->create_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->create_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_create** | [**SchemaCreate**](SchemaCreate.md)|  | 

### Return type

[**Schemas**](Schemas.md)

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
    api_instance = biodata_registry_api_client.SchemasApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete(id)
        print("The response of SchemasApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->delete: %s\n" % e)
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

# **get_schema**
> Schemas get_schema(id)

Get Schema

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schemas import Schemas
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
    api_instance = biodata_registry_api_client.SchemasApi(api_client)
    id = 56 # int | 

    try:
        # Get Schema
        api_response = api_instance.get_schema(id)
        print("The response of SchemasApi->get_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Schemas**](Schemas.md)

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

# **get_schemas**
> List[Schemas] get_schemas(offset=offset, limit=limit)

Get Schemas

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schemas import Schemas
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
    api_instance = biodata_registry_api_client.SchemasApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Schemas
        api_response = api_instance.get_schemas(offset=offset, limit=limit)
        print("The response of SchemasApi->get_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[Schemas]**](Schemas.md)

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
> Schemas update(id, schema_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schema_update import SchemaUpdate
from biodata_registry_api_client.models.schemas import Schemas
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
    api_instance = biodata_registry_api_client.SchemasApi(api_client)
    id = 56 # int | 
    schema_update = biodata_registry_api_client.SchemaUpdate() # SchemaUpdate | 

    try:
        # Update
        api_response = api_instance.update(id, schema_update)
        print("The response of SchemasApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **schema_update** | [**SchemaUpdate**](SchemaUpdate.md)|  | 

### Return type

[**Schemas**](Schemas.md)

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

