# coding: utf-8

"""
    RIDB API

    The Recreation Information Database (RIDB) provides data resources to citizens, offering a single point of access to information about recreational opportunities nationwide. The RIDB represents an authoritative source of information and services for millions of visitors to federal lands, historic sites, museums, and other attractions/resources. This initiative integrates multiple Federal channels and sources about recreation opportunities into a one-stop, searchable database of recreational areas nationwide.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from recdotgov_client.api_client import ApiClient


class ToursApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_facility_tour(self, facility_id, tour_id, **kwargs):  # noqa: E501
        """Retrieve a specific tour by id for a facility  # noqa: E501

        This endpoint retrieves a specific tour for a specific facility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_tour(facility_id, tour_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: Id of the facility (required)
        :param str tour_id: Id of the tour (required)
        :return: Tour
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_facility_tour_with_http_info(
                facility_id, tour_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_facility_tour_with_http_info(
                facility_id, tour_id, **kwargs
            )  # noqa: E501
            return data

    def get_facility_tour_with_http_info(
        self, facility_id, tour_id, **kwargs
    ):  # noqa: E501
        """Retrieve a specific tour by id for a facility  # noqa: E501

        This endpoint retrieves a specific tour for a specific facility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_tour_with_http_info(facility_id, tour_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: Id of the facility (required)
        :param str tour_id: Id of the tour (required)
        :return: Tour
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["facility_id", "tour_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facility_tour" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'facility_id' is set
        if "facility_id" not in params or params["facility_id"] is None:
            raise ValueError(
                "Missing the required parameter `facility_id` when calling `get_facility_tour`"
            )  # noqa: E501
        # verify the required parameter 'tour_id' is set
        if "tour_id" not in params or params["tour_id"] is None:
            raise ValueError(
                "Missing the required parameter `tour_id` when calling `get_facility_tour`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "facility_id" in params:
            path_params["facilityId"] = params["facility_id"]  # noqa: E501
        if "tour_id" in params:
            path_params["tourId"] = params["tour_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Apikey"]  # noqa: E501

        return self.api_client.call_api(
            "/facilities/{facilityId}/tours/{tourId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Tour",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_facility_tours(self, facility_id, **kwargs):  # noqa: E501
        """Retrieve all tours for a facility  # noqa: E501

        This endpoint retrieves all tours for a specific facility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_tours(facility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: Id of the facility (required)
        :param str query: Query filter criteria. Searches on tour name, type, description, and accessible (Yes/No)
        :param int limit: Number of records to return (max 50)
        :param int offset: Start record of overall result set
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_facility_tours_with_http_info(
                facility_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_facility_tours_with_http_info(
                facility_id, **kwargs
            )  # noqa: E501
            return data

    def get_facility_tours_with_http_info(self, facility_id, **kwargs):  # noqa: E501
        """Retrieve all tours for a facility  # noqa: E501

        This endpoint retrieves all tours for a specific facility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_tours_with_http_info(facility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: Id of the facility (required)
        :param str query: Query filter criteria. Searches on tour name, type, description, and accessible (Yes/No)
        :param int limit: Number of records to return (max 50)
        :param int offset: Start record of overall result set
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["facility_id", "query", "limit", "offset"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facility_tours" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'facility_id' is set
        if "facility_id" not in params or params["facility_id"] is None:
            raise ValueError(
                "Missing the required parameter `facility_id` when calling `get_facility_tours`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "facility_id" in params:
            path_params["facilityId"] = params["facility_id"]  # noqa: E501

        query_params = []
        if "query" in params:
            query_params.append(("query", params["query"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Apikey"]  # noqa: E501

        return self.api_client.call_api(
            "/facilities/{facilityId}/tours",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2007",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_tour(self, tour_id, **kwargs):  # noqa: E501
        """Retrieve a specific tour by id  # noqa: E501

        This endpoint retrieves a specific tour.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tour(tour_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tour_id: Id of the tour (required)
        :return: Tour
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_tour_with_http_info(tour_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tour_with_http_info(tour_id, **kwargs)  # noqa: E501
            return data

    def get_tour_with_http_info(self, tour_id, **kwargs):  # noqa: E501
        """Retrieve a specific tour by id  # noqa: E501

        This endpoint retrieves a specific tour.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tour_with_http_info(tour_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tour_id: Id of the tour (required)
        :return: Tour
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["tour_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tour" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'tour_id' is set
        if "tour_id" not in params or params["tour_id"] is None:
            raise ValueError(
                "Missing the required parameter `tour_id` when calling `get_tour`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "tour_id" in params:
            path_params["tourId"] = params["tour_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Apikey"]  # noqa: E501

        return self.api_client.call_api(
            "/tours/{tourId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Tour",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_tours(self, **kwargs):  # noqa: E501
        """Retrieve all tours  # noqa: E501

        This endpoint retrieves all tours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tours(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Query filter criteria. Searches on tour name, type, description, and accessible (Yes/No)
        :param int limit: Number of records to return (max 50)
        :param int offset: Start record of overall result set
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_tours_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_tours_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_tours_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all tours  # noqa: E501

        This endpoint retrieves all tours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tours_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Query filter criteria. Searches on tour name, type, description, and accessible (Yes/No)
        :param int limit: Number of records to return (max 50)
        :param int offset: Start record of overall result set
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["query", "limit", "offset"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tours" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "query" in params:
            query_params.append(("query", params["query"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Apikey"]  # noqa: E501

        return self.api_client.call_api(
            "/tours",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2007",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
