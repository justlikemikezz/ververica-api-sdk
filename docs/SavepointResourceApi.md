# ververica_api_sdk.SavepointResourceApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_savepoint_using_post**](SavepointResourceApi.md#create_savepoint_using_post) | **POST** /api/v1/namespaces/{namespace}/savepoints | Create a new savepoint
[**get_savepoint_using_get**](SavepointResourceApi.md#get_savepoint_using_get) | **GET** /api/v1/namespaces/{namespace}/savepoints/{savepointId} | Get a savepoint by id
[**get_savepoints_using_get**](SavepointResourceApi.md#get_savepoints_using_get) | **GET** /api/v1/namespaces/{namespace}/savepoints | List all savepoints. Can be filtered by DeploymentId


# **create_savepoint_using_post**
> Savepoint create_savepoint_using_post(namespace, savepoint_change)

Create a new savepoint

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.SavepointResourceApi()
namespace = 'namespace_example' # str | namespace
savepoint_change = ververica_api_sdk.Savepoint() # Savepoint | savepointChange

try:
    # Create a new savepoint
    api_response = api_instance.create_savepoint_using_post(namespace, savepoint_change)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavepointResourceApi->create_savepoint_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 
 **savepoint_change** | [**Savepoint**](Savepoint.md)| savepointChange | 

### Return type

[**Savepoint**](Savepoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_savepoint_using_get**
> Savepoint get_savepoint_using_get(namespace, savepoint_id)

Get a savepoint by id

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.SavepointResourceApi()
namespace = 'namespace_example' # str | namespace
savepoint_id = 'savepoint_id_example' # str | savepointId

try:
    # Get a savepoint by id
    api_response = api_instance.get_savepoint_using_get(namespace, savepoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavepointResourceApi->get_savepoint_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 
 **savepoint_id** | [**str**](.md)| savepointId | 

### Return type

[**Savepoint**](Savepoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_savepoints_using_get**
> list[Savepoint] get_savepoints_using_get(namespace, deployment_id=deployment_id, job_id=job_id)

List all savepoints. Can be filtered by DeploymentId

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.SavepointResourceApi()
namespace = 'namespace_example' # str | namespace
deployment_id = 'deployment_id_example' # str | deploymentId (optional)
job_id = 'job_id_example' # str | jobId (optional)

try:
    # List all savepoints. Can be filtered by DeploymentId
    api_response = api_instance.get_savepoints_using_get(namespace, deployment_id=deployment_id, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavepointResourceApi->get_savepoints_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 
 **deployment_id** | [**str**](.md)| deploymentId | [optional] 
 **job_id** | [**str**](.md)| jobId | [optional] 

### Return type

[**list[Savepoint]**](Savepoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

