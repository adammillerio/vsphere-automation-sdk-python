# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.hosts.software.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.hosts.software_client`` module provides classes to get
information about current software on ESX.

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


class InstalledComponents(VapiInterface):
    """
    The ``InstalledComponents`` class provides methods to get installed list of
    components.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.hosts.software.installed_components'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InstalledComponentsStub)
        self._VAPI_OPERATION_IDS = {}

    class InstalledComponentInfo(VapiStruct):
        """
        The ``InstalledComponents.InstalledComponentInfo`` class contains
        attributes that describe the installed component on the host.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     display_name=None,
                     version=None,
                     display_version=None,
                    ):
            """
            :type  display_name: :class:`str`
            :param display_name: Display name of the component.
            :type  version: :class:`str`
            :param version: Version of the installed component
            :type  display_version: :class:`str`
            :param display_version: Human readable version of the component.
            """
            self.display_name = display_name
            self.version = version
            self.display_version = display_version
            VapiStruct.__init__(self)


    InstalledComponentInfo._set_binding_type(type.StructType(
        'com.vmware.esx.hosts.software.installed_components.installed_component_info', {
            'display_name': type.StringType(),
            'version': type.StringType(),
            'display_version': type.StringType(),
        },
        InstalledComponentInfo,
        False,
        None))



    def list(self,
             host,
             ):
        """
        Returns the installed components on the host.

        :type  host: :class:`str`
        :param host: Identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``HostSystem``.
        :rtype: :class:`dict` of :class:`str` and :class:`InstalledComponents.InstalledComponentInfo`
        :return: The components installed on the host.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``com.vmware.esx.hosts.component``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no host associated with ``host`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSoftwareSpecification.Read``.
            * The resource ``HostSystem`` referenced by the parameter ``host``
              requires ``VcIntegrity.lifecycleSoftwareSpecification.Read``.
        """
        return self._invoke('list',
                            {
                            'host': host,
                            })
class _InstalledComponentsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'host': type.IdType(resource_types='HostSystem'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/esx/hosts/{host}/software/installed-components',
            path_variables={
                'host': 'host',
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
                'output_type': type.MapType(type.IdType(), type.ReferenceType(__name__, 'InstalledComponents.InstalledComponentInfo')),
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
            self, iface_name='com.vmware.esx.hosts.software.installed_components',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'InstalledComponents': InstalledComponents,
    }

