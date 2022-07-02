# Facility

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_id** | **str** | RIDB unique Facility ID | 
**legacy_facility_id** | **str** | Legacy Facility ID | 
**org_facility_id** | **str** | The agency&#x27;s internal Facility ID provided to the RIDB by the agency | 
**parent_org_id** | **str** | The parent Organization ID | [optional] 
**parent_rec_area_id** | **str** | The parent RecArea ID | [optional] 
**facility_name** | **str** | Full name of the Facility | 
**facility_description** | **str** | Text describing the main features of the Facility | 
**facility_type_description** | **str** | Description of the type of Facility | 
**facility_use_fee_description** | **str** | Text describing monetary charges associated with entrance to or usage of the Facility | 
**facility_directions** | **str** | Text that provides general directions and/or the general location of the Facility | 
**facility_phone** | **str** | Phone number of the Facility | 
**facility_email** | **str** | Email address of the Facility | 
**facility_reservation_url** | **str** | Internet address (URL) for the web site hosting the reservation system | 
**facility_map_url** | **str** | Internet address (URL) that hosts the Facility map | 
**facility_ada_access** | **str** | Information about the Americans with Disabilities Act accessibility for the Facility | 
**geojson** | [**FacilityGEOJSON**](FacilityGEOJSON.md) |  | 
**facility_longitude** | **float** | Longitude in decimal degrees -180.0 to 180.0 | 
**facility_latitude** | **float** | Latitude in decimal degrees -90.0 to 90.0 | 
**stay_limit** | **str** | Details on the stay limits for the Facility | 
**keywords** | **str** | List of keywords for the Facility | 
**reservable** | **object** | Whether the Facility is reservable | 
**enabled** | **object** | Whether the Facility is enabled | 
**campsite** | [**list[FacilityCampsite]**](FacilityCampsite.md) |  | [optional] 
**permitentrance** | [**list[FacilityPermitEntrance]**](FacilityPermitEntrance.md) |  | [optional] 
**tour** | [**list[FacilityTour]**](FacilityTour.md) |  | [optional] 
**organization** | [**list[Organization]**](Organization.md) |  | [optional] 
**recarea** | [**list[FacilityRecArea]**](FacilityRecArea.md) |  | [optional] 
**facilityaddress** | [**list[FacilityAddress]**](FacilityAddress.md) |  | [optional] 
**activity** | [**list[FacilityActivity]**](FacilityActivity.md) |  | [optional] 
**event** | [**list[Event]**](Event.md) |  | [optional] 
**link** | [**list[Link]**](Link.md) |  | [optional] 
**media** | [**list[Media]**](Media.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

