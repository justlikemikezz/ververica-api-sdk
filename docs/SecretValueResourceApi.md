# ververica_api_sdk.SecretValueResourceApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret_value_using_post**](SecretValueResourceApi.md#create_secret_value_using_post) | **POST** /api/v1/namespaces/{namespace}/secret-values | Create a secret value
[**delete_secret_value_using_delete**](SecretValueResourceApi.md#delete_secret_value_using_delete) | **DELETE** /api/v1/namespaces/{namespace}/secret-values/{name} | Delete a secret value
[**get_secret_value_using_get**](SecretValueResourceApi.md#get_secret_value_using_get) | **GET** /api/v1/namespaces/{namespace}/secret-values/{name} | Get a secret value by name
[**get_secret_values_using_get**](SecretValueResourceApi.md#get_secret_values_using_get) | **GET** /api/v1/namespaces/{namespace}/secret-values | List all secrets values
[**update_secret_value_using_patch**](SecretValueResourceApi.md#update_secret_value_using_patch) | **PATCH** /api/v1/namespaces/{namespace}/secret-values/{name} | Update a secret value


# **create_secret_value_using_post**
> SecretValue create_secret_value_using_post(namespace, secret_value)

Create a secret value

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.SecretValueResourceApi()
namespace = 'namespace_example' # str | namespace
secret_value = ververica_api_sdk.SecretValue() # SecretValue | secretValue

try:
    # Create a secret value
    api_response = api_instance.create_secret_value_using_post(namespace, secret_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretValueResourceApi->create_secret_value_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 
 **secret_value** | [**SecretValue**](SecretValue.md)| secretValue | 

### Return type

[**SecretValue**](SecretValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret_value_using_delete**
> SecretValue delete_secret_value_using_delete(name, namespace)

Delete a secret value

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.SecretValueResourceApi()
name = 'name_example' # str | name
namespace = 'namespace_example' # str | namespace

try:
    # Delete a secret value
    api_response = api_instance.delete_secret_value_using_delete(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretValueResourceApi->delete_secret_value_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **namespace** | **str**| namespace | 

### Return type

[**SecretValue**](SecretValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_value_using_get**
> SecretValue get_secret_value_using_get(name, namespace)

Get a secret value by name

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.SecretValueResourceApi()
name = 'name_example' # str | name
namespace = 'namespace_example' # str | namespace

try:
    # Get a secret value by name
    api_response = api_instance.get_secret_value_using_get(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretValueResourceApi->get_secret_value_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **namespace** | **str**| namespace | 

### Return type

[**SecretValue**](SecretValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_values_using_get**
> ResourceListSecretValue get_secret_values_using_get(namespace)

List all secrets values

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.SecretValueResourceApi()
namespace = 'namespace_example' # str | namespace

try:
    # List all secrets values
    api_response = api_instance.get_secret_values_using_get(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretValueResourceApi->get_secret_values_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace | 

### Return type

[**ResourceListSecretValue**](ResourceListSecretValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret_value_using_patch**
> SecretValue update_secret_value_using_patch(body, name, namespace)

Update a secret value

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.SecretValueResourceApi()
body = ververica_api_sdk.ComDataartisansAppmanagerApiV1EntitySecretvalueSecretValue() # ComDataartisansAppmanagerApiV1EntitySecretvalueSecretValue | 
name = 'name_example' # str | name
namespace = 'namespace_example' # str | namespace

try:
    # Update a secret value
    api_response = api_instance.update_secret_value_using_patch(body, name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretValueResourceApi->update_secret_value_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComDataartisansAppmanagerApiV1EntitySecretvalueSecretValue**](ComDataartisansAppmanagerApiV1EntitySecretvalueSecretValue.md)|  | 
 **name** | **str**| name | 
 **namespace** | **str**| namespace | 

### Return type

[**SecretValue**](SecretValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

