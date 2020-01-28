# ververica_api_sdk.EventResourceApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events_using_get**](EventResourceApi.md#get_events_using_get) | **GET** /api/v1/namespaces/{namespace}/events | Filter all events for a deployment or job


# **get_events_using_get**
> ResourceListEvent get_events_using_get(namespace, deployment_id=deployment_id, job_id=job_id)

Filter all events for a deployment or job

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.EventResourceApi()
namespace = 'namespace_example' # str | namespace
deployment_id = 'deployment_id_example' # str | deploymentId (optional)
job_id = 'job_id_example' # str | jobId (optional)

try:
    # Filter all events for a deployment or job
    api_response = api_instance.get_events_using_get(namespace, deployment_id=deployment_id, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventResourceApi->get_events_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 
 **deployment_id** | [**str**](.md)| deploymentId | [optional] 
 **job_id** | [**str**](.md)| jobId | [optional] 

### Return type

[**ResourceListEvent**](ResourceListEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

