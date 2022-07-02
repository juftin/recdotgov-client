# recdotgov_client.FacilitiesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facilities**](FacilitiesApi.md#get_facilities) | **GET** /facilities | Retrieve all facilities
[**get_organization_facilities**](FacilitiesApi.md#get_organization_facilities) | **GET** /organizations/{orgId}/facilities | Retrieve all facilities for an organization
[**get_rec_area_facilities**](FacilitiesApi.md#get_rec_area_facilities) | **GET** /recareas/{recAreaId}/facilities | Retrieve all facilities for a RecArea

# **get_facilities**
> InlineResponse2002 get_facilities()

Retrieve all facilities

This endpoint retrieves all facilities

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
api_instance = recdotgov_client.FacilitiesApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all facilities
    api_response = api_instance.get_facilities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_facilities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_facilities**
> get_organization_facilities()

Retrieve all facilities for an organization

This endpoint retrieves all facilities belonging to a specific organization.

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
api_instance = recdotgov_client.FacilitiesApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all facilities for an organization
    api_instance.get_organization_facilities()
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_organization_facilities: %s\n" % e)
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

# **get_rec_area_facilities**
> get_rec_area_facilities()

Retrieve all facilities for a RecArea

This endpoint retrieves all facilities belonging to a specific RecArea.

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
api_instance = recdotgov_client.FacilitiesApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all facilities for a RecArea
    api_instance.get_rec_area_facilities()
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_rec_area_facilities: %s\n" % e)
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

