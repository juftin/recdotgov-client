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


class RecreationAreaGEOJSON(object):
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
    swagger_types = {"type": "str", "coordinates": "list[float]"}

    attribute_map = {"type": "TYPE", "coordinates": "COORDINATES"}

    def __init__(self, type=None, coordinates=None):  # noqa: E501
        """RecreationAreaGEOJSON - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._coordinates = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if coordinates is not None:
            self.coordinates = coordinates

    @property
    def type(self):
        """Gets the type of this RecreationAreaGEOJSON.  # noqa: E501


        :return: The type of this RecreationAreaGEOJSON.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecreationAreaGEOJSON.


        :param type: The type of this RecreationAreaGEOJSON.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def coordinates(self):
        """Gets the coordinates of this RecreationAreaGEOJSON.  # noqa: E501


        :return: The coordinates of this RecreationAreaGEOJSON.  # noqa: E501
        :rtype: list[float]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this RecreationAreaGEOJSON.


        :param coordinates: The coordinates of this RecreationAreaGEOJSON.  # noqa: E501
        :type: list[float]
        """

        self._coordinates = coordinates

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(RecreationAreaGEOJSON, dict):
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
        if not isinstance(other, RecreationAreaGEOJSON):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
