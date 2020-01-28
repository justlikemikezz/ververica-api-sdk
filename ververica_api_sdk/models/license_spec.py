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


class LicenseSpec(object):
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
        'expires': 'datetime',
        'license_id': 'str',
        'licensed_to': 'str',
        'params': 'dict(str, str)'
    }

    attribute_map = {
        'expires': 'expires',
        'license_id': 'licenseId',
        'licensed_to': 'licensedTo',
        'params': 'params'
    }

    def __init__(self, expires=None, license_id=None, licensed_to=None, params=None):  # noqa: E501
        """LicenseSpec - a model defined in Swagger"""  # noqa: E501

        self._expires = None
        self._license_id = None
        self._licensed_to = None
        self._params = None
        self.discriminator = None

        if expires is not None:
            self.expires = expires
        if license_id is not None:
            self.license_id = license_id
        if licensed_to is not None:
            self.licensed_to = licensed_to
        if params is not None:
            self.params = params

    @property
    def expires(self):
        """Gets the expires of this LicenseSpec.  # noqa: E501


        :return: The expires of this LicenseSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this LicenseSpec.


        :param expires: The expires of this LicenseSpec.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

    @property
    def license_id(self):
        """Gets the license_id of this LicenseSpec.  # noqa: E501


        :return: The license_id of this LicenseSpec.  # noqa: E501
        :rtype: str
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """Sets the license_id of this LicenseSpec.


        :param license_id: The license_id of this LicenseSpec.  # noqa: E501
        :type: str
        """

        self._license_id = license_id

    @property
    def licensed_to(self):
        """Gets the licensed_to of this LicenseSpec.  # noqa: E501


        :return: The licensed_to of this LicenseSpec.  # noqa: E501
        :rtype: str
        """
        return self._licensed_to

    @licensed_to.setter
    def licensed_to(self, licensed_to):
        """Sets the licensed_to of this LicenseSpec.


        :param licensed_to: The licensed_to of this LicenseSpec.  # noqa: E501
        :type: str
        """

        self._licensed_to = licensed_to

    @property
    def params(self):
        """Gets the params of this LicenseSpec.  # noqa: E501


        :return: The params of this LicenseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this LicenseSpec.


        :param params: The params of this LicenseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._params = params

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
        if issubclass(LicenseSpec, dict):
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
        if not isinstance(other, LicenseSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
