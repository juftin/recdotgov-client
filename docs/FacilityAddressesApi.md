# recdotgov_client.FacilityAddressesApi

All URIs are relative to *https://ridb.recreation.gov/ridb/dist/assets/swagger/RIDB_HOST/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facility_addresses**](FacilityAddressesApi.md#get_facility_addresses) | **GET** /facilityaddresses | Retrieve all facility addresses

# **get_facility_addresses**
> InlineResponse2004 get_facility_addresses()

Retrieve all facility addresses

This endpoint retrieves all facility addresses.

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
api_instance = recdotgov_client.FacilityAddressesApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all facility addresses
    api_response = api_instance.get_facility_addresses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityAddressesApi->get_facility_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

