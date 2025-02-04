# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.namespaces.user.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.namespaces.user_client`` module provides classes to
access namespaces for non-administrative users.

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


class Instances(VapiInterface):
    """
    The ``Instances`` class provides methods to access namespaces for
    non-administrative users.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespaces.user.instances'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InstancesStub)
        self._VAPI_OPERATION_IDS = {}

    class Summary(VapiStruct):
        """
        The ``Instances.Summary`` class contains information about a namespace that
        user is authorized to access.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     namespace=None,
                     master_host=None,
                    ):
            """
            :type  namespace: :class:`str`
            :param namespace: Identifier of the namespace.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.namespaces.Instance``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.namespaces.Instance``.
            :type  master_host: :class:`str`
            :param master_host: IP address or FQDN of the API endpoint for the given namespace.
            """
            self.namespace = namespace
            self.master_host = master_host
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespaces.user.instances.summary', {
            'namespace': type.IdType(resource_types='com.vmware.vcenter.namespaces.Instance'),
            'master_host': type.StringType(),
        },
        Summary,
        False,
        None))



    def list(self):
        """
        Returns namespaces that user making the call is authorized to access.


        :rtype: :class:`list` of :class:`Instances.Summary`
        :return: List of Namespace identifiers together with the API endpoint for
            each namespace.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        """
        return self._invoke('list', None)
class _InstancesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespaces-user/namespaces',
            path_variables={
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
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Instances.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.namespaces.user.instances',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Instances': Instances,
    }

