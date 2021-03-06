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


class ResourceQuotaSpec(object):
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
        'limits': 'ResourceQuotaQuantity',
        'tolerated_overuse': 'ResourceQuotaQuantity',
        'type': 'str'
    }

    attribute_map = {
        'limits': 'limits',
        'tolerated_overuse': 'toleratedOveruse',
        'type': 'type'
    }

    def __init__(self, limits=None, tolerated_overuse=None, type=None):  # noqa: E501
        """ResourceQuotaSpec - a model defined in Swagger"""  # noqa: E501

        self._limits = None
        self._tolerated_overuse = None
        self._type = None
        self.discriminator = None

        if limits is not None:
            self.limits = limits
        if tolerated_overuse is not None:
            self.tolerated_overuse = tolerated_overuse
        if type is not None:
            self.type = type

    @property
    def limits(self):
        """Gets the limits of this ResourceQuotaSpec.  # noqa: E501


        :return: The limits of this ResourceQuotaSpec.  # noqa: E501
        :rtype: ResourceQuotaQuantity
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this ResourceQuotaSpec.


        :param limits: The limits of this ResourceQuotaSpec.  # noqa: E501
        :type: ResourceQuotaQuantity
        """

        self._limits = limits

    @property
    def tolerated_overuse(self):
        """Gets the tolerated_overuse of this ResourceQuotaSpec.  # noqa: E501


        :return: The tolerated_overuse of this ResourceQuotaSpec.  # noqa: E501
        :rtype: ResourceQuotaQuantity
        """
        return self._tolerated_overuse

    @tolerated_overuse.setter
    def tolerated_overuse(self, tolerated_overuse):
        """Sets the tolerated_overuse of this ResourceQuotaSpec.


        :param tolerated_overuse: The tolerated_overuse of this ResourceQuotaSpec.  # noqa: E501
        :type: ResourceQuotaQuantity
        """

        self._tolerated_overuse = tolerated_overuse

    @property
    def type(self):
        """Gets the type of this ResourceQuotaSpec.  # noqa: E501


        :return: The type of this ResourceQuotaSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceQuotaSpec.


        :param type: The type of this ResourceQuotaSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["LIMITED", "UNLIMITED"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ResourceQuotaSpec, dict):
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
        if not isinstance(other, ResourceQuotaSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
