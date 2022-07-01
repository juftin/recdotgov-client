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

class Event(object):
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
        'event_id': 'str',
        'event_name': 'str',
        'resource_link': 'str'
    }

    attribute_map = {
        'event_id': 'EventID',
        'event_name': 'EventName',
        'resource_link': 'ResourceLink'
    }

    def __init__(self, event_id=None, event_name=None, resource_link=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        self._event_id = None
        self._event_name = None
        self._resource_link = None
        self.discriminator = None
        self.event_id = event_id
        self.event_name = event_name
        self.resource_link = resource_link

    @property
    def event_id(self):
        """Gets the event_id of this Event.  # noqa: E501

        Event ID  # noqa: E501

        :return: The event_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Event.

        Event ID  # noqa: E501

        :param event_id: The event_id of this Event.  # noqa: E501
        :type: str
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def event_name(self):
        """Gets the event_name of this Event.  # noqa: E501

        Full name of the Event  # noqa: E501

        :return: The event_name of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this Event.

        Full name of the Event  # noqa: E501

        :param event_name: The event_name of this Event.  # noqa: E501
        :type: str
        """
        if event_name is None:
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def resource_link(self):
        """Gets the resource_link of this Event.  # noqa: E501

        Internet address (URL) to a web site providing details  # noqa: E501

        :return: The resource_link of this Event.  # noqa: E501
        :rtype: str
        """
        return self._resource_link

    @resource_link.setter
    def resource_link(self, resource_link):
        """Sets the resource_link of this Event.

        Internet address (URL) to a web site providing details  # noqa: E501

        :param resource_link: The resource_link of this Event.  # noqa: E501
        :type: str
        """
        if resource_link is None:
            raise ValueError("Invalid value for `resource_link`, must not be `None`")  # noqa: E501

        self._resource_link = resource_link

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
