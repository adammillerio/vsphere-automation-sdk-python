# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.sddcs.networks.edges.statistics.dashboard.
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


class Firewall(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddcs.networks.edges.statistics.dashboard.firewall'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FirewallStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            org,
            sddc,
            edge_id,
            interval=None,
            ):
        """
        Retrieve firewall dashboard statistics for a management or compute
        gateway (NSX Edge).

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  edge_id: :class:`str`
        :param edge_id: Edge Identifier. (required)
        :type  interval: :class:`str` or ``None``
        :param interval: 60 min by default, can be given as 1 - 60 min, oneDay, oneWeek,
            oneMonth, oneYear. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.DashboardStatistics`
        :return: com.vmware.vmc.model.DashboardStatistics
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            'edge_id': edge_id,
                            'interval': interval,
                            })
class Interface(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddcs.networks.edges.statistics.dashboard.interface'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InterfaceStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            org,
            sddc,
            edge_id,
            interval=None,
            ):
        """
        Retrieve interface dashboard statistics for a management or compute
        gateway (NSX Edge).

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  edge_id: :class:`str`
        :param edge_id: Edge Identifier. (required)
        :type  interval: :class:`str` or ``None``
        :param interval: 60 min by default, can be given as 1 - 60 min, oneDay, oneWeek,
            oneMonth, oneYear. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.DashboardStatistics`
        :return: com.vmware.vmc.model.DashboardStatistics
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            'edge_id': edge_id,
                            'interval': interval,
                            })
class Ipsec(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddcs.networks.edges.statistics.dashboard.ipsec'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _IpsecStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            org,
            sddc,
            edge_id,
            interval=None,
            ):
        """
        Retrieve ipsec dashboard statistics for a management or compute gateway
        (NSX Edge).

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  edge_id: :class:`str`
        :param edge_id: Edge Identifier. (required)
        :type  interval: :class:`str` or ``None``
        :param interval: 60 min by default, can be given as 1 - 60 min, oneDay, oneWeek,
            oneMonth, oneYear. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.DashboardStatistics`
        :return: com.vmware.vmc.model.DashboardStatistics
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            'edge_id': edge_id,
                            'interval': interval,
                            })
class _FirewallStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'edge_id': type.StringType(),
            'interval': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/edges/{edgeId}/statistics/dashboard/firewall',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'edge_id': 'edgeId',
            },
            query_parameters={
                'interval': 'interval',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'DashboardStatistics'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.networks.edges.statistics.dashboard.firewall',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _InterfaceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'edge_id': type.StringType(),
            'interval': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/edges/{edgeId}/statistics/dashboard/interface',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'edge_id': 'edgeId',
            },
            query_parameters={
                'interval': 'interval',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'DashboardStatistics'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.networks.edges.statistics.dashboard.interface',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _IpsecStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'edge_id': type.StringType(),
            'interval': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/edges/{edgeId}/statistics/dashboard/ipsec',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'edge_id': 'edgeId',
            },
            query_parameters={
                'interval': 'interval',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'DashboardStatistics'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.networks.edges.statistics.dashboard.ipsec',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Firewall': Firewall,
        'Interface': Interface,
        'Ipsec': Ipsec,
    }

