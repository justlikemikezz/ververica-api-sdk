# coding: utf-8

"""
    Application Manager API

    Application Manager APIs to control Apache Flink jobs  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: platform@ververica.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EnvVar(object):
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
        'name': 'str',
        'value': 'str',
        'value_from': 'JsonNode'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'value_from': 'valueFrom'
    }

    def __init__(self, name=None, value=None, value_from=None):  # noqa: E501
        """EnvVar - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._value = None
        self._value_from = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if value_from is not None:
            self.value_from = value_from

    @property
    def name(self):
        """Gets the name of this EnvVar.  # noqa: E501


        :return: The name of this EnvVar.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvVar.


        :param name: The name of this EnvVar.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this EnvVar.  # noqa: E501


        :return: The value of this EnvVar.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EnvVar.


        :param value: The value of this EnvVar.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_from(self):
        """Gets the value_from of this EnvVar.  # noqa: E501


        :return: The value_from of this EnvVar.  # noqa: E501
        :rtype: JsonNode
        """
        return self._value_from

    @value_from.setter
    def value_from(self, value_from):
        """Sets the value_from of this EnvVar.


        :param value_from: The value_from of this EnvVar.  # noqa: E501
        :type: JsonNode
        """

        self._value_from = value_from

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
        if issubclass(EnvVar, dict):
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
        if not isinstance(other, EnvVar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
