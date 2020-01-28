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


class Savepoint(object):
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
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'SavepointMetadata',
        'spec': 'SavepointSpec',
        'status': 'SavepointStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):  # noqa: E501
        """Savepoint - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        """Gets the api_version of this Savepoint.  # noqa: E501


        :return: The api_version of this Savepoint.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Savepoint.


        :param api_version: The api_version of this Savepoint.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this Savepoint.  # noqa: E501


        :return: The kind of this Savepoint.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Savepoint.


        :param kind: The kind of this Savepoint.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this Savepoint.  # noqa: E501


        :return: The metadata of this Savepoint.  # noqa: E501
        :rtype: SavepointMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Savepoint.


        :param metadata: The metadata of this Savepoint.  # noqa: E501
        :type: SavepointMetadata
        """

        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this Savepoint.  # noqa: E501


        :return: The spec of this Savepoint.  # noqa: E501
        :rtype: SavepointSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this Savepoint.


        :param spec: The spec of this Savepoint.  # noqa: E501
        :type: SavepointSpec
        """

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this Savepoint.  # noqa: E501


        :return: The status of this Savepoint.  # noqa: E501
        :rtype: SavepointStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Savepoint.


        :param status: The status of this Savepoint.  # noqa: E501
        :type: SavepointStatus
        """

        self._status = status

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
        if issubclass(Savepoint, dict):
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
        if not isinstance(other, Savepoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other