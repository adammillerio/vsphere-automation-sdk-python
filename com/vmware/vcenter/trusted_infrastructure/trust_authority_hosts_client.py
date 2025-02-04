# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts_client``
module provides classes that provide information necessary to connect to the
hosts running the Trust Authority Components.

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


class Attestation(VapiInterface):
    """
    The ``Attestation`` class contains information necessary to connect to the
    hosts running Attestation Service. This class was added in vSphere API
    7.0.0.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.attestation'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _AttestationStub)
        self._VAPI_OPERATION_IDS = {}

    class SummaryType(Enum):
        """
        The connection information could include the certificates or be a shorter
        summary. This enumeration was added in vSphere API 7.0.0.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FULL = None
        """
        The full connection information, including certificates. This class
        attribute was added in vSphere API 7.0.0.

        """
        NORMAL = None
        """
        A summary containing only the hostname, port, and the group ID which
        determines the Attestation Services this Attestation Service can
        communicate with. This class attribute was added in vSphere API 7.0.0.

        """
        BRIEF = None
        """
        A brief summary, containing only the hostname for the Attestation Service.
        This class attribute was added in vSphere API 7.0.0.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SummaryType` instance.
            """
            Enum.__init__(string)

    SummaryType._set_values([
        SummaryType('FULL'),
        SummaryType('NORMAL'),
        SummaryType('BRIEF'),
    ])
    SummaryType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.attestation.summary_type',
        SummaryType))


    class Summary(VapiStruct):
        """
        The ``Attestation.Summary`` class contains all the stored information about
        a Attestation Service. This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'summary_type',
                {
                    'BRIEF' : [('host', True), ('address', True)],
                    'NORMAL' : [('host', True), ('address', True), ('group', True), ('cluster', True)],
                    'FULL' : [('host', True), ('address', True), ('group', True), ('cluster', True), ('trusted_CA', True)],
                }
            ),
        ]


        _canonical_to_pep_names = {
                                'trusted_CA': 'trusted_ca',
                                }

        def __init__(self,
                     summary_type=None,
                     host=None,
                     address=None,
                     group=None,
                     cluster=None,
                     trusted_ca=None,
                    ):
            """
            :type  summary_type: :class:`Attestation.SummaryType`
            :param summary_type: Defines the verbosity of the summary. This attribute was added in
                vSphere API 7.0.0.
            :type  host: :class:`str`
            :param host: The trusted ESX on which the service runs. This attribute was added
                in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is one of :attr:`Attestation.SummaryType.BRIEF`,
                :attr:`Attestation.SummaryType.NORMAL`, or
                :attr:`Attestation.SummaryType.FULL`.
            :type  address: :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress`
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is one of :attr:`Attestation.SummaryType.BRIEF`,
                :attr:`Attestation.SummaryType.NORMAL`, or
                :attr:`Attestation.SummaryType.FULL`.
            :type  group: :class:`str`
            :param group: The group ID determines which Attestation Service instances this
                Attestation Service can communicate with. This attribute was added
                in vSphere API 7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is one of :attr:`Attestation.SummaryType.NORMAL`
                or :attr:`Attestation.SummaryType.FULL`.
            :type  cluster: :class:`str`
            :param cluster: The opaque string identifier of the cluster in which the
                Attestation Service is part of. This attribute was added in vSphere
                API 7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is one of :attr:`Attestation.SummaryType.NORMAL`
                or :attr:`Attestation.SummaryType.FULL`.
            :type  trusted_ca: :class:`com.vmware.vcenter.trusted_infrastructure_client.X509CertChain`
            :param trusted_ca: The service's TLS certificate chain. This attribute was added in
                vSphere API 7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is :attr:`Attestation.SummaryType.FULL`.
            """
            self.summary_type = summary_type
            self.host = host
            self.address = address
            self.group = group
            self.cluster = cluster
            self.trusted_ca = trusted_ca
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.attestation.summary', {
            'summary_type': type.ReferenceType(__name__, 'Attestation.SummaryType'),
            'host': type.OptionalType(type.IdType()),
            'address': type.OptionalType(type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress')),
            'group': type.OptionalType(type.StringType()),
            'cluster': type.OptionalType(type.StringType()),
            'trusted_CA': type.OptionalType(type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'X509CertChain')),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Attestation.Info`` class contains all the stored information about a
        Attestation Service. This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'trusted_CA': 'trusted_ca',
                                }

        def __init__(self,
                     host=None,
                     address=None,
                     group=None,
                     cluster=None,
                     trusted_ca=None,
                    ):
            """
            :type  host: :class:`str`
            :param host: The trusted ESX on which the service runs. This attribute was added
                in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
            :type  address: :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress`
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
            :type  group: :class:`str`
            :param group: The group ID determines which Attestation Service instances this
                Attestation Service can communicate with. This attribute was added
                in vSphere API 7.0.0.
            :type  cluster: :class:`str`
            :param cluster: The opaque string identifier of the cluster in which the
                Attestation Service is part of. This attribute was added in vSphere
                API 7.0.0.
            :type  trusted_ca: :class:`com.vmware.vcenter.trusted_infrastructure_client.X509CertChain`
            :param trusted_ca: The service's TLS certificate chain. This attribute was added in
                vSphere API 7.0.0.
            """
            self.host = host
            self.address = address
            self.group = group
            self.cluster = cluster
            self.trusted_ca = trusted_ca
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.attestation.info', {
            'host': type.IdType(resource_types='HostSystem'),
            'address': type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress'),
            'group': type.StringType(),
            'cluster': type.StringType(),
            'trusted_CA': type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'X509CertChain'),
        },
        Info,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Attestation.FilterSpec`` class contains the data necessary for
        identifying a Attestation Service. This class was added in vSphere API
        7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     hosts=None,
                     clusters=None,
                     address=None,
                     groups=None,
                    ):
            """
            :type  hosts: :class:`set` of :class:`str` or ``None``
            :param hosts: A set of host IDs by which to filter the services. This attribute
                was added in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
                If None, the services will not be filtered by the hosts on which
                they run.
            :type  clusters: :class:`set` of :class:`str` or ``None``
            :param clusters: A set of cluster IDs by which to filter the services. This
                attribute was added in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``ClusterComputeResource``.
                If None, the services will not be filtered by the clusters on which
                they run.
            :type  address: :class:`list` of :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress` or ``None``
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
                If None, the services will not be filtered by address.
            :type  groups: :class:`set` of :class:`str` or ``None``
            :param groups: The group IDs determines which Attestation Service instances this
                Attestation Service can communicate with. This attribute was added
                in vSphere API 7.0.0.
                If None, the services will not be filtered by groupId.
            """
            self.hosts = hosts
            self.clusters = clusters
            self.address = address
            self.groups = groups
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.attestation.filter_spec', {
            'hosts': type.OptionalType(type.SetType(type.IdType())),
            'clusters': type.OptionalType(type.SetType(type.IdType())),
            'address': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress'))),
            'groups': type.OptionalType(type.SetType(type.StringType())),
        },
        FilterSpec,
        False,
        None))



    def get(self,
            host,
            ):
        """
        Returns the connection info about the Attestation Service running on
        the specified host. This method was added in vSphere API 7.0.0.

        :type  host: :class:`str`
        :param host: \\\\@{link com.vmware.vcenter.Host} id.
            The parameter must be an identifier for the resource type:
            ``HostSystem``.
        :rtype: :class:`Attestation.Info`
        :return: The :class:`Attestation.Info` instance which contains the
            information necessary to connect to the Attestation Service.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if service's TLS certificate chain is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``host`` doesn't match to any Host.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if connection to ``host`` failed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``TrustedAdmin.ReadTrustedHosts``.
            * The resource ``HostSystem`` referenced by the parameter ``host``
              requires ``System.View``.
        """
        return self._invoke('get',
                            {
                            'host': host,
                            })

    def list(self,
             spec=None,
             projection=None,
             ):
        """
        Returns a list of the hosts running a Attestation Service matching the
        specified :class:`Attestation.FilterSpec`. This method was added in
        vSphere API 7.0.0.

        :type  spec: :class:`Attestation.FilterSpec` or ``None``
        :param spec: Return details about Attestation Services matching the filter.
            If {\\\\@term.unset} return all registered Attestation Services.
        :type  projection: :class:`Attestation.SummaryType` or ``None``
        :param projection: The type of the returned summary - brief, normal, or full.
            If {\\\\@term.unset} a normal projection will be used.
        :rtype: :class:`list` of :class:`Attestation.Summary`
        :return: List of :class:`Attestation.Summary` of Attestation Services.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the response data will exceed the message limit.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``TrustedAdmin.ReadTrustedHosts``.
            * The resource ``HostSystem`` referenced by the attribute
              :attr:`Attestation.FilterSpec.hosts` requires ``System.View``.
            * The resource ``ClusterComputeResource`` referenced by the
              attribute :attr:`Attestation.FilterSpec.clusters` requires
              ``System.View``.
        """
        return self._invoke('list',
                            {
                            'spec': spec,
                            'projection': projection,
                            })
class Kms(VapiInterface):
    """
    The ``Kms`` class contains information necessary to connect to the hosts
    running Key Provider Service. This class was added in vSphere API 7.0.0.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.kms'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _KmsStub)
        self._VAPI_OPERATION_IDS = {}

    class SummaryType(Enum):
        """
        The connection information could include the certificates or be a shorter
        summary. This enumeration was added in vSphere API 7.0.0.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FULL = None
        """
        The full connection information, including certificates. This class
        attribute was added in vSphere API 7.0.0.

        """
        NORMAL = None
        """
        A summary containing only the hostname, port, and the group which
        determines the Attestation Services this Key Provider Service can
        communicate with. This class attribute was added in vSphere API 7.0.0.

        """
        BRIEF = None
        """
        A brief summary, containing only the hostname for the Key Provider Service.
        This class attribute was added in vSphere API 7.0.0.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SummaryType` instance.
            """
            Enum.__init__(string)

    SummaryType._set_values([
        SummaryType('FULL'),
        SummaryType('NORMAL'),
        SummaryType('BRIEF'),
    ])
    SummaryType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.kms.summary_type',
        SummaryType))


    class Summary(VapiStruct):
        """
        The ``Kms.Summary`` class contains all the stored information about a Key
        Provider Service. This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'summary_type',
                {
                    'BRIEF' : [('host', True), ('address', True)],
                    'NORMAL' : [('host', True), ('address', True), ('group', True), ('cluster', True)],
                    'FULL' : [('host', True), ('address', True), ('group', True), ('cluster', True), ('trusted_CA', True)],
                }
            ),
        ]


        _canonical_to_pep_names = {
                                'trusted_CA': 'trusted_ca',
                                }

        def __init__(self,
                     summary_type=None,
                     host=None,
                     address=None,
                     group=None,
                     cluster=None,
                     trusted_ca=None,
                    ):
            """
            :type  summary_type: :class:`Kms.SummaryType`
            :param summary_type: Defines the verbosity of the summary. This attribute was added in
                vSphere API 7.0.0.
            :type  host: :class:`str`
            :param host: The trusted ESX on which the service runs. This attribute was added
                in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is one of :attr:`Kms.SummaryType.BRIEF`,
                :attr:`Kms.SummaryType.NORMAL`, or :attr:`Kms.SummaryType.FULL`.
            :type  address: :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress`
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is one of :attr:`Kms.SummaryType.BRIEF`,
                :attr:`Kms.SummaryType.NORMAL`, or :attr:`Kms.SummaryType.FULL`.
            :type  group: :class:`str`
            :param group: The group ID determines which Attestation Service instances this
                Key Provider Service can communicate with. This attribute was added
                in vSphere API 7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is one of :attr:`Kms.SummaryType.NORMAL` or
                :attr:`Kms.SummaryType.FULL`.
            :type  cluster: :class:`str`
            :param cluster: The opaque string identifier of the cluster in which the Key
                Provider Service is part of. This attribute was added in vSphere
                API 7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is one of :attr:`Kms.SummaryType.NORMAL` or
                :attr:`Kms.SummaryType.FULL`.
            :type  trusted_ca: :class:`com.vmware.vcenter.trusted_infrastructure_client.X509CertChain`
            :param trusted_ca: The service's TLS certificate chain. This attribute was added in
                vSphere API 7.0.0.
                This attribute is optional and it is only relevant when the value
                of ``summaryType`` is :attr:`Kms.SummaryType.FULL`.
            """
            self.summary_type = summary_type
            self.host = host
            self.address = address
            self.group = group
            self.cluster = cluster
            self.trusted_ca = trusted_ca
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.kms.summary', {
            'summary_type': type.ReferenceType(__name__, 'Kms.SummaryType'),
            'host': type.OptionalType(type.IdType()),
            'address': type.OptionalType(type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress')),
            'group': type.OptionalType(type.StringType()),
            'cluster': type.OptionalType(type.StringType()),
            'trusted_CA': type.OptionalType(type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'X509CertChain')),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Kms.Info`` class contains all the stored information about a Key
        Provider Service. This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'trusted_CA': 'trusted_ca',
                                }

        def __init__(self,
                     host=None,
                     address=None,
                     group=None,
                     cluster=None,
                     trusted_ca=None,
                    ):
            """
            :type  host: :class:`str`
            :param host: The trusted ESX on which the service runs. This attribute was added
                in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
            :type  address: :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress`
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
            :type  group: :class:`str`
            :param group: The group ID determines which Attestation Service instances this
                Key Provider Service can communicate with. This attribute was added
                in vSphere API 7.0.0.
            :type  cluster: :class:`str`
            :param cluster: The opaque string identifier of the cluster in which the Key
                Provider Service is part of. This attribute was added in vSphere
                API 7.0.0.
            :type  trusted_ca: :class:`com.vmware.vcenter.trusted_infrastructure_client.X509CertChain`
            :param trusted_ca: The service's TLS certificate chain. This attribute was added in
                vSphere API 7.0.0.
            """
            self.host = host
            self.address = address
            self.group = group
            self.cluster = cluster
            self.trusted_ca = trusted_ca
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.kms.info', {
            'host': type.IdType(resource_types='HostSystem'),
            'address': type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress'),
            'group': type.StringType(),
            'cluster': type.StringType(),
            'trusted_CA': type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'X509CertChain'),
        },
        Info,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Kms.FilterSpec`` class contains the data necessary for identifying a
        Key Provider Service. This class was added in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     hosts=None,
                     clusters=None,
                     address=None,
                     groups=None,
                    ):
            """
            :type  hosts: :class:`set` of :class:`str` or ``None``
            :param hosts: A set of host IDs by which to filter the services. This attribute
                was added in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
                If None, the services will not be filtered by the hosts on which
                they run.
            :type  clusters: :class:`set` of :class:`str` or ``None``
            :param clusters: A set of cluster IDs by which to filter the services. This
                attribute was added in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``ClusterComputeResource``.
                If None, the services will not be filtered by the clusters on which
                they run.
            :type  address: :class:`list` of :class:`com.vmware.vcenter.trusted_infrastructure_client.NetworkAddress` or ``None``
            :param address: The service's address. This attribute was added in vSphere API
                7.0.0.
                If None, the services will not be filtered by address.
            :type  groups: :class:`set` of :class:`str` or ``None``
            :param groups: The group determines reports issued by which Attestation Service
                instances this Key Provider Service can accept. This attribute was
                added in vSphere API 7.0.0.
                If None, the services will not be filtered by groupId.
            """
            self.hosts = hosts
            self.clusters = clusters
            self.address = address
            self.groups = groups
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.kms.filter_spec', {
            'hosts': type.OptionalType(type.SetType(type.IdType())),
            'clusters': type.OptionalType(type.SetType(type.IdType())),
            'address': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.trusted_infrastructure_client', 'NetworkAddress'))),
            'groups': type.OptionalType(type.SetType(type.StringType())),
        },
        FilterSpec,
        False,
        None))



    def get(self,
            host,
            ):
        """
        Returns the connection info about the Key Provider Service running on
        the specified host. This method was added in vSphere API 7.0.0.

        :type  host: :class:`str`
        :param host: \\\\@{link com.vmware.vcenter.Host} id.
            The parameter must be an identifier for the resource type:
            ``HostSystem``.
        :rtype: :class:`Kms.Info`
        :return: The :class:`Kms.Info` instance which contains the information
            necessary to connect to the Key Provider Service.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if service's TLS certificate chain is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``host`` doesn't match to any Host.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if connection to ``host`` failed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``TrustedAdmin.ReadTrustedHosts``.
            * The resource ``HostSystem`` referenced by the parameter ``host``
              requires ``System.View``.
        """
        return self._invoke('get',
                            {
                            'host': host,
                            })

    def list(self,
             spec=None,
             projection=None,
             ):
        """
        Returns a list of the hosts running a Key Provider Service matching the
        specified :class:`Kms.FilterSpec`. This method was added in vSphere API
        7.0.0.

        :type  spec: :class:`Kms.FilterSpec` or ``None``
        :param spec: Return details about Key Provider Services matching the filter.
            If {\\\\@term.unset} return all registered Key Provider Services.
        :type  projection: :class:`Kms.SummaryType` or ``None``
        :param projection: The type of the returned summary - brief, normal, or full.
            If {\\\\@term.unset} a normal projection will be used.
        :rtype: :class:`list` of :class:`Kms.Summary`
        :return: List of :class:`Kms.Summary` of Key Provider Services.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the response data will exceed the message limit.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``TrustedAdmin.ReadTrustedHosts``.
            * The resource ``HostSystem`` referenced by the attribute
              :attr:`Kms.FilterSpec.hosts` requires ``System.View``.
            * The resource ``ClusterComputeResource`` referenced by the
              attribute :attr:`Kms.FilterSpec.clusters` requires ``System.View``.
        """
        return self._invoke('list',
                            {
                            'spec': spec,
                            'projection': projection,
                            })
class _AttestationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'host': type.IdType(resource_types='HostSystem'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/trusted-infrastructure/trust-authority-hosts/{host}/attestation/',
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

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'spec': type.OptionalType(type.ReferenceType(__name__, 'Attestation.FilterSpec')),
            'projection': type.OptionalType(type.ReferenceType(__name__, 'Attestation.SummaryType')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/trusted-infrastructure/trust-authority-hosts/attestation',
            request_body_parameter='spec',
            path_variables={
            },
            query_parameters={
                'projection': 'projection',
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
                'output_type': type.ReferenceType(__name__, 'Attestation.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Attestation.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.attestation',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _KmsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'host': type.IdType(resource_types='HostSystem'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/trusted-infrastructure/trust-authority-hosts/{host}/kms/',
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

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'spec': type.OptionalType(type.ReferenceType(__name__, 'Kms.FilterSpec')),
            'projection': type.OptionalType(type.ReferenceType(__name__, 'Kms.SummaryType')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/trusted-infrastructure/trust-authority-hosts/kms',
            request_body_parameter='spec',
            path_variables={
            },
            query_parameters={
                'projection': 'projection',
            },
            dispatch_parameters={
                'action': 'query',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Kms.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Kms.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.trusted_infrastructure.trust_authority_hosts.kms',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Attestation': Attestation,
        'Kms': Kms,
    }

