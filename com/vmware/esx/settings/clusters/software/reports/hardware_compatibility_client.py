# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.settings.clusters.software.reports.hardware_compatibility.
#---------------------------------------------------------------------------

"""
The
``com.vmware.esx.settings.clusters.software.reports.hardware_compatibility_client``
module provides classes to manage reports pertaining to the desired state
software for a cluster of ESXi hosts.

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


class Details(VapiInterface):
    """
    The ``ComplianceStatus`` class contains the possible different status of
    compliance with respect to target version.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.clusters.software.reports.hardware_compatibility.details'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DetailsStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            cluster,
            ):
        """
        Returns the hcl validation check detailed results.

        :type  cluster: :class:`str`
        :param cluster: identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`com.vmware.esx.settings.clusters.software.reports_client.CheckResult`
        :return: CheckResult hcl validation result.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some other unknown internal error. The accompanying
            error message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system or
            if desired software document is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })
class _DetailsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/esx/settings/clusters/{cluster}/software/reports/hardware-compatibility/details',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.esx.settings.clusters.software.reports_client', 'CheckResult'),
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
            self, iface_name='com.vmware.esx.settings.clusters.software.reports.hardware_compatibility.details',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Details': Details,
    }

