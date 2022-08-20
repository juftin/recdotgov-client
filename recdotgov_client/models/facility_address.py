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


class FacilityAddress(object):
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
        "facility_address_id": "str",
        "facility_id": "str",
        "facility_address_type": "str",
        "facility_street_address1": "str",
        "facility_street_address2": "str",
        "facility_street_address3": "str",
        "city": "str",
        "postal_code": "str",
        "address_state_code": "str",
        "address_country_code": "str",
        "last_updated_date": "date",
    }

    attribute_map = {
        "facility_address_id": "FacilityAddressID",
        "facility_id": "FacilityID",
        "facility_address_type": "FacilityAddressType",
        "facility_street_address1": "FacilityStreetAddress1",
        "facility_street_address2": "FacilityStreetAddress2",
        "facility_street_address3": "FacilityStreetAddress3",
        "city": "City",
        "postal_code": "PostalCode",
        "address_state_code": "AddressStateCode",
        "address_country_code": "AddressCountryCode",
        "last_updated_date": "LastUpdatedDate",
    }

    def __init__(
        self,
        facility_address_id=None,
        facility_id=None,
        facility_address_type=None,
        facility_street_address1=None,
        facility_street_address2=None,
        facility_street_address3=None,
        city=None,
        postal_code=None,
        address_state_code=None,
        address_country_code=None,
        last_updated_date=None,
    ):  # noqa: E501
        """FacilityAddress - a model defined in Swagger"""  # noqa: E501
        self._facility_address_id = None
        self._facility_id = None
        self._facility_address_type = None
        self._facility_street_address1 = None
        self._facility_street_address2 = None
        self._facility_street_address3 = None
        self._city = None
        self._postal_code = None
        self._address_state_code = None
        self._address_country_code = None
        self._last_updated_date = None
        self.discriminator = None
        self.facility_address_id = facility_address_id
        self.facility_id = facility_id
        self.facility_address_type = facility_address_type
        self.facility_street_address1 = facility_street_address1
        self.facility_street_address2 = facility_street_address2
        self.facility_street_address3 = facility_street_address3
        self.city = city
        self.postal_code = postal_code
        self.address_state_code = address_state_code
        self.address_country_code = address_country_code
        self.last_updated_date = last_updated_date

    @property
    def facility_address_id(self):
        """Gets the facility_address_id of this FacilityAddress.  # noqa: E501

        Facility Address ID  # noqa: E501

        :return: The facility_address_id of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._facility_address_id

    @facility_address_id.setter
    def facility_address_id(self, facility_address_id):
        """Sets the facility_address_id of this FacilityAddress.

        Facility Address ID  # noqa: E501

        :param facility_address_id: The facility_address_id of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if facility_address_id is None:
            raise ValueError(
                "Invalid value for `facility_address_id`, must not be `None`"
            )  # noqa: E501

        self._facility_address_id = facility_address_id

    @property
    def facility_id(self):
        """Gets the facility_id of this FacilityAddress.  # noqa: E501

        Facility ID  # noqa: E501

        :return: The facility_id of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        """Sets the facility_id of this FacilityAddress.

        Facility ID  # noqa: E501

        :param facility_id: The facility_id of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if facility_id is None:
            raise ValueError(
                "Invalid value for `facility_id`, must not be `None`"
            )  # noqa: E501

        self._facility_id = facility_id

    @property
    def facility_address_type(self):
        """Gets the facility_address_type of this FacilityAddress.  # noqa: E501

        Address type for the Facility  # noqa: E501

        :return: The facility_address_type of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._facility_address_type

    @facility_address_type.setter
    def facility_address_type(self, facility_address_type):
        """Sets the facility_address_type of this FacilityAddress.

        Address type for the Facility  # noqa: E501

        :param facility_address_type: The facility_address_type of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if facility_address_type is None:
            raise ValueError(
                "Invalid value for `facility_address_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["Default", "Mailing", "Physical"]  # noqa: E501
        if facility_address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `facility_address_type` ({0}), must be one of {1}".format(  # noqa: E501
                    facility_address_type, allowed_values
                )
            )

        self._facility_address_type = facility_address_type

    @property
    def facility_street_address1(self):
        """Gets the facility_street_address1 of this FacilityAddress.  # noqa: E501

        Address line 1 of the Facility  # noqa: E501

        :return: The facility_street_address1 of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._facility_street_address1

    @facility_street_address1.setter
    def facility_street_address1(self, facility_street_address1):
        """Sets the facility_street_address1 of this FacilityAddress.

        Address line 1 of the Facility  # noqa: E501

        :param facility_street_address1: The facility_street_address1 of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if facility_street_address1 is None:
            raise ValueError(
                "Invalid value for `facility_street_address1`, must not be `None`"
            )  # noqa: E501

        self._facility_street_address1 = facility_street_address1

    @property
    def facility_street_address2(self):
        """Gets the facility_street_address2 of this FacilityAddress.  # noqa: E501

        Address line 2 of the Facility  # noqa: E501

        :return: The facility_street_address2 of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._facility_street_address2

    @facility_street_address2.setter
    def facility_street_address2(self, facility_street_address2):
        """Sets the facility_street_address2 of this FacilityAddress.

        Address line 2 of the Facility  # noqa: E501

        :param facility_street_address2: The facility_street_address2 of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if facility_street_address2 is None:
            raise ValueError(
                "Invalid value for `facility_street_address2`, must not be `None`"
            )  # noqa: E501

        self._facility_street_address2 = facility_street_address2

    @property
    def facility_street_address3(self):
        """Gets the facility_street_address3 of this FacilityAddress.  # noqa: E501

        Address line 3 of the Facility  # noqa: E501

        :return: The facility_street_address3 of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._facility_street_address3

    @facility_street_address3.setter
    def facility_street_address3(self, facility_street_address3):
        """Sets the facility_street_address3 of this FacilityAddress.

        Address line 3 of the Facility  # noqa: E501

        :param facility_street_address3: The facility_street_address3 of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if facility_street_address3 is None:
            raise ValueError(
                "Invalid value for `facility_street_address3`, must not be `None`"
            )  # noqa: E501

        self._facility_street_address3 = facility_street_address3

    @property
    def city(self):
        """Gets the city of this FacilityAddress.  # noqa: E501

        City where the Facility is located  # noqa: E501

        :return: The city of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this FacilityAddress.

        City where the Facility is located  # noqa: E501

        :param city: The city of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError(
                "Invalid value for `city`, must not be `None`"
            )  # noqa: E501

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this FacilityAddress.  # noqa: E501

        Postal code for the Facility  # noqa: E501

        :return: The postal_code of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this FacilityAddress.

        Postal code for the Facility  # noqa: E501

        :param postal_code: The postal_code of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if postal_code is None:
            raise ValueError(
                "Invalid value for `postal_code`, must not be `None`"
            )  # noqa: E501

        self._postal_code = postal_code

    @property
    def address_state_code(self):
        """Gets the address_state_code of this FacilityAddress.  # noqa: E501

        State code for the Facility  # noqa: E501

        :return: The address_state_code of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_state_code

    @address_state_code.setter
    def address_state_code(self, address_state_code):
        """Sets the address_state_code of this FacilityAddress.

        State code for the Facility  # noqa: E501

        :param address_state_code: The address_state_code of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if address_state_code is None:
            raise ValueError(
                "Invalid value for `address_state_code`, must not be `None`"
            )  # noqa: E501

        self._address_state_code = address_state_code

    @property
    def address_country_code(self):
        """Gets the address_country_code of this FacilityAddress.  # noqa: E501

        Abbreviated country code for the Facility Address  # noqa: E501

        :return: The address_country_code of this FacilityAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_country_code

    @address_country_code.setter
    def address_country_code(self, address_country_code):
        """Sets the address_country_code of this FacilityAddress.

        Abbreviated country code for the Facility Address  # noqa: E501

        :param address_country_code: The address_country_code of this FacilityAddress.  # noqa: E501
        :type: str
        """
        if address_country_code is None:
            raise ValueError(
                "Invalid value for `address_country_code`, must not be `None`"
            )  # noqa: E501

        self._address_country_code = address_country_code

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this FacilityAddress.  # noqa: E501

        Record last update date  # noqa: E501

        :return: The last_updated_date of this FacilityAddress.  # noqa: E501
        :rtype: date
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this FacilityAddress.

        Record last update date  # noqa: E501

        :param last_updated_date: The last_updated_date of this FacilityAddress.  # noqa: E501
        :type: date
        """
        if last_updated_date is None:
            raise ValueError(
                "Invalid value for `last_updated_date`, must not be `None`"
            )  # noqa: E501

        self._last_updated_date = last_updated_date

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
        if issubclass(FacilityAddress, dict):
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
        if not isinstance(other, FacilityAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
