# recdotgov_client.DefaultApi

All URIs are relative to *https://ridb.recreation.gov/ridb/dist/assets/swagger/RIDB_HOST/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity**](DefaultApi.md#get_activity) | **GET** /activities/{activityId} | Retrieve a specific activity by id
[**get_all_facility_media**](DefaultApi.md#get_all_facility_media) | **GET** /facilities/{facilityId}/media | Retrieve all media for a facility
[**get_all_rec_area_media**](DefaultApi.md#get_all_rec_area_media) | **GET** /recareas/{recAreaId}/media | Retrieve all media for a RecArea
[**get_campsite**](DefaultApi.md#get_campsite) | **GET** /campsites/{campsiteId} | Retrieve a specific campsite by id
[**get_event**](DefaultApi.md#get_event) | **GET** /events/{eventId} | Retrieve a specific event by id
[**get_facility**](DefaultApi.md#get_facility) | **GET** /facilities/{facilityId} | Retrieve a specific facility by id
[**get_facility_activities**](DefaultApi.md#get_facility_activities) | **GET** /facilities/{facilityId}/activities | Retrieve all activities for a facility
[**get_facility_activity**](DefaultApi.md#get_facility_activity) | **GET** /facilities/{facilityId}/activities/{activityId} | Retrieve a specific activity by id for a facility
[**get_facility_address**](DefaultApi.md#get_facility_address) | **GET** /facilityaddresses/{facilityAddressId} | Retrieve a specific facility address by id
[**get_facility_campsite**](DefaultApi.md#get_facility_campsite) | **GET** /facilities/{facilityId}/campsites/{campsiteId} | Retrieve a specific campsite by id for a facility
[**get_facility_campsites**](DefaultApi.md#get_facility_campsites) | **GET** /facilities/{facilityId}/campsites | Retrieve all campsites for a facility
[**get_facility_event**](DefaultApi.md#get_facility_event) | **GET** /facilities/{facilityId}/events/{eventId} | Retrieve a specific event by id for a facility
[**get_facility_events**](DefaultApi.md#get_facility_events) | **GET** /facilities/{facilityId}/events | Retrieve all events for a facility
[**get_facility_facility_address**](DefaultApi.md#get_facility_facility_address) | **GET** /facilities/{facilityId}/facilityaddresses/{facilityAddressId} | Retrieve a specific facility address by id for a facility
[**get_facility_facility_addresses**](DefaultApi.md#get_facility_facility_addresses) | **GET** /facilities/{facilityId}/facilityaddresses | Retrieve all facility addresses for a facility
[**get_facility_link**](DefaultApi.md#get_facility_link) | **GET** /facilities/{facilityId}/links/{linkId} | Retrieve a specific link by id for a facility
[**get_facility_links**](DefaultApi.md#get_facility_links) | **GET** /facilities/{facilityId}/links | Retrieve all links for a facility
[**get_facility_media**](DefaultApi.md#get_facility_media) | **GET** /facilities/{facilityId}/media/{mediaId} | Retrieve a specific media by id for a facility
[**get_facility_permit_entrance**](DefaultApi.md#get_facility_permit_entrance) | **GET** /facilities/{facilityId}/permitentrances/{permitEntranceId} | Retrieve a specific permit entrance by id for a facility
[**get_facility_permit_entrances**](DefaultApi.md#get_facility_permit_entrances) | **GET** /facilities/{facilityId}/permitentrances | Retrieve all permit entrances for a facility
[**get_facility_tour**](DefaultApi.md#get_facility_tour) | **GET** /facilities/{facilityId}/tours/{tourId} | Retrieve a specific tour by id for a facility
[**get_facility_tours**](DefaultApi.md#get_facility_tours) | **GET** /facilities/{facilityId}/tours | Retrieve all tours for a facility
[**get_link**](DefaultApi.md#get_link) | **GET** /links/{linkId} | Retrieve a specific link by id
[**get_media**](DefaultApi.md#get_media) | **GET** /media/{mediaId} | Retrieve a specific media by id
[**get_organization**](DefaultApi.md#get_organization) | **GET** /organizations/{orgId} | Retrieve a specific organization by id
[**get_organization_facility**](DefaultApi.md#get_organization_facility) | **GET** /organizations/{orgId}/facilities/{facilityId} | Retrieve a specific facility by id for an organization
[**get_organization_rec_area**](DefaultApi.md#get_organization_rec_area) | **GET** /organizations/{orgId}/recareas/{recAreaId} | Retrieve a specific RecArea by id for an organization
[**get_organization_rec_areas**](DefaultApi.md#get_organization_rec_areas) | **GET** /organizations/{orgId}/recareas | Retrieve all RecAreas for an organization
[**get_permit_entrance**](DefaultApi.md#get_permit_entrance) | **GET** /permitentrances/{permitentranceId} | Retrieve a specific permit entrance by id
[**get_permit_entrance_attributes**](DefaultApi.md#get_permit_entrance_attributes) | **GET** /permitentrances/{permitEntranceId}/attributes | Retrieve all attributes for a permit entrance
[**get_rec_area**](DefaultApi.md#get_rec_area) | **GET** /recareas/{recAreaId} | Retrieve a specific RecArea by id
[**get_rec_area_activities**](DefaultApi.md#get_rec_area_activities) | **GET** /recareas/{recAreaId}/activities | Retrieve all activities for a RecArea
[**get_rec_area_activity**](DefaultApi.md#get_rec_area_activity) | **GET** /recareas/{recAreaId}/activities/{activityId} | Retrieve a specific activity by id for a RecArea
[**get_rec_area_address**](DefaultApi.md#get_rec_area_address) | **GET** /recareaaddresses/{recAreaAddressId} | Retrieve a specific RecArea address by id
[**get_rec_area_event**](DefaultApi.md#get_rec_area_event) | **GET** /recareas/{recAreaId}/events/{eventId} | Retrieve a specific event by id for a RecArea
[**get_rec_area_events**](DefaultApi.md#get_rec_area_events) | **GET** /recareas/{recAreaId}/events | Retrieve all events for a RecArea
[**get_rec_area_facility**](DefaultApi.md#get_rec_area_facility) | **GET** /recareas/{recAreaId}/facilities/{facilityId} | Retrieve a specific facility by id for a RecArea
[**get_rec_area_link**](DefaultApi.md#get_rec_area_link) | **GET** /recareas/{recAreaId}/links/{linkId} | Retrieve a specific link by id for a RecArea
[**get_rec_area_links**](DefaultApi.md#get_rec_area_links) | **GET** /recareas/{recAreaId}/links | Retrieve all links for a RecArea
[**get_rec_area_media**](DefaultApi.md#get_rec_area_media) | **GET** /recareas/{recAreaId}/media/{mediaId} | Retrieve a specific media by id for a RecArea
[**get_rec_area_rec_area_address**](DefaultApi.md#get_rec_area_rec_area_address) | **GET** /recareas/{recAreaId}/recareaaddresses/{recAreaAddressId} | Retrieve a specific RecArea address by id for a RecArea
[**get_rec_area_rec_area_addresses**](DefaultApi.md#get_rec_area_rec_area_addresses) | **GET** /recareas/{recAreaId}/recareaaddresses | Retrieve all RecArea addresses for a RecArea
[**get_tour**](DefaultApi.md#get_tour) | **GET** /tours/{tourId} | Retrieve a specific tour by id

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
activity_id = 'activity_id_example' # str | Id of the activity

try:
    # Retrieve a specific activity by id
    api_response = api_instance.get_activity(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_activity: %s\n" % e)
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

# **get_all_facility_media**
> get_all_facility_media()

Retrieve all media for a facility

This endpoint retrieves all media for a specific facility.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all media for a facility
    api_instance.get_all_facility_media()
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_facility_media: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rec_area_media**
> get_all_rec_area_media()

Retrieve all media for a RecArea

This endpoint retrieves all media for a specific RecArea.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all media for a RecArea
    api_instance.get_all_rec_area_media()
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_rec_area_media: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
campsite_id = 'campsite_id_example' # str | Id of the campsite

try:
    # Retrieve a specific campsite by id
    api_response = api_instance.get_campsite(campsite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_campsite: %s\n" % e)
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

# **get_event**
> Event get_event(event_id)

Retrieve a specific event by id

This endpoint retrieves a specific event.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
event_id = 'event_id_example' # str | Id of the event

try:
    # Retrieve a specific event by id
    api_response = api_instance.get_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Id of the event | 

### Return type

[**Event**](Event.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility**
> Facility get_facility(facility_id)

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | Id of the facility

try:
    # Retrieve a specific facility by id
    api_response = api_instance.get_facility(facility_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| Id of the facility | 

### Return type

[**Facility**](Facility.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_activities**
> get_facility_activities()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all activities for a facility
    api_instance.get_facility_activities()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_activities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_activity**
> get_facility_activity()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific activity by id for a facility
    api_instance.get_facility_activity()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_activity: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
facility_address_id = 'facility_address_id_example' # str | Id of the facility address

try:
    # Retrieve a specific facility address by id
    api_response = api_instance.get_facility_address(facility_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_address: %s\n" % e)
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

# **get_facility_campsite**
> get_facility_campsite()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific campsite by id for a facility
    api_instance.get_facility_campsite()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_campsite: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_campsites**
> get_facility_campsites()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all campsites for a facility
    api_instance.get_facility_campsites()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_campsites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_event**
> get_facility_event()

Retrieve a specific event by id for a facility

This endpoint retrieves a specific event for a specific facility.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific event by id for a facility
    api_instance.get_facility_event()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_event: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_events**
> get_facility_events()

Retrieve all events for a facility

This endpoint retrieves all events for a specific facility.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all events for a facility
    api_instance.get_facility_events()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_facility_address**
> get_facility_facility_address()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific facility address by id for a facility
    api_instance.get_facility_facility_address()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_facility_address: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_facility_addresses**
> get_facility_facility_addresses()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all facility addresses for a facility
    api_instance.get_facility_facility_addresses()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_facility_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_link**
> get_facility_link()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific link by id for a facility
    api_instance.get_facility_link()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_link: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_links**
> get_facility_links()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all links for a facility
    api_instance.get_facility_links()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_links: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_media**
> get_facility_media()

Retrieve a specific media by id for a facility

This endpoint retrieves a specific media for a specific facility.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific media by id for a facility
    api_instance.get_facility_media()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_media: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_permit_entrance**
> get_facility_permit_entrance()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific permit entrance by id for a facility
    api_instance.get_facility_permit_entrance()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_permit_entrance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_permit_entrances**
> get_facility_permit_entrances()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all permit entrances for a facility
    api_instance.get_facility_permit_entrances()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_permit_entrances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_tour**
> get_facility_tour()

Retrieve a specific tour by id for a facility

This endpoint retrieves a specific tour for a specific facility.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific tour by id for a facility
    api_instance.get_facility_tour()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_tour: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_tours**
> get_facility_tours()

Retrieve all tours for a facility

This endpoint retrieves all tours for a specific facility.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all tours for a facility
    api_instance.get_facility_tours()
except ApiException as e:
    print("Exception when calling DefaultApi->get_facility_tours: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
link_id = 'link_id_example' # str | Id of the link

try:
    # Retrieve a specific link by id
    api_response = api_instance.get_link(link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_link: %s\n" % e)
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

# **get_media**
> Media get_media(media_id)

Retrieve a specific media by id

This endpoint retrieves a specific media.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
media_id = 'media_id_example' # str | Id of the media

try:
    # Retrieve a specific media by id
    api_response = api_instance.get_media(media_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Id of the media | 

### Return type

[**Media**](Media.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> list[Organization] get_organization(org_id)

Retrieve a specific organization by id

This endpoint retrieves a specific organization.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
org_id = 'org_id_example' # str | Id of the organization

try:
    # Retrieve a specific organization by id
    api_response = api_instance.get_organization(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Id of the organization | 

### Return type

[**list[Organization]**](Organization.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_facility**
> get_organization_facility()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific facility by id for an organization
    api_instance.get_organization_facility()
except ApiException as e:
    print("Exception when calling DefaultApi->get_organization_facility: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_rec_area**
> get_organization_rec_area()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific RecArea by id for an organization
    api_instance.get_organization_rec_area()
except ApiException as e:
    print("Exception when calling DefaultApi->get_organization_rec_area: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_rec_areas**
> get_organization_rec_areas()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all RecAreas for an organization
    api_instance.get_organization_rec_areas()
except ApiException as e:
    print("Exception when calling DefaultApi->get_organization_rec_areas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
permit_entrance_id = 'permit_entrance_id_example' # str | Id of the permit entrance

try:
    # Retrieve a specific permit entrance by id
    api_response = api_instance.get_permit_entrance(permit_entrance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_permit_entrance: %s\n" % e)
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

# **get_permit_entrance_attributes**
> get_permit_entrance_attributes()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all attributes for a permit entrance
    api_instance.get_permit_entrance_attributes()
except ApiException as e:
    print("Exception when calling DefaultApi->get_permit_entrance_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area**
> RecreationArea get_rec_area(rec_area_id)

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
rec_area_id = 'rec_area_id_example' # str | Id of the RecArea

try:
    # Retrieve a specific RecArea by id
    api_response = api_instance.get_rec_area(rec_area_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rec_area_id** | **str**| Id of the RecArea | 

### Return type

[**RecreationArea**](RecreationArea.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_activities**
> get_rec_area_activities()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all activities for a RecArea
    api_instance.get_rec_area_activities()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_activities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_activity**
> get_rec_area_activity()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific activity by id for a RecArea
    api_instance.get_rec_area_activity()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_activity: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
rec_area_address_id = 'rec_area_address_id_example' # str | Id of the RecArea address

try:
    # Retrieve a specific RecArea address by id
    api_response = api_instance.get_rec_area_address(rec_area_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_address: %s\n" % e)
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

# **get_rec_area_event**
> get_rec_area_event()

Retrieve a specific event by id for a RecArea

This endpoint retrieves a specific event for a specific RecArea.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific event by id for a RecArea
    api_instance.get_rec_area_event()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_event: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_events**
> get_rec_area_events()

Retrieve all events for a RecArea

This endpoint retrieves all events for a specific RecArea.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all events for a RecArea
    api_instance.get_rec_area_events()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_facility**
> get_rec_area_facility()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific facility by id for a RecArea
    api_instance.get_rec_area_facility()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_facility: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_link**
> get_rec_area_link()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific link by id for a RecArea
    api_instance.get_rec_area_link()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_link: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_links**
> get_rec_area_links()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all links for a RecArea
    api_instance.get_rec_area_links()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_links: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_media**
> get_rec_area_media()

Retrieve a specific media by id for a RecArea

This endpoint retrieves a specific media for a specific RecArea.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific media by id for a RecArea
    api_instance.get_rec_area_media()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_media: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_rec_area_address**
> get_rec_area_rec_area_address()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve a specific RecArea address by id for a RecArea
    api_instance.get_rec_area_rec_area_address()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_rec_area_address: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rec_area_rec_area_addresses**
> get_rec_area_rec_area_addresses()

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))

try:
    # Retrieve all RecArea addresses for a RecArea
    api_instance.get_rec_area_rec_area_addresses()
except ApiException as e:
    print("Exception when calling DefaultApi->get_rec_area_rec_area_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tour**
> Tour get_tour(tour_id)

Retrieve a specific tour by id

This endpoint retrieves a specific tour.

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
api_instance = recdotgov_client.DefaultApi(recdotgov_client.ApiClient(configuration))
tour_id = 'tour_id_example' # str | Id of the tour

try:
    # Retrieve a specific tour by id
    api_response = api_instance.get_tour(tour_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tour: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tour_id** | **str**| Id of the tour | 

### Return type

[**Tour**](Tour.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

