# recdotgov_client.PermitEntrancesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facility_permit_entrance**](PermitEntrancesApi.md#get_facility_permit_entrance) | **GET** /facilities/{facilityId}/permitentrances/{permitEntranceId} | Retrieve a specific permit entrance by id for a facility
[**get_facility_permit_entrances**](PermitEntrancesApi.md#get_facility_permit_entrances) | **GET** /facilities/{facilityId}/permitentrances | Retrieve all permit entrances for a facility
[**get_permit_entrance**](PermitEntrancesApi.md#get_permit_entrance) | **GET** /permitentrances/{permitentranceId} | Retrieve a specific permit entrance by id
[**get_permit_entrances**](PermitEntrancesApi.md#get_permit_entrances) | **GET** /permitentrances | Retrieve all permit entrances

# **get_facility_permit_entrance**
> PermitEntrance get_facility_permit_entrance(facility_id, permit_entrance_id)

Retrieve a specific permit entrance by id for a facility

This endpoint retrieves a specific permit entrance for a specific facility.

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
facility_id = 'facility_id_example' # str | Id of the facility
permit_entrance_id = 'permit_entrance_id_example' # str | Id of the permit entrance

try:
    # Retrieve a specific permit entrance by id for a facility
    api_response = api_instance.get_facility_permit_entrance(facility_id, permit_entrance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermitEntrancesApi->get_facility_permit_entrance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **permit_entrance_id** | **str**| Id of the permit entrance | 

### Return type

[**PermitEntrance**](PermitEntrance.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_permit_entrances**
> InlineResponse2006 get_facility_permit_entrances(facility_id, query=query, limit=limit, offset=offset)

Retrieve all permit entrances for a facility

This endpoint retrieves all permit entrances for a specific facility.

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
facility_id = 'facility_id_example' # str | Id of the facility
query = 'query_example' # str | Query filter criteria. Searches on permit name, type (Campground, Cabin, etc.), description, accessible (Yes/No), district, and town (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all permit entrances for a facility
    api_response = api_instance.get_facility_permit_entrances(facility_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermitEntrancesApi->get_facility_permit_entrances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **query** | **str**| Query filter criteria. Searches on permit name, type (Campground, Cabin, etc.), description, accessible (Yes/No), district, and town | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permit_entrance**
> PermitEntrance get_permit_entrance(permit_entrance_id)

Retrieve a specific permit entrance by id

This endpoint retrieves a specific permit entrance.

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
permit_entrance_id = 'permit_entrance_id_example' # str | Id of the permit entrance

try:
    # Retrieve a specific permit entrance by id
    api_response = api_instance.get_permit_entrance(permit_entrance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermitEntrancesApi->get_permit_entrance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permit_entrance_id** | **str**| Id of the permit entrance | 

### Return type

[**PermitEntrance**](PermitEntrance.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permit_entrances**
> InlineResponse2006 get_permit_entrances(query=query, limit=limit, offset=offset)

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
query = 'query_example' # str | Query filter criteria. Searches on permit name, type (Campground, Cabin, etc.), description, accessible (Yes/No), district, and town (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all permit entrances
    api_response = api_instance.get_permit_entrances(query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermitEntrancesApi->get_permit_entrances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter criteria. Searches on permit name, type (Campground, Cabin, etc.), description, accessible (Yes/No), district, and town | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

