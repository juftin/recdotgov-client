# recdotgov_client.FacilitiesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facilities**](FacilitiesApi.md#get_facilities) | **GET** /facilities | Retrieve all facilities
[**get_facility**](FacilitiesApi.md#get_facility) | **GET** /facilities/{facilityId} | Retrieve a specific facility by id
[**get_organization_facilities**](FacilitiesApi.md#get_organization_facilities) | **GET** /organizations/{orgId}/facilities | Retrieve all facilities for an organization
[**get_organization_facility**](FacilitiesApi.md#get_organization_facility) | **GET** /organizations/{orgId}/facilities/{facilityId} | Retrieve a specific facility by id for an organization
[**get_rec_area_facilities**](FacilitiesApi.md#get_rec_area_facilities) | **GET** /recareas/{recAreaId}/facilities | Retrieve all facilities for a RecArea
[**get_rec_area_facility**](FacilitiesApi.md#get_rec_area_facility) | **GET** /recareas/{recAreaId}/facilities/{facilityId} | Retrieve a specific facility by id for a RecArea

# **get_facilities**
> InlineResponse2002 get_facilities(query=query, limit=limit, offset=offset, full=full, state=state, latitude=latitude, longitude=longitude, radius=radius, activity=activity, lastupdated=lastupdated, sort=sort)

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
query = 'query_example' # str | Query filter criteria. Searches on facility name, description, keywords, and stay limit (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)
state = ['state_example'] # list[str] | Comma delimited list of 2 character state codes (optional)
latitude = 1.2 # float | Latitude of the point in decimal degrees (optional)
longitude = 1.2 # float | Longitude of the point in decimal degrees (optional)
radius = 25 # float | Distance (in miles) by which to include search results (optional) (default to 25)
activity = ['activity_example'] # list[str] | Comma delimited list of activity IDs or keyword (optional)
lastupdated = 'lastupdated_example' # str | Return all records modified since this date **Date Format: (mm-dd-yyyy)** (optional)
sort = 'sort_example' # str | Sort the results by \"ID\", \"Date\" or \"Name\" (optional)

try:
    # Retrieve all facilities
    api_response = api_instance.get_facilities(query=query, limit=limit, offset=offset, full=full, state=state, latitude=latitude, longitude=longitude, radius=radius, activity=activity, lastupdated=lastupdated, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter criteria. Searches on facility name, description, keywords, and stay limit | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 
 **state** | [**list[str]**](str.md)| Comma delimited list of 2 character state codes | [optional] 
 **latitude** | **float**| Latitude of the point in decimal degrees | [optional] 
 **longitude** | **float**| Longitude of the point in decimal degrees | [optional] 
 **radius** | **float**| Distance (in miles) by which to include search results | [optional] [default to 25]
 **activity** | [**list[str]**](str.md)| Comma delimited list of activity IDs or keyword | [optional] 
 **lastupdated** | **str**| Return all records modified since this date **Date Format: (mm-dd-yyyy)** | [optional] 
 **sort** | **str**| Sort the results by \&quot;ID\&quot;, \&quot;Date\&quot; or \&quot;Name\&quot; | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility**
> Facility get_facility(facility_id, full=full)

Retrieve a specific facility by id

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
api_instance = recdotgov_client.FacilitiesApi(recdotgov_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | Id of the facility
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)

try:
    # Retrieve a specific facility by id
    api_response = api_instance.get_facility(facility_id, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 

### Return type

[**Facility**](Facility.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_facilities**
> InlineResponse2002 get_organization_facilities(org_id, query=query, limit=limit, offset=offset, full=full, state=state, activity=activity, lastupdated=lastupdated, sort=sort)

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
org_id = 'org_id_example' # str | Id of the organization
query = 'query_example' # str | Query filter criteria. Searches on facility name, description, keywords, and stay limit (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)
state = ['state_example'] # list[str] | Comma delimited list of 2 character state codes (optional)
activity = ['activity_example'] # list[str] | Comma delimited list of activity IDs or keyword (optional)
lastupdated = 'lastupdated_example' # str | Return all records modified since this date **Date Format: (mm-dd-yyyy)** (optional)
sort = 'sort_example' # str | Sort the results by \"ID\", \"Date\" or \"Name\" (optional)

try:
    # Retrieve all facilities for an organization
    api_response = api_instance.get_organization_facilities(org_id, query=query, limit=limit, offset=offset, full=full, state=state, activity=activity, lastupdated=lastupdated, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_organization_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Id of the organization | 
 **query** | **str**| Query filter criteria. Searches on facility name, description, keywords, and stay limit | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 
 **state** | [**list[str]**](str.md)| Comma delimited list of 2 character state codes | [optional] 
 **activity** | [**list[str]**](str.md)| Comma delimited list of activity IDs or keyword | [optional] 
 **lastupdated** | **str**| Return all records modified since this date **Date Format: (mm-dd-yyyy)** | [optional] 
 **sort** | **str**| Sort the results by \&quot;ID\&quot;, \&quot;Date\&quot; or \&quot;Name\&quot; | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_facility**
> Facility get_organization_facility(org_id, facility_id, full=full)

Retrieve a specific facility by id for an organization

This endpoint retrieves a specific facility belonging to a specific organization.

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
org_id = 'org_id_example' # str | Id of the organization
facility_id = 'facility_id_example' # str | Id of the facility
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)

try:
    # Retrieve a specific facility by id for an organization
    api_response = api_instance.get_organization_facility(org_id, facility_id, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_organization_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Id of the organization | 
 **facility_id** | **str**| Id of the facility | 
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 

### Return type

[**Facility**](Facility.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_facilities**
> InlineResponse2002 get_rec_area_facilities(rec_area_id, query=query, limit=limit, offset=offset, full=full, state=state, activity=activity, lastupdated=lastupdated, sort=sort)

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
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
query = 'query_example' # str | Query filter criteria. Searches on facility name, description, keywords, and stay limit (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)
state = ['state_example'] # list[str] | Comma delimited list of 2 character state codes (optional)
activity = ['activity_example'] # list[str] | Comma delimited list of activity IDs or keyword (optional)
lastupdated = 'lastupdated_example' # str | Return all records modified since this date **Date Format: (mm-dd-yyyy)** (optional)
sort = 'sort_example' # str | Sort the results by \"ID\", \"Date\" or \"Name\" (optional)

try:
    # Retrieve all facilities for a RecArea
    api_response = api_instance.get_rec_area_facilities(rec_area_id, query=query, limit=limit, offset=offset, full=full, state=state, activity=activity, lastupdated=lastupdated, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_rec_area_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **query** | **str**| Query filter criteria. Searches on facility name, description, keywords, and stay limit | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 
 **state** | [**list[str]**](str.md)| Comma delimited list of 2 character state codes | [optional] 
 **activity** | [**list[str]**](str.md)| Comma delimited list of activity IDs or keyword | [optional] 
 **lastupdated** | **str**| Return all records modified since this date **Date Format: (mm-dd-yyyy)** | [optional] 
 **sort** | **str**| Sort the results by \&quot;ID\&quot;, \&quot;Date\&quot; or \&quot;Name\&quot; | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_facility**
> Facility get_rec_area_facility(rec_area_id, facility_id, full=full)

Retrieve a specific facility by id for a RecArea

This endpoint retrieves a specific facility belonging to a specific RecArea.

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
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
facility_id = 'facility_id_example' # str | Id of the facility
full = 'full_example' # str | Return the full record details or compact (abbreviated) details (optional)

try:
    # Retrieve a specific facility by id for a RecArea
    api_response = api_instance.get_rec_area_facility(rec_area_id, facility_id, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilitiesApi->get_rec_area_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **facility_id** | **str**| Id of the facility | 
 **full** | **str**| Return the full record details or compact (abbreviated) details | [optional] 

### Return type

[**Facility**](Facility.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

