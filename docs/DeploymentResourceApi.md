# ververica_api_sdk.DeploymentResourceApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment_using_post**](DeploymentResourceApi.md#create_deployment_using_post) | **POST** /api/v1/namespaces/{namespace}/deployments | Create a deployment
[**delete_deployment_using_delete**](DeploymentResourceApi.md#delete_deployment_using_delete) | **DELETE** /api/v1/namespaces/{namespace}/deployments/{deploymentId} | Delete deployment
[**get_deployment_using_get**](DeploymentResourceApi.md#get_deployment_using_get) | **GET** /api/v1/namespaces/{namespace}/deployments/{deploymentId} | Get a deployment by id
[**get_deployments_using_get**](DeploymentResourceApi.md#get_deployments_using_get) | **GET** /api/v1/namespaces/{namespace}/deployments | List all deployments
[**update_deployment_using_patch**](DeploymentResourceApi.md#update_deployment_using_patch) | **PATCH** /api/v1/namespaces/{namespace}/deployments/{deploymentId} | Update a deployment


# **create_deployment_using_post**
> Deployment create_deployment_using_post(deployment_change, namespace)

Create a deployment

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentResourceApi()
deployment_change = ververica_api_sdk.Deployment() # Deployment | deploymentChange
namespace = 'namespace_example' # str | namespace

try:
    # Create a deployment
    api_response = api_instance.create_deployment_using_post(deployment_change, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentResourceApi->create_deployment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_change** | [**Deployment**](Deployment.md)| deploymentChange | 
 **namespace** | **str**| namespace | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment_using_delete**
> Deployment delete_deployment_using_delete(deployment_id, namespace)

Delete deployment

This operation expects the deployment to be in desired state CANCELLED

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentResourceApi()
deployment_id = 'deployment_id_example' # str | deploymentId
namespace = 'namespace_example' # str | namespace

try:
    # Delete deployment
    api_response = api_instance.delete_deployment_using_delete(deployment_id, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentResourceApi->delete_deployment_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | [**str**](.md)| deploymentId | 
 **namespace** | **str**| namespace | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_using_get**
> Deployment get_deployment_using_get(deployment_id, namespace)

Get a deployment by id

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentResourceApi()
deployment_id = 'deployment_id_example' # str | deploymentId
namespace = 'namespace_example' # str | namespace

try:
    # Get a deployment by id
    api_response = api_instance.get_deployment_using_get(deployment_id, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentResourceApi->get_deployment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | [**str**](.md)| deploymentId | 
 **namespace** | **str**| namespace | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_using_get**
> ResourceListDeployment get_deployments_using_get(namespace, label_selector=label_selector)

List all deployments

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentResourceApi()
namespace = 'namespace_example' # str | namespace
label_selector = 'label_selector_example' # str | labelSelector (optional)

try:
    # List all deployments
    api_response = api_instance.get_deployments_using_get(namespace, label_selector=label_selector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentResourceApi->get_deployments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 
 **label_selector** | **str**| labelSelector | [optional] 

### Return type

[**ResourceListDeployment**](ResourceListDeployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deployment_using_patch**
> Deployment update_deployment_using_patch(body, deployment_id, namespace)

Update a deployment

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.DeploymentResourceApi()
body = ververica_api_sdk.ComDataartisansAppmanagerApiV1EntityDeploymentDeployment() # ComDataartisansAppmanagerApiV1EntityDeploymentDeployment | 
deployment_id = 'deployment_id_example' # str | deploymentId
namespace = 'namespace_example' # str | namespace

try:
    # Update a deployment
    api_response = api_instance.update_deployment_using_patch(body, deployment_id, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentResourceApi->update_deployment_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComDataartisansAppmanagerApiV1EntityDeploymentDeployment**](ComDataartisansAppmanagerApiV1EntityDeploymentDeployment.md)|  | 
 **deployment_id** | [**str**](.md)| deploymentId | 
 **namespace** | **str**| namespace | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

