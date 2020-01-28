# ververica_api_sdk.DeploymentTargetResourceApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment_target_using_post**](DeploymentTargetResourceApi.md#create_deployment_target_using_post) | **POST** /api/v1/namespaces/{namespace}/deployment-targets | Create a deployment target
[**delete_deployment_target_using_delete**](DeploymentTargetResourceApi.md#delete_deployment_target_using_delete) | **DELETE** /api/v1/namespaces/{namespace}/deployment-targets/{name} | Delete a deployment target
[**get_deployment_target_using_get**](DeploymentTargetResourceApi.md#get_deployment_target_using_get) | **GET** /api/v1/namespaces/{namespace}/deployment-targets/{name} | Get a deployment target by name
[**get_deployment_targets_using_get**](DeploymentTargetResourceApi.md#get_deployment_targets_using_get) | **GET** /api/v1/namespaces/{namespace}/deployment-targets | List all deployment targets


# **create_deployment_target_using_post**
> DeploymentTarget create_deployment_target_using_post(deployment_target, namespace)

Create a deployment target

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentTargetResourceApi()
deployment_target = ververica_api_sdk.DeploymentTarget() # DeploymentTarget | deploymentTarget
namespace = 'namespace_example' # str | namespace

try:
    # Create a deployment target
    api_response = api_instance.create_deployment_target_using_post(deployment_target, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentTargetResourceApi->create_deployment_target_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_target** | [**DeploymentTarget**](DeploymentTarget.md)| deploymentTarget | 
 **namespace** | **str**| namespace | 

### Return type

[**DeploymentTarget**](DeploymentTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment_target_using_delete**
> DeploymentTarget delete_deployment_target_using_delete(name, namespace)

Delete a deployment target

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentTargetResourceApi()
name = 'name_example' # str | name
namespace = 'namespace_example' # str | namespace

try:
    # Delete a deployment target
    api_response = api_instance.delete_deployment_target_using_delete(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentTargetResourceApi->delete_deployment_target_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **namespace** | **str**| namespace | 

### Return type

[**DeploymentTarget**](DeploymentTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_target_using_get**
> DeploymentTarget get_deployment_target_using_get(name, namespace)

Get a deployment target by name

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentTargetResourceApi()
name = 'name_example' # str | name
namespace = 'namespace_example' # str | namespace

try:
    # Get a deployment target by name
    api_response = api_instance.get_deployment_target_using_get(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentTargetResourceApi->get_deployment_target_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **namespace** | **str**| namespace | 

### Return type

[**DeploymentTarget**](DeploymentTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_targets_using_get**
> ResourceListDeploymentTarget get_deployment_targets_using_get(namespace)

List all deployment targets

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentTargetResourceApi()
namespace = 'namespace_example' # str | namespace

try:
    # List all deployment targets
    api_response = api_instance.get_deployment_targets_using_get(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentTargetResourceApi->get_deployment_targets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 

### Return type

[**ResourceListDeploymentTarget**](ResourceListDeploymentTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

