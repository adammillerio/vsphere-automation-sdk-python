# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.cluster.
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


class Backups(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.cluster.backups'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BackupsStub)
        self._VAPI_OPERATION_IDS = {}


    def retrievesshfingerprint(self,
                               remote_server_fingerprint_request,
                               ):
        """
        Get SHA256 fingerprint of ECDSA key of remote server. The caller should
        independently verify that the key is trusted.

        :type  remote_server_fingerprint_request: :class:`com.vmware.nsx_policy.model_client.RemoteServerFingerprintRequest`
        :param remote_server_fingerprint_request: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.RemoteServerFingerprint`
        :return: com.vmware.nsx_policy.model.RemoteServerFingerprint
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
        return self._invoke('retrievesshfingerprint',
                            {
                            'remote_server_fingerprint_request': remote_server_fingerprint_request,
                            })
class Restore(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.cluster.restore'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RestoreStub)
        self._VAPI_OPERATION_IDS = {}


    def advance(self,
                advance_cluster_restore_request,
                ):
        """
        Advance any currently suspended restore operation. The operation might
        have been suspended because (1) the user had suspended it previously,
        or (2) the operation is waiting for user input, to be provided as a
        part of the POST request body. This operation is only valid when a GET
        cluster/restore/status returns a status with value SUSPENDED.
        Otherwise, a 409 response is returned.

        :type  advance_cluster_restore_request: :class:`com.vmware.nsx_policy.model_client.AdvanceClusterRestoreRequest`
        :param advance_cluster_restore_request: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('advance',
                            {
                            'advance_cluster_restore_request': advance_cluster_restore_request,
                            })

    def cancel(self):
        """
        This operation is only valid when a restore is in suspended state. The
        UI user can cancel any restore operation when the restore is suspended
        either due to an error, or for a user input. The API user would need to
        monitor the progression of a restore by calling periodically
        \"/api/v1/cluster/restore/status\" API. The response object
        (ClusterRestoreStatus), contains a field \"endpoints\". The API user
        can cancel the restore process if 'cancel' action is shown in the
        endpoint field. This operation is only valid when a GET
        cluster/restore/status returns a status with value SUSPENDED.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('cancel', None)

    def retry(self):
        """
        Retry any currently in-progress, failed restore operation. Only the
        last step of the multi-step restore operation would have failed,and
        only that step is retried. This operation is only valid when a GET
        cluster/restore/status returns a status with value FAILED. Otherwise, a
        409 response is returned.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('retry', None)

    def start(self,
              initiate_cluster_restore_request,
              ):
        """
        Start the restore of an NSX cluster, from some previously backed-up
        configuration. This operation is only valid when a GET
        cluster/restore/status returns a status with value NOT_STARTED.
        Otherwise, a 409 response is returned.

        :type  initiate_cluster_restore_request: :class:`com.vmware.nsx_policy.model_client.InitiateClusterRestoreRequest`
        :param initiate_cluster_restore_request: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('start',
                            {
                            'initiate_cluster_restore_request': initiate_cluster_restore_request,
                            })

    def suspend(self):
        """
        Suspend any currently running restore operation. The restore operation
        is made up of a number of steps. When this call is issued, any
        currently running step is allowed to finish (successfully or with
        errors), and the next step (and therefore the entire restore operation)
        is suspended until a subsequent resume or cancel call is issued. This
        operation is only valid when a GET cluster/restore/status returns a
        status with value RUNNING. Otherwise, a 409 response is returned.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('suspend', None)
class _BackupsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for retrievesshfingerprint operation
        retrievesshfingerprint_input_type = type.StructType('operation-input', {
            'remote_server_fingerprint_request': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RemoteServerFingerprintRequest'),
        })
        retrievesshfingerprint_error_dict = {
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
        retrievesshfingerprint_input_value_validator_list = [
        ]
        retrievesshfingerprint_output_validator_list = [
        ]
        retrievesshfingerprint_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/backups?action=retrieve_ssh_fingerprint',
            request_body_parameter='remote_server_fingerprint_request',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'retrievesshfingerprint': {
                'input_type': retrievesshfingerprint_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RemoteServerFingerprint'),
                'errors': retrievesshfingerprint_error_dict,
                'input_value_validator_list': retrievesshfingerprint_input_value_validator_list,
                'output_validator_list': retrievesshfingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'retrievesshfingerprint': retrievesshfingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.cluster.backups',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _RestoreStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for advance operation
        advance_input_type = type.StructType('operation-input', {
            'advance_cluster_restore_request': type.ReferenceType('com.vmware.nsx_policy.model_client', 'AdvanceClusterRestoreRequest'),
        })
        advance_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        advance_input_value_validator_list = [
        ]
        advance_output_validator_list = [
        ]
        advance_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=advance',
            request_body_parameter='advance_cluster_restore_request',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {})
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        cancel_input_value_validator_list = [
        ]
        cancel_output_validator_list = [
        ]
        cancel_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=cancel',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for retry operation
        retry_input_type = type.StructType('operation-input', {})
        retry_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        retry_input_value_validator_list = [
        ]
        retry_output_validator_list = [
        ]
        retry_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=retry',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for start operation
        start_input_type = type.StructType('operation-input', {
            'initiate_cluster_restore_request': type.ReferenceType('com.vmware.nsx_policy.model_client', 'InitiateClusterRestoreRequest'),
        })
        start_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        start_input_value_validator_list = [
        ]
        start_output_validator_list = [
        ]
        start_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=start',
            request_body_parameter='initiate_cluster_restore_request',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for suspend operation
        suspend_input_type = type.StructType('operation-input', {})
        suspend_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        suspend_input_value_validator_list = [
        ]
        suspend_output_validator_list = [
        ]
        suspend_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=suspend',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'advance': {
                'input_type': advance_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': advance_error_dict,
                'input_value_validator_list': advance_input_value_validator_list,
                'output_validator_list': advance_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'cancel': {
                'input_type': cancel_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': cancel_error_dict,
                'input_value_validator_list': cancel_input_value_validator_list,
                'output_validator_list': cancel_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'retry': {
                'input_type': retry_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': retry_error_dict,
                'input_value_validator_list': retry_input_value_validator_list,
                'output_validator_list': retry_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'start': {
                'input_type': start_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': start_error_dict,
                'input_value_validator_list': start_input_value_validator_list,
                'output_validator_list': start_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'suspend': {
                'input_type': suspend_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': suspend_error_dict,
                'input_value_validator_list': suspend_input_value_validator_list,
                'output_validator_list': suspend_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'advance': advance_rest_metadata,
            'cancel': cancel_rest_metadata,
            'retry': retry_rest_metadata,
            'start': start_rest_metadata,
            'suspend': suspend_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.cluster.restore',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Backups': Backups,
        'Restore': Restore,
        'backups': 'com.vmware.nsx_policy.cluster.backups_client.StubFactory',
        'restore': 'com.vmware.nsx_policy.cluster.restore_client.StubFactory',
    }

