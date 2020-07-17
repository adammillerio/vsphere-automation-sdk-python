# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation.
#---------------------------------------------------------------------------

"""
The
``com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation_client``
module provides classes for configuring Attestation Services for Trusted
Clusters.

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


class Services(VapiInterface):
    """
    The ``Services`` class manages the Attestation Service instances a Trusted
    Cluster is configured to use. This class was added in vSphere API 7.0.0.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation.services'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServicesStub)
        self._VAPI_OPERATION_IDS = {}
        self._VAPI_OPERATION_IDS.update({'create_task': 'create$task'})
        self._VAPI_OPERATION_IDS.update({'delete_task': 'delete$task'})

    class Summary(VapiStruct):
        """
        The ``Services.Summary`` class contains basic information about a
        registered Attestation Service instance that is configured for a cluster.
        This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     service=None,
                     address=None,
                     group=None,
                     trust_authority_cluster=None,
                    ):
            """
            :type  service: :class:`str`
            :param service: The service's unique identifier. This attribute was added in
                vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.attestation.Service``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.attestation.Service``.
            :type  address: :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress`
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
            :type  group: :class:`str`
            :param group: The group specifies the Key Provider Service instances can accept
                reports issued by this Attestation Service instance. This attribute
                was added in vSphere API 7.0.0.
            :type  trust_authority_cluster: :class:`str`
            :param trust_authority_cluster: The cluster specifies the Trust Authority Cluster this Attestation
                Service belongs to. This attribute was added in vSphere API 7.0.0.
            """
            self.service = service
            self.address = address
            self.group = group
            self.trust_authority_cluster = trust_authority_cluster
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation.services.summary', {
            'service': type.IdType(resource_types='com.vmware.vcenter.trusted_infrastructure.attestation.Service'),
            'address': type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress'),
            'group': type.StringType(),
            'trust_authority_cluster': type.StringType(),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Services.Info`` class contains all the stored information about a
        registered Attestation Service instance that is configured for a cluster.
        This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'trusted_CA': 'trusted_ca',
                                }

        def __init__(self,
                     address=None,
                     trusted_ca=None,
                     group=None,
                     trust_authority_cluster=None,
                    ):
            """
            :type  address: :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress`
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
            :type  trusted_ca: :class:`com.vmware.vcenter.trusted_infrastructure_client.X509CertChain`
            :param trusted_ca: The service's TLS certificate chain. This attribute was added in
                vSphere API 7.0.0.
            :type  group: :class:`str`
            :param group: The group determines the Key Provider Service instances can accept
                reports issued by this Attestation Service instance. This attribute
                was added in vSphere API 7.0.0.
            :type  trust_authority_cluster: :class:`str`
            :param trust_authority_cluster: The cluster specifies the Trust Authority Cluster this Attestation
                Service belongs to. This attribute was added in vSphere API 7.0.0.
            """
            self.address = address
            self.trusted_ca = trusted_ca
            self.group = group
            self.trust_authority_cluster = trust_authority_cluster
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation.services.info', {
            'address': type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress'),
            'trusted_CA': type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'X509CertChain'),
            'group': type.StringType(),
            'trust_authority_cluster': type.StringType(),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Services.CreateSpec`` class contains the data necessary for
        configuring a registered Attestation Service instance with a cluster in the
        environment. This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'SERVICE' : [('service', True)],
                    'CLUSTER' : [('trust_authority_cluster', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     service=None,
                     trust_authority_cluster=None,
                    ):
            """
            :type  type: :class:`Services.CreateSpec.SourceType`
            :param type: Source of truth for the configuration of the Attestation Service.
                This attribute was added in vSphere API 7.0.0.
            :type  service: :class:`str`
            :param service: The service's unique ID. This attribute was added in vSphere API
                7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.attestation.Service``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.attestation.Service``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Services.CreateSpec.SourceType.SERVICE`.
            :type  trust_authority_cluster: :class:`str`
            :param trust_authority_cluster: The attestation cluster's unique ID. This attribute was added in
                vSphere API 7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Services.CreateSpec.SourceType.CLUSTER`.
            """
            self.type = type
            self.service = service
            self.trust_authority_cluster = trust_authority_cluster
            VapiStruct.__init__(self)


        class SourceType(Enum):
            """
            The ``Services.CreateSpec.SourceType`` class specifies the source of truth
            the Attestation Service will use for its configuration. This enumeration
            was added in vSphere API 7.0.0.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            SERVICE = None
            """
            The Attestation Service will be configured based on an ID of an specific
            Attestation Service. This class attribute was added in vSphere API 7.0.0.

            """
            CLUSTER = None
            """
            The Attestation Service will be configured based on an ID of a whole
            attestation cluster. This class attribute was added in vSphere API 7.0.0.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`SourceType` instance.
                """
                Enum.__init__(string)

        SourceType._set_values([
            SourceType('SERVICE'),
            SourceType('CLUSTER'),
        ])
        SourceType._set_binding_type(type.EnumType(
            'com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation.services.create_spec.source_type',
            SourceType))

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation.services.create_spec', {
            'type': type.ReferenceType(__name__, 'Services.CreateSpec.SourceType'),
            'service': type.OptionalType(type.IdType()),
            'trust_authority_cluster': type.OptionalType(type.StringType()),
        },
        CreateSpec,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Services.FilterSpec`` class contains the data necessary for
        identifying a Attestation service instance. This class was added in vSphere
        API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     services=None,
                     address=None,
                     group=None,
                     trust_authority_cluster=None,
                    ):
            """
            :type  services: :class:`set` of :class:`str` or ``None``
            :param services: A set of IDs by which to filter the services. This attribute was
                added in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.attestation.Service``.
                When methods return a value of this class as a return value, the
                attribute will contain identifiers for the resource type:
                ``com.vmware.vcenter.trusted_infrastructure.attestation.Service``.
                If None, the services will not be filtered by ID.
            :type  address: :class:`list` of :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress` or ``None``
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
                If None, the services will not be filtered by address.
            :type  group: :class:`set` of :class:`str` or ``None``
            :param group: The group specifies the Key Provider Service instances can accept
                reports issued by this Attestation Service instance. This attribute
                was added in vSphere API 7.0.0.
                If None, the services will not be filtered by group.
            :type  trust_authority_cluster: :class:`set` of :class:`str` or ``None``
            :param trust_authority_cluster: The cluster specifies the Trust Authority Cluster this Attestation
                Service instance belongs to. This attribute was added in vSphere
                API 7.0.0.
                If None, the services will not be filtered by
                trustAuthorityCluster.
            """
            self.services = services
            self.address = address
            self.group = group
            self.trust_authority_cluster = trust_authority_cluster
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation.services.filter_spec', {
            'services': type.OptionalType(type.SetType(type.IdType())),
            'address': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress'))),
            'group': type.OptionalType(type.SetType(type.StringType())),
            'trust_authority_cluster': type.OptionalType(type.SetType(type.StringType())),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             cluster,
             spec=None,
             ):
        """
        Returns the basic information about all configured Attestation Service
        instances used by this cluster. This method was added in vSphere API
        7.0.0.

        :type  cluster: :class:`str`
        :param cluster: The ID of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`Services.FilterSpec` or ``None``
        :param spec: Only return services matching the filters.
            If {\\\\@term.unset} return all services.
        :rtype: :class:`list` of :class:`Services.Summary`
        :return: Basic information about all configured Attestation Service
            instances used by this cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the cluster ID is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``TrustedAdmin.ReadTrustedHosts``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires ``System.View``.
        """
        return self._invoke('list',
                            {
                            'cluster': cluster,
                            'spec': spec,
                            })

    def get(self,
            cluster,
            service,
            ):
        """
        Returns detailed information about the given registered Attestation
        Service instance that is configured for the given cluster. This method
        was added in vSphere API 7.0.0.

        :type  cluster: :class:`str`
        :param cluster: The ID of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  service: :class:`str`
        :param service: The ID of the service.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.trusted_infrastructure.attestation.Service``.
        :rtype: :class:`Services.Info`
        :return: Detailed information about the specified Attestation Service
            configured for the given cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the cluster or the service ID is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``TrustedAdmin.ReadTrustedHosts``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires ``System.View``.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            'service': service,
                            })


    def create_task(self,
               cluster,
               spec,
               ):
        """
        Configures the cluster to use a the given registered Attestation
        Service. This method was added in vSphere API 7.0.0.

        :type  cluster: :class:`str`
        :param cluster: The ID of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`Services.CreateSpec`
        :param spec: Describes the registered instance of the Attestation Service
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the Attestation Service is already configured for this cluster
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            for any other error.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the CreateSpec is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the cluster ID is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if all the hosts in the cluster do not have VMware vSphere Trust
            Authority enabled license.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        """
        task_id = self._invoke('create$task',
                                {
                                'cluster': cluster,
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.IdType(resource_types='com.vmware.vcenter.trusted_infrastructure.attestation.Service'))
        return task_instance


    def delete_task(self,
               cluster,
               service,
               ):
        """
        Removes the Attestation Service instance from the configuration of the
        given cluster. This method was added in vSphere API 7.0.0.

        :type  cluster: :class:`str`
        :param cluster: the unique ID of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  service: :class:`str`
        :param service: the registered Attestation Service instance unique identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.trusted_infrastructure.attestation.Service``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the Attestation Service instance or the cluster are not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        """
        task_id = self._invoke('delete$task',
                                {
                                'cluster': cluster,
                                'service': service,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance
class _ServicesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.OptionalType(type.ReferenceType(__name__, 'Services.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
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
            http_method='POST',
            url_template='/vcenter/trusted-infrastructure/trusted-clusters/{cluster}/attestation/services',
            request_body_parameter='spec',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'query',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'service': type.IdType(resource_types='com.vmware.vcenter.trusted_infrastructure.attestation.Service'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
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
            url_template='/vcenter/trusted-infrastructure/trusted-clusters/{cluster}/attestation/services/{service}',
            path_variables={
                'cluster': 'cluster',
                'service': 'service',
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

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.ReferenceType(__name__, 'Services.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/trusted-infrastructure/trusted-clusters/{cluster}/attestation/services',
            request_body_parameter='spec',
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
            'service': type.IdType(resource_types='com.vmware.vcenter.trusted_infrastructure.attestation.Service'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
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
            url_template='/vcenter/trusted-infrastructure/trusted-clusters/{cluster}/attestation/services/{service}',
            path_variables={
                'cluster': 'cluster',
                'service': 'service',
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'Services.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Services.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create$task': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
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
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.trusted_infrastructure.trusted_clusters.attestation.services',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Services': Services,
    }

