# recdotgov_client.ActivitiesApi

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activities**](ActivitiesApi.md#get_activities) | **GET** /activities | Retrieve all activities
[**get_activity**](ActivitiesApi.md#get_activity) | **GET** /activities/{activityId} | Retrieve a specific activity by id
[**get_facility_activities**](ActivitiesApi.md#get_facility_activities) | **GET** /facilities/{facilityId}/activities | Retrieve all activities for a facility
[**get_facility_activity**](ActivitiesApi.md#get_facility_activity) | **GET** /facilities/{facilityId}/activities/{activityId} | Retrieve a specific activity by id for a facility
[**get_rec_area_activities**](ActivitiesApi.md#get_rec_area_activities) | **GET** /recareas/{recAreaId}/activities | Retrieve all activities for a RecArea
[**get_rec_area_activity**](ActivitiesApi.md#get_rec_area_activity) | **GET** /recareas/{recAreaId}/activities/{activityId} | Retrieve a specific activity by id for a RecArea

# **get_activities**
> InlineResponse2008 get_activities(query=query, limit=limit, offset=offset)

Retrieve all activities

This endpoint retrieves all activities.

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
api_instance = recdotgov_client.ActivitiesApi(recdotgov_client.ApiClient(configuration))
query = 'query_example' # str | Query filter criteria. Searches on activity name (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all activities
    api_response = api_instance.get_activities(query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter criteria. Searches on activity name | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity**
> Activity get_activity(activity_id)

Retrieve a specific activity by id

This endpoint retrieves a specific activity.

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
api_instance = recdotgov_client.ActivitiesApi(recdotgov_client.ApiClient(configuration))
activity_id = 'activity_id_example' # str | Id of the activity

try:
    # Retrieve a specific activity by id
    api_response = api_instance.get_activity(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| Id of the activity | 

### Return type

[**Activity**](Activity.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_activities**
> InlineResponse2008 get_facility_activities(facility_id, query=query, limit=limit, offset=offset)

Retrieve all activities for a facility

This endpoint retrieves all activities for a specific facility.

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
api_instance = recdotgov_client.ActivitiesApi(recdotgov_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | Id of the facility
query = 'query_example' # str | Query filter criteria. Searches on activity name (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all activities for a facility
    api_response = api_instance.get_facility_activities(facility_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_facility_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **query** | **str**| Query filter criteria. Searches on activity name | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_activity**
> Activity get_facility_activity(facility_id, activity_id)

Retrieve a specific activity by id for a facility

This endpoint retrieves a specific activity for a specific facility.

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
api_instance = recdotgov_client.ActivitiesApi(recdotgov_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | Id of the facility
activity_id = 'activity_id_example' # str | Id of the activity

try:
    # Retrieve a specific activity by id for a facility
    api_response = api_instance.get_facility_activity(facility_id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_facility_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 
 **activity_id** | **str**| Id of the activity | 

### Return type

[**Activity**](Activity.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_activities**
> InlineResponse2008 get_rec_area_activities(rec_area_id, query=query, limit=limit, offset=offset)

Retrieve all activities for a RecArea

This endpoint retrieves all activities for a specific RecArea.

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
api_instance = recdotgov_client.ActivitiesApi(recdotgov_client.ApiClient(configuration))
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
query = 'query_example' # str | Query filter criteria. Searches on activity name (optional)
limit = 50 # int | Number of records to return (max 50) (optional) (default to 50)
offset = 0 # int | Start record of overall result set (optional) (default to 0)

try:
    # Retrieve all activities for a RecArea
    api_response = api_instance.get_rec_area_activities(rec_area_id, query=query, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_rec_area_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **query** | **str**| Query filter criteria. Searches on activity name | [optional] 
 **limit** | **int**| Number of records to return (max 50) | [optional] [default to 50]
 **offset** | **int**| Start record of overall result set | [optional] [default to 0]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_activity**
> Activity get_rec_area_activity(rec_area_id, activity_id)

Retrieve a specific activity by id for a RecArea

This endpoint retrieves a specific activity for a specific RecArea.

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
api_instance = recdotgov_client.ActivitiesApi(recdotgov_client.ApiClient(configuration))
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea
activity_id = 'activity_id_example' # str | Id of the activity

try:
    # Retrieve a specific activity by id for a RecArea
    api_response = api_instance.get_rec_area_activity(rec_area_id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_rec_area_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 
 **activity_id** | **str**| Id of the activity | 

### Return type

[**Activity**](Activity.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

