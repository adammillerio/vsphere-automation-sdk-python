# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.settings.hosts.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.settings.hosts_client`` module provides classes to manage
desired state configuration and software for a standalone ESX host.

"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from com.vmware.cis_client import Tasks
from vmware.vapi.stdlib.client.task import Task
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


class Software(VapiInterface):
    """
    The ``Software`` class provides methods to manage desired software
    specification of a standalone ESX host.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.hosts.software'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SoftwareStub)
        self._VAPI_OPERATION_IDS = {}
        self._VAPI_OPERATION_IDS.update({'scan_task': 'scan$task'})



    def scan_task(self,
             host,
             ):
        """
        Scans the host against the host's desired state.. The result of this
        operation can be queried by calling the cis/tasks/{task-id} where the
        task-id is the response of this operation.

        :type  host: :class:`str`
        :param host: Identifier of the host.
            The parameter must be an identifier for the resource type:
            ``HostSystem``.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is unknown internal error. The accompanying error message
            will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no host associated with ``host`` in the system or if
            desired software document is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            If the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            If the host is not a standlone host, but instead part of a cluster.
        """
        task_id = self._invoke('scan$task',
                                {
                                'host': host,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.ReferenceType('com.vmware.esx.settings_client', 'HostCompliance'))
        return task_instance
class _SoftwareStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for scan operation
        scan_input_type = type.StructType('operation-input', {
            'host': type.IdType(resource_types='HostSystem'),
        })
        scan_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        scan_input_value_validator_list = [
        ]
        scan_output_validator_list = [
        ]
        scan_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/hosts/{host}/software',
            path_variables={
                'host': 'host',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'scan',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        operations = {
            'scan$task': {
                'input_type': scan_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': scan_error_dict,
                'input_value_validator_list': scan_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'scan': scan_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.hosts.software',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Software': Software,
    }

