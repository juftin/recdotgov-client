# recdotgov_client.CampsitesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campsite**](CampsitesApi.md#get_campsite) | **GET** /campsites/{campsiteId} | Retrieve a specific campsite by id
[**get_campsites**](CampsitesApi.md#get_campsites) | **GET** /campsites | Retrieve all campsites
[**get_facility_campsite**](CampsitesApi.md#get_facility_campsite) | **GET** /facilities/{facilityId}/campsites/{campsiteId} | Retrieve a specific campsite by id for a facility
[**get_facility_campsites**](CampsitesApi.md#get_facility_campsites) | **GET** /facilities/{facilityId}/campsites | Retrieve all campsites for a facility

# **get_campsite**
> Campsite get_campsite(campsite_id)

Retrieve a specific campsite by id

This endpoint retrieves a specific campsite.

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
api_instance = recdotgov_client.CampsitesApi(recdotgov_client.ApiClient(configuration))
campsite_id = 'campsite_id_example' # str | Id of the campsite

try:
    # Retrieve a specific campsite by id
    api_response = api_instance.get_campsite(campsite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampsitesApi->get_campsite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campsite_id** | **str**| Id of the campsite | 

### Return type

[**Campsite**](Campsite.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campsites**
> InlineResponse2005 get_campsites(query=query, limit=limit, offset=offset)

Retrieve all campsites

This endpoint retrieves all campsites

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
api_instance = recdotgov_client.CampsitesApi(recdotgov_client.ApiClient(configuration))
query = 'query_example' # str | Query filter criteria. Searches on campsite name, type, loop, type of use (Overnight/Day), campsite accessible (Yes/No) (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all campsites
    api_response = api_instance.get_campsites(query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampsitesApi->get_campsites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter criteria. Searches on campsite name, type, loop, type of use (Overnight/Day), campsite accessible (Yes/No) | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_campsite**
> Campsite get_facility_campsite(facility_id, campsite_id)

Retrieve a specific campsite by id for a facility

This endpoint retrieves a specific campsite for a specific facility.

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
api_instance = recdotgov_client.CampsitesApi(recdotgov_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | Id of the facility
campsite_id = 'campsite_id_example' # str | Id of the campsite

try:
    # Retrieve a specific campsite by id for a facility
    api_response = api_instance.get_facility_campsite(facility_id, campsite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampsitesApi->get_facility_campsite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **campsite_id** | **str**| Id of the campsite | 

### Return type

[**Campsite**](Campsite.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_campsites**
> InlineResponse2005 get_facility_campsites(facility_id, query=query, limit=limit, offset=offset)

Retrieve all campsites for a facility

This endpoint retrieves all campsites for a specific facility.

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
api_instance = recdotgov_client.CampsitesApi(recdotgov_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | Id of the facility
query = 'query_example' # str | Query filter criteria. Searches on campsite name, type, loop, type of use (Overnight/Day), campsite accessible (Yes/No) (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all campsites for a facility
    api_response = api_instance.get_facility_campsites(facility_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampsitesApi->get_facility_campsites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **query** | **str**| Query filter criteria. Searches on campsite name, type, loop, type of use (Overnight/Day), campsite accessible (Yes/No) | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

