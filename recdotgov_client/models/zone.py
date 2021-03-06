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


class Zone(object):
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
    swagger_types = {"permit_entrance_zone_id": "str", "zone": "str"}

    attribute_map = {"permit_entrance_zone_id": "PermitEntranceZoneID", "zone": "Zone"}

    def __init__(self, permit_entrance_zone_id=None, zone=None):  # noqa: E501
        """Zone - a model defined in Swagger"""  # noqa: E501
        self._permit_entrance_zone_id = None
        self._zone = None
        self.discriminator = None
        self.permit_entrance_zone_id = permit_entrance_zone_id
        self.zone = zone

    @property
    def permit_entrance_zone_id(self):
        """Gets the permit_entrance_zone_id of this Zone.  # noqa: E501

        Attribute ID  # noqa: E501

        :return: The permit_entrance_zone_id of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._permit_entrance_zone_id

    @permit_entrance_zone_id.setter
    def permit_entrance_zone_id(self, permit_entrance_zone_id):
        """Sets the permit_entrance_zone_id of this Zone.

        Attribute ID  # noqa: E501

        :param permit_entrance_zone_id: The permit_entrance_zone_id of this Zone.  # noqa: E501
        :type: str
        """
        if permit_entrance_zone_id is None:
            raise ValueError(
                "Invalid value for `permit_entrance_zone_id`, must not be `None`"
            )  # noqa: E501

        self._permit_entrance_zone_id = permit_entrance_zone_id

    @property
    def zone(self):
        """Gets the zone of this Zone.  # noqa: E501

        Attribute value  # noqa: E501

        :return: The zone of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this Zone.

        Attribute value  # noqa: E501

        :param zone: The zone of this Zone.  # noqa: E501
        :type: str
        """
        if zone is None:
            raise ValueError(
                "Invalid value for `zone`, must not be `None`"
            )  # noqa: E501

        self._zone = zone

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
        if issubclass(Zone, dict):
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
        if not isinstance(other, Zone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
