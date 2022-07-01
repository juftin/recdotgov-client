# recdotgov_client.EventsApi

All URIs are relative to *https://ridb.recreation.gov/ridb/dist/assets/swagger/RIDB_HOST/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events**](EventsApi.md#get_events) | **GET** /events | Retrieve all events

# **get_events**
> InlineResponse20011 get_events()

Retrieve all events

This endpoint retrieves all events.

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
api_instance = recdotgov_client.EventsApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all events
    api_response = api_instance.get_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

