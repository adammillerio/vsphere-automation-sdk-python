# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vm.compute.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.vm.compute_client`` module provides classes for
quering the status of compute policies on virtual machines in VMware Cloud on
AWS. Usage beyond VMware Cloud on AWS is not supported.

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


class Policies(VapiInterface):
    """
    The ``Policies`` class provides methods to query the status of policies on
    virtual machines in VMware Cloud on AWS. Usage beyond VMware Cloud on AWS
    is not supported. **Warning:** This class is available as Technology
    Preview. These are early access APIs provided to test, automate and provide
    feedback on the feature. Since this can change based on feedback, VMware
    does not guarantee backwards compatibility and recommends against using
    them in production environments. Some Technology Preview APIs might only be
    applicable to specific environments.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.vm.compute.policies'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PoliciesStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``Policies.Info`` class contains information about the compliance of a
        virtual machine with a compute policy. **Warning:** This class is available
        as Technology Preview. These are early access APIs provided to test,
        automate and provide feedback on the feature. Since this can change based
        on feedback, VMware does not guarantee backwards compatibility and
        recommends against using them in production environments. Some Technology
        Preview APIs might only be applicable to specific environments.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                    ):
            """
            :type  status: :class:`com.vmware.vcenter.compute.policies_client.ObjectCompliance`
            :param status: The compliance status of the policy on a specified
                object.**Warning:** This attribute is available as Technology
                Preview. These are early access APIs provided to test, automate and
                provide feedback on the feature. Since this can change based on
                feedback, VMware does not guarantee backwards compatibility and
                recommends against using them in production environments. Some
                Technology Preview APIs might only be applicable to specific
                environments.
            """
            self.status = status
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.compute.policies.info', {
            'status': type.ReferenceType('com.vmware.vcenter.compute.policies_client', 'ObjectCompliance'),
        },
        Info,
        False,
        None))



    def get(self,
            vm,
            policy,
            ):
        """
        Returns information about the compliance of a virtual machine with a
        compute policy in VMware Cloud on AWS. Usage beyond VMware Cloud on AWS
        is not supported. **Warning:** This method is available as Technology
        Preview. These are early access APIs provided to test, automate and
        provide feedback on the feature. Since this can change based on
        feedback, VMware does not guarantee backwards compatibility and
        recommends against using them in production environments. Some
        Technology Preview APIs might only be applicable to specific
        environments.

        :type  vm: :class:`str`
        :param vm: Identifier of the virtual machine to query the status for.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  policy: :class:`str`
        :param policy: Identifier of the policy to query the status for.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.compute.Resources.COMPUTE_POLICY``.
        :rtype: :class:`Policies.Info`
        :return: Information about the compliance of the specified virtual machine
            with the specified compute policy.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a virtual machine with the given identifier does not exist, or
            if a policy with the given identifier does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            'policy': policy,
                            })
class _PoliciesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'policy': type.IdType(resource_types='com.vmware.vcenter.compute.Resources.COMPUTE_POLICY'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/compute/policies/{policy}',
            path_variables={
                'vm': 'vm',
                'policy': 'policy',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Policies.Info'),
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
            self, iface_name='com.vmware.vcenter.vm.compute.policies',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Policies': Policies,
    }

