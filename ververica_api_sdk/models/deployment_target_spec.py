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


class DeploymentTargetSpec(object):
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
        'kubernetes': 'KubernetesTarget',
        'deployment_patch_set': 'JsonNode'
    }

    attribute_map = {
        'kubernetes': 'kubernetes',
        'deployment_patch_set': 'deploymentPatchSet'
    }

    def __init__(self, kubernetes=None, deployment_patch_set=None):  # noqa: E501
        """DeploymentTargetSpec - a model defined in Swagger"""  # noqa: E501

        self._kubernetes = None
        self._deployment_patch_set = None
        self.discriminator = None

        if kubernetes is not None:
            self.kubernetes = kubernetes
        if deployment_patch_set is not None:
            self.deployment_patch_set = deployment_patch_set

    @property
    def kubernetes(self):
        """Gets the kubernetes of this DeploymentTargetSpec.  # noqa: E501


        :return: The kubernetes of this DeploymentTargetSpec.  # noqa: E501
        :rtype: KubernetesTarget
        """
        return self._kubernetes

    @kubernetes.setter
    def kubernetes(self, kubernetes):
        """Sets the kubernetes of this DeploymentTargetSpec.


        :param kubernetes: The kubernetes of this DeploymentTargetSpec.  # noqa: E501
        :type: KubernetesTarget
        """

        self._kubernetes = kubernetes

    @property
    def deployment_patch_set(self):
        """Gets the deployment_patch_set of this DeploymentTargetSpec.  # noqa: E501


        :return: The deployment_patch_set of this DeploymentTargetSpec.  # noqa: E501
        :rtype: JsonNode
        """
        return self._deployment_patch_set

    @deployment_patch_set.setter
    def deployment_patch_set(self, deployment_patch_set):
        """Sets the deployment_patch_set of this DeploymentTargetSpec.


        :param deployment_patch_set: The deployment_patch_set of this DeploymentTargetSpec.  # noqa: E501
        :type: JsonNode
        """

        self._deployment_patch_set = deployment_patch_set

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
        if issubclass(DeploymentTargetSpec, dict):
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
        if not isinstance(other, DeploymentTargetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
