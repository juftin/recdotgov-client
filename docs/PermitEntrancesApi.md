# recdotgov_client.PermitEntrancesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permit_entrances**](PermitEntrancesApi.md#get_permit_entrances) | **GET** /permitentrances | Retrieve all permit entrances

# **get_permit_entrances**
> InlineResponse2006 get_permit_entrances()

Retrieve all permit entrances

This endpoint retrieves all permit entrances

### Example
```python
from __future__ import print_function
import time
import recdotgov_client
from recdotgov_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = recdotgov_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = recdotgov_client.PermitEntrancesApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all permit entrances
    api_response = api_instance.get_permit_entrances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermitEntrancesApi->get_permit_entrances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

