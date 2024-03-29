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


class InlineResponse20011(object):
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
    swagger_types = {"recdata": "list[Event]", "metadata": "InlineResponse200METADATA"}

    attribute_map = {"recdata": "RECDATA", "metadata": "METADATA"}

    def __init__(self, recdata=None, metadata=None):  # noqa: E501
        """InlineResponse20011 - a model defined in Swagger"""  # noqa: E501
        self._recdata = None
        self._metadata = None
        self.discriminator = None
        if recdata is not None:
            self.recdata = recdata
        if metadata is not None:
            self.metadata = metadata

    @property
    def recdata(self):
        """Gets the recdata of this InlineResponse20011.  # noqa: E501


        :return: The recdata of this InlineResponse20011.  # noqa: E501
        :rtype: list[Event]
        """
        return self._recdata

    @recdata.setter
    def recdata(self, recdata):
        """Sets the recdata of this InlineResponse20011.


        :param recdata: The recdata of this InlineResponse20011.  # noqa: E501
        :type: list[Event]
        """

        self._recdata = recdata

    @property
    def metadata(self):
        """Gets the metadata of this InlineResponse20011.  # noqa: E501


        :return: The metadata of this InlineResponse20011.  # noqa: E501
        :rtype: InlineResponse200METADATA
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InlineResponse20011.


        :param metadata: The metadata of this InlineResponse20011.  # noqa: E501
        :type: InlineResponse200METADATA
        """

        self._metadata = metadata

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
        if issubclass(InlineResponse20011, dict):
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
        if not isinstance(other, InlineResponse20011):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
