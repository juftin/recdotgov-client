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
from recdotgov_client.api.organizations_api import OrganizationsApi  # noqa: E501
from recdotgov_client.rest import ApiException


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self):
        self.api = OrganizationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_organization(self):
        """Test case for get_organization

        Retrieve a specific organization by id  # noqa: E501
        """
        pass

    def test_get_organizations(self):
        """Test case for get_organizations

        Retrieve all organizations  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
