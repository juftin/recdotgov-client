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

class Attribute(object):
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
        'attribute_id': 'int',
        'attribute_name': 'str',
        'attribute_value': 'str'
    }

    attribute_map = {
        'attribute_id': 'AttributeID',
        'attribute_name': 'AttributeName',
        'attribute_value': 'AttributeValue'
    }

    def __init__(self, attribute_id=None, attribute_name=None, attribute_value=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501
        self._attribute_id = None
        self._attribute_name = None
        self._attribute_value = None
        self.discriminator = None
        if attribute_id is not None:
            self.attribute_id = attribute_id
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value

    @property
    def attribute_id(self):
        """Gets the attribute_id of this Attribute.  # noqa: E501

        Attribute ID  # noqa: E501

        :return: The attribute_id of this Attribute.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this Attribute.

        Attribute ID  # noqa: E501

        :param attribute_id: The attribute_id of this Attribute.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def attribute_name(self):
        """Gets the attribute_name of this Attribute.  # noqa: E501

        Attribute name  # noqa: E501

        :return: The attribute_name of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this Attribute.

        Attribute name  # noqa: E501

        :param attribute_name: The attribute_name of this Attribute.  # noqa: E501
        :type: str
        """
        if attribute_name is None:
            raise ValueError("Invalid value for `attribute_name`, must not be `None`")  # noqa: E501

        self._attribute_name = attribute_name

    @property
    def attribute_value(self):
        """Gets the attribute_value of this Attribute.  # noqa: E501

        Attribute value  # noqa: E501

        :return: The attribute_value of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """Sets the attribute_value of this Attribute.

        Attribute value  # noqa: E501

        :param attribute_value: The attribute_value of this Attribute.  # noqa: E501
        :type: str
        """
        if attribute_value is None:
            raise ValueError("Invalid value for `attribute_value`, must not be `None`")  # noqa: E501

        self._attribute_value = attribute_value

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
        if issubclass(Attribute, dict):
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
