# coding: utf-8

"""
    RIDB API

    The Recreation Information Database (RIDB) provides data resources to citizens, offering a single point of access to information about recreational opportunities nationwide. The RIDB represents an authoritative source of information and services for millions of visitors to federal lands, historic sites, museums, and other attractions/resources. This initiative integrates multiple Federal channels and sources about recreation opportunities into a one-stop, searchable database of recreational areas nationwide.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FacilityCampsite(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'campsite_id': 'str',
        'campsite_name': 'str'
    }

    attribute_map = {
        'campsite_id': 'CampsiteID',
        'campsite_name': 'CampsiteName'
    }

    def __init__(self, campsite_id=None, campsite_name=None):  # noqa: E501
        """FacilityCampsite - a model defined in Swagger"""  # noqa: E501
        self._campsite_id = None
        self._campsite_name = None
        self.discriminator = None
        self.campsite_id = campsite_id
        self.campsite_name = campsite_name

    @property
    def campsite_id(self):
        """Gets the campsite_id of this FacilityCampsite.  # noqa: E501

        Campsite ID  # noqa: E501

        :return: The campsite_id of this FacilityCampsite.  # noqa: E501
        :rtype: str
        """
        return self._campsite_id

    @campsite_id.setter
    def campsite_id(self, campsite_id):
        """Sets the campsite_id of this FacilityCampsite.

        Campsite ID  # noqa: E501

        :param campsite_id: The campsite_id of this FacilityCampsite.  # noqa: E501
        :type: str
        """
        if campsite_id is None:
            raise ValueError("Invalid value for `campsite_id`, must not be `None`")  # noqa: E501

        self._campsite_id = campsite_id

    @property
    def campsite_name(self):
        """Gets the campsite_name of this FacilityCampsite.  # noqa: E501

        Campsite Name  # noqa: E501

        :return: The campsite_name of this FacilityCampsite.  # noqa: E501
        :rtype: str
        """
        return self._campsite_name

    @campsite_name.setter
    def campsite_name(self, campsite_name):
        """Sets the campsite_name of this FacilityCampsite.

        Campsite Name  # noqa: E501

        :param campsite_name: The campsite_name of this FacilityCampsite.  # noqa: E501
        :type: str
        """
        if campsite_name is None:
            raise ValueError("Invalid value for `campsite_name`, must not be `None`")  # noqa: E501

        self._campsite_name = campsite_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FacilityCampsite, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FacilityCampsite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
