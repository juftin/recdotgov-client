# recdotgov_client.RecreationAreaAddressesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rec_area_address**](RecreationAreaAddressesApi.md#get_rec_area_address) | **GET** /recareaaddresses/{recAreaAddressId} | Retrieve a specific RecArea address by id
[**get_rec_area_addresses**](RecreationAreaAddressesApi.md#get_rec_area_addresses) | **GET** /recareaaddresses | Retrieve all RecArea addresses
[**get_rec_area_rec_area_address**](RecreationAreaAddressesApi.md#get_rec_area_rec_area_address) | **GET** /recareas/{recAreaId}/recareaaddresses/{recAreaAddressId} | Retrieve a specific RecArea address by id for a RecArea
[**get_rec_area_rec_area_addresses**](RecreationAreaAddressesApi.md#get_rec_area_rec_area_addresses) | **GET** /recareas/{recAreaId}/recareaaddresses | Retrieve all RecArea addresses for a RecArea

# **get_rec_area_address**
> RecreationAreaAddress get_rec_area_address(rec_area_address_id)

Retrieve a specific RecArea address by id

This endpoint retrieves a specific RecArea.

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
api_instance = recdotgov_client.RecreationAreaAddressesApi(recdotgov_client.ApiClient(configuration))
rec_area_address_id = 'rec_area_address_id_example' # str | Id of the RecArea address

try:
    # Retrieve a specific RecArea address by id
    api_response = api_instance.get_rec_area_address(rec_area_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreaAddressesApi->get_rec_area_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_address_id** | **str**| Id of the RecArea address | 

### Return type

[**RecreationAreaAddress**](RecreationAreaAddress.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_addresses**
> InlineResponse2003 get_rec_area_addresses(query=query, limit=limit, offset=offset)

Retrieve all RecArea addresses

This endpoint retrieves all RecArea addresses.

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
api_instance = recdotgov_client.RecreationAreaAddressesApi(recdotgov_client.ApiClient(configuration))
query = 'query_example' # str | Query filter criteria. Searches on city, state, postal code, country code, and street address fields 1, 2, and 3 (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all RecArea addresses
    api_response = api_instance.get_rec_area_addresses(query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreaAddressesApi->get_rec_area_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter criteria. Searches on city, state, postal code, country code, and street address fields 1, 2, and 3 | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_rec_area_address**
> RecreationAreaAddress get_rec_area_rec_area_address(rec_area_id, rec_area_address_id)

Retrieve a specific RecArea address by id for a RecArea

This endpoint retrieves a specific RecArea for a specific RecArea.

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
api_instance = recdotgov_client.RecreationAreaAddressesApi(recdotgov_client.ApiClient(configuration))
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
rec_area_address_id = 'rec_area_address_id_example' # str | Id of the RecArea address

try:
    # Retrieve a specific RecArea address by id for a RecArea
    api_response = api_instance.get_rec_area_rec_area_address(rec_area_id, rec_area_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreaAddressesApi->get_rec_area_rec_area_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **rec_area_address_id** | **str**| Id of the RecArea address | 

### Return type

[**RecreationAreaAddress**](RecreationAreaAddress.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_rec_area_addresses**
> InlineResponse2003 get_rec_area_rec_area_addresses(rec_area_id, query=query, limit=limit, offset=offset)

Retrieve all RecArea addresses for a RecArea

This endpoint retrieves all RecArea addresses for a specific RecArea.

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
api_instance = recdotgov_client.RecreationAreaAddressesApi(recdotgov_client.ApiClient(configuration))
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
query = 'query_example' # str | Query filter criteria. Searches on city, state, postal code, country code, and street address fields 1, 2, and 3 (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all RecArea addresses for a RecArea
    api_response = api_instance.get_rec_area_rec_area_addresses(rec_area_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreaAddressesApi->get_rec_area_rec_area_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **query** | **str**| Query filter criteria. Searches on city, state, postal code, country code, and street address fields 1, 2, and 3 | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

