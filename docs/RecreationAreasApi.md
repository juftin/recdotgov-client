# recdotgov_client.RecreationAreasApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_rec_area**](RecreationAreasApi.md#get_organization_rec_area) | **GET** /organizations/{orgId}/recareas/{recAreaId} | Retrieve a specific RecArea by id for an organization
[**get_organization_rec_areas**](RecreationAreasApi.md#get_organization_rec_areas) | **GET** /organizations/{orgId}/recareas | Retrieve all RecAreas for an organization
[**get_rec_area**](RecreationAreasApi.md#get_rec_area) | **GET** /recareas/{recAreaId} | Retrieve a specific RecArea by id
[**get_rec_areas**](RecreationAreasApi.md#get_rec_areas) | **GET** /recareas | Retrieve all RecAreas

# **get_organization_rec_area**
> RecreationArea get_organization_rec_area(rec_area_id, full=full)

Retrieve a specific RecArea by id for an organization

This endpoint retrieves a specific RecArea belonging to a specific organization.

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
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)

try:
    # Retrieve a specific RecArea by id for an organization
    api_response = api_instance.get_organization_rec_area(rec_area_id, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreasApi->get_organization_rec_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 

### Return type

[**RecreationArea**](RecreationArea.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_rec_areas**
> InlineResponse2001 get_organization_rec_areas(org_id, query=query, limit=limit, offset=offset, full=full, state=state, activity=activity, lastupdated=lastupdated, sort=sort)

Retrieve all RecAreas for an organization

This endpoint retrieves all RecAreas belonging to a specific organization.

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
org_id = 'org_id_example' # str | Id of the organization
query = 'query_example' # str | Query filter criteria. Searches on RecArea name, description, keywords, and stay limit (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)
state = ['state_example'] # list[str] | Comma delimited list of 2 character state codes (optional)
activity = ['activity_example'] # list[str] | Comma delimited list of activity IDs or keyword (optional)
lastupdated = 'lastupdated_example' # str | Return all records modified since this date **Date Format: (mm-dd-yyyy)** (optional)
sort = 'sort_example' # str | Sort the results by \"ID\", \"Date\" or \"Name\" (optional)

try:
    # Retrieve all RecAreas for an organization
    api_response = api_instance.get_organization_rec_areas(org_id, query=query, limit=limit, offset=offset, full=full, state=state, activity=activity, lastupdated=lastupdated, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreasApi->get_organization_rec_areas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Id of the organization | 
 **query** | **str**| Query filter criteria. Searches on RecArea name, description, keywords, and stay limit | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 
 **state** | [**list[str]**](str.md)| Comma delimited list of 2 character state codes | [optional] 
 **activity** | [**list[str]**](str.md)| Comma delimited list of activity IDs or keyword | [optional] 
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

# **get_rec_area**
> RecreationArea get_rec_area(rec_area_id, full=full)

Retrieve a specific RecArea by id

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
api_instance = recdotgov_client.RecreationAreasApi(recdotgov_client.ApiClient(configuration))
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)

try:
    # Retrieve a specific RecArea by id
    api_response = api_instance.get_rec_area(rec_area_id, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreasApi->get_rec_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 

### Return type

[**RecreationArea**](RecreationArea.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_areas**
> InlineResponse2001 get_rec_areas(query=query, limit=limit, offset=offset, full=full, state=state, activity=activity, latitude=latitude, longitude=longitude, radius=radius, lastupdated=lastupdated, sort=sort)

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
query = 'query_example' # str | Query filter criteria. Searches on RecArea name, description, keywords, and stay limit (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)
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
    api_response = api_instance.get_rec_areas(query=query, limit=limit, offset=offset, full=full, state=state, activity=activity, latitude=latitude, longitude=longitude, radius=radius, lastupdated=lastupdated, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecreationAreasApi->get_rec_areas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter criteria. Searches on RecArea name, description, keywords, and stay limit | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]
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

