# coding: utf-8

"""
    Application Manager API

    Application Manager APIs to control Apache Flink jobs  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: platform@ververica.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ververica_api_sdk
from ververica_api_sdk.api.deployment_target_resource_api import DeploymentTargetResourceApi  # noqa: E501
from ververica_api_sdk.rest import ApiException


class TestDeploymentTargetResourceApi(unittest.TestCase):
    """DeploymentTargetResourceApi unit test stubs"""

    def setUp(self):
        self.api = ververica_api_sdk.api.deployment_target_resource_api.DeploymentTargetResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_deployment_target_using_post(self):
        """Test case for create_deployment_target_using_post

        Create a deployment target  # noqa: E501
        """
        pass

    def test_delete_deployment_target_using_delete(self):
        """Test case for delete_deployment_target_using_delete

        Delete a deployment target  # noqa: E501
        """
        pass

    def test_get_deployment_target_using_get(self):
        """Test case for get_deployment_target_using_get

        Get a deployment target by name  # noqa: E501
        """
        pass

    def test_get_deployment_targets_using_get(self):
        """Test case for get_deployment_targets_using_get

        List all deployment targets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
