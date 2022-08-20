# recdotgov_client.LinksApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facility_link**](LinksApi.md#get_facility_link) | **GET** /facilities/{facilityId}/links/{linkId} | Retrieve a specific link by id for a facility
[**get_facility_links**](LinksApi.md#get_facility_links) | **GET** /facilities/{facilityId}/links | Retrieve all links for a facility
[**get_link**](LinksApi.md#get_link) | **GET** /links/{linkId} | Retrieve a specific link by id
[**get_links**](LinksApi.md#get_links) | **GET** /links | Retrieve all links
[**get_rec_area_link**](LinksApi.md#get_rec_area_link) | **GET** /recareas/{recAreaId}/links/{linkId} | Retrieve a specific link by id for a RecArea
[**get_rec_area_links**](LinksApi.md#get_rec_area_links) | **GET** /recareas/{recAreaId}/links | Retrieve all links for a RecArea

# **get_facility_link**
> Link get_facility_link(facility_id, link_id)

Retrieve a specific link by id for a facility

This endpoint retrieves a specific link for a specific facility.

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
api_instance = recdotgov_client.LinksApi(recdotgov_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | Id of the facility
link_id = 'link_id_example' # str | Id of the link

try:
    # Retrieve a specific link by id for a facility
    api_response = api_instance.get_facility_link(facility_id, link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_facility_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **link_id** | **str**| Id of the link | 

### Return type

[**Link**](Link.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_links**
> InlineResponse20012 get_facility_links(facility_id, query=query, limit=limit, offset=offset)

Retrieve all links for a facility

This endpoint retrieves all links for a specific facility.

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
api_instance = recdotgov_client.LinksApi(recdotgov_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | Id of the facility
query = 'query_example' # str | Query filter criteria. Searches on title, description, and link type (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all links for a facility
    api_response = api_instance.get_facility_links(facility_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_facility_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **query** | **str**| Query filter criteria. Searches on title, description, and link type | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link**
> Link get_link(link_id)

Retrieve a specific link by id

This endpoint retrieves a specific link.

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
api_instance = recdotgov_client.LinksApi(recdotgov_client.ApiClient(configuration))
link_id = 'link_id_example' # str | Id of the link

try:
    # Retrieve a specific link by id
    api_response = api_instance.get_link(link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**| Id of the link | 

### Return type

[**Link**](Link.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_links**
> InlineResponse20012 get_links(query=query, limit=limit, offset=offset)

Retrieve all links

This endpoint retrieves all links.

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
api_instance = recdotgov_client.LinksApi(recdotgov_client.ApiClient(configuration))
query = 'query_example' # str | Query filter criteria. Searches on title, description, and link type (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all links
    api_response = api_instance.get_links(query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter criteria. Searches on title, description, and link type | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_link**
> Link get_rec_area_link(rec_area_id, link_id)

Retrieve a specific link by id for a RecArea

This endpoint retrieves a specific link for a specific RecArea.

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
api_instance = recdotgov_client.LinksApi(recdotgov_client.ApiClient(configuration))
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
link_id = 'link_id_example' # str | Id of the link

try:
    # Retrieve a specific link by id for a RecArea
    api_response = api_instance.get_rec_area_link(rec_area_id, link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_rec_area_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **link_id** | **str**| Id of the link | 

### Return type

[**Link**](Link.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_links**
> InlineResponse20012 get_rec_area_links(rec_area_id, query=query, limit=limit, offset=offset)

Retrieve all links for a RecArea

This endpoint retrieves all links for a specific RecArea.

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
api_instance = recdotgov_client.LinksApi(recdotgov_client.ApiClient(configuration))
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
query = 'query_example' # str | Query filter criteria. Searches on title, description, and link type (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all links for a RecArea
    api_response = api_instance.get_rec_area_links(rec_area_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_rec_area_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **query** | **str**| Query filter criteria. Searches on title, description, and link type | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

