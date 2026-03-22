# biodata_registry_api_client.SchemaEntitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schema_entity**](SchemaEntitiesApi.md#create_schema_entity) | **POST** /schema_entity | Create Schema Entity
[**delete**](SchemaEntitiesApi.md#delete) | **DELETE** /schema_entity | Delete
[**get_schema_entities**](SchemaEntitiesApi.md#get_schema_entities) | **GET** /schema_entities | Get Schema Entities
[**get_schema_entity**](SchemaEntitiesApi.md#get_schema_entity) | **GET** /schema_entity | Get Schema Entity
[**update**](SchemaEntitiesApi.md#update) | **PUT** /schema_entity | Update


# **create_schema_entity**
> SchemaEntities create_schema_entity(schema_entity_create)

Create Schema Entity

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schema_entities import SchemaEntities
from biodata_registry_api_client.models.schema_entity_create import SchemaEntityCreate
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
    api_instance = biodata_registry_api_client.SchemaEntitiesApi(api_client)
    schema_entity_create = biodata_registry_api_client.SchemaEntityCreate() # SchemaEntityCreate | 

    try:
        # Create Schema Entity
        api_response = api_instance.create_schema_entity(schema_entity_create)
        print("The response of SchemaEntitiesApi->create_schema_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaEntitiesApi->create_schema_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_entity_create** | [**SchemaEntityCreate**](SchemaEntityCreate.md)|  | 

### Return type

[**SchemaEntities**](SchemaEntities.md)

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
    api_instance = biodata_registry_api_client.SchemaEntitiesApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete(id)
        print("The response of SchemaEntitiesApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaEntitiesApi->delete: %s\n" % e)
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

# **get_schema_entities**
> List[SchemaEntities] get_schema_entities(offset=offset, limit=limit)

Get Schema Entities

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schema_entities import SchemaEntities
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
    api_instance = biodata_registry_api_client.SchemaEntitiesApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Schema Entities
        api_response = api_instance.get_schema_entities(offset=offset, limit=limit)
        print("The response of SchemaEntitiesApi->get_schema_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaEntitiesApi->get_schema_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[SchemaEntities]**](SchemaEntities.md)

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

# **get_schema_entity**
> SchemaEntities get_schema_entity(id)

Get Schema Entity

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schema_entities import SchemaEntities
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
    api_instance = biodata_registry_api_client.SchemaEntitiesApi(api_client)
    id = 56 # int | 

    try:
        # Get Schema Entity
        api_response = api_instance.get_schema_entity(id)
        print("The response of SchemaEntitiesApi->get_schema_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaEntitiesApi->get_schema_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SchemaEntities**](SchemaEntities.md)

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
> SchemaEntities update(id, schema_entity_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schema_entities import SchemaEntities
from biodata_registry_api_client.models.schema_entity_update import SchemaEntityUpdate
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
    api_instance = biodata_registry_api_client.SchemaEntitiesApi(api_client)
    id = 56 # int | 
    schema_entity_update = biodata_registry_api_client.SchemaEntityUpdate() # SchemaEntityUpdate | 

    try:
        # Update
        api_response = api_instance.update(id, schema_entity_update)
        print("The response of SchemaEntitiesApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaEntitiesApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **schema_entity_update** | [**SchemaEntityUpdate**](SchemaEntityUpdate.md)|  | 

### Return type

[**SchemaEntities**](SchemaEntities.md)

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

