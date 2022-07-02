# recdotgov_client.RecreationAreasApi

All URIs are relative to *https://ridb.recreation.gov/ridb/dist/assets/swagger/RIDB_HOST/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rec_areas**](RecreationAreasApi.md#get_rec_areas) | **GET** /recareas | Retrieve all RecAreas

# **get_rec_areas**
> InlineResponse2001 get_rec_areas(full=full, state=state, activity=activity, latitude=latitude, longitude=longitude, radius=radius, lastupdated=lastupdated, sort=sort)

Retrieve all RecAreas

This endpoint retrieves all RecAreas.

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
api_instance = recdotgov_client.RecreationAreasApi(recdotgov_client.ApiClient(configuration))
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)
state = ['state_example'] # list[str] | Comma delimited list of 2 character state codes (optional)
activity = ['activity_example'] # list[str] | Comma delimited list of activity IDs or keyword (optional)
latitude = 1.2 # float | Latitude of the point in decimal degrees (optional)
longitude = 1.2 # float | Longitude of the point in decimal degrees (optional)
radius = 25 # float | Distance (in miles) by which to include search results (optional) (default to 25)
lastupdated = 'lastupdated_example' # str | Return all records modified since this date **Date Format: (mm-dd-yyyy)** (optional)
sort = 'sort_example' # str | Sort the results by \"ID\", \"Date\" or \"Name\" (optional)

try:
    # Retrieve all RecAreas
    api_response = api_instance.get_rec_areas(full=full, state=state, activity=activity, latitude=latitude, longitude=longitude, radius=radius, lastupdated=lastupdated, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreasApi->get_rec_areas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 
 **state** | [**list[str]**](str.md)| Comma delimited list of 2 character state codes | [optional] 
 **activity** | [**list[str]**](str.md)| Comma delimited list of activity IDs or keyword | [optional] 
 **latitude** | **float**| Latitude of the point in decimal degrees | [optional] 
 **longitude** | **float**| Longitude of the point in decimal degrees | [optional] 
 **radius** | **float**| Distance (in miles) by which to include search results | [optional] [default to 25]
 **lastupdated** | **str**| Return all records modified since this date **Date Format: (mm-dd-yyyy)** | [optional] 
 **sort** | **str**| Sort the results by \&quot;ID\&quot;, \&quot;Date\&quot; or \&quot;Name\&quot; | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

