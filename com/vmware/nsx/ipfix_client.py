# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.ipfix.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class Collectorconfigs(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ipfix.collectorconfigs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CollectorconfigsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               ipfix_collector_config,
               ):
        """
        Create a new IPFIX collector configuration

        :type  ipfix_collector_config: :class:`com.vmware.nsx.model_client.IpfixCollectorConfig`
        :param ipfix_collector_config: (required)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixCollectorConfig`
        :return: com.vmware.nsx.model.IpfixCollectorConfig
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('create',
                            {
                            'ipfix_collector_config': ipfix_collector_config,
                            })

    def delete(self,
               collector_config_id,
               ):
        """
        Delete an existing IPFIX collector configuration

        :type  collector_config_id: :class:`str`
        :param collector_config_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('delete',
                            {
                            'collector_config_id': collector_config_id,
                            })

    def get(self,
            collector_config_id,
            ):
        """
        Get an existing IPFIX collector configuration

        :type  collector_config_id: :class:`str`
        :param collector_config_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixCollectorConfig`
        :return: com.vmware.nsx.model.IpfixCollectorConfig
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'collector_config_id': collector_config_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List IPFIX collector configurations

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixCollectorConfigListResult`
        :return: com.vmware.nsx.model.IpfixCollectorConfigListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               collector_config_id,
               ipfix_collector_config,
               ):
        """
        Update an existing IPFIX collector configuration

        :type  collector_config_id: :class:`str`
        :param collector_config_id: (required)
        :type  ipfix_collector_config: :class:`com.vmware.nsx.model_client.IpfixCollectorConfig`
        :param ipfix_collector_config: (required)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixCollectorConfig`
        :return: com.vmware.nsx.model.IpfixCollectorConfig
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('update',
                            {
                            'collector_config_id': collector_config_id,
                            'ipfix_collector_config': ipfix_collector_config,
                            })
class Configs(VapiInterface):
    """
    
    """
    LIST_IPFIX_CONFIG_TYPE_IPFIXSWITCHCONFIG = "IpfixSwitchConfig"
    """
    Possible value for ``ipfixConfigType`` of method :func:`Configs.list`.

    """
    LIST_IPFIX_CONFIG_TYPE_IPFIXDFWCONFIG = "IpfixDfwConfig"
    """
    Possible value for ``ipfixConfigType`` of method :func:`Configs.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ipfix.configs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ConfigsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               ipfix_config,
               ):
        """
        Create a new IPFIX configuration

        :type  ipfix_config: :class:`vmware.vapi.struct.VapiStruct`
        :param ipfix_config: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixConfig`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.IpfixConfig
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixConfig`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('create',
                            {
                            'ipfix_config': ipfix_config,
                            })

    def delete(self,
               config_id,
               ):
        """
        Delete an existing IPFIX configuration

        :type  config_id: :class:`str`
        :param config_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('delete',
                            {
                            'config_id': config_id,
                            })

    def get(self,
            config_id,
            ):
        """
        Get an existing IPFIX configuration

        :type  config_id: :class:`str`
        :param config_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.IpfixConfig
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixConfig`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'config_id': config_id,
                            })

    def list(self,
             applied_to=None,
             cursor=None,
             included_fields=None,
             ipfix_config_type=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List IPFIX configuration

        :type  applied_to: :class:`str` or ``None``
        :param applied_to: Applied To (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  ipfix_config_type: :class:`str` or ``None``
        :param ipfix_config_type: Supported IPFIX Config Types. (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixConfigListResult`
        :return: com.vmware.nsx.model.IpfixConfigListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'applied_to': applied_to,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'ipfix_config_type': ipfix_config_type,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               config_id,
               ipfix_config,
               ):
        """
        Update an existing IPFIX configuration

        :type  config_id: :class:`str`
        :param config_id: (required)
        :type  ipfix_config: :class:`vmware.vapi.struct.VapiStruct`
        :param ipfix_config: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixConfig`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.IpfixConfig
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixConfig`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('update',
                            {
                            'config_id': config_id,
                            'ipfix_config': ipfix_config,
                            })
class _CollectorconfigsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ipfix_collector_config': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorConfig'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/ipfix/collectorconfigs',
            request_body_parameter='ipfix_collector_config',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'collector_config_id': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/ipfix/collectorconfigs/{collector-config-id}',
            path_variables={
                'collector_config_id': 'collector-config-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'collector_config_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/ipfix/collectorconfigs/{collector-config-id}',
            path_variables={
                'collector_config_id': 'collector-config-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/ipfix/collectorconfigs',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'collector_config_id': type.StringType(),
            'ipfix_collector_config': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorConfig'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/ipfix/collectorconfigs/{collector-config-id}',
            request_body_parameter='ipfix_collector_config',
            path_variables={
                'collector_config_id': 'collector-config-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorConfig'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorConfig'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorConfigListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorConfig'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.ipfix.collectorconfigs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ConfigsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ipfix_config': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixConfig')]),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/ipfix/configs',
            request_body_parameter='ipfix_config',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'config_id': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/ipfix/configs/{config-id}',
            path_variables={
                'config_id': 'config-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'config_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/ipfix/configs/{config-id}',
            path_variables={
                'config_id': 'config-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'applied_to': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'ipfix_config_type': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/ipfix/configs',
            path_variables={
            },
            query_parameters={
                'applied_to': 'applied_to',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'ipfix_config_type': 'ipfix_config_type',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'config_id': type.StringType(),
            'ipfix_config': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixConfig')]),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        update_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/ipfix/configs/{config-id}',
            request_body_parameter='ipfix_config',
            path_variables={
                'config_id': 'config-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixConfig')]),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixConfig')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixConfigListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixConfig')]),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.ipfix.configs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Collectorconfigs': Collectorconfigs,
        'Configs': Configs,
    }

