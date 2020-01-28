# ververica_api_sdk.JobResourceApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_using_get**](JobResourceApi.md#get_job_using_get) | **GET** /api/v1/namespaces/{namespace}/jobs/{jobId} | Get a job by id
[**get_jobs_using_get**](JobResourceApi.md#get_jobs_using_get) | **GET** /api/v1/namespaces/{namespace}/jobs | List all jobs. Can be filtered by DeploymentId


# **get_job_using_get**
> Job get_job_using_get(job_id, namespace)

Get a job by id

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.JobResourceApi()
job_id = 'job_id_example' # str | jobId
namespace = 'namespace_example' # str | namespace

try:
    # Get a job by id
    api_response = api_instance.get_job_using_get(job_id, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobResourceApi->get_job_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| jobId | 
 **namespace** | **str**| namespace | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_using_get**
> ResourceListJob get_jobs_using_get(namespace, deployment_id=deployment_id)

List all jobs. Can be filtered by DeploymentId

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.JobResourceApi()
namespace = 'namespace_example' # str | namespace
deployment_id = 'deployment_id_example' # str | deploymentId (optional)

try:
    # List all jobs. Can be filtered by DeploymentId
    api_response = api_instance.get_jobs_using_get(namespace, deployment_id=deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobResourceApi->get_jobs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 
 **deployment_id** | [**str**](.md)| deploymentId | [optional] 

### Return type

[**ResourceListJob**](ResourceListJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

