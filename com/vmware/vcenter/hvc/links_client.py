# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.hvc.links.
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


class Sync(VapiInterface):
    """
    The ``Sync`` class provides methods to create a sync session, get
    information on Sync. Usage beyond VMware Cloud on AWS is not supported.
    **Warning:** This class is available as Technology Preview. These are early
    access APIs provided to test, automate and provide feedback on the feature.
    Since this can change based on feedback, VMware does not guarantee
    backwards compatibility and recommends against using them in production
    environments. Some Technology Preview APIs might only be applicable to
    specific environments.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.hvc.links.sync'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SyncStub)
        self._VAPI_OPERATION_IDS = {}

    class Credentials(VapiStruct):
        """
        The ``Sync.Credentials`` class specifies user credentials to make a
        successful connection to remote endpoint. **Warning:** This class is
        available as Technology Preview. These are early access APIs provided to
        test, automate and provide feedback on the feature. Since this can change
        based on feedback, VMware does not guarantee backwards compatibility and
        recommends against using them in production environments. Some Technology
        Preview APIs might only be applicable to specific environments.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     user_name=None,
                     password=None,
                    ):
            """
            :type  user_name: :class:`str`
            :param user_name: Name of the user to authenticate. **Warning:** This attribute is
                available as Technology Preview. These are early access APIs
                provided to test, automate and provide feedback on the feature.
                Since this can change based on feedback, VMware does not guarantee
                backwards compatibility and recommends against using them in
                production environments. Some Technology Preview APIs might only be
                applicable to specific environments.
            :type  password: :class:`str`
            :param password: Password for the user. **Warning:** This attribute is available as
                Technology Preview. These are early access APIs provided to test,
                automate and provide feedback on the feature. Since this can change
                based on feedback, VMware does not guarantee backwards
                compatibility and recommends against using them in production
                environments. Some Technology Preview APIs might only be applicable
                to specific environments.
            """
            self.user_name = user_name
            self.password = password
            VapiStruct.__init__(self)


    Credentials._set_binding_type(type.StructType(
        'com.vmware.vcenter.hvc.links.sync.credentials', {
            'user_name': type.StringType(),
            'password': type.SecretType(),
        },
        Credentials,
        False,
        None))



    def reset(self,
              link,
              ):
        """
        Resets the sync state between the linked domains by initiating a fresh
        sync for all providers. If an existing sync is in progress this cancels
        the sync. Usage beyond VMware Cloud on AWS is not supported.
        **Warning:** This method is available as Technology Preview. These are
        early access APIs provided to test, automate and provide feedback on
        the feature. Since this can change based on feedback, VMware does not
        guarantee backwards compatibility and recommends against using them in
        production environments. Some Technology Preview APIs might only be
        applicable to specific environments.

        :type  link: :class:`str`
        :param link: Unique identifier of the link.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.hvc.Links``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the link Identifier associated with ``link`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user is not authorized to perform this operation.
        """
        return self._invoke('reset',
                            {
                            'link': link,
                            })
class _SyncStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for reset operation
        reset_input_type = type.StructType('operation-input', {
            'link': type.IdType(resource_types='com.vmware.vcenter.hvc.Links'),
        })
        reset_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        reset_input_value_validator_list = [
        ]
        reset_output_validator_list = [
        ]
        reset_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/hvc/links/{link_id}/sync?action=reset',
            path_variables={
                'link': 'link_id',
            },
            query_parameters={
            }
        )

        operations = {
            'reset': {
                'input_type': reset_input_type,
                'output_type': type.VoidType(),
                'errors': reset_error_dict,
                'input_value_validator_list': reset_input_value_validator_list,
                'output_validator_list': reset_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'reset': reset_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.hvc.links.sync',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Sync': Sync,
        'sync': 'com.vmware.vcenter.hvc.links.sync_client.StubFactory',
    }

