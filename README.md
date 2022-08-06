# recdotgov-client
The Recreation Information Database (RIDB) provides data resources to citizens, offering a single point of access to information about recreational opportunities nationwide. The RIDB represents an authoritative source of information and services for millions of visitors to federal lands, historic sites, museums, and other attractions/resources. This initiative integrates multiple Federal channels and sources about recreation opportunities into a one-stop, searchable database of recreational areas nationwide.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 0.1.12
- Build date: 2022-08-06T04:23:39.701Z[GMT]
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import recdotgov_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import recdotgov_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

try:
    # Retrieve all activities
    api_response = api_instance.get_activities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activities: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://ridb.recreation.gov/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivitiesApi* | [**get_activities**](docs/ActivitiesApi.md#get_activities) | **GET** /activities | Retrieve all activities
*AttributesApi* | [**get_campsite_attributes**](docs/AttributesApi.md#get_campsite_attributes) | **GET** /campsites/{campsiteId}/attributes | Retrieve all attributes for a campsite
*AttributesApi* | [**get_tour_attributes**](docs/AttributesApi.md#get_tour_attributes) | **GET** /tours/{tourId}/attributes | Retrieve all attributes for a tour
*CampsitesApi* | [**get_campsites**](docs/CampsitesApi.md#get_campsites) | **GET** /campsites | Retrieve all campsites
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **GET** /events | Retrieve all events
*FacilitiesApi* | [**get_facilities**](docs/FacilitiesApi.md#get_facilities) | **GET** /facilities | Retrieve all facilities
*FacilitiesApi* | [**get_organization_facilities**](docs/FacilitiesApi.md#get_organization_facilities) | **GET** /organizations/{orgId}/facilities | Retrieve all facilities for an organization
*FacilitiesApi* | [**get_rec_area_facilities**](docs/FacilitiesApi.md#get_rec_area_facilities) | **GET** /recareas/{recAreaId}/facilities | Retrieve all facilities for a RecArea
*FacilityAddressesApi* | [**get_facility_addresses**](docs/FacilityAddressesApi.md#get_facility_addresses) | **GET** /facilityaddresses | Retrieve all facility addresses
*LinksApi* | [**get_links**](docs/LinksApi.md#get_links) | **GET** /links | Retrieve all links
*MediaApi* | [**get_all_media**](docs/MediaApi.md#get_all_media) | **GET** /media | Retrieve all media
*OrganizationsApi* | [**get_organizations**](docs/OrganizationsApi.md#get_organizations) | **GET** /organizations | Retrieve all organizations
*PermitEntrancesApi* | [**get_permit_entrances**](docs/PermitEntrancesApi.md#get_permit_entrances) | **GET** /permitentrances | Retrieve all permit entrances
*RecreationAreaAddressesApi* | [**get_rec_area_addresses**](docs/RecreationAreaAddressesApi.md#get_rec_area_addresses) | **GET** /recareaaddresses | Retrieve all RecArea addresses
*RecreationAreasApi* | [**get_rec_areas**](docs/RecreationAreasApi.md#get_rec_areas) | **GET** /recareas | Retrieve all RecAreas
*ToursApi* | [**get_tours**](docs/ToursApi.md#get_tours) | **GET** /tours | Retrieve all tours
*ZonesApi* | [**get_permit_entrance_zone**](docs/ZonesApi.md#get_permit_entrance_zone) | **GET** /permitentrances/{permitEntranceId}/zones/{zoneId} | Retrieve a zone for a permit entrance
*ZonesApi* | [**get_permit_entrance_zones**](docs/ZonesApi.md#get_permit_entrance_zones) | **GET** /permitentrances/{permitEntranceId}/zones | Retrieve all zones for a permit entrance
*DefaultApi* | [**get_activity**](docs/DefaultApi.md#get_activity) | **GET** /activities/{activityId} | Retrieve a specific activity by id
*DefaultApi* | [**get_all_facility_media**](docs/DefaultApi.md#get_all_facility_media) | **GET** /facilities/{facilityId}/media | Retrieve all media for a facility
*DefaultApi* | [**get_all_rec_area_media**](docs/DefaultApi.md#get_all_rec_area_media) | **GET** /recareas/{recAreaId}/media | Retrieve all media for a RecArea
*DefaultApi* | [**get_campsite**](docs/DefaultApi.md#get_campsite) | **GET** /campsites/{campsiteId} | Retrieve a specific campsite by id
*DefaultApi* | [**get_event**](docs/DefaultApi.md#get_event) | **GET** /events/{eventId} | Retrieve a specific event by id
*DefaultApi* | [**get_facility**](docs/DefaultApi.md#get_facility) | **GET** /facilities/{facilityId} | Retrieve a specific facility by id
*DefaultApi* | [**get_facility_activities**](docs/DefaultApi.md#get_facility_activities) | **GET** /facilities/{facilityId}/activities | Retrieve all activities for a facility
*DefaultApi* | [**get_facility_activity**](docs/DefaultApi.md#get_facility_activity) | **GET** /facilities/{facilityId}/activities/{activityId} | Retrieve a specific activity by id for a facility
*DefaultApi* | [**get_facility_address**](docs/DefaultApi.md#get_facility_address) | **GET** /facilityaddresses/{facilityAddressId} | Retrieve a specific facility address by id
*DefaultApi* | [**get_facility_campsite**](docs/DefaultApi.md#get_facility_campsite) | **GET** /facilities/{facilityId}/campsites/{campsiteId} | Retrieve a specific campsite by id for a facility
*DefaultApi* | [**get_facility_campsites**](docs/DefaultApi.md#get_facility_campsites) | **GET** /facilities/{facilityId}/campsites | Retrieve all campsites for a facility
*DefaultApi* | [**get_facility_event**](docs/DefaultApi.md#get_facility_event) | **GET** /facilities/{facilityId}/events/{eventId} | Retrieve a specific event by id for a facility
*DefaultApi* | [**get_facility_events**](docs/DefaultApi.md#get_facility_events) | **GET** /facilities/{facilityId}/events | Retrieve all events for a facility
*DefaultApi* | [**get_facility_facility_address**](docs/DefaultApi.md#get_facility_facility_address) | **GET** /facilities/{facilityId}/facilityaddresses/{facilityAddressId} | Retrieve a specific facility address by id for a facility
*DefaultApi* | [**get_facility_facility_addresses**](docs/DefaultApi.md#get_facility_facility_addresses) | **GET** /facilities/{facilityId}/facilityaddresses | Retrieve all facility addresses for a facility
*DefaultApi* | [**get_facility_link**](docs/DefaultApi.md#get_facility_link) | **GET** /facilities/{facilityId}/links/{linkId} | Retrieve a specific link by id for a facility
*DefaultApi* | [**get_facility_links**](docs/DefaultApi.md#get_facility_links) | **GET** /facilities/{facilityId}/links | Retrieve all links for a facility
*DefaultApi* | [**get_facility_media**](docs/DefaultApi.md#get_facility_media) | **GET** /facilities/{facilityId}/media/{mediaId} | Retrieve a specific media by id for a facility
*DefaultApi* | [**get_facility_permit_entrance**](docs/DefaultApi.md#get_facility_permit_entrance) | **GET** /facilities/{facilityId}/permitentrances/{permitEntranceId} | Retrieve a specific permit entrance by id for a facility
*DefaultApi* | [**get_facility_permit_entrances**](docs/DefaultApi.md#get_facility_permit_entrances) | **GET** /facilities/{facilityId}/permitentrances | Retrieve all permit entrances for a facility
*DefaultApi* | [**get_facility_tour**](docs/DefaultApi.md#get_facility_tour) | **GET** /facilities/{facilityId}/tours/{tourId} | Retrieve a specific tour by id for a facility
*DefaultApi* | [**get_facility_tours**](docs/DefaultApi.md#get_facility_tours) | **GET** /facilities/{facilityId}/tours | Retrieve all tours for a facility
*DefaultApi* | [**get_link**](docs/DefaultApi.md#get_link) | **GET** /links/{linkId} | Retrieve a specific link by id
*DefaultApi* | [**get_media**](docs/DefaultApi.md#get_media) | **GET** /media/{mediaId} | Retrieve a specific media by id
*DefaultApi* | [**get_organization**](docs/DefaultApi.md#get_organization) | **GET** /organizations/{orgId} | Retrieve a specific organization by id
*DefaultApi* | [**get_organization_facility**](docs/DefaultApi.md#get_organization_facility) | **GET** /organizations/{orgId}/facilities/{facilityId} | Retrieve a specific facility by id for an organization
*DefaultApi* | [**get_organization_rec_area**](docs/DefaultApi.md#get_organization_rec_area) | **GET** /organizations/{orgId}/recareas/{recAreaId} | Retrieve a specific RecArea by id for an organization
*DefaultApi* | [**get_organization_rec_areas**](docs/DefaultApi.md#get_organization_rec_areas) | **GET** /organizations/{orgId}/recareas | Retrieve all RecAreas for an organization
*DefaultApi* | [**get_permit_entrance**](docs/DefaultApi.md#get_permit_entrance) | **GET** /permitentrances/{permitentranceId} | Retrieve a specific permit entrance by id
*DefaultApi* | [**get_permit_entrance_attributes**](docs/DefaultApi.md#get_permit_entrance_attributes) | **GET** /permitentrances/{permitEntranceId}/attributes | Retrieve all attributes for a permit entrance
*DefaultApi* | [**get_rec_area**](docs/DefaultApi.md#get_rec_area) | **GET** /recareas/{recAreaId} | Retrieve a specific RecArea by id
*DefaultApi* | [**get_rec_area_activities**](docs/DefaultApi.md#get_rec_area_activities) | **GET** /recareas/{recAreaId}/activities | Retrieve all activities for a RecArea
*DefaultApi* | [**get_rec_area_activity**](docs/DefaultApi.md#get_rec_area_activity) | **GET** /recareas/{recAreaId}/activities/{activityId} | Retrieve a specific activity by id for a RecArea
*DefaultApi* | [**get_rec_area_address**](docs/DefaultApi.md#get_rec_area_address) | **GET** /recareaaddresses/{recAreaAddressId} | Retrieve a specific RecArea address by id
*DefaultApi* | [**get_rec_area_event**](docs/DefaultApi.md#get_rec_area_event) | **GET** /recareas/{recAreaId}/events/{eventId} | Retrieve a specific event by id for a RecArea
*DefaultApi* | [**get_rec_area_events**](docs/DefaultApi.md#get_rec_area_events) | **GET** /recareas/{recAreaId}/events | Retrieve all events for a RecArea
*DefaultApi* | [**get_rec_area_facility**](docs/DefaultApi.md#get_rec_area_facility) | **GET** /recareas/{recAreaId}/facilities/{facilityId} | Retrieve a specific facility by id for a RecArea
*DefaultApi* | [**get_rec_area_link**](docs/DefaultApi.md#get_rec_area_link) | **GET** /recareas/{recAreaId}/links/{linkId} | Retrieve a specific link by id for a RecArea
*DefaultApi* | [**get_rec_area_links**](docs/DefaultApi.md#get_rec_area_links) | **GET** /recareas/{recAreaId}/links | Retrieve all links for a RecArea
*DefaultApi* | [**get_rec_area_media**](docs/DefaultApi.md#get_rec_area_media) | **GET** /recareas/{recAreaId}/media/{mediaId} | Retrieve a specific media by id for a RecArea
*DefaultApi* | [**get_rec_area_rec_area_address**](docs/DefaultApi.md#get_rec_area_rec_area_address) | **GET** /recareas/{recAreaId}/recareaaddresses/{recAreaAddressId} | Retrieve a specific RecArea address by id for a RecArea
*DefaultApi* | [**get_rec_area_rec_area_addresses**](docs/DefaultApi.md#get_rec_area_rec_area_addresses) | **GET** /recareas/{recAreaId}/recareaaddresses | Retrieve all RecArea addresses for a RecArea
*DefaultApi* | [**get_tour**](docs/DefaultApi.md#get_tour) | **GET** /tours/{tourId} | Retrieve a specific tour by id

## Documentation For Models

 - [Activity](docs/Activity.md)
 - [Attribute](docs/Attribute.md)
 - [Campsite](docs/Campsite.md)
 - [Event](docs/Event.md)
 - [Facility](docs/Facility.md)
 - [FacilityActivity](docs/FacilityActivity.md)
 - [FacilityAddress](docs/FacilityAddress.md)
 - [FacilityCampsite](docs/FacilityCampsite.md)
 - [FacilityGEOJSON](docs/FacilityGEOJSON.md)
 - [FacilityPermitEntrance](docs/FacilityPermitEntrance.md)
 - [FacilityRecArea](docs/FacilityRecArea.md)
 - [FacilityTour](docs/FacilityTour.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse200METADATA](docs/InlineResponse200METADATA.md)
 - [InlineResponse200METADATAPARAMETERS](docs/InlineResponse200METADATAPARAMETERS.md)
 - [InlineResponse200METADATARESULTS](docs/InlineResponse200METADATARESULTS.md)
 - [Link](docs/Link.md)
 - [Media](docs/Media.md)
 - [Organization](docs/Organization.md)
 - [PermitEntrance](docs/PermitEntrance.md)
 - [PermittedEquipment](docs/PermittedEquipment.md)
 - [RecreationArea](docs/RecreationArea.md)
 - [RecreationAreaActivity](docs/RecreationAreaActivity.md)
 - [RecreationAreaAddress](docs/RecreationAreaAddress.md)
 - [RecreationAreaFacility](docs/RecreationAreaFacility.md)
 - [RecreationAreaGEOJSON](docs/RecreationAreaGEOJSON.md)
 - [Tour](docs/Tour.md)
 - [TourMEMBERTOURS](docs/TourMEMBERTOURS.md)
 - [Zone](docs/Zone.md)

## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: HTTP header


## Author


