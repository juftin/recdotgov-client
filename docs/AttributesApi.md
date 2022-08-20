# recdotgov_client.AttributesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campsite_attributes**](AttributesApi.md#get_campsite_attributes) | **GET** /campsites/{campsiteId}/attributes | Retrieve all attributes for a campsite
[**get_permit_entrance_attributes**](AttributesApi.md#get_permit_entrance_attributes) | **GET** /permitentrances/{permitEntranceId}/attributes | Retrieve all attributes for a permit entrance
[**get_tour_attributes**](AttributesApi.md#get_tour_attributes) | **GET** /tours/{tourId}/attributes | Retrieve all attributes for a tour

# **get_campsite_attributes**
> InlineResponse2009 get_campsite_attributes(campsite_id, query=query, limit=limit, offset=offset)

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
campsite_id = 'campsite_id_example' # str | Id of the campsite
query = 'query_example' # str | Query filter criteria. Searches on attribute name (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all attributes for a campsite
    api_response = api_instance.get_campsite_attributes(campsite_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_campsite_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campsite_id** | **str**| Id of the campsite | 
 **query** | **str**| Query filter criteria. Searches on attribute name | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permit_entrance_attributes**
> InlineResponse2009 get_permit_entrance_attributes(permit_entrance_id, query=query, limit=limit, offset=offset)

Retrieve all attributes for a permit entrance

This endpoint retrieves all attributes for a specific permit entrance.

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
permit_entrance_id = 'permit_entrance_id_example' # str | Id of the permit entrance
query = 'query_example' # str | Query filter criteria. Searches on attribute name (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all attributes for a permit entrance
    api_response = api_instance.get_permit_entrance_attributes(permit_entrance_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_permit_entrance_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permit_entrance_id** | **str**| Id of the permit entrance | 
 **query** | **str**| Query filter criteria. Searches on attribute name | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tour_attributes**
> InlineResponse2009 get_tour_attributes(tour_id, query=query, limit=limit, offset=offset)

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
tour_id = 'tour_id_example' # str | Id of the tour
query = 'query_example' # str | Query filter criteria. Searches on attribute name (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all attributes for a tour
    api_response = api_instance.get_tour_attributes(tour_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_tour_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tour_id** | **str**| Id of the tour | 
 **query** | **str**| Query filter criteria. Searches on attribute name | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

