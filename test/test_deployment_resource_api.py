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
from ververica_api_sdk.api.deployment_resource_api import DeploymentResourceApi  # noqa: E501
from ververica_api_sdk.rest import ApiException


class TestDeploymentResourceApi(unittest.TestCase):
    """DeploymentResourceApi unit test stubs"""

    def setUp(self):
        self.api = ververica_api_sdk.api.deployment_resource_api.DeploymentResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_deployment_using_post(self):
        """Test case for create_deployment_using_post

        Create a deployment  # noqa: E501
        """
        pass

    def test_delete_deployment_using_delete(self):
        """Test case for delete_deployment_using_delete

        Delete deployment  # noqa: E501
        """
        pass

    def test_get_deployment_using_get(self):
        """Test case for get_deployment_using_get

        Get a deployment by id  # noqa: E501
        """
        pass

    def test_get_deployments_using_get(self):
        """Test case for get_deployments_using_get

        List all deployments  # noqa: E501
        """
        pass

    def test_update_deployment_using_patch(self):
        """Test case for update_deployment_using_patch

        Update a deployment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()