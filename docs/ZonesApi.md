# recdotgov_client.ZonesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permit_entrance_zone**](ZonesApi.md#get_permit_entrance_zone) | **GET** /permitentrances/{permitEntranceId}/zones/{zoneId} | Retrieve a zone for a permit entrance
[**get_permit_entrance_zones**](ZonesApi.md#get_permit_entrance_zones) | **GET** /permitentrances/{permitEntranceId}/zones | Retrieve all zones for a permit entrance

# **get_permit_entrance_zone**
> Zone get_permit_entrance_zone(zone_id)

Retrieve a zone for a permit entrance

This endpoint retrieves a specific zone for a specific permit entrance.

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
api_instance = recdotgov_client.ZonesApi(recdotgov_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | Id of the zone

try:
    # Retrieve a zone for a permit entrance
    api_response = api_instance.get_permit_entrance_zone(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->get_permit_entrance_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| Id of the zone | 

### Return type

[**Zone**](Zone.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permit_entrance_zones**
> InlineResponse20010 get_permit_entrance_zones()

Retrieve all zones for a permit entrance

This endpoint retrieves all zones for a specific permit entrance.

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
api_instance = recdotgov_client.ZonesApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all zones for a permit entrance
    api_response = api_instance.get_permit_entrance_zones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->get_permit_entrance_zones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

