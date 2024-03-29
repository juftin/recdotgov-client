# Tour

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tour_id** | **str** | Tour ID | 
**facility_id** | **str** | Facility ID the tour belongs to | 
**tour_name** | **str** | Tour name | 
**tour_type** | **str** | Tour Type | 
**tour_description** | **str** | Tour description | 
**tour_duration** | **int** | Tour duration | 
**tour_accessible** | **bool** | Is the tour accessible by vehicle | 
**created_date** | **date** | Record creation date | 
**last_updated_date** | **date** | Record last update date | 
**attributes** | [**list[Attribute]**](Attribute.md) | Array of Attributes for the tour | 
**entitymedia** | [**list[Media]**](Media.md) | Media records for Tour | 
**membertours** | [**list[TourMEMBERTOURS]**](TourMEMBERTOURS.md) | Tour IDs of associated or multi-part Tours | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

