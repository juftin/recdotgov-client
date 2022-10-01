# RecreationArea

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rec_area_id** | **str** | RIDB unique RecArea ID | 
**org_rec_area_id** | **str** | The agency&#x27;s internal RecArea ID provided to the RIDB by the agency | 
**parent_org_id** | **str** | Parent Organization ID | [optional] 
**rec_area_name** | **str** | Full name of the RecArea | 
**rec_area_description** | **str** | Text that describes the RecArea | 
**rec_area_fee_description** | **str** | Text describing monetary charges associated with entrance to or usage of a RecArea | 
**rec_area_directions** | **str** | Directions to the RecArea | 
**rec_area_phone** | **str** | Phone number for RecArea | 
**rec_area_email** | **str** | Email address of the RecArea | 
**rec_area_reservation_url** | **str** | Internet address (URL) for the web site hosting the reservation system | 
**rec_area_map_url** | **str** | Internet address (URL) that hosts the RecArea map | 
**geojson** | [**RecreationAreaGEOJSON**](RecreationAreaGEOJSON.md) |  | 
**rec_area_longitude** | **float** | Longitude in decimal degrees -180.0 to 180.0 | 
**rec_area_latitude** | **float** | Latitude in decimal degrees -90.0 to 90.0 | 
**stay_limit** | **str** | Details on the stay limits for the RecArea | 
**keywords** | **str** | List of keywords for the RecArea | 
**reservable** | **bool** | Whether the RecArea is reservable | 
**enabled** | **bool** | Whether the RecArea is enabled | 
**last_updated_date** | **date** | Record last update date | 
**organization** | [**list[Organization]**](Organization.md) |  | [optional] 
**facility** | [**list[RecreationAreaFacility]**](RecreationAreaFacility.md) |  | [optional] 
**recareaaddress** | [**list[RecreationAreaAddress]**](RecreationAreaAddress.md) |  | [optional] 
**activity** | [**list[RecreationAreaActivity]**](RecreationAreaActivity.md) |  | [optional] 
**event** | [**list[Event]**](Event.md) |  | [optional] 
**media** | [**list[Media]**](Media.md) |  | [optional] 
**link** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

