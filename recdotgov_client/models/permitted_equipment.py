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

class PermittedEquipment(object):
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
        'equipment_name': 'str',
        'max_length': 'float'
    }

    attribute_map = {
        'equipment_name': 'EquipmentName',
        'max_length': 'MaxLength'
    }

    def __init__(self, equipment_name=None, max_length=None):  # noqa: E501
        """PermittedEquipment - a model defined in Swagger"""  # noqa: E501
        self._equipment_name = None
        self._max_length = None
        self.discriminator = None
        self.equipment_name = equipment_name
        self.max_length = max_length

    @property
    def equipment_name(self):
        """Gets the equipment_name of this PermittedEquipment.  # noqa: E501

        Equipment name  # noqa: E501

        :return: The equipment_name of this PermittedEquipment.  # noqa: E501
        :rtype: str
        """
        return self._equipment_name

    @equipment_name.setter
    def equipment_name(self, equipment_name):
        """Sets the equipment_name of this PermittedEquipment.

        Equipment name  # noqa: E501

        :param equipment_name: The equipment_name of this PermittedEquipment.  # noqa: E501
        :type: str
        """
        if equipment_name is None:
            raise ValueError("Invalid value for `equipment_name`, must not be `None`")  # noqa: E501

        self._equipment_name = equipment_name

    @property
    def max_length(self):
        """Gets the max_length of this PermittedEquipment.  # noqa: E501

        Maximum length of equipment  # noqa: E501

        :return: The max_length of this PermittedEquipment.  # noqa: E501
        :rtype: float
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this PermittedEquipment.

        Maximum length of equipment  # noqa: E501

        :param max_length: The max_length of this PermittedEquipment.  # noqa: E501
        :type: float
        """
        if max_length is None:
            raise ValueError("Invalid value for `max_length`, must not be `None`")  # noqa: E501

        self._max_length = max_length

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
        if issubclass(PermittedEquipment, dict):
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
        if not isinstance(other, PermittedEquipment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
