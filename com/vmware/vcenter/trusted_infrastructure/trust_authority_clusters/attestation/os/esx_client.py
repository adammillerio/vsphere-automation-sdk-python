# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.
#---------------------------------------------------------------------------

"""
The
``com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx_client``
module provides the interfaces for configuring ESX host metadata.

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


class BaseImages(VapiInterface):
    """
    The ``BaseImages`` class provides methods to manage trusted instances of
    ESX software on a cluster level. This class was added in vSphere API 7.0.0.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage"
    """
    Resource type for ESX base image. This class attribute was added in vSphere API
    7.0.0.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.base_images'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BaseImagesStub)
        self._VAPI_OPERATION_IDS = {}
        self._VAPI_OPERATION_IDS.update({'import_from_imgdb_task': 'import_from_imgdb$task'})
        self._VAPI_OPERATION_IDS.update({'list_task': 'list$task'})
        self._VAPI_OPERATION_IDS.update({'delete_task': 'delete$task'})
        self._VAPI_OPERATION_IDS.update({'get_task': 'get$task'})

    class Health(Enum):
        """
        The ``BaseImages.Health`` class is indicator for the consistency of the
        hosts status in the cluster. This enumeration was added in vSphere API
        7.0.0.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        NONE = None
        """
        No status available. This class attribute was added in vSphere API 7.0.0.

        """
        OK = None
        """
        Each host in the cluster is in consistent state with the rest hosts in the
        cluster. This class attribute was added in vSphere API 7.0.0.

        """
        WARNING = None
        """
        Attestation is funtioning, however there is an issue that requires
        attention. This class attribute was added in vSphere API 7.0.0.

        """
        ERROR = None
        """
        Not all hosts in the cluster are in consistent state. This class attribute
        was added in vSphere API 7.0.0.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Health` instance.
            """
            Enum.__init__(string)

    Health._set_values([
        Health('NONE'),
        Health('OK'),
        Health('WARNING'),
        Health('ERROR'),
    ])
    Health._set_binding_type(type.EnumType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.base_images.health',
        Health))


    class Summary(VapiStruct):
        """
        The ``BaseImages.Summary`` class contains information that summarizes an
        ESX base image. This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     version=None,
                     display_name=None,
                     health=None,
                    ):
            """
            :type  version: :class:`str`
            :param version: A unique ESX version number. This attribute was added in vSphere
                API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage``.
            :type  display_name: :class:`str`
            :param display_name: A unique ESX version formatted for display. This attribute was
                added in vSphere API 7.0.0.
            :type  health: :class:`BaseImages.Health`
            :param health: A health indicator which indicates whether each host in the cluster
                has this version of the ESX base image. This attribute was added in
                vSphere API 7.0.0.
            """
            self.version = version
            self.display_name = display_name
            self.health = health
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.base_images.summary', {
            'version': type.IdType(resource_types='com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage'),
            'display_name': type.StringType(),
            'health': type.ReferenceType(__name__, 'BaseImages.Health'),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``BaseImages.Info`` class contains information that describes an ESX
        base image. This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     display_name=None,
                     health=None,
                     details=None,
                    ):
            """
            :type  display_name: :class:`str`
            :param display_name: A unique ESX version formatted for display. This attribute was
                added in vSphere API 7.0.0.
            :type  health: :class:`BaseImages.Health`
            :param health: A health indicator which indicates whether each host in the cluster
                has this version of the ESX base image. This attribute was added in
                vSphere API 7.0.0.
            :type  details: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param details: Details regarding the health. 
                
                When the ``BaseImages.Health`` is not :attr:`BaseImages.Health.OK`
                or :attr:`BaseImages.Health.NONE`, this member will provide an
                actionable description of the issues present.. This attribute was
                added in vSphere API 7.0.0.
            """
            self.display_name = display_name
            self.health = health
            self.details = details
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.base_images.info', {
            'display_name': type.StringType(),
            'health': type.ReferenceType(__name__, 'BaseImages.Health'),
            'details': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        Info,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``BaseImages.FilterSpec`` class contains the data necessary for
        identifying a Trust Authority Host in a cluster. This class was added in
        vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     version=None,
                     display_name=None,
                     health=None,
                    ):
            """
            :type  version: :class:`set` of :class:`str` or ``None``
            :param version: Search criteria by ESX base image version numbers. This attribute
                was added in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage``.
                When methods return a value of this class as a return value, the
                attribute will contain identifiers for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage``.
                version if {\\\\@term.unset} return all ESX version numbers.
            :type  display_name: :class:`set` of :class:`str` or ``None``
            :param display_name: Search criteria by ESX base image version version numbers. This
                attribute was added in vSphere API 7.0.0.
                displayName if {\\\\@term.unset} return all ESX display version
                numbers.
            :type  health: :class:`set` of :class:`BaseImages.Health` or ``None``
            :param health: Search criteria by health indicator. This attribute was added in
                vSphere API 7.0.0.
                health if {\\\\@term.unset} return all health indicators.
            """
            self.version = version
            self.display_name = display_name
            self.health = health
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.base_images.filter_spec', {
            'version': type.OptionalType(type.SetType(type.IdType())),
            'display_name': type.OptionalType(type.SetType(type.StringType())),
            'health': type.OptionalType(type.SetType(type.ReferenceType(__name__, 'BaseImages.Health'))),
        },
        FilterSpec,
        False,
        None))




    def import_from_imgdb_task(self,
                          cluster,
                          imgdb,
                          ):
        """
        Import ESX metadata as a new trusted base image to each host in the
        cluster. 
        
        Import a boot_imgdb.tgz file which contains metadata that describes a
        trusted ESX base image. A boot_imgdb.tgz file can be downloaded from a
        representative host.. This method was added in vSphere API 7.0.0.

        :type  cluster: :class:`str`
        :param cluster: The id of the cluster on which the operation will be executed.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  imgdb: :class:`str`
        :param imgdb: ESX metadata on a cluster level.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if ESX metadata for the same version has already been added.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the imgdb is invalid or cluster id is empty.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the cluster is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        """
        task_id = self._invoke('import_from_imgdb$task',
                                {
                                'cluster': cluster,
                                'imgdb': imgdb,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.IdType(resource_types='com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage'))
        return task_instance


    def list_task(self,
             cluster,
             spec=None,
             ):
        """
        Return a list of trusted ESX base images. This method was added in
        vSphere API 7.0.0.

        :type  cluster: :class:`str`
        :param cluster: The id of the cluster on which the operation will be executed.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`BaseImages.FilterSpec` or ``None``
        :param spec: The search specification.
            if {\\\\@term.unset} return all information.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the cluster id is empty.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the cluster is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        """
        task_id = self._invoke('list$task',
                                {
                                'cluster': cluster,
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.ListType(type.ReferenceType(__name__, 'BaseImages.Summary')))
        return task_instance


    def delete_task(self,
               cluster,
               version,
               ):
        """
        Remove a trusted ESX base image of each ESX in the cluster. This method
        was added in vSphere API 7.0.0.

        :type  cluster: :class:`str`
        :param cluster: The id of the cluster on which the operation will be executed.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  version: :class:`str`
        :param version: The ESX base image version.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the version is invalid or the cluster id is empty.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the version or cluster is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        """
        task_id = self._invoke('delete$task',
                                {
                                'cluster': cluster,
                                'version': version,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance


    def get_task(self,
            cluster,
            version,
            ):
        """
        Get the trusted ESX base version details. This method was added in
        vSphere API 7.0.0.

        :type  cluster: :class:`str`
        :param cluster: The id of the cluster on which the operation will be executed.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  version: :class:`str`
        :param version: The ESX base image version.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage``.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the version is invalid or the cluster id is empty.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the version or cluster is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        """
        task_id = self._invoke('get$task',
                                {
                                'cluster': cluster,
                                'version': version,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.ReferenceType(__name__, 'BaseImages.Info'))
        return task_instance
class _BaseImagesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for import_from_imgdb operation
        import_from_imgdb_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'imgdb': type.BlobType(),
        })
        import_from_imgdb_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        import_from_imgdb_input_value_validator_list = [
        ]
        import_from_imgdb_output_validator_list = [
        ]
        import_from_imgdb_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/trusted-infrastructure/trust-authority-clusters/{cluster}/attestation/os/esx/base-images',
            request_body_parameter='imgdb',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'import-from-imgdb',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.OptionalType(type.ReferenceType(__name__, 'BaseImages.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/trusted-infrastructure/trust-authority-clusters/{cluster}/attestation/os/esx/base-images',
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

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'version': type.IdType(resource_types='com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/trusted-infrastructure/trust-authority-clusters/{cluster}/attestation/os/esx/base-images/{version}',
            path_variables={
                'cluster': 'cluster',
                'version': 'version',
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

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'version': type.IdType(resource_types='com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.BaseImage'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/trusted-infrastructure/trust-authority-clusters/{cluster}/attestation/os/esx/base-images/{version}',
            path_variables={
                'cluster': 'cluster',
                'version': 'version',
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
            'import_from_imgdb$task': {
                'input_type': import_from_imgdb_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': import_from_imgdb_error_dict,
                'input_value_validator_list': import_from_imgdb_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'list$task': {
                'input_type': list_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'delete$task': {
                'input_type': delete_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'get$task': {
                'input_type': get_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'import_from_imgdb': import_from_imgdb_rest_metadata,
            'list': list_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.trusted_infrastructure.trust_authority_clusters.attestation.os.esx.base_images',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'BaseImages': BaseImages,
    }

