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

class FacilityTour(object):
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
        'tour_id': 'str',
        'tour_name': 'str'
    }

    attribute_map = {
        'tour_id': 'TourID',
        'tour_name': 'TourName'
    }

    def __init__(self, tour_id=None, tour_name=None):  # noqa: E501
        """FacilityTour - a model defined in Swagger"""  # noqa: E501
        self._tour_id = None
        self._tour_name = None
        self.discriminator = None
        self.tour_id = tour_id
        self.tour_name = tour_name

    @property
    def tour_id(self):
        """Gets the tour_id of this FacilityTour.  # noqa: E501

        Tour ID  # noqa: E501

        :return: The tour_id of this FacilityTour.  # noqa: E501
        :rtype: str
        """
        return self._tour_id

    @tour_id.setter
    def tour_id(self, tour_id):
        """Sets the tour_id of this FacilityTour.

        Tour ID  # noqa: E501

        :param tour_id: The tour_id of this FacilityTour.  # noqa: E501
        :type: str
        """
        if tour_id is None:
            raise ValueError("Invalid value for `tour_id`, must not be `None`")  # noqa: E501

        self._tour_id = tour_id

    @property
    def tour_name(self):
        """Gets the tour_name of this FacilityTour.  # noqa: E501

        Tour name  # noqa: E501

        :return: The tour_name of this FacilityTour.  # noqa: E501
        :rtype: str
        """
        return self._tour_name

    @tour_name.setter
    def tour_name(self, tour_name):
        """Sets the tour_name of this FacilityTour.

        Tour name  # noqa: E501

        :param tour_name: The tour_name of this FacilityTour.  # noqa: E501
        :type: str
        """
        if tour_name is None:
            raise ValueError("Invalid value for `tour_name`, must not be `None`")  # noqa: E501

        self._tour_name = tour_name

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
        if issubclass(FacilityTour, dict):
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
        if not isinstance(other, FacilityTour):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
