# ververica_api_sdk.StatusResourceApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status_using_get**](StatusResourceApi.md#get_status_using_get) | **GET** /api/v1/status | Check that the server is running
[**get_system_info_using_get**](StatusResourceApi.md#get_system_info_using_get) | **GET** /api/v1/status/system-info | Get system&#39;s information


# **get_status_using_get**
> object get_status_using_get()

Check that the server is running

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.StatusResourceApi()

try:
    # Check that the server is running
    api_response = api_instance.get_status_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusResourceApi->get_status_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_info_using_get**
> SystemInformation get_system_info_using_get()

Get system's information

### Example
```python
from __future__ import print_function
import time
import ververica_api_sdk
from ververica_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_api_sdk.StatusResourceApi()

try:
    # Get system's information
    api_response = api_instance.get_system_info_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusResourceApi->get_system_info_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInformation**](SystemInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

