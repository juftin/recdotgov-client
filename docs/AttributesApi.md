# recdotgov_client.AttributesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campsite_attributes**](AttributesApi.md#get_campsite_attributes) | **GET** /campsites/{campsiteId}/attributes | Retrieve all attributes for a campsite
[**get_tour_attributes**](AttributesApi.md#get_tour_attributes) | **GET** /tours/{tourId}/attributes | Retrieve all attributes for a tour

# **get_campsite_attributes**
> InlineResponse2009 get_campsite_attributes()

Retrieve all attributes for a campsite

This endpoint retrieves all attributes for a specific campsite.

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
api_instance = recdotgov_client.AttributesApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all attributes for a campsite
    api_response = api_instance.get_campsite_attributes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_campsite_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tour_attributes**
> get_tour_attributes()

Retrieve all attributes for a tour

This endpoint retrieves all attributes for a specific tour.

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
api_instance = recdotgov_client.AttributesApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all attributes for a tour
    api_instance.get_tour_attributes()
except ApiException as e:
    print("Exception when calling AttributesApi->get_tour_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

