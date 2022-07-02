# coding: utf-8

"""
    RIDB API

    The Recreation Information Database (RIDB) provides data resources to citizens, offering a single point of access to information about recreational opportunities nationwide. The RIDB represents an authoritative source of information and services for millions of visitors to federal lands, historic sites, museums, and other attractions/resources. This initiative integrates multiple Federal channels and sources about recreation opportunities into a one-stop, searchable database of recreational areas nationwide.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import recdotgov_client
from recdotgov_client.api.facilities_api import FacilitiesApi  # noqa: E501
from recdotgov_client.rest import ApiException


class TestFacilitiesApi(unittest.TestCase):
    """FacilitiesApi unit test stubs"""

    def setUp(self):
        self.api = FacilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_facilities(self):
        """Test case for get_facilities

        Retrieve all facilities  # noqa: E501
        """
        pass

    def test_get_organization_facilities(self):
        """Test case for get_organization_facilities

        Retrieve all facilities for an organization  # noqa: E501
        """
        pass

    def test_get_rec_area_facilities(self):
        """Test case for get_rec_area_facilities

        Retrieve all facilities for a RecArea  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
