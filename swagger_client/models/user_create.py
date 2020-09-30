# coding: utf-8

"""
    Stytch

    This is the Stytch api.  You can find out more about Stytch at  [stytch.io](https://stytch.io).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@stytch.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserCreate(object):
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
        'email': 'str',
        'name': 'UserCreateName',
        'attributes': 'Attributes'
    }

    attribute_map = {
        'email': 'email',
        'name': 'name',
        'attributes': 'attributes'
    }

    def __init__(self, email=None, name=None, attributes=None):  # noqa: E501
        """UserCreate - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._name = None
        self._attributes = None
        self.discriminator = None
        self.email = email
        if name is not None:
            self.name = name
        if attributes is not None:
            self.attributes = attributes

    @property
    def email(self):
        """Gets the email of this UserCreate.  # noqa: E501

        The email to use for email magic links. This can be changed later via the update endpoint.  # noqa: E501

        :return: The email of this UserCreate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserCreate.

        The email to use for email magic links. This can be changed later via the update endpoint.  # noqa: E501

        :param email: The email of this UserCreate.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this UserCreate.  # noqa: E501


        :return: The name of this UserCreate.  # noqa: E501
        :rtype: UserCreateName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserCreate.


        :param name: The name of this UserCreate.  # noqa: E501
        :type: UserCreateName
        """

        self._name = name

    @property
    def attributes(self):
        """Gets the attributes of this UserCreate.  # noqa: E501


        :return: The attributes of this UserCreate.  # noqa: E501
        :rtype: Attributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this UserCreate.


        :param attributes: The attributes of this UserCreate.  # noqa: E501
        :type: Attributes
        """

        self._attributes = attributes

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
        if issubclass(UserCreate, dict):
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
        if not isinstance(other, UserCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other