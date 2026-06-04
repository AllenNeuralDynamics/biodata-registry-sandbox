# biodata_registry_api_client.CoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_acquisition**](CoreApi.md#create_acquisition) | **POST** /acquisition | Create Acquisition
[**create_data_asset**](CoreApi.md#create_data_asset) | **POST** /data_asset | Create Data Asset
[**create_instrument**](CoreApi.md#create_instrument) | **POST** /instrument | Create Instrument
[**create_process**](CoreApi.md#create_process) | **POST** /process | Create Process
[**create_quality_control**](CoreApi.md#create_quality_control) | **POST** /quality_control | Create Quality Control
[**create_schema**](CoreApi.md#create_schema) | **POST** /schema | Create Schema
[**create_schema_entity**](CoreApi.md#create_schema_entity) | **POST** /schema_entity | Create Schema Entity
[**create_specimen**](CoreApi.md#create_specimen) | **POST** /specimen | Create Specimen
[**create_specimen_procedure**](CoreApi.md#create_specimen_procedure) | **POST** /specimen_procedure | Create Specimen Procedure
[**create_subject**](CoreApi.md#create_subject) | **POST** /subject | Create Subject
[**create_subject_procedure**](CoreApi.md#create_subject_procedure) | **POST** /subject_procedure | Create Subject Procedure
[**delete_acquisition**](CoreApi.md#delete_acquisition) | **DELETE** /acquisition | Delete
[**delete_data_asset**](CoreApi.md#delete_data_asset) | **DELETE** /data_asset | Delete
[**delete_instrument**](CoreApi.md#delete_instrument) | **DELETE** /instrument | Delete
[**delete_process**](CoreApi.md#delete_process) | **DELETE** /process | Delete
[**delete_quality_control**](CoreApi.md#delete_quality_control) | **DELETE** /quality_control | Delete
[**delete_schema**](CoreApi.md#delete_schema) | **DELETE** /schema | Delete
[**delete_schema_entity**](CoreApi.md#delete_schema_entity) | **DELETE** /schema_entity | Delete
[**delete_specimen**](CoreApi.md#delete_specimen) | **DELETE** /specimen | Delete
[**delete_specimen_procedure**](CoreApi.md#delete_specimen_procedure) | **DELETE** /specimen_procedure | Delete
[**delete_subject**](CoreApi.md#delete_subject) | **DELETE** /subject | Delete
[**delete_subject_procedure**](CoreApi.md#delete_subject_procedure) | **DELETE** /subject_procedure | Delete
[**get_acquisition**](CoreApi.md#get_acquisition) | **GET** /acquisition | Get Acquisition
[**get_acquisition_specimens**](CoreApi.md#get_acquisition_specimens) | **GET** /acquisition_specimens | Get Acquisition Subjects
[**get_acquisition_subjects**](CoreApi.md#get_acquisition_subjects) | **GET** /acquisition_subjects | Get Acquisition Subjects
[**get_acquisitions**](CoreApi.md#get_acquisitions) | **GET** /acquisitions | Get Acquisitions
[**get_data_asset**](CoreApi.md#get_data_asset) | **GET** /data_asset | Get Data Asset
[**get_data_asset_collections**](CoreApi.md#get_data_asset_collections) | **GET** /data_asset_collections | Get Data Asset Collections
[**get_data_asset_process_inputs**](CoreApi.md#get_data_asset_process_inputs) | **GET** /data_asset_process_inputs | Get Data Asset Process Inputs
[**get_data_assets**](CoreApi.md#get_data_assets) | **GET** /data_assets | Get Data Assets
[**get_instrument**](CoreApi.md#get_instrument) | **GET** /instrument | Get Instrument
[**get_instruments**](CoreApi.md#get_instruments) | **GET** /instruments | Get Instruments
[**get_process**](CoreApi.md#get_process) | **GET** /process | Get Process
[**get_process_data_asset_inputs**](CoreApi.md#get_process_data_asset_inputs) | **GET** /process_data_asset_inputs | Get Process Data Asset Inputs
[**get_processes**](CoreApi.md#get_processes) | **GET** /processes | Get Processes
[**get_quality_control**](CoreApi.md#get_quality_control) | **GET** /quality_control | Get Quality Control
[**get_quality_controls**](CoreApi.md#get_quality_controls) | **GET** /quality_controls | Get Quality Controls
[**get_schema**](CoreApi.md#get_schema) | **GET** /schema | Get Schema
[**get_schema_entities**](CoreApi.md#get_schema_entities) | **GET** /schema_entities | Get Schema Entities
[**get_schema_entity**](CoreApi.md#get_schema_entity) | **GET** /schema_entity | Get Schema Entity
[**get_schemas**](CoreApi.md#get_schemas) | **GET** /schemas | Get Schemas
[**get_specimen**](CoreApi.md#get_specimen) | **GET** /specimen | Get Specimen
[**get_specimen_acquisitions**](CoreApi.md#get_specimen_acquisitions) | **GET** /specimen_acquisitions | Get Specimen Acquisitions
[**get_specimen_procedure**](CoreApi.md#get_specimen_procedure) | **GET** /specimen_procedure | Get Specimen Procedure
[**get_specimen_procedure_specimen_inputs**](CoreApi.md#get_specimen_procedure_specimen_inputs) | **GET** /specimen_procedure_specimen_inputs | Get Specimen Procedure Specimen Inputs
[**get_specimen_procedure_specimen_outputs**](CoreApi.md#get_specimen_procedure_specimen_outputs) | **GET** /specimen_procedure_specimen_outputs | Get Specimen Procedure Specimen Outputs
[**get_specimen_procedures**](CoreApi.md#get_specimen_procedures) | **GET** /specimen_procedures | Get Specimen Procedures
[**get_specimen_specimen_procedure_inputs**](CoreApi.md#get_specimen_specimen_procedure_inputs) | **GET** /specimen_specimen_procedure_inputs | Get Specimen Specimen Procedure Inputs
[**get_specimen_specimen_procedure_outputs**](CoreApi.md#get_specimen_specimen_procedure_outputs) | **GET** /specimen_specimen_procedure_outputs | Get Specimen Specimen Procedure Outputs
[**get_specimen_subject_procedures**](CoreApi.md#get_specimen_subject_procedures) | **GET** /specimen_subject_procedures | Get Specimen Subject Procedures
[**get_specimens**](CoreApi.md#get_specimens) | **GET** /specimens | Get Specimens
[**get_subject**](CoreApi.md#get_subject) | **GET** /subject | Get Subject
[**get_subject_acquisitions**](CoreApi.md#get_subject_acquisitions) | **GET** /subject_acquisitions | Get Subject Acquisitions
[**get_subject_procedure**](CoreApi.md#get_subject_procedure) | **GET** /subject_procedure | Get Subject Procedure
[**get_subject_procedure_specimens**](CoreApi.md#get_subject_procedure_specimens) | **GET** /subject_procedure_specimens | Get Subject Procedure Specimens
[**get_subject_procedures**](CoreApi.md#get_subject_procedures) | **GET** /subject_procedures | Get Subject Procedures
[**get_subjects**](CoreApi.md#get_subjects) | **GET** /subjects | Get Subjects
[**put_acquisition_specimen**](CoreApi.md#put_acquisition_specimen) | **PUT** /acquisition_specimen | Add Acquisition Specimen
[**put_acquisition_subject**](CoreApi.md#put_acquisition_subject) | **PUT** /acquisition_subject | Add Acquisition Subject
[**put_data_asset_collection**](CoreApi.md#put_data_asset_collection) | **PUT** /data_asset_collection | Add Data Asset Collection
[**put_data_asset_process_input**](CoreApi.md#put_data_asset_process_input) | **PUT** /data_asset_process_input | Add Data Asset Process Input
[**put_process_data_asset_input**](CoreApi.md#put_process_data_asset_input) | **PUT** /process_data_asset_input | Add Process Data Asset Input
[**put_specimen_acquisition**](CoreApi.md#put_specimen_acquisition) | **PUT** /specimen_acquisition | Add Specimen Acquisition
[**put_specimen_procedure_specimen_input**](CoreApi.md#put_specimen_procedure_specimen_input) | **PUT** /specimen_procedure_specimen_input | Add Specimen Procedure Specimen Input
[**put_specimen_procedure_specimen_output**](CoreApi.md#put_specimen_procedure_specimen_output) | **PUT** /specimen_procedure_specimen_output | Add Specimen Procedure Specimen Output
[**put_specimen_specimen_procedure_input**](CoreApi.md#put_specimen_specimen_procedure_input) | **PUT** /specimen_specimen_procedure_input | Add Specimen Specimen Procedure Input
[**put_specimen_specimen_procedure_output**](CoreApi.md#put_specimen_specimen_procedure_output) | **PUT** /specimen_specimen_procedure_output | Add Specimen Specimen Procedure Output
[**put_specimen_subject_procedure**](CoreApi.md#put_specimen_subject_procedure) | **PUT** /specimen_subject_procedure | Add Specimen Subject Procedure
[**put_subject_acquisition**](CoreApi.md#put_subject_acquisition) | **PUT** /subject_acquisition | Add Subject Acquisition
[**put_subject_procedure_specimen**](CoreApi.md#put_subject_procedure_specimen) | **PUT** /subject_procedure_specimen | Add Subject Procedure Specimen
[**remove_acquisition_specimen**](CoreApi.md#remove_acquisition_specimen) | **DELETE** /acquisition_specimen | Remove Acquisition Specimen
[**remove_acquisition_subject**](CoreApi.md#remove_acquisition_subject) | **DELETE** /acquisition_subject | Remove Acquisition Subject
[**remove_data_asset_collection**](CoreApi.md#remove_data_asset_collection) | **DELETE** /data_asset_collection | Remove Collection Data Asset
[**remove_data_asset_process_input**](CoreApi.md#remove_data_asset_process_input) | **DELETE** /data_asset_process_input | Remove Data Asset Process Input
[**remove_process_data_asset_input**](CoreApi.md#remove_process_data_asset_input) | **DELETE** /process_data_asset_input | Remove Process Data Asset Input
[**remove_specimen_acquisition**](CoreApi.md#remove_specimen_acquisition) | **DELETE** /specimen_acquisition | Remove Specimen Acquisition
[**remove_specimen_procedure_specimen_input**](CoreApi.md#remove_specimen_procedure_specimen_input) | **DELETE** /specimen_procedure_specimen_input | Remove Specimen Procedure Specimen Input
[**remove_specimen_procedure_specimen_output**](CoreApi.md#remove_specimen_procedure_specimen_output) | **DELETE** /specimen_procedure_specimen_output | Remove Specimen Procedure Specimen Output
[**remove_specimen_specimen_procedure_input**](CoreApi.md#remove_specimen_specimen_procedure_input) | **DELETE** /specimen_specimen_procedure_input | Remove Specimen Specimen Procedure Input
[**remove_specimen_specimen_procedure_output**](CoreApi.md#remove_specimen_specimen_procedure_output) | **DELETE** /specimen_specimen_procedure_output | Remove Specimen Specimen Procedure Output
[**remove_specimen_subject_procedure**](CoreApi.md#remove_specimen_subject_procedure) | **DELETE** /specimen_subject_procedure | Remove Specimen Subject Procedure
[**remove_subject_acquisition**](CoreApi.md#remove_subject_acquisition) | **DELETE** /subject_acquisition | Remove Subject Acquisition
[**remove_subject_procedure_specimen**](CoreApi.md#remove_subject_procedure_specimen) | **DELETE** /subject_procedure_specimen | Remove Subject Procedure Specimen
[**update_acquisition**](CoreApi.md#update_acquisition) | **PUT** /acquisition | Update
[**update_data_asset**](CoreApi.md#update_data_asset) | **PUT** /data_asset | Update
[**update_instrument**](CoreApi.md#update_instrument) | **PUT** /instrument | Update
[**update_process**](CoreApi.md#update_process) | **PUT** /process | Update
[**update_quality_control**](CoreApi.md#update_quality_control) | **PUT** /quality_control | Update
[**update_schema**](CoreApi.md#update_schema) | **PUT** /schema | Update
[**update_schema_entity**](CoreApi.md#update_schema_entity) | **PUT** /schema_entity | Update
[**update_specimen**](CoreApi.md#update_specimen) | **PUT** /specimen | Update
[**update_specimen_procedure**](CoreApi.md#update_specimen_procedure) | **PUT** /specimen_procedure | Update
[**update_subject**](CoreApi.md#update_subject) | **PUT** /subject | Update
[**update_subject_procedure**](CoreApi.md#update_subject_procedure) | **PUT** /subject_procedure | Update


# **create_acquisition**
> Acquisitions create_acquisition(acquisition_create)

Create Acquisition

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.acquisition_create import AcquisitionCreate
from biodata_registry_api_client.models.acquisitions import Acquisitions
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    acquisition_create = biodata_registry_api_client.AcquisitionCreate() # AcquisitionCreate | 

    try:
        # Create Acquisition
        api_response = api_instance.create_acquisition(acquisition_create)
        print("The response of CoreApi->create_acquisition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_acquisition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acquisition_create** | [**AcquisitionCreate**](AcquisitionCreate.md)|  | 

### Return type

[**Acquisitions**](Acquisitions.md)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    data_asset_create = biodata_registry_api_client.DataAssetCreate() # DataAssetCreate | 

    try:
        # Create Data Asset
        api_response = api_instance.create_data_asset(data_asset_create)
        print("The response of CoreApi->create_data_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_data_asset: %s\n" % e)
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

# **create_instrument**
> Instruments create_instrument(instrument_create)

Create Instrument

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.instrument_create import InstrumentCreate
from biodata_registry_api_client.models.instruments import Instruments
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    instrument_create = biodata_registry_api_client.InstrumentCreate() # InstrumentCreate | 

    try:
        # Create Instrument
        api_response = api_instance.create_instrument(instrument_create)
        print("The response of CoreApi->create_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_create** | [**InstrumentCreate**](InstrumentCreate.md)|  | 

### Return type

[**Instruments**](Instruments.md)

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

# **create_process**
> Processes create_process(process_create)

Create Process

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.process_create import ProcessCreate
from biodata_registry_api_client.models.processes import Processes
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    process_create = biodata_registry_api_client.ProcessCreate() # ProcessCreate | 

    try:
        # Create Process
        api_response = api_instance.create_process(process_create)
        print("The response of CoreApi->create_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_create** | [**ProcessCreate**](ProcessCreate.md)|  | 

### Return type

[**Processes**](Processes.md)

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

# **create_quality_control**
> QualityControls create_quality_control(quality_control_create)

Create Quality Control

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.quality_control_create import QualityControlCreate
from biodata_registry_api_client.models.quality_controls import QualityControls
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    quality_control_create = biodata_registry_api_client.QualityControlCreate() # QualityControlCreate | 

    try:
        # Create Quality Control
        api_response = api_instance.create_quality_control(quality_control_create)
        print("The response of CoreApi->create_quality_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_quality_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality_control_create** | [**QualityControlCreate**](QualityControlCreate.md)|  | 

### Return type

[**QualityControls**](QualityControls.md)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    schema_create = biodata_registry_api_client.SchemaCreate() # SchemaCreate | 

    try:
        # Create Schema
        api_response = api_instance.create_schema(schema_create)
        print("The response of CoreApi->create_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_schema: %s\n" % e)
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    schema_entity_create = biodata_registry_api_client.SchemaEntityCreate() # SchemaEntityCreate | 

    try:
        # Create Schema Entity
        api_response = api_instance.create_schema_entity(schema_entity_create)
        print("The response of CoreApi->create_schema_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_schema_entity: %s\n" % e)
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

# **create_specimen**
> Specimens create_specimen(specimen_create)

Create Specimen

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimen_create import SpecimenCreate
from biodata_registry_api_client.models.specimens import Specimens
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    specimen_create = biodata_registry_api_client.SpecimenCreate() # SpecimenCreate | 

    try:
        # Create Specimen
        api_response = api_instance.create_specimen(specimen_create)
        print("The response of CoreApi->create_specimen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_specimen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specimen_create** | [**SpecimenCreate**](SpecimenCreate.md)|  | 

### Return type

[**Specimens**](Specimens.md)

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

# **create_specimen_procedure**
> SpecimenProcedures create_specimen_procedure(specimen_procedure_create)

Create Specimen Procedure

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimen_procedure_create import SpecimenProcedureCreate
from biodata_registry_api_client.models.specimen_procedures import SpecimenProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    specimen_procedure_create = biodata_registry_api_client.SpecimenProcedureCreate() # SpecimenProcedureCreate | 

    try:
        # Create Specimen Procedure
        api_response = api_instance.create_specimen_procedure(specimen_procedure_create)
        print("The response of CoreApi->create_specimen_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_specimen_procedure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specimen_procedure_create** | [**SpecimenProcedureCreate**](SpecimenProcedureCreate.md)|  | 

### Return type

[**SpecimenProcedures**](SpecimenProcedures.md)

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

# **create_subject**
> Subjects create_subject(subject_create)

Create Subject

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subject_create import SubjectCreate
from biodata_registry_api_client.models.subjects import Subjects
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    subject_create = biodata_registry_api_client.SubjectCreate() # SubjectCreate | 

    try:
        # Create Subject
        api_response = api_instance.create_subject(subject_create)
        print("The response of CoreApi->create_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_create** | [**SubjectCreate**](SubjectCreate.md)|  | 

### Return type

[**Subjects**](Subjects.md)

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

# **create_subject_procedure**
> SubjectProcedures create_subject_procedure(subject_procedure_create)

Create Subject Procedure

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subject_procedure_create import SubjectProcedureCreate
from biodata_registry_api_client.models.subject_procedures import SubjectProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    subject_procedure_create = biodata_registry_api_client.SubjectProcedureCreate() # SubjectProcedureCreate | 

    try:
        # Create Subject Procedure
        api_response = api_instance.create_subject_procedure(subject_procedure_create)
        print("The response of CoreApi->create_subject_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->create_subject_procedure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_procedure_create** | [**SubjectProcedureCreate**](SubjectProcedureCreate.md)|  | 

### Return type

[**SubjectProcedures**](SubjectProcedures.md)

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

# **delete_acquisition**
> object delete_acquisition(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_acquisition(id)
        print("The response of CoreApi->delete_acquisition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_acquisition: %s\n" % e)
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

# **delete_data_asset**
> object delete_data_asset(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_data_asset(id)
        print("The response of CoreApi->delete_data_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_data_asset: %s\n" % e)
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

# **delete_instrument**
> object delete_instrument(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_instrument(id)
        print("The response of CoreApi->delete_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_instrument: %s\n" % e)
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

# **delete_process**
> object delete_process(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_process(id)
        print("The response of CoreApi->delete_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_process: %s\n" % e)
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

# **delete_quality_control**
> object delete_quality_control(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_quality_control(id)
        print("The response of CoreApi->delete_quality_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_quality_control: %s\n" % e)
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

# **delete_schema**
> object delete_schema(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_schema(id)
        print("The response of CoreApi->delete_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_schema: %s\n" % e)
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

# **delete_schema_entity**
> object delete_schema_entity(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_schema_entity(id)
        print("The response of CoreApi->delete_schema_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_schema_entity: %s\n" % e)
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

# **delete_specimen**
> object delete_specimen(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_specimen(id)
        print("The response of CoreApi->delete_specimen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_specimen: %s\n" % e)
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

# **delete_specimen_procedure**
> object delete_specimen_procedure(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_specimen_procedure(id)
        print("The response of CoreApi->delete_specimen_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_specimen_procedure: %s\n" % e)
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

# **delete_subject**
> object delete_subject(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_subject(id)
        print("The response of CoreApi->delete_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_subject: %s\n" % e)
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

# **delete_subject_procedure**
> object delete_subject_procedure(id)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.delete_subject_procedure(id)
        print("The response of CoreApi->delete_subject_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->delete_subject_procedure: %s\n" % e)
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

# **get_acquisition**
> Acquisitions get_acquisition(id)

Get Acquisition

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.acquisitions import Acquisitions
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Acquisition
        api_response = api_instance.get_acquisition(id)
        print("The response of CoreApi->get_acquisition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_acquisition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Acquisitions**](Acquisitions.md)

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

# **get_acquisition_specimens**
> List[Specimens] get_acquisition_specimens(id)

Get Acquisition Subjects

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimens import Specimens
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Acquisition Subjects
        api_response = api_instance.get_acquisition_specimens(id)
        print("The response of CoreApi->get_acquisition_specimens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_acquisition_specimens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Specimens]**](Specimens.md)

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

# **get_acquisition_subjects**
> List[Subjects] get_acquisition_subjects(id)

Get Acquisition Subjects

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subjects import Subjects
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Acquisition Subjects
        api_response = api_instance.get_acquisition_subjects(id)
        print("The response of CoreApi->get_acquisition_subjects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_acquisition_subjects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Subjects]**](Subjects.md)

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

# **get_acquisitions**
> AcquisitionsPage get_acquisitions(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)

Get Acquisitions

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.acquisitions_page import AcquisitionsPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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

    try:
        # Get Acquisitions
        api_response = api_instance.get_acquisitions(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)
        print("The response of CoreApi->get_acquisitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_acquisitions: %s\n" % e)
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

### Return type

[**AcquisitionsPage**](AcquisitionsPage.md)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Data Asset
        api_response = api_instance.get_data_asset(id)
        print("The response of CoreApi->get_data_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_data_asset: %s\n" % e)
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

# **get_data_asset_collections**
> List[Collections] get_data_asset_collections(id)

Get Data Asset Collections

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Data Asset Collections
        api_response = api_instance.get_data_asset_collections(id)
        print("The response of CoreApi->get_data_asset_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_data_asset_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **get_data_asset_process_inputs**
> List[Processes] get_data_asset_process_inputs(id)

Get Data Asset Process Inputs

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.processes import Processes
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Data Asset Process Inputs
        api_response = api_instance.get_data_asset_process_inputs(id)
        print("The response of CoreApi->get_data_asset_process_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_data_asset_process_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Processes]**](Processes.md)

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
> DataAssetsPage get_data_assets(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike, location__ilike=location__ilike)

Get Data Assets

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.data_assets_page import DataAssetsPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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
    name__ilike = 'name__ilike_example' # str |  (optional)
    location__ilike = 'location__ilike_example' # str |  (optional)

    try:
        # Get Data Assets
        api_response = api_instance.get_data_assets(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike, location__ilike=location__ilike)
        print("The response of CoreApi->get_data_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_data_assets: %s\n" % e)
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
 **name__ilike** | **str**|  | [optional] 
 **location__ilike** | **str**|  | [optional] 

### Return type

[**DataAssetsPage**](DataAssetsPage.md)

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

# **get_instrument**
> Instruments get_instrument(id)

Get Instrument

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.instruments import Instruments
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Instrument
        api_response = api_instance.get_instrument(id)
        print("The response of CoreApi->get_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Instruments**](Instruments.md)

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

# **get_instruments**
> InstrumentsPage get_instruments(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike)

Get Instruments

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.instruments_page import InstrumentsPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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
    name__ilike = 'name__ilike_example' # str |  (optional)

    try:
        # Get Instruments
        api_response = api_instance.get_instruments(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike)
        print("The response of CoreApi->get_instruments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_instruments: %s\n" % e)
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
 **name__ilike** | **str**|  | [optional] 

### Return type

[**InstrumentsPage**](InstrumentsPage.md)

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

# **get_process**
> Processes get_process(id)

Get Process

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.processes import Processes
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Process
        api_response = api_instance.get_process(id)
        print("The response of CoreApi->get_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Processes**](Processes.md)

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

# **get_process_data_asset_inputs**
> List[DataAssets] get_process_data_asset_inputs(id)

Get Process Data Asset Inputs

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Process Data Asset Inputs
        api_response = api_instance.get_process_data_asset_inputs(id)
        print("The response of CoreApi->get_process_data_asset_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_process_data_asset_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **get_processes**
> ProcessesPage get_processes(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)

Get Processes

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.processes_page import ProcessesPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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

    try:
        # Get Processes
        api_response = api_instance.get_processes(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)
        print("The response of CoreApi->get_processes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_processes: %s\n" % e)
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

### Return type

[**ProcessesPage**](ProcessesPage.md)

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

# **get_quality_control**
> QualityControls get_quality_control(id)

Get Quality Control

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.quality_controls import QualityControls
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Quality Control
        api_response = api_instance.get_quality_control(id)
        print("The response of CoreApi->get_quality_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_quality_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**QualityControls**](QualityControls.md)

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

# **get_quality_controls**
> QualityControlsPage get_quality_controls(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)

Get Quality Controls

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.quality_controls_page import QualityControlsPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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

    try:
        # Get Quality Controls
        api_response = api_instance.get_quality_controls(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)
        print("The response of CoreApi->get_quality_controls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_quality_controls: %s\n" % e)
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

### Return type

[**QualityControlsPage**](QualityControlsPage.md)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Schema
        api_response = api_instance.get_schema(id)
        print("The response of CoreApi->get_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_schema: %s\n" % e)
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

# **get_schema_entities**
> SchemaEntitiesPage get_schema_entities(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike)

Get Schema Entities

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schema_entities_page import SchemaEntitiesPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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
    name__ilike = 'name__ilike_example' # str |  (optional)

    try:
        # Get Schema Entities
        api_response = api_instance.get_schema_entities(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike)
        print("The response of CoreApi->get_schema_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_schema_entities: %s\n" % e)
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
 **name__ilike** | **str**|  | [optional] 

### Return type

[**SchemaEntitiesPage**](SchemaEntitiesPage.md)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Schema Entity
        api_response = api_instance.get_schema_entity(id)
        print("The response of CoreApi->get_schema_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_schema_entity: %s\n" % e)
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

# **get_schemas**
> SchemasPage get_schemas(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike, version=version)

Get Schemas

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.schemas_page import SchemasPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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
    name__ilike = 'name__ilike_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Get Schemas
        api_response = api_instance.get_schemas(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike, version=version)
        print("The response of CoreApi->get_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_schemas: %s\n" % e)
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
 **name__ilike** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**SchemasPage**](SchemasPage.md)

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

# **get_specimen**
> Specimens get_specimen(id)

Get Specimen

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimens import Specimens
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Specimen
        api_response = api_instance.get_specimen(id)
        print("The response of CoreApi->get_specimen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Specimens**](Specimens.md)

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

# **get_specimen_acquisitions**
> List[Acquisitions] get_specimen_acquisitions(id)

Get Specimen Acquisitions

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.acquisitions import Acquisitions
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Specimen Acquisitions
        api_response = api_instance.get_specimen_acquisitions(id)
        print("The response of CoreApi->get_specimen_acquisitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen_acquisitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Acquisitions]**](Acquisitions.md)

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

# **get_specimen_procedure**
> SpecimenProcedures get_specimen_procedure(id)

Get Specimen Procedure

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimen_procedures import SpecimenProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Specimen Procedure
        api_response = api_instance.get_specimen_procedure(id)
        print("The response of CoreApi->get_specimen_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen_procedure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SpecimenProcedures**](SpecimenProcedures.md)

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

# **get_specimen_procedure_specimen_inputs**
> List[Specimens] get_specimen_procedure_specimen_inputs(id)

Get Specimen Procedure Specimen Inputs

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimens import Specimens
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Specimen Procedure Specimen Inputs
        api_response = api_instance.get_specimen_procedure_specimen_inputs(id)
        print("The response of CoreApi->get_specimen_procedure_specimen_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen_procedure_specimen_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Specimens]**](Specimens.md)

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

# **get_specimen_procedure_specimen_outputs**
> List[Specimens] get_specimen_procedure_specimen_outputs(id)

Get Specimen Procedure Specimen Outputs

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimens import Specimens
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Specimen Procedure Specimen Outputs
        api_response = api_instance.get_specimen_procedure_specimen_outputs(id)
        print("The response of CoreApi->get_specimen_procedure_specimen_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen_procedure_specimen_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Specimens]**](Specimens.md)

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

# **get_specimen_procedures**
> SpecimenProceduresPage get_specimen_procedures(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)

Get Specimen Procedures

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimen_procedures_page import SpecimenProceduresPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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

    try:
        # Get Specimen Procedures
        api_response = api_instance.get_specimen_procedures(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)
        print("The response of CoreApi->get_specimen_procedures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen_procedures: %s\n" % e)
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

### Return type

[**SpecimenProceduresPage**](SpecimenProceduresPage.md)

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

# **get_specimen_specimen_procedure_inputs**
> List[SpecimenProcedures] get_specimen_specimen_procedure_inputs(id)

Get Specimen Specimen Procedure Inputs

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimen_procedures import SpecimenProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Specimen Specimen Procedure Inputs
        api_response = api_instance.get_specimen_specimen_procedure_inputs(id)
        print("The response of CoreApi->get_specimen_specimen_procedure_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen_specimen_procedure_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[SpecimenProcedures]**](SpecimenProcedures.md)

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

# **get_specimen_specimen_procedure_outputs**
> List[SpecimenProcedures] get_specimen_specimen_procedure_outputs(id)

Get Specimen Specimen Procedure Outputs

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimen_procedures import SpecimenProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Specimen Specimen Procedure Outputs
        api_response = api_instance.get_specimen_specimen_procedure_outputs(id)
        print("The response of CoreApi->get_specimen_specimen_procedure_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen_specimen_procedure_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[SpecimenProcedures]**](SpecimenProcedures.md)

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

# **get_specimen_subject_procedures**
> List[SubjectProcedures] get_specimen_subject_procedures(id)

Get Specimen Subject Procedures

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subject_procedures import SubjectProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Specimen Subject Procedures
        api_response = api_instance.get_specimen_subject_procedures(id)
        print("The response of CoreApi->get_specimen_subject_procedures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimen_subject_procedures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[SubjectProcedures]**](SubjectProcedures.md)

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

# **get_specimens**
> SpecimensPage get_specimens(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike)

Get Specimens

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimens_page import SpecimensPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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
    name__ilike = 'name__ilike_example' # str |  (optional)

    try:
        # Get Specimens
        api_response = api_instance.get_specimens(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike)
        print("The response of CoreApi->get_specimens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_specimens: %s\n" % e)
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
 **name__ilike** | **str**|  | [optional] 

### Return type

[**SpecimensPage**](SpecimensPage.md)

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

# **get_subject**
> Subjects get_subject(id)

Get Subject

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subjects import Subjects
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Subject
        api_response = api_instance.get_subject(id)
        print("The response of CoreApi->get_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Subjects**](Subjects.md)

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

# **get_subject_acquisitions**
> List[Acquisitions] get_subject_acquisitions(id)

Get Subject Acquisitions

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.acquisitions import Acquisitions
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Subject Acquisitions
        api_response = api_instance.get_subject_acquisitions(id)
        print("The response of CoreApi->get_subject_acquisitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_subject_acquisitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Acquisitions]**](Acquisitions.md)

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

# **get_subject_procedure**
> SubjectProcedures get_subject_procedure(id)

Get Subject Procedure

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subject_procedures import SubjectProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Subject Procedure
        api_response = api_instance.get_subject_procedure(id)
        print("The response of CoreApi->get_subject_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_subject_procedure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SubjectProcedures**](SubjectProcedures.md)

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

# **get_subject_procedure_specimens**
> List[Specimens] get_subject_procedure_specimens(id)

Get Subject Procedure Specimens

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimens import Specimens
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 

    try:
        # Get Subject Procedure Specimens
        api_response = api_instance.get_subject_procedure_specimens(id)
        print("The response of CoreApi->get_subject_procedure_specimens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_subject_procedure_specimens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Specimens]**](Specimens.md)

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

# **get_subject_procedures**
> SubjectProceduresPage get_subject_procedures(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)

Get Subject Procedures

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subject_procedures_page import SubjectProceduresPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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

    try:
        # Get Subject Procedures
        api_response = api_instance.get_subject_procedures(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte)
        print("The response of CoreApi->get_subject_procedures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_subject_procedures: %s\n" % e)
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

### Return type

[**SubjectProceduresPage**](SubjectProceduresPage.md)

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

# **get_subjects**
> SubjectsPage get_subjects(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike)

Get Subjects

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subjects_page import SubjectsPage
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
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
    name__ilike = 'name__ilike_example' # str |  (optional)

    try:
        # Get Subjects
        api_response = api_instance.get_subjects(next_token=next_token, limit=limit, created_at__gt=created_at__gt, created_at__lt=created_at__lt, created_at__gte=created_at__gte, created_at__lte=created_at__lte, updated_at__gt=updated_at__gt, updated_at__lt=updated_at__lt, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, name__ilike=name__ilike)
        print("The response of CoreApi->get_subjects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_subjects: %s\n" % e)
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
 **name__ilike** | **str**|  | [optional] 

### Return type

[**SubjectsPage**](SubjectsPage.md)

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

# **put_acquisition_specimen**
> object put_acquisition_specimen(id, specimen_id)

Add Acquisition Specimen

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_id = 56 # int | 

    try:
        # Add Acquisition Specimen
        api_response = api_instance.put_acquisition_specimen(id, specimen_id)
        print("The response of CoreApi->put_acquisition_specimen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_acquisition_specimen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_id** | **int**|  | 

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

# **put_acquisition_subject**
> object put_acquisition_subject(id, subject_id)

Add Acquisition Subject

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    subject_id = 56 # int | 

    try:
        # Add Acquisition Subject
        api_response = api_instance.put_acquisition_subject(id, subject_id)
        print("The response of CoreApi->put_acquisition_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_acquisition_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **subject_id** | **int**|  | 

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

# **put_data_asset_collection**
> object put_data_asset_collection(id, collection_id)

Add Data Asset Collection

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    collection_id = 56 # int | 

    try:
        # Add Data Asset Collection
        api_response = api_instance.put_data_asset_collection(id, collection_id)
        print("The response of CoreApi->put_data_asset_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_data_asset_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **collection_id** | **int**|  | 

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

# **put_data_asset_process_input**
> object put_data_asset_process_input(id, process_id)

Add Data Asset Process Input

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    process_id = 56 # int | 

    try:
        # Add Data Asset Process Input
        api_response = api_instance.put_data_asset_process_input(id, process_id)
        print("The response of CoreApi->put_data_asset_process_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_data_asset_process_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **process_id** | **int**|  | 

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

# **put_process_data_asset_input**
> object put_process_data_asset_input(id, data_asset_id)

Add Process Data Asset Input

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    data_asset_id = 56 # int | 

    try:
        # Add Process Data Asset Input
        api_response = api_instance.put_process_data_asset_input(id, data_asset_id)
        print("The response of CoreApi->put_process_data_asset_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_process_data_asset_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **data_asset_id** | **int**|  | 

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

# **put_specimen_acquisition**
> object put_specimen_acquisition(id, acquisition_id)

Add Specimen Acquisition

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    acquisition_id = 56 # int | 

    try:
        # Add Specimen Acquisition
        api_response = api_instance.put_specimen_acquisition(id, acquisition_id)
        print("The response of CoreApi->put_specimen_acquisition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_specimen_acquisition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **acquisition_id** | **int**|  | 

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

# **put_specimen_procedure_specimen_input**
> object put_specimen_procedure_specimen_input(id, specimen_id)

Add Specimen Procedure Specimen Input

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_id = 56 # int | 

    try:
        # Add Specimen Procedure Specimen Input
        api_response = api_instance.put_specimen_procedure_specimen_input(id, specimen_id)
        print("The response of CoreApi->put_specimen_procedure_specimen_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_specimen_procedure_specimen_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_id** | **int**|  | 

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

# **put_specimen_procedure_specimen_output**
> object put_specimen_procedure_specimen_output(id, specimen_id)

Add Specimen Procedure Specimen Output

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_id = 56 # int | 

    try:
        # Add Specimen Procedure Specimen Output
        api_response = api_instance.put_specimen_procedure_specimen_output(id, specimen_id)
        print("The response of CoreApi->put_specimen_procedure_specimen_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_specimen_procedure_specimen_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_id** | **int**|  | 

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

# **put_specimen_specimen_procedure_input**
> object put_specimen_specimen_procedure_input(id, specimen_procedure_id)

Add Specimen Specimen Procedure Input

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_procedure_id = 56 # int | 

    try:
        # Add Specimen Specimen Procedure Input
        api_response = api_instance.put_specimen_specimen_procedure_input(id, specimen_procedure_id)
        print("The response of CoreApi->put_specimen_specimen_procedure_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_specimen_specimen_procedure_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_procedure_id** | **int**|  | 

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

# **put_specimen_specimen_procedure_output**
> object put_specimen_specimen_procedure_output(id, specimen_procedure_id)

Add Specimen Specimen Procedure Output

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_procedure_id = 56 # int | 

    try:
        # Add Specimen Specimen Procedure Output
        api_response = api_instance.put_specimen_specimen_procedure_output(id, specimen_procedure_id)
        print("The response of CoreApi->put_specimen_specimen_procedure_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_specimen_specimen_procedure_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_procedure_id** | **int**|  | 

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

# **put_specimen_subject_procedure**
> object put_specimen_subject_procedure(id, subject_procedure_id)

Add Specimen Subject Procedure

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    subject_procedure_id = 56 # int | 

    try:
        # Add Specimen Subject Procedure
        api_response = api_instance.put_specimen_subject_procedure(id, subject_procedure_id)
        print("The response of CoreApi->put_specimen_subject_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_specimen_subject_procedure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **subject_procedure_id** | **int**|  | 

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

# **put_subject_acquisition**
> object put_subject_acquisition(id, acquisition_id)

Add Subject Acquisition

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    acquisition_id = 56 # int | 

    try:
        # Add Subject Acquisition
        api_response = api_instance.put_subject_acquisition(id, acquisition_id)
        print("The response of CoreApi->put_subject_acquisition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_subject_acquisition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **acquisition_id** | **int**|  | 

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

# **put_subject_procedure_specimen**
> object put_subject_procedure_specimen(id, specimen_id)

Add Subject Procedure Specimen

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_id = 56 # int | 

    try:
        # Add Subject Procedure Specimen
        api_response = api_instance.put_subject_procedure_specimen(id, specimen_id)
        print("The response of CoreApi->put_subject_procedure_specimen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->put_subject_procedure_specimen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_id** | **int**|  | 

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

# **remove_acquisition_specimen**
> object remove_acquisition_specimen(id, specimen_id)

Remove Acquisition Specimen

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_id = 56 # int | 

    try:
        # Remove Acquisition Specimen
        api_response = api_instance.remove_acquisition_specimen(id, specimen_id)
        print("The response of CoreApi->remove_acquisition_specimen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_acquisition_specimen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_id** | **int**|  | 

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

# **remove_acquisition_subject**
> object remove_acquisition_subject(id, subject_id)

Remove Acquisition Subject

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    subject_id = 56 # int | 

    try:
        # Remove Acquisition Subject
        api_response = api_instance.remove_acquisition_subject(id, subject_id)
        print("The response of CoreApi->remove_acquisition_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_acquisition_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **subject_id** | **int**|  | 

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

# **remove_data_asset_collection**
> object remove_data_asset_collection(id, collection_id)

Remove Collection Data Asset

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    collection_id = 56 # int | 

    try:
        # Remove Collection Data Asset
        api_response = api_instance.remove_data_asset_collection(id, collection_id)
        print("The response of CoreApi->remove_data_asset_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_data_asset_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **collection_id** | **int**|  | 

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

# **remove_data_asset_process_input**
> object remove_data_asset_process_input(id, process_id)

Remove Data Asset Process Input

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    process_id = 56 # int | 

    try:
        # Remove Data Asset Process Input
        api_response = api_instance.remove_data_asset_process_input(id, process_id)
        print("The response of CoreApi->remove_data_asset_process_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_data_asset_process_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **process_id** | **int**|  | 

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

# **remove_process_data_asset_input**
> object remove_process_data_asset_input(id, data_asset_id)

Remove Process Data Asset Input

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    data_asset_id = 56 # int | 

    try:
        # Remove Process Data Asset Input
        api_response = api_instance.remove_process_data_asset_input(id, data_asset_id)
        print("The response of CoreApi->remove_process_data_asset_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_process_data_asset_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **data_asset_id** | **int**|  | 

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

# **remove_specimen_acquisition**
> object remove_specimen_acquisition(id, acquisition_id)

Remove Specimen Acquisition

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    acquisition_id = 56 # int | 

    try:
        # Remove Specimen Acquisition
        api_response = api_instance.remove_specimen_acquisition(id, acquisition_id)
        print("The response of CoreApi->remove_specimen_acquisition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_specimen_acquisition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **acquisition_id** | **int**|  | 

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

# **remove_specimen_procedure_specimen_input**
> object remove_specimen_procedure_specimen_input(id, specimen_id)

Remove Specimen Procedure Specimen Input

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_id = 56 # int | 

    try:
        # Remove Specimen Procedure Specimen Input
        api_response = api_instance.remove_specimen_procedure_specimen_input(id, specimen_id)
        print("The response of CoreApi->remove_specimen_procedure_specimen_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_specimen_procedure_specimen_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_id** | **int**|  | 

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

# **remove_specimen_procedure_specimen_output**
> object remove_specimen_procedure_specimen_output(id, specimen_id)

Remove Specimen Procedure Specimen Output

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_id = 56 # int | 

    try:
        # Remove Specimen Procedure Specimen Output
        api_response = api_instance.remove_specimen_procedure_specimen_output(id, specimen_id)
        print("The response of CoreApi->remove_specimen_procedure_specimen_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_specimen_procedure_specimen_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_id** | **int**|  | 

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

# **remove_specimen_specimen_procedure_input**
> object remove_specimen_specimen_procedure_input(id, specimen_procedure_id)

Remove Specimen Specimen Procedure Input

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_procedure_id = 56 # int | 

    try:
        # Remove Specimen Specimen Procedure Input
        api_response = api_instance.remove_specimen_specimen_procedure_input(id, specimen_procedure_id)
        print("The response of CoreApi->remove_specimen_specimen_procedure_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_specimen_specimen_procedure_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_procedure_id** | **int**|  | 

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

# **remove_specimen_specimen_procedure_output**
> object remove_specimen_specimen_procedure_output(id, specimen_procedure_id)

Remove Specimen Specimen Procedure Output

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_procedure_id = 56 # int | 

    try:
        # Remove Specimen Specimen Procedure Output
        api_response = api_instance.remove_specimen_specimen_procedure_output(id, specimen_procedure_id)
        print("The response of CoreApi->remove_specimen_specimen_procedure_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_specimen_specimen_procedure_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_procedure_id** | **int**|  | 

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

# **remove_specimen_subject_procedure**
> object remove_specimen_subject_procedure(id, subject_procedure_id)

Remove Specimen Subject Procedure

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    subject_procedure_id = 56 # int | 

    try:
        # Remove Specimen Subject Procedure
        api_response = api_instance.remove_specimen_subject_procedure(id, subject_procedure_id)
        print("The response of CoreApi->remove_specimen_subject_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_specimen_subject_procedure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **subject_procedure_id** | **int**|  | 

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

# **remove_subject_acquisition**
> object remove_subject_acquisition(id, acquisition_id)

Remove Subject Acquisition

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    acquisition_id = 56 # int | 

    try:
        # Remove Subject Acquisition
        api_response = api_instance.remove_subject_acquisition(id, acquisition_id)
        print("The response of CoreApi->remove_subject_acquisition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_subject_acquisition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **acquisition_id** | **int**|  | 

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

# **remove_subject_procedure_specimen**
> object remove_subject_procedure_specimen(id, specimen_id)

Remove Subject Procedure Specimen

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_id = 56 # int | 

    try:
        # Remove Subject Procedure Specimen
        api_response = api_instance.remove_subject_procedure_specimen(id, specimen_id)
        print("The response of CoreApi->remove_subject_procedure_specimen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->remove_subject_procedure_specimen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_id** | **int**|  | 

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

# **update_acquisition**
> Acquisitions update_acquisition(id, acquisition_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.acquisition_update import AcquisitionUpdate
from biodata_registry_api_client.models.acquisitions import Acquisitions
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    acquisition_update = biodata_registry_api_client.AcquisitionUpdate() # AcquisitionUpdate | 

    try:
        # Update
        api_response = api_instance.update_acquisition(id, acquisition_update)
        print("The response of CoreApi->update_acquisition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_acquisition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **acquisition_update** | [**AcquisitionUpdate**](AcquisitionUpdate.md)|  | 

### Return type

[**Acquisitions**](Acquisitions.md)

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

# **update_data_asset**
> DataAssets update_data_asset(id, data_asset_update)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    data_asset_update = biodata_registry_api_client.DataAssetUpdate() # DataAssetUpdate | 

    try:
        # Update
        api_response = api_instance.update_data_asset(id, data_asset_update)
        print("The response of CoreApi->update_data_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_data_asset: %s\n" % e)
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

# **update_instrument**
> Instruments update_instrument(id, instrument_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.instrument_update import InstrumentUpdate
from biodata_registry_api_client.models.instruments import Instruments
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    instrument_update = biodata_registry_api_client.InstrumentUpdate() # InstrumentUpdate | 

    try:
        # Update
        api_response = api_instance.update_instrument(id, instrument_update)
        print("The response of CoreApi->update_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **instrument_update** | [**InstrumentUpdate**](InstrumentUpdate.md)|  | 

### Return type

[**Instruments**](Instruments.md)

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

# **update_process**
> Processes update_process(id, process_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.process_update import ProcessUpdate
from biodata_registry_api_client.models.processes import Processes
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    process_update = biodata_registry_api_client.ProcessUpdate() # ProcessUpdate | 

    try:
        # Update
        api_response = api_instance.update_process(id, process_update)
        print("The response of CoreApi->update_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **process_update** | [**ProcessUpdate**](ProcessUpdate.md)|  | 

### Return type

[**Processes**](Processes.md)

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

# **update_quality_control**
> QualityControls update_quality_control(id, quality_control_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.quality_control_update import QualityControlUpdate
from biodata_registry_api_client.models.quality_controls import QualityControls
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    quality_control_update = biodata_registry_api_client.QualityControlUpdate() # QualityControlUpdate | 

    try:
        # Update
        api_response = api_instance.update_quality_control(id, quality_control_update)
        print("The response of CoreApi->update_quality_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_quality_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **quality_control_update** | [**QualityControlUpdate**](QualityControlUpdate.md)|  | 

### Return type

[**QualityControls**](QualityControls.md)

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

# **update_schema**
> Schemas update_schema(id, schema_update)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    schema_update = biodata_registry_api_client.SchemaUpdate() # SchemaUpdate | 

    try:
        # Update
        api_response = api_instance.update_schema(id, schema_update)
        print("The response of CoreApi->update_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_schema: %s\n" % e)
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

# **update_schema_entity**
> SchemaEntities update_schema_entity(id, schema_entity_update)

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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    schema_entity_update = biodata_registry_api_client.SchemaEntityUpdate() # SchemaEntityUpdate | 

    try:
        # Update
        api_response = api_instance.update_schema_entity(id, schema_entity_update)
        print("The response of CoreApi->update_schema_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_schema_entity: %s\n" % e)
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

# **update_specimen**
> Specimens update_specimen(id, specimen_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimen_update import SpecimenUpdate
from biodata_registry_api_client.models.specimens import Specimens
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_update = biodata_registry_api_client.SpecimenUpdate() # SpecimenUpdate | 

    try:
        # Update
        api_response = api_instance.update_specimen(id, specimen_update)
        print("The response of CoreApi->update_specimen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_specimen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_update** | [**SpecimenUpdate**](SpecimenUpdate.md)|  | 

### Return type

[**Specimens**](Specimens.md)

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

# **update_specimen_procedure**
> SpecimenProcedures update_specimen_procedure(id, specimen_procedure_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.specimen_procedure_update import SpecimenProcedureUpdate
from biodata_registry_api_client.models.specimen_procedures import SpecimenProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    specimen_procedure_update = biodata_registry_api_client.SpecimenProcedureUpdate() # SpecimenProcedureUpdate | 

    try:
        # Update
        api_response = api_instance.update_specimen_procedure(id, specimen_procedure_update)
        print("The response of CoreApi->update_specimen_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_specimen_procedure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **specimen_procedure_update** | [**SpecimenProcedureUpdate**](SpecimenProcedureUpdate.md)|  | 

### Return type

[**SpecimenProcedures**](SpecimenProcedures.md)

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

# **update_subject**
> Subjects update_subject(id, subject_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subject_update import SubjectUpdate
from biodata_registry_api_client.models.subjects import Subjects
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    subject_update = biodata_registry_api_client.SubjectUpdate() # SubjectUpdate | 

    try:
        # Update
        api_response = api_instance.update_subject(id, subject_update)
        print("The response of CoreApi->update_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **subject_update** | [**SubjectUpdate**](SubjectUpdate.md)|  | 

### Return type

[**Subjects**](Subjects.md)

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

# **update_subject_procedure**
> SubjectProcedures update_subject_procedure(id, subject_procedure_update)

Update

### Example


```python
import biodata_registry_api_client
from biodata_registry_api_client.models.subject_procedure_update import SubjectProcedureUpdate
from biodata_registry_api_client.models.subject_procedures import SubjectProcedures
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
    api_instance = biodata_registry_api_client.CoreApi(api_client)
    id = 56 # int | 
    subject_procedure_update = biodata_registry_api_client.SubjectProcedureUpdate() # SubjectProcedureUpdate | 

    try:
        # Update
        api_response = api_instance.update_subject_procedure(id, subject_procedure_update)
        print("The response of CoreApi->update_subject_procedure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->update_subject_procedure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **subject_procedure_update** | [**SubjectProcedureUpdate**](SubjectProcedureUpdate.md)|  | 

### Return type

[**SubjectProcedures**](SubjectProcedures.md)

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

