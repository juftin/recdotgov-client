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

class Media(object):
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
        'entity_media_id': 'str',
        'media_type': 'str',
        'entity_id': 'str',
        'entity_type': 'str',
        'title': 'str',
        'subtitle': 'str',
        'description': 'str',
        'embed_code': 'str',
        'height': 'int',
        'width': 'int',
        'is_primary': 'bool',
        'is_preview': 'bool',
        'is_gallery': 'bool',
        'url': 'str',
        'credits': 'str'
    }

    attribute_map = {
        'entity_media_id': 'EntityMediaID',
        'media_type': 'MediaType',
        'entity_id': 'EntityID',
        'entity_type': 'EntityType',
        'title': 'Title',
        'subtitle': 'Subtitle',
        'description': 'Description',
        'embed_code': 'EmbedCode',
        'height': 'Height',
        'width': 'Width',
        'is_primary': 'IsPrimary',
        'is_preview': 'IsPreview',
        'is_gallery': 'IsGallery',
        'url': 'URL',
        'credits': 'Credits'
    }

    def __init__(self, entity_media_id=None, media_type=None, entity_id=None, entity_type=None, title=None, subtitle=None, description=None, embed_code=None, height=None, width=None, is_primary=None, is_preview=None, is_gallery=None, url=None, credits=None):  # noqa: E501
        """Media - a model defined in Swagger"""  # noqa: E501
        self._entity_media_id = None
        self._media_type = None
        self._entity_id = None
        self._entity_type = None
        self._title = None
        self._subtitle = None
        self._description = None
        self._embed_code = None
        self._height = None
        self._width = None
        self._is_primary = None
        self._is_preview = None
        self._is_gallery = None
        self._url = None
        self._credits = None
        self.discriminator = None
        self.entity_media_id = entity_media_id
        self.media_type = media_type
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.embed_code = embed_code
        self.height = height
        self.width = width
        if is_primary is not None:
            self.is_primary = is_primary
        if is_preview is not None:
            self.is_preview = is_preview
        if is_gallery is not None:
            self.is_gallery = is_gallery
        self.url = url
        self.credits = credits

    @property
    def entity_media_id(self):
        """Gets the entity_media_id of this Media.  # noqa: E501

        Primary Key  # noqa: E501

        :return: The entity_media_id of this Media.  # noqa: E501
        :rtype: str
        """
        return self._entity_media_id

    @entity_media_id.setter
    def entity_media_id(self, entity_media_id):
        """Sets the entity_media_id of this Media.

        Primary Key  # noqa: E501

        :param entity_media_id: The entity_media_id of this Media.  # noqa: E501
        :type: str
        """
        if entity_media_id is None:
            raise ValueError("Invalid value for `entity_media_id`, must not be `None`")  # noqa: E501

        self._entity_media_id = entity_media_id

    @property
    def media_type(self):
        """Gets the media_type of this Media.  # noqa: E501

        Type of Media, e.g. Image, Video, etc.  # noqa: E501

        :return: The media_type of this Media.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Media.

        Type of Media, e.g. Image, Video, etc.  # noqa: E501

        :param media_type: The media_type of this Media.  # noqa: E501
        :type: str
        """
        if media_type is None:
            raise ValueError("Invalid value for `media_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Image", "Video"]  # noqa: E501
        if media_type not in allowed_values:
            raise ValueError(
                "Invalid value for `media_type` ({0}), must be one of {1}"  # noqa: E501
                .format(media_type, allowed_values)
            )

        self._media_type = media_type

    @property
    def entity_id(self):
        """Gets the entity_id of this Media.  # noqa: E501

        RecArea ID OR Facility ID OR Tour ID OR Permit Entrance ID OR Campsite ID  # noqa: E501

        :return: The entity_id of this Media.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this Media.

        RecArea ID OR Facility ID OR Tour ID OR Permit Entrance ID OR Campsite ID  # noqa: E501

        :param entity_id: The entity_id of this Media.  # noqa: E501
        :type: str
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this Media.  # noqa: E501

        RecArea, Facility, Tour, Entrance, or Site  # noqa: E501

        :return: The entity_type of this Media.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Media.

        RecArea, Facility, Tour, Entrance, or Site  # noqa: E501

        :param entity_type: The entity_type of this Media.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def title(self):
        """Gets the title of this Media.  # noqa: E501

        Full title of the entity media  # noqa: E501

        :return: The title of this Media.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Media.

        Full title of the entity media  # noqa: E501

        :param title: The title of this Media.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def subtitle(self):
        """Gets the subtitle of this Media.  # noqa: E501

        Optional subtitle of the entity media  # noqa: E501

        :return: The subtitle of this Media.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this Media.

        Optional subtitle of the entity media  # noqa: E501

        :param subtitle: The subtitle of this Media.  # noqa: E501
        :type: str
        """
        if subtitle is None:
            raise ValueError("Invalid value for `subtitle`, must not be `None`")  # noqa: E501

        self._subtitle = subtitle

    @property
    def description(self):
        """Gets the description of this Media.  # noqa: E501

        Optional description of the entity media  # noqa: E501

        :return: The description of this Media.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Media.

        Optional description of the entity media  # noqa: E501

        :param description: The description of this Media.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def embed_code(self):
        """Gets the embed_code of this Media.  # noqa: E501

        Optional embedded code for media entity  # noqa: E501

        :return: The embed_code of this Media.  # noqa: E501
        :rtype: str
        """
        return self._embed_code

    @embed_code.setter
    def embed_code(self, embed_code):
        """Sets the embed_code of this Media.

        Optional embedded code for media entity  # noqa: E501

        :param embed_code: The embed_code of this Media.  # noqa: E501
        :type: str
        """
        if embed_code is None:
            raise ValueError("Invalid value for `embed_code`, must not be `None`")  # noqa: E501

        self._embed_code = embed_code

    @property
    def height(self):
        """Gets the height of this Media.  # noqa: E501

        Height in pixels for media image  # noqa: E501

        :return: The height of this Media.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Media.

        Height in pixels for media image  # noqa: E501

        :param height: The height of this Media.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def width(self):
        """Gets the width of this Media.  # noqa: E501

        Width in pixels for the media image  # noqa: E501

        :return: The width of this Media.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Media.

        Width in pixels for the media image  # noqa: E501

        :param width: The width of this Media.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def is_primary(self):
        """Gets the is_primary of this Media.  # noqa: E501

        Whether the image is a primary image  # noqa: E501

        :return: The is_primary of this Media.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """Sets the is_primary of this Media.

        Whether the image is a primary image  # noqa: E501

        :param is_primary: The is_primary of this Media.  # noqa: E501
        :type: bool
        """

        self._is_primary = is_primary

    @property
    def is_preview(self):
        """Gets the is_preview of this Media.  # noqa: E501

        Whether the image is a preview image  # noqa: E501

        :return: The is_preview of this Media.  # noqa: E501
        :rtype: bool
        """
        return self._is_preview

    @is_preview.setter
    def is_preview(self, is_preview):
        """Sets the is_preview of this Media.

        Whether the image is a preview image  # noqa: E501

        :param is_preview: The is_preview of this Media.  # noqa: E501
        :type: bool
        """

        self._is_preview = is_preview

    @property
    def is_gallery(self):
        """Gets the is_gallery of this Media.  # noqa: E501

        Whether the image is a gallery image  # noqa: E501

        :return: The is_gallery of this Media.  # noqa: E501
        :rtype: bool
        """
        return self._is_gallery

    @is_gallery.setter
    def is_gallery(self, is_gallery):
        """Sets the is_gallery of this Media.

        Whether the image is a gallery image  # noqa: E501

        :param is_gallery: The is_gallery of this Media.  # noqa: E501
        :type: bool
        """

        self._is_gallery = is_gallery

    @property
    def url(self):
        """Gets the url of this Media.  # noqa: E501

        Internet address (URL) to the entity media  # noqa: E501

        :return: The url of this Media.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Media.

        Internet address (URL) to the entity media  # noqa: E501

        :param url: The url of this Media.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def credits(self):
        """Gets the credits of this Media.  # noqa: E501

        Optional credit for entity media  # noqa: E501

        :return: The credits of this Media.  # noqa: E501
        :rtype: str
        """
        return self._credits

    @credits.setter
    def credits(self, credits):
        """Sets the credits of this Media.

        Optional credit for entity media  # noqa: E501

        :param credits: The credits of this Media.  # noqa: E501
        :type: str
        """
        if credits is None:
            raise ValueError("Invalid value for `credits`, must not be `None`")  # noqa: E501

        self._credits = credits

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
        if issubclass(Media, dict):
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
        if not isinstance(other, Media):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other