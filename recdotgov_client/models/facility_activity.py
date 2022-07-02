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


class FacilityActivity(object):
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
        "activity_id": "str",
        "facility_id": "str",
        "activity_name": "str",
        "facility_activity_description": "str",
        "facility_activity_fee_description": "str",
    }

    attribute_map = {
        "activity_id": "ActivityID",
        "facility_id": "FacilityID",
        "activity_name": "ActivityName",
        "facility_activity_description": "FacilityActivityDescription",
        "facility_activity_fee_description": "FacilityActivityFeeDescription",
    }

    def __init__(
        self,
        activity_id=None,
        facility_id=None,
        activity_name=None,
        facility_activity_description=None,
        facility_activity_fee_description=None,
    ):  # noqa: E501
        """FacilityActivity - a model defined in Swagger"""  # noqa: E501
        self._activity_id = None
        self._facility_id = None
        self._activity_name = None
        self._facility_activity_description = None
        self._facility_activity_fee_description = None
        self.discriminator = None
        self.activity_id = activity_id
        self.facility_id = facility_id
        self.activity_name = activity_name
        self.facility_activity_description = facility_activity_description
        self.facility_activity_fee_description = facility_activity_fee_description

    @property
    def activity_id(self):
        """Gets the activity_id of this FacilityActivity.  # noqa: E501

        Activity ID  # noqa: E501

        :return: The activity_id of this FacilityActivity.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this FacilityActivity.

        Activity ID  # noqa: E501

        :param activity_id: The activity_id of this FacilityActivity.  # noqa: E501
        :type: str
        """
        if activity_id is None:
            raise ValueError(
                "Invalid value for `activity_id`, must not be `None`"
            )  # noqa: E501

        self._activity_id = activity_id

    @property
    def facility_id(self):
        """Gets the facility_id of this FacilityActivity.  # noqa: E501

        Parent Facility ID of the Actitvity  # noqa: E501

        :return: The facility_id of this FacilityActivity.  # noqa: E501
        :rtype: str
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        """Sets the facility_id of this FacilityActivity.

        Parent Facility ID of the Actitvity  # noqa: E501

        :param facility_id: The facility_id of this FacilityActivity.  # noqa: E501
        :type: str
        """
        if facility_id is None:
            raise ValueError(
                "Invalid value for `facility_id`, must not be `None`"
            )  # noqa: E501

        self._facility_id = facility_id

    @property
    def activity_name(self):
        """Gets the activity_name of this FacilityActivity.  # noqa: E501

        Name of the Activity  # noqa: E501

        :return: The activity_name of this FacilityActivity.  # noqa: E501
        :rtype: str
        """
        return self._activity_name

    @activity_name.setter
    def activity_name(self, activity_name):
        """Sets the activity_name of this FacilityActivity.

        Name of the Activity  # noqa: E501

        :param activity_name: The activity_name of this FacilityActivity.  # noqa: E501
        :type: str
        """
        if activity_name is None:
            raise ValueError(
                "Invalid value for `activity_name`, must not be `None`"
            )  # noqa: E501

        self._activity_name = activity_name

    @property
    def facility_activity_description(self):
        """Gets the facility_activity_description of this FacilityActivity.  # noqa: E501

        Description of the Activity  # noqa: E501

        :return: The facility_activity_description of this FacilityActivity.  # noqa: E501
        :rtype: str
        """
        return self._facility_activity_description

    @facility_activity_description.setter
    def facility_activity_description(self, facility_activity_description):
        """Sets the facility_activity_description of this FacilityActivity.

        Description of the Activity  # noqa: E501

        :param facility_activity_description: The facility_activity_description of this FacilityActivity.  # noqa: E501
        :type: str
        """
        if facility_activity_description is None:
            raise ValueError(
                "Invalid value for `facility_activity_description`, must not be `None`"
            )  # noqa: E501

        self._facility_activity_description = facility_activity_description

    @property
    def facility_activity_fee_description(self):
        """Gets the facility_activity_fee_description of this FacilityActivity.  # noqa: E501

        Text describing monetary charges associated with the Activity  # noqa: E501

        :return: The facility_activity_fee_description of this FacilityActivity.  # noqa: E501
        :rtype: str
        """
        return self._facility_activity_fee_description

    @facility_activity_fee_description.setter
    def facility_activity_fee_description(self, facility_activity_fee_description):
        """Sets the facility_activity_fee_description of this FacilityActivity.

        Text describing monetary charges associated with the Activity  # noqa: E501

        :param facility_activity_fee_description: The facility_activity_fee_description of this FacilityActivity.  # noqa: E501
        :type: str
        """
        if facility_activity_fee_description is None:
            raise ValueError(
                "Invalid value for `facility_activity_fee_description`, must not be `None`"
            )  # noqa: E501

        self._facility_activity_fee_description = facility_activity_fee_description

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
        if issubclass(FacilityActivity, dict):
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
        if not isinstance(other, FacilityActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
