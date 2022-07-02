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


class RecreationAreaAddress(object):
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
        "rec_area_address_id": "str",
        "rec_area_id": "str",
        "rec_area_address_type": "str",
        "rec_area_street_address1": "str",
        "rec_area_street_address2": "str",
        "rec_area_street_address3": "str",
        "city": "str",
        "postal_code": "str",
        "address_state_code": "str",
        "address_country_code": "str",
    }

    attribute_map = {
        "rec_area_address_id": "RecAreaAddressID",
        "rec_area_id": "RecAreaID",
        "rec_area_address_type": "RecAreaAddressType",
        "rec_area_street_address1": "RecAreaStreetAddress1",
        "rec_area_street_address2": "RecAreaStreetAddress2",
        "rec_area_street_address3": "RecAreaStreetAddress3",
        "city": "City",
        "postal_code": "PostalCode",
        "address_state_code": "AddressStateCode",
        "address_country_code": "AddressCountryCode",
    }

    def __init__(
        self,
        rec_area_address_id=None,
        rec_area_id=None,
        rec_area_address_type=None,
        rec_area_street_address1=None,
        rec_area_street_address2=None,
        rec_area_street_address3=None,
        city=None,
        postal_code=None,
        address_state_code=None,
        address_country_code=None,
    ):  # noqa: E501
        """RecreationAreaAddress - a model defined in Swagger"""  # noqa: E501
        self._rec_area_address_id = None
        self._rec_area_id = None
        self._rec_area_address_type = None
        self._rec_area_street_address1 = None
        self._rec_area_street_address2 = None
        self._rec_area_street_address3 = None
        self._city = None
        self._postal_code = None
        self._address_state_code = None
        self._address_country_code = None
        self.discriminator = None
        self.rec_area_address_id = rec_area_address_id
        self.rec_area_id = rec_area_id
        self.rec_area_address_type = rec_area_address_type
        self.rec_area_street_address1 = rec_area_street_address1
        self.rec_area_street_address2 = rec_area_street_address2
        self.rec_area_street_address3 = rec_area_street_address3
        self.city = city
        self.postal_code = postal_code
        self.address_state_code = address_state_code
        self.address_country_code = address_country_code

    @property
    def rec_area_address_id(self):
        """Gets the rec_area_address_id of this RecreationAreaAddress.  # noqa: E501

        RecArea Address ID  # noqa: E501

        :return: The rec_area_address_id of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._rec_area_address_id

    @rec_area_address_id.setter
    def rec_area_address_id(self, rec_area_address_id):
        """Sets the rec_area_address_id of this RecreationAreaAddress.

        RecArea Address ID  # noqa: E501

        :param rec_area_address_id: The rec_area_address_id of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if rec_area_address_id is None:
            raise ValueError(
                "Invalid value for `rec_area_address_id`, must not be `None`"
            )  # noqa: E501

        self._rec_area_address_id = rec_area_address_id

    @property
    def rec_area_id(self):
        """Gets the rec_area_id of this RecreationAreaAddress.  # noqa: E501

        RecArea ID  # noqa: E501

        :return: The rec_area_id of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._rec_area_id

    @rec_area_id.setter
    def rec_area_id(self, rec_area_id):
        """Sets the rec_area_id of this RecreationAreaAddress.

        RecArea ID  # noqa: E501

        :param rec_area_id: The rec_area_id of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if rec_area_id is None:
            raise ValueError(
                "Invalid value for `rec_area_id`, must not be `None`"
            )  # noqa: E501

        self._rec_area_id = rec_area_id

    @property
    def rec_area_address_type(self):
        """Gets the rec_area_address_type of this RecreationAreaAddress.  # noqa: E501

        Address type for the RecArea  # noqa: E501

        :return: The rec_area_address_type of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._rec_area_address_type

    @rec_area_address_type.setter
    def rec_area_address_type(self, rec_area_address_type):
        """Sets the rec_area_address_type of this RecreationAreaAddress.

        Address type for the RecArea  # noqa: E501

        :param rec_area_address_type: The rec_area_address_type of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if rec_area_address_type is None:
            raise ValueError(
                "Invalid value for `rec_area_address_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["Default", "Mailing", "Physical"]  # noqa: E501
        if rec_area_address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rec_area_address_type` ({0}), must be one of {1}".format(  # noqa: E501
                    rec_area_address_type, allowed_values
                )
            )

        self._rec_area_address_type = rec_area_address_type

    @property
    def rec_area_street_address1(self):
        """Gets the rec_area_street_address1 of this RecreationAreaAddress.  # noqa: E501

        Address line 1 of the RecArea  # noqa: E501

        :return: The rec_area_street_address1 of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._rec_area_street_address1

    @rec_area_street_address1.setter
    def rec_area_street_address1(self, rec_area_street_address1):
        """Sets the rec_area_street_address1 of this RecreationAreaAddress.

        Address line 1 of the RecArea  # noqa: E501

        :param rec_area_street_address1: The rec_area_street_address1 of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if rec_area_street_address1 is None:
            raise ValueError(
                "Invalid value for `rec_area_street_address1`, must not be `None`"
            )  # noqa: E501

        self._rec_area_street_address1 = rec_area_street_address1

    @property
    def rec_area_street_address2(self):
        """Gets the rec_area_street_address2 of this RecreationAreaAddress.  # noqa: E501

        Address line 2 of the RecArea  # noqa: E501

        :return: The rec_area_street_address2 of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._rec_area_street_address2

    @rec_area_street_address2.setter
    def rec_area_street_address2(self, rec_area_street_address2):
        """Sets the rec_area_street_address2 of this RecreationAreaAddress.

        Address line 2 of the RecArea  # noqa: E501

        :param rec_area_street_address2: The rec_area_street_address2 of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if rec_area_street_address2 is None:
            raise ValueError(
                "Invalid value for `rec_area_street_address2`, must not be `None`"
            )  # noqa: E501

        self._rec_area_street_address2 = rec_area_street_address2

    @property
    def rec_area_street_address3(self):
        """Gets the rec_area_street_address3 of this RecreationAreaAddress.  # noqa: E501

        Address line 3 of the RecArea  # noqa: E501

        :return: The rec_area_street_address3 of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._rec_area_street_address3

    @rec_area_street_address3.setter
    def rec_area_street_address3(self, rec_area_street_address3):
        """Sets the rec_area_street_address3 of this RecreationAreaAddress.

        Address line 3 of the RecArea  # noqa: E501

        :param rec_area_street_address3: The rec_area_street_address3 of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if rec_area_street_address3 is None:
            raise ValueError(
                "Invalid value for `rec_area_street_address3`, must not be `None`"
            )  # noqa: E501

        self._rec_area_street_address3 = rec_area_street_address3

    @property
    def city(self):
        """Gets the city of this RecreationAreaAddress.  # noqa: E501

        City where the RecArea is located  # noqa: E501

        :return: The city of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this RecreationAreaAddress.

        City where the RecArea is located  # noqa: E501

        :param city: The city of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError(
                "Invalid value for `city`, must not be `None`"
            )  # noqa: E501

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this RecreationAreaAddress.  # noqa: E501

        Postal code for the RecArea  # noqa: E501

        :return: The postal_code of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this RecreationAreaAddress.

        Postal code for the RecArea  # noqa: E501

        :param postal_code: The postal_code of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if postal_code is None:
            raise ValueError(
                "Invalid value for `postal_code`, must not be `None`"
            )  # noqa: E501

        self._postal_code = postal_code

    @property
    def address_state_code(self):
        """Gets the address_state_code of this RecreationAreaAddress.  # noqa: E501

        State code for the RecArea  # noqa: E501

        :return: The address_state_code of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_state_code

    @address_state_code.setter
    def address_state_code(self, address_state_code):
        """Sets the address_state_code of this RecreationAreaAddress.

        State code for the RecArea  # noqa: E501

        :param address_state_code: The address_state_code of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if address_state_code is None:
            raise ValueError(
                "Invalid value for `address_state_code`, must not be `None`"
            )  # noqa: E501

        self._address_state_code = address_state_code

    @property
    def address_country_code(self):
        """Gets the address_country_code of this RecreationAreaAddress.  # noqa: E501

        Abbreviated country code for the RecArea  # noqa: E501

        :return: The address_country_code of this RecreationAreaAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_country_code

    @address_country_code.setter
    def address_country_code(self, address_country_code):
        """Sets the address_country_code of this RecreationAreaAddress.

        Abbreviated country code for the RecArea  # noqa: E501

        :param address_country_code: The address_country_code of this RecreationAreaAddress.  # noqa: E501
        :type: str
        """
        if address_country_code is None:
            raise ValueError(
                "Invalid value for `address_country_code`, must not be `None`"
            )  # noqa: E501

        self._address_country_code = address_country_code

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
        if issubclass(RecreationAreaAddress, dict):
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
        if not isinstance(other, RecreationAreaAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
