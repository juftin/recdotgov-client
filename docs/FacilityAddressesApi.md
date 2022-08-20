# recdotgov_client.FacilityAddressesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facility_address**](FacilityAddressesApi.md#get_facility_address) | **GET** /facilityaddresses/{facilityAddressId} | Retrieve a specific facility address by id
[**get_facility_addresses**](FacilityAddressesApi.md#get_facility_addresses) | **GET** /facilityaddresses | Retrieve all facility addresses
[**get_facility_facility_address**](FacilityAddressesApi.md#get_facility_facility_address) | **GET** /facilities/{facilityId}/facilityaddresses/{facilityAddressId} | Retrieve a specific facility address by id for a facility
[**get_facility_facility_addresses**](FacilityAddressesApi.md#get_facility_facility_addresses) | **GET** /facilities/{facilityId}/facilityaddresses | Retrieve all facility addresses for a facility

# **get_facility_address**
> FacilityAddress get_facility_address(facility_address_id)

Retrieve a specific facility address by id

This endpoint retrieves a specific facility.

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
facility_address_id = 'facility_address_id_example' # str | Id of the facility address

try:
    # Retrieve a specific facility address by id
    api_response = api_instance.get_facility_address(facility_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityAddressesApi->get_facility_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_address_id** | **str**| Id of the facility address | 

### Return type

[**FacilityAddress**](FacilityAddress.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_addresses**
> InlineResponse2004 get_facility_addresses(query=query, limit=limit, offset=offset)

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
query = 'query_example' # str | Query filter criteria. Searches on city, state, postal code, country code, and street address fields 1, 2, and 3 (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all facility addresses
    api_response = api_instance.get_facility_addresses(query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityAddressesApi->get_facility_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter criteria. Searches on city, state, postal code, country code, and street address fields 1, 2, and 3 | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_facility_address**
> FacilityAddress get_facility_facility_address(facility_id, facility_address_id)

Retrieve a specific facility address by id for a facility

This endpoint retrieves a specific facility for a specific facility.

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
facility_id = 'facility_id_example' # str | Id of the facility
facility_address_id = 'facility_address_id_example' # str | Id of the facility address

try:
    # Retrieve a specific facility address by id for a facility
    api_response = api_instance.get_facility_facility_address(facility_id, facility_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityAddressesApi->get_facility_facility_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **facility_address_id** | **str**| Id of the facility address | 

### Return type

[**FacilityAddress**](FacilityAddress.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_facility_addresses**
> InlineResponse2004 get_facility_facility_addresses(facility_id, query=query, limit=limit, offset=offset)

Retrieve all facility addresses for a facility

This endpoint retrieves all facility addresses for a specific facility.

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
facility_id = 'facility_id_example' # str | Id of the facility
query = 'query_example' # str | Query filter criteria. Searches on city, state, postal code, country code, and street address fields 1, 2, and 3 (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all facility addresses for a facility
    api_response = api_instance.get_facility_facility_addresses(facility_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityAddressesApi->get_facility_facility_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **query** | **str**| Query filter criteria. Searches on city, state, postal code, country code, and street address fields 1, 2, and 3 | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

