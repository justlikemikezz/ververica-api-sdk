# coding: utf-8

"""
    Application Manager API

    Application Manager APIs to control Apache Flink jobs  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: platform@ververica.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ververica_api_sdk.api_client import ApiClient


class EventResourceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_events_using_get(self, namespace, **kwargs):  # noqa: E501
        """Filter all events for a deployment or job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_using_get(namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: namespace (required)
        :param str deployment_id: deploymentId
        :param str job_id: jobId
        :return: ResourceListEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_events_using_get_with_http_info(namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.get_events_using_get_with_http_info(namespace, **kwargs)  # noqa: E501
            return data

    def get_events_using_get_with_http_info(self, namespace, **kwargs):  # noqa: E501
        """Filter all events for a deployment or job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_using_get_with_http_info(namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: namespace (required)
        :param str deployment_id: deploymentId
        :param str job_id: jobId
        :return: ResourceListEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'deployment_id', 'job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `get_events_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []
        if 'deployment_id' in params:
            query_params.append(('deploymentId', params['deployment_id']))  # noqa: E501
        if 'job_id' in params:
            query_params.append(('jobId', params['job_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/namespaces/{namespace}/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceListEvent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
