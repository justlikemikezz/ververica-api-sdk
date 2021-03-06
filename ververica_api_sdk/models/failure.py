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


class Failure(object):
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
        'message': 'str',
        'reason': 'str',
        'failed_at': 'datetime'
    }

    attribute_map = {
        'message': 'message',
        'reason': 'reason',
        'failed_at': 'failedAt'
    }

    def __init__(self, message=None, reason=None, failed_at=None):  # noqa: E501
        """Failure - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._reason = None
        self._failed_at = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        if failed_at is not None:
            self.failed_at = failed_at

    @property
    def message(self):
        """Gets the message of this Failure.  # noqa: E501


        :return: The message of this Failure.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Failure.


        :param message: The message of this Failure.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this Failure.  # noqa: E501


        :return: The reason of this Failure.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Failure.


        :param reason: The reason of this Failure.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def failed_at(self):
        """Gets the failed_at of this Failure.  # noqa: E501


        :return: The failed_at of this Failure.  # noqa: E501
        :rtype: datetime
        """
        return self._failed_at

    @failed_at.setter
    def failed_at(self, failed_at):
        """Sets the failed_at of this Failure.


        :param failed_at: The failed_at of this Failure.  # noqa: E501
        :type: datetime
        """

        self._failed_at = failed_at

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
        if issubclass(Failure, dict):
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
        if not isinstance(other, Failure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
