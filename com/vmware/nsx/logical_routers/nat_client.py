# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.logical_routers.nat.
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


class Rules(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.logical_routers.nat.rules'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RulesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               logical_router_id,
               nat_rule,
               ):
        """
        Add a NAT rule in a specific logical router.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  nat_rule: :class:`com.vmware.nsx.model_client.NatRule`
        :param nat_rule: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NatRule`
        :return: com.vmware.nsx.model.NatRule
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
                            'logical_router_id': logical_router_id,
                            'nat_rule': nat_rule,
                            })

    def createmultiple(self,
                       logical_router_id,
                       nat_rule_list,
                       ):
        """
        Create multiple NAT rules in a specific logical router. The API
        succeeds only when all rules are accepted and created successfully. Any
        one validation voilation will fail the API, no rule will be created.
        The ruleIds of each rules can be found from the responsed message.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  nat_rule_list: :class:`com.vmware.nsx.model_client.NatRuleList`
        :param nat_rule_list: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NatRuleList`
        :return: com.vmware.nsx.model.NatRuleList
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
        return self._invoke('createmultiple',
                            {
                            'logical_router_id': logical_router_id,
                            'nat_rule_list': nat_rule_list,
                            })

    def delete(self,
               logical_router_id,
               rule_id,
               ):
        """
        Delete a specific NAT rule from a logical router

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
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
                            'logical_router_id': logical_router_id,
                            'rule_id': rule_id,
                            })

    def get(self,
            logical_router_id,
            rule_id,
            ):
        """
        Get a specific NAT rule from a given logical router

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NatRule`
        :return: com.vmware.nsx.model.NatRule
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
                            'logical_router_id': logical_router_id,
                            'rule_id': rule_id,
                            })

    def list(self,
             logical_router_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns paginated list of all user defined NAT rules of the specific
        logical router

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
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
        :rtype: :class:`com.vmware.nsx.model_client.NatRuleListResult`
        :return: com.vmware.nsx.model.NatRuleListResult
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
                            'logical_router_id': logical_router_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               logical_router_id,
               rule_id,
               nat_rule,
               ):
        """
        Update a specific NAT rule from a given logical router.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
        :type  nat_rule: :class:`com.vmware.nsx.model_client.NatRule`
        :param nat_rule: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NatRule`
        :return: com.vmware.nsx.model.NatRule
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
                            'logical_router_id': logical_router_id,
                            'rule_id': rule_id,
                            'nat_rule': nat_rule,
                            })
class _RulesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'nat_rule': type.ReferenceType('com.vmware.nsx.model_client', 'NatRule'),
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
            url_template='/api/v1/logical-routers/{logical-router-id}/nat/rules',
            request_body_parameter='nat_rule',
            path_variables={
                'logical_router_id': 'logical-router-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for createmultiple operation
        createmultiple_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'nat_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'NatRuleList'),
        })
        createmultiple_error_dict = {
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
        createmultiple_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        createmultiple_output_validator_list = [
            HasFieldsOfValidator()
        ]
        createmultiple_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/logical-routers/{logical-router-id}/nat/rules?action=create_multiple',
            request_body_parameter='nat_rule_list',
            path_variables={
                'logical_router_id': 'logical-router-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'rule_id': type.StringType(),
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
            url_template='/api/v1/logical-routers/{logical-router-id}/nat/rules/{rule-id}',
            path_variables={
                'logical_router_id': 'logical-router-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'rule_id': type.StringType(),
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
            url_template='/api/v1/logical-routers/{logical-router-id}/nat/rules/{rule-id}',
            path_variables={
                'logical_router_id': 'logical-router-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-routers/{logical-router-id}/nat/rules',
            path_variables={
                'logical_router_id': 'logical-router-id',
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
            'logical_router_id': type.StringType(),
            'rule_id': type.StringType(),
            'nat_rule': type.ReferenceType('com.vmware.nsx.model_client', 'NatRule'),
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
            url_template='/api/v1/logical-routers/{logical-router-id}/nat/rules/{rule-id}',
            request_body_parameter='nat_rule',
            path_variables={
                'logical_router_id': 'logical-router-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NatRule'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'createmultiple': {
                'input_type': createmultiple_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NatRuleList'),
                'errors': createmultiple_error_dict,
                'input_value_validator_list': createmultiple_input_value_validator_list,
                'output_validator_list': createmultiple_output_validator_list,
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NatRule'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NatRuleListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NatRule'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'createmultiple': createmultiple_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.logical_routers.nat.rules',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Rules': Rules,
        'rules': 'com.vmware.nsx.logical_routers.nat.rules_client.StubFactory',
    }

