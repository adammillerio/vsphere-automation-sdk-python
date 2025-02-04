# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.settings.clusters.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.settings.clusters_client`` module provides classes to
manage desired state configuration and software for a cluster of ESX hosts.

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


class DepotOverrides(VapiInterface):
    """
    The ``DepotOverrides`` class provides methods to manage software depots
    overriden for a given cluster. In general ESX servers reach out to vCenter
    (VUM) to fetch the metadata and payloads required for lifecycle operations.
    But in ROBO environments ESX clusters can't (or because of bandwidth
    requirements shouldn't) reach out to vCenter to fetch payloads and
    metadata. This class allows setting cluster level overrides for depots. If
    any depots are provided for a cluster, then vCenter level depots are not
    used for that cluster's remediation. These are not synced periodically at
    vCenter and are only used by ESXs for lifecycle operations.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.clusters.depot_overrides'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DepotOverridesStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``DepotOverrides.Info`` class defines the information regarding depot
        overrides for a given cluster.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     depots=None,
                    ):
            """
            :type  depots: :class:`list` of :class:`DepotOverrides.Depot`
            :param depots: List of the depot overrides.
            """
            self.depots = depots
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.depot_overrides.info', {
            'depots': type.ListType(type.ReferenceType(__name__, 'DepotOverrides.Depot')),
        },
        Info,
        False,
        None))


    class Depot(VapiStruct):
        """
        The ``DepotOverrides.Depot`` class defines the information regarding a
        particular depot override for a given cluster.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     location=None,
                    ):
            """
            :type  location: :class:`str`
            :param location: Location of the depot override. This could be a location of zip
                file or location to an index.xml file.
            """
            self.location = location
            VapiStruct.__init__(self)


    Depot._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.depot_overrides.depot', {
            'location': type.URIType(),
        },
        Depot,
        False,
        None))



    def get(self,
            cluster,
            ):
        """
        Returns the information about currently configured depot overrides for
        a given cluster.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`DepotOverrides.Info`
        :return: Information about currently configured depot overrides for a given
            cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires
              ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })

    def add(self,
            cluster,
            depot,
            ):
        """
        Adds a new depot override to the list of currently configured depot
        overrides for a given cluster.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  depot: :class:`DepotOverrides.Depot`
        :param depot: Information of a depot override.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If an invalid location is provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if depot override with given information already exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('add',
                            {
                            'cluster': cluster,
                            'depot': depot,
                            })

    def remove(self,
               cluster,
               depot,
               ):
        """
        Removes a depot override from the list of currently configured depot
        overrides for a given cluster.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  depot: :class:`DepotOverrides.Depot`
        :param depot: Information of the depot override to be removed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no depot override with given information or no cluster
            associated with identifier {param.name cluster} in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('remove',
                            {
                            'cluster': cluster,
                            'depot': depot,
                            })
class Software(VapiInterface):
    """
    The ``Software`` class provides methods to manage desired software
    specification of an ESX cluster.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.clusters.software'
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
        self._VAPI_OPERATION_IDS.update({'apply_task': 'apply$task'})
        self._VAPI_OPERATION_IDS.update({'check_task': 'check$task'})

    class ExportType(Enum):
        """
        The ``Software.ExportType`` class defines the formats in which software
        specification document or image can be exported.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SOFTWARE_SPEC = None
        """
        Export software specification document.

        """
        ISO_IMAGE = None
        """
        Export ISO image.

        """
        OFFLINE_BUNDLE = None
        """
        Export offline bundle.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ExportType` instance.
            """
            Enum.__init__(string)

    ExportType._set_values([
        ExportType('SOFTWARE_SPEC'),
        ExportType('ISO_IMAGE'),
        ExportType('OFFLINE_BUNDLE'),
    ])
    ExportType._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.clusters.software.export_type',
        ExportType))


    class Status(Enum):
        """
        The ``Software.Status`` class defines the status result for a particular
        check.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        OK = None
        """
        The check indicates a success.

        """
        WARNING = None
        """
        The check indicates a warning.

        """
        TIMEOUT = None
        """
        The check did not return in a timely manner.

        """
        ERROR = None
        """
        The check indicates an error.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Status` instance.
            """
            Enum.__init__(string)

    Status._set_values([
        Status('OK'),
        Status('WARNING'),
        Status('TIMEOUT'),
        Status('ERROR'),
    ])
    Status._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.clusters.software.status',
        Status))


    class ExportSpec(VapiStruct):
        """
        The ``Software.ExportSpec`` class contains information describing how a
        software specification or image should be exported.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     export_software_spec=None,
                     export_iso_image=None,
                     export_offline_bundle=None,
                    ):
            """
            :type  export_software_spec: :class:`bool`
            :param export_software_spec: Whether to export software specification document.
            :type  export_iso_image: :class:`bool`
            :param export_iso_image: Whether to export ISO image.
            :type  export_offline_bundle: :class:`bool`
            :param export_offline_bundle: Whether to export offline bundle.
            """
            self.export_software_spec = export_software_spec
            self.export_iso_image = export_iso_image
            self.export_offline_bundle = export_offline_bundle
            VapiStruct.__init__(self)


    ExportSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.export_spec', {
            'export_software_spec': type.BooleanType(),
            'export_iso_image': type.BooleanType(),
            'export_offline_bundle': type.BooleanType(),
        },
        ExportSpec,
        False,
        None))


    class ApplySpec(VapiStruct):
        """
        The ``Software.ApplySpec`` class contains attributes that describe the
        specification to be used for applying the desired software document to a
        cluster.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     commit=None,
                     hosts=None,
                     accept_eula=None,
                    ):
            """
            :type  commit: :class:`str` or ``None``
            :param commit: The minimum commit identifier of the desired software document to
                be used during the :func:`Software.apply` method.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.commit``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.esx.settings.commit``.
                if None or empty the apply method will use the latest commit to
                fetch the desired state document.
            :type  hosts: :class:`set` of :class:`str` or ``None``
            :param hosts: The specific hosts within the cluster to be considered during the
                :func:`Software.apply` method.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
                if None or empty the :func:`Software.apply` method will remediate
                all hosts within the cluster.
            :type  accept_eula: :class:`bool` or ``None``
            :param accept_eula: Accept the VMware End User License Agreement (EULA) before starting
                the :func:`Software.apply` method. The VMware EULA is available for
                download at, https://www.vmware.com/download/eula.html
                if None the :func:`Software.apply` method could fail due to the
                EULA not being accepted.
            """
            self.commit = commit
            self.hosts = hosts
            self.accept_eula = accept_eula
            VapiStruct.__init__(self)


    ApplySpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.apply_spec', {
            'commit': type.OptionalType(type.IdType()),
            'hosts': type.OptionalType(type.SetType(type.IdType())),
            'accept_eula': type.OptionalType(type.BooleanType()),
        },
        ApplySpec,
        False,
        None))


    class ApplyStatus(VapiStruct):
        """
        The ``Software.ApplyStatus`` class contains attributes that describe the
        status of an :func:`Software.apply` method.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     start_time=None,
                     end_time=None,
                     notifications=None,
                    ):
            """
            :type  status: :class:`Software.ApplyStatus.Status`
            :param status: The status of the method.
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time when the method started.
            :type  end_time: :class:`datetime.datetime`
            :param end_time: Time when the method completed.
            :type  notifications: :class:`com.vmware.esx.settings_client.Notifications`
            :param notifications: Notifications providing additional information about the status of
                the method.
            """
            self.status = status
            self.start_time = start_time
            self.end_time = end_time
            self.notifications = notifications
            VapiStruct.__init__(self)


        class Status(Enum):
            """
            The ``Software.ApplyStatus.Status`` class contains the possible different
            status codes that can be returned while trying to :func:`Software.apply`
            the desired software specification to hosts within the cluster.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            OK = None
            """
            The method completed successfully.

            """
            SKIPPED = None
            """
            The method was skipped.

            """
            TIMED_OUT = None
            """
            The method timed out.

            """
            ERROR = None
            """
            The method encountered an unspecified error.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Status` instance.
                """
                Enum.__init__(string)

        Status._set_values([
            Status('OK'),
            Status('SKIPPED'),
            Status('TIMED_OUT'),
            Status('ERROR'),
        ])
        Status._set_binding_type(type.EnumType(
            'com.vmware.esx.settings.clusters.software.apply_status.status',
            Status))

    ApplyStatus._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.apply_status', {
            'status': type.ReferenceType(__name__, 'Software.ApplyStatus.Status'),
            'start_time': type.DateTimeType(),
            'end_time': type.DateTimeType(),
            'notifications': type.ReferenceType('com.vmware.esx.settings_client', 'Notifications'),
        },
        ApplyStatus,
        False,
        None))


    class ApplyResult(VapiStruct):
        """
        The ``Software.ApplyResult`` class contains attributes that describe the
        result of an :func:`Software.apply` method.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     commit=None,
                     host_info=None,
                     host_status=None,
                     successful_hosts=None,
                     failed_hosts=None,
                     skipped_hosts=None,
                    ):
            """
            :type  status: :class:`Software.ApplyStatus` or ``None``
            :param status: Specifies the aggregated status of the :func:`Software.apply`
                method.
                None if the :func:`Software.apply` method is in progress.
            :type  commit: :class:`str`
            :param commit: The identifier of the commit used to fetch the desired software
                document to be applied to all hosts within the cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.commit``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.esx.settings.commit``.
            :type  host_info: :class:`dict` of :class:`str` and :class:`com.vmware.esx.settings_client.HostInfo`
            :param host_info: Information of the hosts in this cluster to which the desired
                software document specified by the
                :attr:`Software.ApplyResult.commit` should be applied to.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``HostSystem``. When methods return a value of this class as
                a return value, the key in the attribute :class:`dict` will be an
                identifier for the resource type: ``HostSystem``.
            :type  host_status: :class:`dict` of :class:`str` and :class:`Software.ApplyStatus`
            :param host_status: Status of the hosts in this cluster to which the desired software
                document specified by the :attr:`Software.ApplyResult.commit` was
                applied to. Hosts on which the :func:`Software.apply` method was
                successful are specified by
                :attr:`Software.ApplyResult.successful_hosts`. Hosts on which the
                apply method failed are specified by
                :attr:`Software.ApplyResult.failed_hosts`. Hosts which were skipped
                by the :func:`Software.apply` method are specified by
                :attr:`Software.ApplyResult.skipped_hosts`.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``HostSystem``. When methods return a value of this class as
                a return value, the key in the attribute :class:`dict` will be an
                identifier for the resource type: ``HostSystem``.
            :type  successful_hosts: :class:`set` of :class:`str`
            :param successful_hosts: Hosts in this cluster to which the desired software document
                specified by the :attr:`Software.ApplyResult.commit` has been
                successfully applied to.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
            :type  failed_hosts: :class:`set` of :class:`str`
            :param failed_hosts: Hosts in this cluster to which the desired software document
                specified by the :attr:`Software.ApplyResult.commit` failed to be
                applied to.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
            :type  skipped_hosts: :class:`set` of :class:`str`
            :param skipped_hosts: Hosts in this cluster that were skipped by the
                :func:`Software.apply` method.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
            """
            self.status = status
            self.commit = commit
            self.host_info = host_info
            self.host_status = host_status
            self.successful_hosts = successful_hosts
            self.failed_hosts = failed_hosts
            self.skipped_hosts = skipped_hosts
            VapiStruct.__init__(self)


    ApplyResult._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.apply_result', {
            'status': type.OptionalType(type.ReferenceType(__name__, 'Software.ApplyStatus')),
            'commit': type.IdType(resource_types='com.vmware.esx.settings.commit'),
            'host_info': type.MapType(type.IdType(), type.ReferenceType('com.vmware.esx.settings_client', 'HostInfo')),
            'host_status': type.MapType(type.IdType(), type.ReferenceType(__name__, 'Software.ApplyStatus')),
            'successful_hosts': type.SetType(type.IdType()),
            'failed_hosts': type.SetType(type.IdType()),
            'skipped_hosts': type.SetType(type.IdType()),
        },
        ApplyResult,
        False,
        None))


    class CheckSpec(VapiStruct):
        """
        The ``Software.CheckSpec`` class contains attributes that describe the
        specification to be used for running checks on the cluster before the
        :func:`Software.apply` method.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     commit=None,
                     hosts=None,
                    ):
            """
            :type  commit: :class:`str` or ``None``
            :param commit: The minimum commit identifier of the desired software document to
                be used during the check method.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.commit``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.esx.settings.commit``.
                if None or empty the check opertion will use the latest commit to
                fetch the desired state document.
            :type  hosts: :class:`set` of :class:`str` or ``None``
            :param hosts: The specific hosts for which checks need to be performed
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
                if None or empty checks are run for all hosts within the cluster.
            """
            self.commit = commit
            self.hosts = hosts
            VapiStruct.__init__(self)


    CheckSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.check_spec', {
            'commit': type.OptionalType(type.IdType()),
            'hosts': type.OptionalType(type.SetType(type.IdType())),
        },
        CheckSpec,
        False,
        None))


    class CheckInfo(VapiStruct):
        """
        The ``Software.CheckInfo`` class contains attributes that describe a
        particular check.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     check=None,
                     name=None,
                     description=None,
                    ):
            """
            :type  check: :class:`str`
            :param check: The check identifier.
            :type  name: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param name: The check name.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Human-readable check description.
            """
            self.check = check
            self.name = name
            self.description = description
            VapiStruct.__init__(self)


    CheckInfo._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.check_info', {
            'check': type.StringType(),
            'name': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        },
        CheckInfo,
        False,
        None))


    class CheckStatus(VapiStruct):
        """
        The ``Software.CheckStatus`` class contains attributes that describe a
        check result.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     check=None,
                     status=None,
                     issues=None,
                    ):
            """
            :type  check: :class:`Software.CheckInfo`
            :param check: Information about this check.
            :type  status: :class:`Software.Status`
            :param status: The status of this check.
            :type  issues: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param issues: The issues encountered while running this check.
            """
            self.check = check
            self.status = status
            self.issues = issues
            VapiStruct.__init__(self)


    CheckStatus._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.check_status', {
            'check': type.ReferenceType(__name__, 'Software.CheckInfo'),
            'status': type.ReferenceType(__name__, 'Software.Status'),
            'issues': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        CheckStatus,
        False,
        None))


    class EntityCheckResult(VapiStruct):
        """
        The ``Software.EntityCheckResult`` class contains attributes that describe
        aggregated status of all checks performed on a specific entity.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'CLUSTER' : [('cluster', True)],
                    'HOST' : [('host', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     cluster=None,
                     host=None,
                     status=None,
                     check_statuses=None,
                    ):
            """
            :type  type: :class:`Software.EntityCheckResult.EntityType`
            :param type: The entity type for which these checks are being run.
            :type  cluster: :class:`str`
            :param cluster: If the entity type is CLUSTER then the cluster identifier for which
                the checks have been run.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``ClusterComputeResource``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`Software.EntityCheckResult.EntityType.CLUSTER`.
            :type  host: :class:`str`
            :param host: If the entity type is HOST then the host identifier for which the
                checks have been run.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Software.EntityCheckResult.EntityType.HOST`.
            :type  status: :class:`Software.Status`
            :param status: Aggregated status from all checks performed on this entity.
            :type  check_statuses: :class:`list` of :class:`Software.CheckStatus`
            :param check_statuses: List of ``Software.CheckStatus`` for all checks performed.
            """
            self.type = type
            self.cluster = cluster
            self.host = host
            self.status = status
            self.check_statuses = check_statuses
            VapiStruct.__init__(self)


        class EntityType(Enum):
            """
            The ``Software.EntityCheckResult.EntityType`` class contains the entitites
            on which checks can be performed.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            CLUSTER = None
            """
            Entity type Cluster

            """
            HOST = None
            """
            Entity type Host

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`EntityType` instance.
                """
                Enum.__init__(string)

        EntityType._set_values([
            EntityType('CLUSTER'),
            EntityType('HOST'),
        ])
        EntityType._set_binding_type(type.EnumType(
            'com.vmware.esx.settings.clusters.software.entity_check_result.entity_type',
            EntityType))

    EntityCheckResult._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.entity_check_result', {
            'type': type.ReferenceType(__name__, 'Software.EntityCheckResult.EntityType'),
            'cluster': type.OptionalType(type.IdType()),
            'host': type.OptionalType(type.IdType()),
            'status': type.ReferenceType(__name__, 'Software.Status'),
            'check_statuses': type.ListType(type.ReferenceType(__name__, 'Software.CheckStatus')),
        },
        EntityCheckResult,
        False,
        None))


    class CheckResult(VapiStruct):
        """
        The ``Software.CheckResult`` class contains attributes that describe
        aggregated status of all checks performed.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     start_time=None,
                     end_time=None,
                     commit=None,
                     host_info=None,
                     entity_results=None,
                    ):
            """
            :type  status: :class:`Software.Status`
            :param status: Aggregated status from all checks performed.
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time when the operation started.
            :type  end_time: :class:`datetime.datetime`
            :param end_time: Time when the operation completed.
            :type  commit: :class:`str`
            :param commit: The identifier of the commit on which checks have been run.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.commit``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.esx.settings.commit``.
            :type  host_info: :class:`dict` of :class:`str` and :class:`com.vmware.esx.settings_client.HostInfo`
            :param host_info: Information about the hosts in this cluster for which checks have
                been requested to be run.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``HostSystem``. When methods return a value of this class as
                a return value, the key in the attribute :class:`dict` will be an
                identifier for the resource type: ``HostSystem``.
            :type  entity_results: :class:`list` of :class:`Software.EntityCheckResult`
            :param entity_results: List of ``Software.EntityCheckResult`` for all entities for which
                checks have been run.
            """
            self.status = status
            self.start_time = start_time
            self.end_time = end_time
            self.commit = commit
            self.host_info = host_info
            self.entity_results = entity_results
            VapiStruct.__init__(self)


    CheckResult._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.check_result', {
            'status': type.ReferenceType(__name__, 'Software.Status'),
            'start_time': type.DateTimeType(),
            'end_time': type.DateTimeType(),
            'commit': type.IdType(resource_types='com.vmware.esx.settings.commit'),
            'host_info': type.MapType(type.IdType(), type.ReferenceType('com.vmware.esx.settings_client', 'HostInfo')),
            'entity_results': type.ListType(type.ReferenceType(__name__, 'Software.EntityCheckResult')),
        },
        CheckResult,
        False,
        None))



    def get(self,
            cluster,
            ):
        """
        Returns the complete desired software specification.

        :type  cluster: :class:`str`
        :param cluster: Identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`com.vmware.esx.settings_client.SoftwareInfo`
        :return: Cluster software specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is unknown internal error. The accompanying error message
            will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            If the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSoftwareSpecification.Read``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires
              ``VcIntegrity.lifecycleSoftwareSpecification.Read``.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })


    def scan_task(self,
             cluster,
             ):
        """
        Scans all the hosts in the cluster against the cluster's desired state.
        The result of this operation can be queried by calling the
        cis/tasks/{task-id} where the task-id is the response of this
        operation.

        :type  cluster: :class:`str`
        :param cluster: Identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is unknown internal error. The accompanying error message
            will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system or
            if desired software document is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            If the caller is not authenticated.
        """
        task_id = self._invoke('scan$task',
                                {
                                'cluster': cluster,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.ReferenceType('com.vmware.esx.settings_client', 'ClusterCompliance'))
        return task_instance

    def export(self,
               cluster,
               spec,
               ):
        """
        Exports the desired software specification document and/or image. This
        API will not export the solution section of the desired software
        specification.

        :type  cluster: :class:`str`
        :param cluster: Identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`Software.ExportSpec`
        :param spec: 
        :rtype: :class:`dict` of :class:`Software.ExportType` and :class:`str`
        :return: A map from export type to URL of the exported data for that type.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is am unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system or
            if desired software document is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            If the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSoftwareSpecification.Read``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires
              ``VcIntegrity.lifecycleSoftwareSpecification.Read``.
        """
        return self._invoke('export',
                            {
                            'cluster': cluster,
                            'spec': spec,
                            })


    def apply_task(self,
              cluster,
              spec,
              ):
        """
        Applies the desired software document associated with the given cluster
        to hosts within the cluster. If ``commit`` attribute is :class:`set`,
        it implies the minimum commit that the :func:`Software.apply` method
        should use, however if subsequent commits have been made to the desired
        state document the apply method will use the most recent desired state
        document. The result of this operation can be queried by calling the
        cis/tasks/{task-id} where the task-id is the response of this
        operation.

        :type  cluster: :class:`str`
        :param cluster: Identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`Software.ApplySpec`
        :param spec: Apply specification.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            If the cluster is already at specified commit as described in the
            apply specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is an unknown internal error or if the EULA has not been
            accepted. The accompanying error message will give more details
            about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the ``commit`` attribute of ``spec`` specifies an invalid
            commit, or the ``hosts`` attribute of ``spec`` specifies an invalid
            host or a host not part of the cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            If there is another operation in progress.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system or
            if desired software document is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
            If the operation times out.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            If the caller is not authenticated.
        """
        task_id = self._invoke('apply$task',
                                {
                                'cluster': cluster,
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.ReferenceType(__name__, 'Software.ApplyResult'))
        return task_instance


    def check_task(self,
              cluster,
              spec,
              ):
        """
        Runs checks on the cluster before applying the desired software
        document across all hosts in the cluster. Checks if all hosts in the
        cluster are in a good state to be updated with the desired software
        document. If ``commit`` attribute is :class:`set` it implies the
        minimum commit that the check method should use, however if subsequent
        commits have been made to the desired state document the check method
        will use the most recent desired state document. The result of this
        operation can be queried by calling the cis/tasks/{task-id} where the
        task-id is the response of this operation.

        :type  cluster: :class:`str`
        :param cluster: Identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`Software.CheckSpec`
        :param spec: Check specification.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is unknown internal error. The accompanying error message
            will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the ``commit`` attribute of ``spec`` specifies an invalid
            commit, or the ``hosts`` attribute of ``spec`` specifies an invalid
            host or a host not part of the cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            If there is another operation in progress or if the ``commit``
            attribute of ``spec`` specifies a commit that has already been
            applied.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
            If the operation times out.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            If the caller is not authenticated.
        """
        task_id = self._invoke('check$task',
                                {
                                'cluster': cluster,
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.ReferenceType(__name__, 'Software.CheckResult'))
        return task_instance
class _DepotOverridesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/esx/settings/clusters/{cluster}/depot-overrides',
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

        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'depot': type.ReferenceType(__name__, 'DepotOverrides.Depot'),
        })
        add_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        add_input_value_validator_list = [
        ]
        add_output_validator_list = [
        ]
        add_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/clusters/{cluster}/depot-overrides',
            request_body_parameter='depot',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'add',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        # properties for remove operation
        remove_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'depot': type.ReferenceType(__name__, 'DepotOverrides.Depot'),
        })
        remove_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        remove_input_value_validator_list = [
        ]
        remove_output_validator_list = [
        ]
        remove_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/clusters/{cluster}/depot-overrides',
            request_body_parameter='depot',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'remove',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'DepotOverrides.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'add': {
                'input_type': add_input_type,
                'output_type': type.VoidType(),
                'errors': add_error_dict,
                'input_value_validator_list': add_input_value_validator_list,
                'output_validator_list': add_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'remove': {
                'input_type': remove_input_type,
                'output_type': type.VoidType(),
                'errors': remove_error_dict,
                'input_value_validator_list': remove_input_value_validator_list,
                'output_validator_list': remove_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'add': add_rest_metadata,
            'remove': remove_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.clusters.depot_overrides',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SoftwareStub(ApiInterfaceStub):
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
            url_template='/esx/settings/clusters/{cluster}/software',
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

        # properties for scan operation
        scan_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
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

        }
        scan_input_value_validator_list = [
        ]
        scan_output_validator_list = [
        ]
        scan_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/clusters/{cluster}/software',
            path_variables={
                'cluster': 'cluster',
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

        # properties for export operation
        export_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.ReferenceType(__name__, 'Software.ExportSpec'),
        })
        export_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        export_input_value_validator_list = [
        ]
        export_output_validator_list = [
        ]
        export_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/clusters/{cluster}/software',
            request_body_parameter='spec',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'export',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        # properties for apply operation
        apply_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.ReferenceType(__name__, 'Software.ApplySpec'),
        })
        apply_error_dict = {
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        apply_input_value_validator_list = [
        ]
        apply_output_validator_list = [
        ]
        apply_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/clusters/{cluster}/software',
            request_body_parameter='spec',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'apply',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.ReferenceType(__name__, 'Software.CheckSpec'),
        })
        check_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        check_input_value_validator_list = [
        ]
        check_output_validator_list = [
        ]
        check_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/clusters/{cluster}/software',
            request_body_parameter='spec',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'check',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.esx.settings_client', 'SoftwareInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'scan$task': {
                'input_type': scan_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': scan_error_dict,
                'input_value_validator_list': scan_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'export': {
                'input_type': export_input_type,
                'output_type': type.MapType(type.ReferenceType(__name__, 'Software.ExportType'), type.URIType()),
                'errors': export_error_dict,
                'input_value_validator_list': export_input_value_validator_list,
                'output_validator_list': export_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'apply$task': {
                'input_type': apply_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': apply_error_dict,
                'input_value_validator_list': apply_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check$task': {
                'input_type': check_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_error_dict,
                'input_value_validator_list': check_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'scan': scan_rest_metadata,
            'export': export_rest_metadata,
            'apply': apply_rest_metadata,
            'check': check_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.clusters.software',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'DepotOverrides': DepotOverrides,
        'Software': Software,
        'enablement': 'com.vmware.esx.settings.clusters.enablement_client.StubFactory',
        'policies': 'com.vmware.esx.settings.clusters.policies_client.StubFactory',
        'software': 'com.vmware.esx.settings.clusters.software_client.StubFactory',
    }

