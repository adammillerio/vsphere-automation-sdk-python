# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.namespace_management.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.namespace_management_client`` module provides classes
for managing Namespaces.

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

class SizingHint(Enum):
    """
    The ``SizingHint`` class determines the configuration of Kubernetes API
    server and the worker nodes. It also determines the default values
    associated with the maximum number of pods and services. Use
    :func:`ClusterSizeInfo.get` to get information associated with a
    ``SizingHint``.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    TINY = None
    """
    Cluster size of 'tiny'.

    """
    SMALL = None
    """
    Cluster size of 'small'.

    """
    MEDIUM = None
    """
    Cluster size of 'medium'.

    """
    LARGE = None
    """
    Cluster size of 'large'.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`SizingHint` instance.
        """
        Enum.__init__(string)

SizingHint._set_values([
    SizingHint('TINY'),
    SizingHint('SMALL'),
    SizingHint('MEDIUM'),
    SizingHint('LARGE'),
])
SizingHint._set_binding_type(type.EnumType(
    'com.vmware.vcenter.namespace_management.sizing_hint',
    SizingHint))




class Ipv4Cidr(VapiStruct):
    """
    The ``Ipv4Cidr`` class contains the specification for representing CIDR
    notation of IP range. For example, this can be used to represent 256 IP
    addresses using 10.10.10.0/24.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 address=None,
                 prefix=None,
                ):
        """
        :type  address: :class:`str`
        :param address: The IPv4 address.
        :type  prefix: :class:`long`
        :param prefix: The CIDR prefix.
        """
        self.address = address
        self.prefix = prefix
        VapiStruct.__init__(self)


Ipv4Cidr._set_binding_type(type.StructType(
    'com.vmware.vcenter.namespace_management.ipv4_cidr', {
        'address': type.StringType(),
        'prefix': type.IntegerType(),
    },
    Ipv4Cidr,
    False,
    None))



class Clusters(VapiInterface):
    """
    The ``Clusters`` class provides methods to enable and disable vSphere
    Namespaces on a vSphere cluster.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.clusters'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClustersStub)
        self._VAPI_OPERATION_IDS = {}

    class ConfigStatus(Enum):
        """
        The ``Clusters.ConfigStatus`` class describes the status of reaching the
        desired state configuration for the cluster.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        CONFIGURING = None
        """
        The Namespace configuration is being applied to the cluster.

        """
        REMOVING = None
        """
        The Namespace configuration is being removed from the cluster.

        """
        RUNNING = None
        """
        The cluster is configured correctly with the Namespace configuration.

        """
        ERROR = None
        """
        Failed to apply the Namespace configuration to the cluster, user
        intervention needed.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ConfigStatus` instance.
            """
            Enum.__init__(string)

    ConfigStatus._set_values([
        ConfigStatus('CONFIGURING'),
        ConfigStatus('REMOVING'),
        ConfigStatus('RUNNING'),
        ConfigStatus('ERROR'),
    ])
    ConfigStatus._set_binding_type(type.EnumType(
        'com.vmware.vcenter.namespace_management.clusters.config_status',
        ConfigStatus))


    class KubernetesStatus(Enum):
        """
        The ``Clusters.KubernetesStatus`` class describes the cluster's ability to
        deploy pods.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        READY = None
        """
        The cluster is able to accept pods.

        """
        WARNING = None
        """
        The cluster may be able to accept pods, but has warning messages.

        """
        ERROR = None
        """
        The cluster may not be able to accept pods and has error messages.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`KubernetesStatus` instance.
            """
            Enum.__init__(string)

    KubernetesStatus._set_values([
        KubernetesStatus('READY'),
        KubernetesStatus('WARNING'),
        KubernetesStatus('ERROR'),
    ])
    KubernetesStatus._set_binding_type(type.EnumType(
        'com.vmware.vcenter.namespace_management.clusters.kubernetes_status',
        KubernetesStatus))


    class NetworkProvider(Enum):
        """
        Identifies the network plugin that cluster networking functionalities for
        this vSphere Namespaces Cluster.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        NSXT_CONTAINER_PLUGIN = None
        """
        NSX-T Container Plugin.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`NetworkProvider` instance.
            """
            Enum.__init__(string)

    NetworkProvider._set_values([
        NetworkProvider('NSXT_CONTAINER_PLUGIN'),
    ])
    NetworkProvider._set_binding_type(type.EnumType(
        'com.vmware.vcenter.namespace_management.clusters.network_provider',
        NetworkProvider))


    class Message(VapiStruct):
        """
        The ``Clusters.Message`` class contains the information about the object
        configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     severity=None,
                     details=None,
                    ):
            """
            :type  severity: :class:`Clusters.Message.Severity`
            :param severity: Type of the message.
            :type  details: :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
            :param details: Details about the message.
                If None, message details are not required for taking actions.
            """
            self.severity = severity
            self.details = details
            VapiStruct.__init__(self)


        class Severity(Enum):
            """
            The ``Clusters.Message.Severity`` class represents the severity of the
            message.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            INFO = None
            """
            Informational message. This may be accompanied by vCenter event.

            """
            WARNING = None
            """
            Warning message. This may be accompanied by vCenter event.

            """
            ERROR = None
            """
            Error message. This is accompanied by vCenter event and/or alarm.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Severity` instance.
                """
                Enum.__init__(string)

        Severity._set_values([
            Severity('INFO'),
            Severity('WARNING'),
            Severity('ERROR'),
        ])
        Severity._set_binding_type(type.EnumType(
            'com.vmware.vcenter.namespace_management.clusters.message.severity',
            Severity))

    Message._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.message', {
            'severity': type.ReferenceType(__name__, 'Clusters.Message.Severity'),
            'details': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        Message,
        False,
        None))


    class Stats(VapiStruct):
        """
        The ``Clusters.Stats`` class contains the basic runtime statistics about a
        vSphere Namespaces-enabled cluster.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     cpu_used=None,
                     cpu_capacity=None,
                     memory_used=None,
                     memory_capacity=None,
                     storage_used=None,
                     storage_capacity=None,
                    ):
            """
            :type  cpu_used: :class:`long`
            :param cpu_used: Overall CPU usage of the cluster, in MHz. This is the sum of CPU
                usage across all worker nodes in the cluster.
            :type  cpu_capacity: :class:`long`
            :param cpu_capacity: Total CPU capacity in the cluster available for vSphere Namespaces,
                in MHz. This is the sum of CPU capacities from all worker nodes in
                the cluster.
            :type  memory_used: :class:`long`
            :param memory_used: Overall memory usage of the cluster, in mebibytes. This is the sum
                of memory usage across all worker nodes in the cluster.
            :type  memory_capacity: :class:`long`
            :param memory_capacity: Total memory capacity of the cluster available for vSphere
                Namespaces, in mebibytes. This is the sum of memory capacities from
                all worker nodesin the cluster.
            :type  storage_used: :class:`long`
            :param storage_used: Overall storage used by the cluster, in mebibytes. This is the sum
                of storage used across all worker nodes in the cluster.
            :type  storage_capacity: :class:`long`
            :param storage_capacity: Overall storage capacity of the cluster available for vSphere
                Namespaces, in mebibytes. This is the sum of total storage
                available from all worker nodes in the cluster.
            """
            self.cpu_used = cpu_used
            self.cpu_capacity = cpu_capacity
            self.memory_used = memory_used
            self.memory_capacity = memory_capacity
            self.storage_used = storage_used
            self.storage_capacity = storage_capacity
            VapiStruct.__init__(self)


    Stats._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.stats', {
            'cpu_used': type.IntegerType(),
            'cpu_capacity': type.IntegerType(),
            'memory_used': type.IntegerType(),
            'memory_capacity': type.IntegerType(),
            'storage_used': type.IntegerType(),
            'storage_capacity': type.IntegerType(),
        },
        Stats,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Clusters.Summary`` class contains the basic information about the
        cluster statistics and status related to vSphere Namespaces.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     cluster=None,
                     cluster_name=None,
                     stats=None,
                     config_status=None,
                     kubernetes_status=None,
                    ):
            """
            :type  cluster: :class:`str`
            :param cluster: Identifier for the cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``ClusterComputeResource``.
            :type  cluster_name: :class:`str`
            :param cluster_name: Name of the cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ClusterComputeResource.name``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``ClusterComputeResource.name``.
            :type  stats: :class:`Clusters.Stats`
            :param stats: Basic runtime statistics for the cluster.
            :type  config_status: :class:`Clusters.ConfigStatus`
            :param config_status: Current setting for ``Clusters.ConfigStatus``.
            :type  kubernetes_status: :class:`Clusters.KubernetesStatus`
            :param kubernetes_status: Current setting for ``Clusters.KubernetesStatus``.
            """
            self.cluster = cluster
            self.cluster_name = cluster_name
            self.stats = stats
            self.config_status = config_status
            self.kubernetes_status = kubernetes_status
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.summary', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'cluster_name': type.IdType(resource_types='ClusterComputeResource.name'),
            'stats': type.ReferenceType(__name__, 'Clusters.Stats'),
            'config_status': type.ReferenceType(__name__, 'Clusters.ConfigStatus'),
            'kubernetes_status': type.ReferenceType(__name__, 'Clusters.KubernetesStatus'),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Clusters.Info`` class contains detailed information about the cluster
        statistics and status related to vSphere Namespaces.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'network_provider',
                {
                    'NSXT_CONTAINER_PLUGIN' : [('ncp_cluster_network_info', True)],
                }
            ),
        ]


        _canonical_to_pep_names = {
                                'master_DNS': 'master_dns',
                                'worker_DNS': 'worker_dns',
                                'master_DNS_search_domains': 'master_dns_search_domains',
                                }

        def __init__(self,
                     stat_summary=None,
                     config_status=None,
                     messages=None,
                     kubernetes_status=None,
                     kubernetes_status_messages=None,
                     api_server_management_endpoint=None,
                     api_server_cluster_endpoint=None,
                     api_servers=None,
                     tls_management_endpoint_certificate=None,
                     tls_endpoint_certificate=None,
                     network_provider=None,
                     ncp_cluster_network_info=None,
                     service_cidr=None,
                     master_dns=None,
                     worker_dns=None,
                     master_dns_search_domains=None,
                     default_kubernetes_service_content_library=None,
                    ):
            """
            :type  stat_summary: :class:`Clusters.Stats`
            :param stat_summary: Basic runtime statistics for the cluster.
            :type  config_status: :class:`Clusters.ConfigStatus`
            :param config_status: Current setting for ``Clusters.ConfigStatus``.
            :type  messages: :class:`list` of :class:`Clusters.Message`
            :param messages: Current set of messages associated with the object.
            :type  kubernetes_status: :class:`Clusters.KubernetesStatus`
            :param kubernetes_status: Current setting for ``Clusters.KubernetesStatus``.
            :type  kubernetes_status_messages: :class:`list` of :class:`Clusters.Message`
            :param kubernetes_status_messages: Current set of messages associated with the object.
            :type  api_server_management_endpoint: :class:`str`
            :param api_server_management_endpoint: Kubernetes API Server IP address on the management network. This is
                a floating IP and assigned to one of the control plane VMs on the
                management network. This endpoint is used by vSphere components.
            :type  api_server_cluster_endpoint: :class:`str`
            :param api_server_cluster_endpoint: Kubernetes API Server IP address via cluster network. This is the
                IP address of the Kubernetes LoadBalancer type service fronting the
                apiservers. This endpoint is the one configured in kubeconfig after
                login, and used for most human and application interaction with
                Kubernetes.
            :type  api_servers: :class:`set` of :class:`str`
            :param api_servers: Identifier of the Kubernetes API servers. These are the IP
                addresses of the VM instances for the Kubernetes control plane on
                the management network.
            :type  tls_management_endpoint_certificate: :class:`str` or ``None``
            :param tls_management_endpoint_certificate: PEM-encoded x509 certificate used by TLS endpoint on Kubernetes API
                servers when accessed from the management network, e.g. from ESX
                servers or VCSA. This certificate is only valid for use with the
                apiServerManagementEndpoint.
            :type  tls_endpoint_certificate: :class:`str` or ``None``
            :param tls_endpoint_certificate: PEM-encoded x509 certificate used by TLS endpoint on Kubernetes API
                servers when accessed via the load balancer, e.g. devops user on
                corporate network. This certificate is only valid for use with the
                apiServerClusterEndpoint.
            :type  network_provider: :class:`Clusters.NetworkProvider`
            :param network_provider: The provider of cluster networking for this vSphere Namespaces
                cluster.
            :type  ncp_cluster_network_info: :class:`Clusters.NCPClusterNetworkInfo`
            :param ncp_cluster_network_info: Specification for the NSX Container Plugin cluster network.
                This attribute is optional and it is only relevant when the value
                of ``networkProvider`` is
                :attr:`Clusters.NetworkProvider.NSXT_CONTAINER_PLUGIN`.
            :type  service_cidr: :class:`Ipv4Cidr`
            :param service_cidr: CIDR block from which Kubernetes allocates service cluster IP
                addresses.
            :type  master_dns: :class:`list` of :class:`str` or ``None``
            :param master_dns: List of DNS server IP addresses to use on Kubernetes API server,
                specified in order of preference.
            :type  worker_dns: :class:`list` of :class:`str` or ``None``
            :param worker_dns: List of DNS server IP addresses to use for pods that execute on the
                worker nodes (which are native pods on ESXi hosts in the vSphere
                Namespaces Supervisor).
            :type  master_dns_search_domains: :class:`list` of :class:`str` or ``None``
            :param master_dns_search_domains: List of domains (for example "vmware.com") to be searched when
                trying to lookup a host name on Kubernetes API server, specified in
                order of preference.
            :type  default_kubernetes_service_content_library: :class:`str` or ``None``
            :param default_kubernetes_service_content_library: Identifier of the Content Library which holds the VM Images for
                vSphere Kubernetes Service. This Content Library should be
                subscribed to VMware's hosted vSphere Kubernetes Service
                Repository.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.Library``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.content.Library``.
            """
            self.stat_summary = stat_summary
            self.config_status = config_status
            self.messages = messages
            self.kubernetes_status = kubernetes_status
            self.kubernetes_status_messages = kubernetes_status_messages
            self.api_server_management_endpoint = api_server_management_endpoint
            self.api_server_cluster_endpoint = api_server_cluster_endpoint
            self.api_servers = api_servers
            self.tls_management_endpoint_certificate = tls_management_endpoint_certificate
            self.tls_endpoint_certificate = tls_endpoint_certificate
            self.network_provider = network_provider
            self.ncp_cluster_network_info = ncp_cluster_network_info
            self.service_cidr = service_cidr
            self.master_dns = master_dns
            self.worker_dns = worker_dns
            self.master_dns_search_domains = master_dns_search_domains
            self.default_kubernetes_service_content_library = default_kubernetes_service_content_library
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.info', {
            'stat_summary': type.ReferenceType(__name__, 'Clusters.Stats'),
            'config_status': type.ReferenceType(__name__, 'Clusters.ConfigStatus'),
            'messages': type.ListType(type.ReferenceType(__name__, 'Clusters.Message')),
            'kubernetes_status': type.ReferenceType(__name__, 'Clusters.KubernetesStatus'),
            'kubernetes_status_messages': type.ListType(type.ReferenceType(__name__, 'Clusters.Message')),
            'api_server_management_endpoint': type.StringType(),
            'api_server_cluster_endpoint': type.StringType(),
            'api_servers': type.SetType(type.StringType()),
            'tls_management_endpoint_certificate': type.OptionalType(type.StringType()),
            'tls_endpoint_certificate': type.OptionalType(type.StringType()),
            'network_provider': type.ReferenceType(__name__, 'Clusters.NetworkProvider'),
            'ncp_cluster_network_info': type.OptionalType(type.ReferenceType(__name__, 'Clusters.NCPClusterNetworkInfo')),
            'service_cidr': type.ReferenceType(__name__, 'Ipv4Cidr'),
            'master_DNS': type.OptionalType(type.ListType(type.StringType())),
            'worker_DNS': type.OptionalType(type.ListType(type.StringType())),
            'master_DNS_search_domains': type.OptionalType(type.ListType(type.StringType())),
            'default_kubernetes_service_content_library': type.OptionalType(type.IdType()),
        },
        Info,
        False,
        None))


    class Ipv4Range(VapiStruct):
        """
        The ``Clusters.Ipv4Range`` contains specification to configure multiple
        interfaces in IPv4. The range of IPv4 addresses is derived by incrementing
        the startingAddress to the specified addressCount. To use the object for a
        single IPv4 address specification, set addressCount to 1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     starting_address=None,
                     address_count=None,
                     subnet_mask=None,
                     gateway=None,
                    ):
            """
            :type  starting_address: :class:`str`
            :param starting_address: The IPv4 address denoting the start of the range.
            :type  address_count: :class:`long`
            :param address_count: The number of IP addresses in the range. Addresses are derived by
                incrementing :attr:`Clusters.Ipv4Range.starting_address`.
            :type  subnet_mask: :class:`str`
            :param subnet_mask: Subnet mask to be set.
            :type  gateway: :class:`str`
            :param gateway: The IPv4 address of the gateway associated with the range indicated
                by :attr:`Clusters.Ipv4Range.starting_address` and
                :attr:`Clusters.Ipv4Range.address_count`.
            """
            self.starting_address = starting_address
            self.address_count = address_count
            self.subnet_mask = subnet_mask
            self.gateway = gateway
            VapiStruct.__init__(self)


    Ipv4Range._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.ipv4_range', {
            'starting_address': type.StringType(),
            'address_count': type.IntegerType(),
            'subnet_mask': type.StringType(),
            'gateway': type.StringType(),
        },
        Ipv4Range,
        False,
        None))


    class NetworkSpec(VapiStruct):
        """
        The ``Clusters.NetworkSpec`` contains information related to network
        configuration for one or more interfaces.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'mode',
                {
                    'DHCP' : [('floating_IP', False)],
                    'STATICRANGE' : [('address_range', True)],
                }
            ),
        ]


        _canonical_to_pep_names = {
                                'floating_IP': 'floating_ip',
                                }

        def __init__(self,
                     floating_ip=None,
                     network=None,
                     mode=None,
                     address_range=None,
                    ):
            """
            :type  floating_ip: :class:`str` or ``None``
            :param floating_ip: Optionally specify the Floating IP used by the HA master cluster in
                the DHCP case.
                This attribute is optional and it is only relevant when the value
                of ``mode`` is :attr:`Clusters.NetworkSpec.Ipv4Mode.DHCP`.
            :type  network: :class:`str`
            :param network: Identifier for the network.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Network``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Network``.
            :type  mode: :class:`Clusters.NetworkSpec.Ipv4Mode`
            :param mode: The address assignment mode.
            :type  address_range: :class:`Clusters.Ipv4Range`
            :param address_range: Settings for the interfaces on the network.
                This attribute is optional and it is only relevant when the value
                of ``mode`` is :attr:`Clusters.NetworkSpec.Ipv4Mode.STATICRANGE`.
            """
            self.floating_ip = floating_ip
            self.network = network
            self.mode = mode
            self.address_range = address_range
            VapiStruct.__init__(self)


        class Ipv4Mode(Enum):
            """
            The ``Clusters.NetworkSpec.Ipv4Mode`` class defines various IPv4 address
            assignment modes.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            DHCP = None
            """
            The address is automatically assigned by a DHCP server.

            """
            STATICRANGE = None
            """
            The address is static.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Ipv4Mode` instance.
                """
                Enum.__init__(string)

        Ipv4Mode._set_values([
            Ipv4Mode('DHCP'),
            Ipv4Mode('STATICRANGE'),
        ])
        Ipv4Mode._set_binding_type(type.EnumType(
            'com.vmware.vcenter.namespace_management.clusters.network_spec.ipv4_mode',
            Ipv4Mode))

    NetworkSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.network_spec', {
            'floating_IP': type.OptionalType(type.StringType()),
            'network': type.IdType(resource_types='Network'),
            'mode': type.ReferenceType(__name__, 'Clusters.NetworkSpec.Ipv4Mode'),
            'address_range': type.OptionalType(type.ReferenceType(__name__, 'Clusters.Ipv4Range')),
        },
        NetworkSpec,
        False,
        None))


    class ImageRegistry(VapiStruct):
        """
        The ``Clusters.ImageRegistry`` class contains the specification required to
        configure container image registry endpoint.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     hostname=None,
                     port=None,
                    ):
            """
            :type  hostname: :class:`str`
            :param hostname: IP address or the hostname of container image registry.
            :type  port: :class:`long` or ``None``
            :param port: Port number of the container image registry.
                If None, defaults to 443.
            """
            self.hostname = hostname
            self.port = port
            VapiStruct.__init__(self)


    ImageRegistry._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.image_registry', {
            'hostname': type.StringType(),
            'port': type.OptionalType(type.IntegerType()),
        },
        ImageRegistry,
        False,
        None))


    class ImageStorageSpec(VapiStruct):
        """
        The ``Clusters.ImageStorageSpec`` class contains the specification required
        to configure storage used for container images.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     storage_policy=None,
                    ):
            """
            :type  storage_policy: :class:`str`
            :param storage_policy: Identifier of the storage policy.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``SpsStorageProfile``. When methods return a value of this class as
                a return value, the attribute will be an identifier for the
                resource type: ``SpsStorageProfile``.
            """
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)


    ImageStorageSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.image_storage_spec', {
            'storage_policy': type.IdType(resource_types='SpsStorageProfile'),
        },
        ImageStorageSpec,
        False,
        None))


    class NCPClusterNetworkInfo(VapiStruct):
        """
        The ``Clusters.NCPClusterNetworkInfo`` class contains the NSX Container
        Plugin-specific cluster networking configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     pod_cidrs=None,
                     ingress_cidrs=None,
                     egress_cidrs=None,
                     cluster_distributed_switch=None,
                     nsx_edge_cluster=None,
                     default_ingress_tls_certificate=None,
                    ):
            """
            :type  pod_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param pod_cidrs: CIDR blocks from which Kubernetes allocates pod IP addresses.
            :type  ingress_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param ingress_cidrs: CIDR blocks from which NSX assigns IP addresses for Kubernetes
                Ingresses and Kubernetes Services of type LoadBalancer.
            :type  egress_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param egress_cidrs: CIDR blocks from which NSX assigns IP addresses used for performing
                SNAT from container IPs to external IPs.
            :type  cluster_distributed_switch: :class:`str`
            :param cluster_distributed_switch: vSphere Distributed Switch used to connect this cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``vSphereDistributedSwitch``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``vSphereDistributedSwitch``.
            :type  nsx_edge_cluster: :class:`str`
            :param nsx_edge_cluster: NSX Edge Cluster to be used for Kubernetes Services of type
                LoadBalancer, Kubernetes Ingresses, and NSX SNAT.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``NSXEdgeCluster``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``NSXEdgeCluster``.
            :type  default_ingress_tls_certificate: :class:`str`
            :param default_ingress_tls_certificate: PEM-encoded x509 certificate used by NSX as a default fallback
                certificate for Kubernetes Ingress services.
            """
            self.pod_cidrs = pod_cidrs
            self.ingress_cidrs = ingress_cidrs
            self.egress_cidrs = egress_cidrs
            self.cluster_distributed_switch = cluster_distributed_switch
            self.nsx_edge_cluster = nsx_edge_cluster
            self.default_ingress_tls_certificate = default_ingress_tls_certificate
            VapiStruct.__init__(self)


    NCPClusterNetworkInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.NCP_cluster_network_info', {
            'pod_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'ingress_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'egress_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'cluster_distributed_switch': type.IdType(resource_types='vSphereDistributedSwitch'),
            'nsx_edge_cluster': type.IdType(resource_types='NSXEdgeCluster'),
            'default_ingress_tls_certificate': type.StringType(),
        },
        NCPClusterNetworkInfo,
        False,
        None))


    class NCPClusterNetworkEnableSpec(VapiStruct):
        """
        The ``Clusters.NCPClusterNetworkEnableSpec`` class encapsulates the NSX
        Container Plugin-specific cluster networking configuration parameters for
        the vSphere Namespaces Cluster Enable operation.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     pod_cidrs=None,
                     ingress_cidrs=None,
                     egress_cidrs=None,
                     cluster_distributed_switch=None,
                     nsx_edge_cluster=None,
                    ):
            """
            :type  pod_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param pod_cidrs: CIDR blocks from which Kubernetes allocates pod IP addresses. This
                range should not overlap with those in null,
                :attr:`Clusters.NCPClusterNetworkEnableSpec.ingress_cidrs`,
                :attr:`Clusters.NCPClusterNetworkEnableSpec.egress_cidrs`, or other
                services running in the datacenter. All Pod CIDR blocks must be of
                at least subnet size /23.
            :type  ingress_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param ingress_cidrs: CIDR blocks from which NSX assigns IP addresses for Kubernetes
                Ingresses and Kubernetes Services of type LoadBalancer. These
                ranges should not overlap with those in
                :attr:`Clusters.NCPClusterNetworkEnableSpec.pod_cidrs`, null,
                :attr:`Clusters.NCPClusterNetworkEnableSpec.egress_cidrs`, or other
                services running in the datacenter.
            :type  egress_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param egress_cidrs: CIDR blocks from which NSX assigns IP addresses used for performing
                SNAT from container IPs to external IPs. These ranges should not
                overlap with those in
                :attr:`Clusters.NCPClusterNetworkEnableSpec.pod_cidrs`, null,
                :attr:`Clusters.NCPClusterNetworkEnableSpec.ingress_cidrs`, or
                other services running in the datacenter.
            :type  cluster_distributed_switch: :class:`str` or ``None``
            :param cluster_distributed_switch: vSphere Distributed Switch used to connect this cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``vSphereDistributedSwitch``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``vSphereDistributedSwitch``.
                This field is required when configuring a cluster that uses NSX-T.
                If None and using NSXe, the system will choose a suitable vSphere
                Distributed Switch.
            :type  nsx_edge_cluster: :class:`str` or ``None``
            :param nsx_edge_cluster: NSX Edge Cluster to be used for Kubernetes Services of type
                LoadBalancer, Kubernetes Ingresses, and NSX SNAT.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``NSXEdgeCluster``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``NSXEdgeCluster``.
                This field is required when configuring a cluster that uses NSX-T.
                If None and using NSXe, the system will choose a suitable NSX Edge
                Cluster.
            """
            self.pod_cidrs = pod_cidrs
            self.ingress_cidrs = ingress_cidrs
            self.egress_cidrs = egress_cidrs
            self.cluster_distributed_switch = cluster_distributed_switch
            self.nsx_edge_cluster = nsx_edge_cluster
            VapiStruct.__init__(self)


    NCPClusterNetworkEnableSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.NCP_cluster_network_enable_spec', {
            'pod_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'ingress_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'egress_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'cluster_distributed_switch': type.OptionalType(type.IdType()),
            'nsx_edge_cluster': type.OptionalType(type.IdType()),
        },
        NCPClusterNetworkEnableSpec,
        False,
        None))


    class NCPClusterNetworkUpdateSpec(VapiStruct):
        """
        The ``Clusters.NCPClusterNetworkUpdateSpec`` class encapsulates the NSX
        Container Plugin-specific cluster networking configuration parameters for
        the vSphere Namespaces Cluster Update operation.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     pod_cidrs=None,
                     ingress_cidrs=None,
                     egress_cidrs=None,
                     default_ingress_tls_certificate=None,
                    ):
            """
            :type  pod_cidrs: :class:`list` of :class:`Ipv4Cidr` or ``None``
            :param pod_cidrs: CIDR blocks from which Kubernetes allocates pod IP addresses. This
                range should not overlap with those in null,
                :attr:`Clusters.NCPClusterNetworkUpdateSpec.ingress_cidrs`,
                :attr:`Clusters.NCPClusterNetworkUpdateSpec.egress_cidrs`, or other
                services running in the datacenter. An update operation only allows
                for addition of new CIDR blocks to the existing list. All Pod CIDR
                blocks must be of at least subnet size /23.
                If None, CIDRs from which Kubernetes allocates pod IP addresses
                will not be modified.
            :type  ingress_cidrs: :class:`list` of :class:`Ipv4Cidr` or ``None``
            :param ingress_cidrs: CIDR blocks from which NSX assigns IP addresses for Kubernetes
                Ingresses and Kubernetes Services of type LoadBalancer. These
                ranges should not overlap with those in
                :attr:`Clusters.NCPClusterNetworkUpdateSpec.pod_cidrs`, null,
                :attr:`Clusters.NCPClusterNetworkUpdateSpec.egress_cidrs`, or other
                services running in the datacenter. An update operation only allows
                for addition of new CIDR blocks to the existing list.
                If None, CIDRs from which Kubernetes allocates ingress IP addresses
                will not be modified.
            :type  egress_cidrs: :class:`list` of :class:`Ipv4Cidr` or ``None``
            :param egress_cidrs: CIDR blocks from which NSX assigns IP addresses used for performing
                SNAT from container IPs to external IPs. These ranges should not
                overlap with those in
                :attr:`Clusters.NCPClusterNetworkUpdateSpec.pod_cidrs`, null,
                :attr:`Clusters.NCPClusterNetworkUpdateSpec.ingress_cidrs`, or
                other services running in the datacenter. An update operation only
                allows for addition of new CIDR blocks to the existing list.
                If None, CIDR from which Kubernetes allocates egress IP addresses
                will not be modified.
            :type  default_ingress_tls_certificate: :class:`str` or ``None``
            :param default_ingress_tls_certificate: PEM-encoded x509 certificate used by NSX as a default fallback
                certificate for Kubernetes Ingress services.
            """
            self.pod_cidrs = pod_cidrs
            self.ingress_cidrs = ingress_cidrs
            self.egress_cidrs = egress_cidrs
            self.default_ingress_tls_certificate = default_ingress_tls_certificate
            VapiStruct.__init__(self)


    NCPClusterNetworkUpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.NCP_cluster_network_update_spec', {
            'pod_cidrs': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr'))),
            'ingress_cidrs': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr'))),
            'egress_cidrs': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr'))),
            'default_ingress_tls_certificate': type.OptionalType(type.StringType()),
        },
        NCPClusterNetworkUpdateSpec,
        False,
        None))


    class NCPClusterNetworkSetSpec(VapiStruct):
        """
        The ``Clusters.NCPClusterNetworkSetSpec`` class encapsulates the NSX
        Container Plugin-specific cluster networking configuration parameters for
        the vSphere Namespaces Cluster Set operation.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     pod_cidrs=None,
                     ingress_cidrs=None,
                     egress_cidrs=None,
                     default_ingress_tls_certificate=None,
                    ):
            """
            :type  pod_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param pod_cidrs: CIDR blocks from which Kubernetes allocates pod IP addresses. This
                range should not overlap with those in null,
                :attr:`Clusters.NCPClusterNetworkSetSpec.ingress_cidrs`,
                :attr:`Clusters.NCPClusterNetworkSetSpec.egress_cidrs`, or other
                services running in the datacenter. A set operation only allows for
                addition of new CIDR blocks to the existing list. All Pod CIDR
                blocks must be of at least subnet size /23.
            :type  ingress_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param ingress_cidrs: CIDR blocks from which NSX assigns IP addresses for Kubernetes
                Ingresses and Kubernetes Services of type LoadBalancer. These
                ranges should not overlap with those in
                :attr:`Clusters.NCPClusterNetworkSetSpec.pod_cidrs`, null,
                :attr:`Clusters.NCPClusterNetworkSetSpec.egress_cidrs`, or other
                services running in the datacenter. A set operation only allows for
                addition of new CIDR blocks to the existing list.
            :type  egress_cidrs: :class:`list` of :class:`Ipv4Cidr`
            :param egress_cidrs: CIDR blocks from which NSX assigns IP addresses used for performing
                SNAT from container IPs to external IPs. These ranges should not
                overlap with those in
                :attr:`Clusters.NCPClusterNetworkSetSpec.pod_cidrs`, null,
                :attr:`Clusters.NCPClusterNetworkSetSpec.ingress_cidrs`, or other
                services running in the datacenter. A set operation only allows for
                addition of new CIDR blocks to the existing list.
            :type  default_ingress_tls_certificate: :class:`str`
            :param default_ingress_tls_certificate: PEM-encoded x509 certificate used by NSX as a default fallback
                certificate for Kubernetes Ingress services.
            """
            self.pod_cidrs = pod_cidrs
            self.ingress_cidrs = ingress_cidrs
            self.egress_cidrs = egress_cidrs
            self.default_ingress_tls_certificate = default_ingress_tls_certificate
            VapiStruct.__init__(self)


    NCPClusterNetworkSetSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.NCP_cluster_network_set_spec', {
            'pod_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'ingress_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'egress_cidrs': type.ListType(type.ReferenceType(__name__, 'Ipv4Cidr')),
            'default_ingress_tls_certificate': type.StringType(),
        },
        NCPClusterNetworkSetSpec,
        False,
        None))


    class EnableSpec(VapiStruct):
        """
        The ``Clusters.EnableSpec`` class contains the specification required to
        enable vSphere Namespaces on a cluster.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'network_provider',
                {
                    'NSXT_CONTAINER_PLUGIN' : [('ncp_cluster_network_spec', True)],
                }
            ),
        ]


        _canonical_to_pep_names = {
                                'master_DNS': 'master_dns',
                                'worker_DNS': 'worker_dns',
                                'master_DNS_search_domains': 'master_dns_search_domains',
                                'master_NTP_servers': 'master_ntp_servers',
                                'Master_DNS_names': 'master_dns_names',
                                }

        def __init__(self,
                     size_hint=None,
                     service_cidr=None,
                     network_provider=None,
                     ncp_cluster_network_spec=None,
                     master_management_network=None,
                     master_dns=None,
                     worker_dns=None,
                     master_dns_search_domains=None,
                     master_ntp_servers=None,
                     master_storage_policy=None,
                     ephemeral_storage_policy=None,
                     login_banner=None,
                     master_dns_names=None,
                     image_storage=None,
                     default_image_registry=None,
                     default_image_repository=None,
                     default_kubernetes_service_content_library=None,
                    ):
            """
            :type  size_hint: :class:`SizingHint`
            :param size_hint: This affects the size and resources allocated to the Kubernetes API
                server and the worker nodes. It also affects the suggested default
                serviceCidr and podCidrs.
            :type  service_cidr: :class:`Ipv4Cidr`
            :param service_cidr: CIDR block from which Kubernetes allocates service cluster IP
                addresses. This range should not overlap with those in null, null,
                null, or other services running in the datacenter.
            :type  network_provider: :class:`Clusters.NetworkProvider`
            :param network_provider: The provider of cluster networking for this vSphere Namespaces
                cluster.
            :type  ncp_cluster_network_spec: :class:`Clusters.NCPClusterNetworkEnableSpec`
            :param ncp_cluster_network_spec: Specification for the NSX Container Plugin cluster network.
                This attribute is optional and it is only relevant when the value
                of ``networkProvider`` is
                :attr:`Clusters.NetworkProvider.NSXT_CONTAINER_PLUGIN`.
            :type  master_management_network: :class:`Clusters.NetworkSpec`
            :param master_management_network: Specification for the management network on Kubernetes API server.
                :attr:`Clusters.NetworkSpec.mode` must be STATICRANGE as we require
                Kubernetes API server to have a stable address.
            :type  master_dns: :class:`list` of :class:`str` or ``None``
            :param master_dns: List of DNS server IP addresses to use on Kubernetes API server,
                specified in order of preference.
                If None, no default DNS servers are set.
            :type  worker_dns: :class:`list` of :class:`str` or ``None``
            :param worker_dns: List of DNS server IP addresses to use on the worker nodes,
                specified in order of preference.
                If None, no default DNS servers are set.
            :type  master_dns_search_domains: :class:`list` of :class:`str` or ``None``
            :param master_dns_search_domains: List of domains (for example "vmware.com") to be searched when
                trying to lookup a host name on Kubernetes API server, specified in
                order of preference.
                If None, no default DNS search domains are set.
            :type  master_ntp_servers: :class:`list` of :class:`str` or ``None``
            :param master_ntp_servers: List of NTP server DNS names or IP addresses to use on Kubernetes
                API server, specified in order of preference.
                If None, VMware Tools based time synchronization is enabled.
            :type  master_storage_policy: :class:`str`
            :param master_storage_policy: Identifier of storage policy associated with Kubernetes API server.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``SpsStorageProfile``. When methods return a value of this class as
                a return value, the attribute will be an identifier for the
                resource type: ``SpsStorageProfile``.
            :type  ephemeral_storage_policy: :class:`str`
            :param ephemeral_storage_policy: Identifier of storage policy associated with ephemeral disks of all
                the Kubernetes Pods in the cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``SpsStorageProfile``. When methods return a value of this class as
                a return value, the attribute will be an identifier for the
                resource type: ``SpsStorageProfile``.
            :type  login_banner: :class:`str` or ``None``
            :param login_banner: Disclaimer to be displayed prior to login via the Kubectl plugin.
                If None, just skip it.
            :type  master_dns_names: :class:`list` of :class:`str` or ``None``
            :param master_dns_names: List of additional DNS names to associate with the Kubernetes API
                server. These DNS names are embedded in the TLS certificate
                presented by the API server.
                If None, no additional DNS names are embedded in the TLS
                certificate.
            :type  image_storage: :class:`Clusters.ImageStorageSpec`
            :param image_storage: Specification for storage to be used for container images.
            :type  default_image_registry: :class:`Clusters.ImageRegistry` or ``None``
            :param default_image_registry: Default image registry to use when Kubernetes Pod container
                specification does not specify it as part of the container image
                name.
                If None, defaults to Docker Hub.
            :type  default_image_repository: :class:`str` or ``None``
            :param default_image_repository: Default image repository to use when Kubernetes Pod container
                specification does not specify it as part of the container image
                name.
                If None, defaults to Docker Hub official repository in case of
                Docker Hub image registry, otherwise defaults to empty string.
            :type  default_kubernetes_service_content_library: :class:`str` or ``None``
            :param default_kubernetes_service_content_library: Identifier of the Content Library which holds the VM Images for
                vSphere Kubernetes Service. This Content Library should be
                subscribed to VMware's hosted vSphere Kubernetes Service
                Repository.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.Library``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.content.Library``.
                If None, the Content Library identifier will not be set.
            """
            self.size_hint = size_hint
            self.service_cidr = service_cidr
            self.network_provider = network_provider
            self.ncp_cluster_network_spec = ncp_cluster_network_spec
            self.master_management_network = master_management_network
            self.master_dns = master_dns
            self.worker_dns = worker_dns
            self.master_dns_search_domains = master_dns_search_domains
            self.master_ntp_servers = master_ntp_servers
            self.master_storage_policy = master_storage_policy
            self.ephemeral_storage_policy = ephemeral_storage_policy
            self.login_banner = login_banner
            self.master_dns_names = master_dns_names
            self.image_storage = image_storage
            self.default_image_registry = default_image_registry
            self.default_image_repository = default_image_repository
            self.default_kubernetes_service_content_library = default_kubernetes_service_content_library
            VapiStruct.__init__(self)


    EnableSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.enable_spec', {
            'size_hint': type.ReferenceType(__name__, 'SizingHint'),
            'service_cidr': type.ReferenceType(__name__, 'Ipv4Cidr'),
            'network_provider': type.ReferenceType(__name__, 'Clusters.NetworkProvider'),
            'ncp_cluster_network_spec': type.OptionalType(type.ReferenceType(__name__, 'Clusters.NCPClusterNetworkEnableSpec')),
            'master_management_network': type.ReferenceType(__name__, 'Clusters.NetworkSpec'),
            'master_DNS': type.OptionalType(type.ListType(type.StringType())),
            'worker_DNS': type.OptionalType(type.ListType(type.StringType())),
            'master_DNS_search_domains': type.OptionalType(type.ListType(type.StringType())),
            'master_NTP_servers': type.OptionalType(type.ListType(type.StringType())),
            'master_storage_policy': type.IdType(resource_types='SpsStorageProfile'),
            'ephemeral_storage_policy': type.IdType(resource_types='SpsStorageProfile'),
            'login_banner': type.OptionalType(type.StringType()),
            'Master_DNS_names': type.OptionalType(type.ListType(type.StringType())),
            'image_storage': type.ReferenceType(__name__, 'Clusters.ImageStorageSpec'),
            'default_image_registry': type.OptionalType(type.ReferenceType(__name__, 'Clusters.ImageRegistry')),
            'default_image_repository': type.OptionalType(type.StringType()),
            'default_kubernetes_service_content_library': type.OptionalType(type.IdType()),
        },
        EnableSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Clusters.UpdateSpec`` class contains the specification required to
        update the configuration on the Cluster. This class is applied partially,
        and only the specified fields will replace or modify their existing
        counterparts.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'network_provider',
                {
                    'NSXT_CONTAINER_PLUGIN' : [('ncp_cluster_network_spec', False)],
                }
            ),
        ]


        _canonical_to_pep_names = {
                                'master_DNS': 'master_dns',
                                'worker_DNS': 'worker_dns',
                                'master_DNS_search_domains': 'master_dns_search_domains',
                                'master_NTP_servers': 'master_ntp_servers',
                                }

        def __init__(self,
                     size_hint=None,
                     network_provider=None,
                     ncp_cluster_network_spec=None,
                     master_dns=None,
                     worker_dns=None,
                     master_dns_search_domains=None,
                     master_ntp_servers=None,
                     master_storage_policy=None,
                     ephemeral_storage_policy=None,
                     login_banner=None,
                     image_storage=None,
                     default_image_registry=None,
                     default_image_repository=None,
                     tls_endpoint_certificate=None,
                     default_kubernetes_service_content_library=None,
                    ):
            """
            :type  size_hint: :class:`SizingHint` or ``None``
            :param size_hint: This affects the size and resources allocated to the Kubernetes API
                server.
                If None, size and resources allocated to Kubernetes API server will
                not be modified.
            :type  network_provider: :class:`Clusters.NetworkProvider` or ``None``
            :param network_provider: The provider of cluster networking for this vSphere Namespaces
                cluster.
                If None, the existing effective cluster network specification will
                not be modified.
            :type  ncp_cluster_network_spec: :class:`Clusters.NCPClusterNetworkUpdateSpec` or ``None``
            :param ncp_cluster_network_spec: Updated specification for the cluster network configuration.
                If unset, existing effective value will not be modified If None,
                the existing effective cluster network specification will not be
                modified.
            :type  master_dns: :class:`list` of :class:`str` or ``None``
            :param master_dns: List of DNS server IP addresses to use on Kubernetes API server,
                specified in order of preference.
                If :class:`set`, DNS servers set on Kubernetes API server will be
                replaced. Otherwise, they will not be modified.
            :type  worker_dns: :class:`list` of :class:`str` or ``None``
            :param worker_dns: List of DNS server IP addresses to use on the worker nodes,
                specified in order of preference.
                If :class:`set`, DNS servers set on worker nodes will be replaced.
                Otherwise, they will not be modified.
            :type  master_dns_search_domains: :class:`list` of :class:`str` or ``None``
            :param master_dns_search_domains: List of domains (for example "vmware.com") to be searched when
                trying to lookup a host name on Kubernetes API server, specified in
                order of preference.
                If :class:`set`, DNS search domains on Kubernetes API server will
                be replaced. Otherwise, they will not be modified.
            :type  master_ntp_servers: :class:`list` of :class:`str` or ``None``
            :param master_ntp_servers: List of NTP server DNS names or IP addresses to use on Kubernetes
                API server, specified in order of preference.
                If :class:`set`, NTP servers on Kubernetes API server will be
                replaced. Otherwise, they will not be modified.
            :type  master_storage_policy: :class:`str` or ``None``
            :param master_storage_policy: Identifier of storage policy associated with Kubernetes API server.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``SpsStorageProfile``. When methods return a value of this class as
                a return value, the attribute will be an identifier for the
                resource type: ``SpsStorageProfile``.
                If None, storage policy associated with Kubernetes API server will
                not be modified.
            :type  ephemeral_storage_policy: :class:`str` or ``None``
            :param ephemeral_storage_policy: Identifier of storage policy associated with ephemeral disks of all
                the Kubernetes Pods in the cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``SpsStorageProfile``. When methods return a value of this class as
                a return value, the attribute will be an identifier for the
                resource type: ``SpsStorageProfile``.
                If None, storage policy associated with ephemeral disks of all the
                Kubernetes Pods will not be modified.
            :type  login_banner: :class:`str` or ``None``
            :param login_banner: Disclaimer to be displayed prior to login via the Kubectl plugin.
                If None, disclaimer to be displayed prior to login via the Kubectl
                plugin will not be modified.
            :type  image_storage: :class:`Clusters.ImageStorageSpec` or ``None``
            :param image_storage: Specification for storage to be used for container images.
                If None, configuration of storage used for container images is not
                modified.
            :type  default_image_registry: :class:`Clusters.ImageRegistry` or ``None``
            :param default_image_registry: Default image registry to use when Kubernetes Pod container
                specification does not specify it as part of the container image
                name.
                If None, default image registry will not be modified.
            :type  default_image_repository: :class:`str` or ``None``
            :param default_image_repository: Default image repository to use when Kubernetes Pod container
                specification does not specify it as part of the container image
                name.
                If None, default image repository will not be modified.
            :type  tls_endpoint_certificate: :class:`str` or ``None``
            :param tls_endpoint_certificate: Certificate issued for Kubernetes API Server. Certificate used must
                be created by signing the Certificate Signing Request obtained from
                null Because a ``CertificateSigningRequest`` is created on an
                existing Namespaces-enabled ``Cluster``, you must use the
                ``Clusters.UpdateSpec`` to specify this ``tlsEndpointCertificate``
                on an existing ``Cluster`` rather than during initially enabling
                Namespaces on a ``Cluster``.
                If None, Kubernetes API Server certificate will not be modified.
            :type  default_kubernetes_service_content_library: :class:`str` or ``None``
            :param default_kubernetes_service_content_library: Identifier of the Content Library which holds the VM Images for
                vSphere Kubernetes Service. This Content Library should be
                subscribed to VMware's hosted vSphere Kubernetes Service
                Repository. Modifying or clearing the Content Library identifier
                will not affect existing vSphere Kubernetes Service clusters.
                However, upgrades or scale-out of existing clusters may be affected
                if the new Content Library doesn't have the necessary VM Images.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.Library``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.content.Library``.
                If None, the Content Library identifier will not be modified.
            """
            self.size_hint = size_hint
            self.network_provider = network_provider
            self.ncp_cluster_network_spec = ncp_cluster_network_spec
            self.master_dns = master_dns
            self.worker_dns = worker_dns
            self.master_dns_search_domains = master_dns_search_domains
            self.master_ntp_servers = master_ntp_servers
            self.master_storage_policy = master_storage_policy
            self.ephemeral_storage_policy = ephemeral_storage_policy
            self.login_banner = login_banner
            self.image_storage = image_storage
            self.default_image_registry = default_image_registry
            self.default_image_repository = default_image_repository
            self.tls_endpoint_certificate = tls_endpoint_certificate
            self.default_kubernetes_service_content_library = default_kubernetes_service_content_library
            VapiStruct.__init__(self)


    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.update_spec', {
            'size_hint': type.OptionalType(type.ReferenceType(__name__, 'SizingHint')),
            'network_provider': type.OptionalType(type.ReferenceType(__name__, 'Clusters.NetworkProvider')),
            'ncp_cluster_network_spec': type.OptionalType(type.ReferenceType(__name__, 'Clusters.NCPClusterNetworkUpdateSpec')),
            'master_DNS': type.OptionalType(type.ListType(type.StringType())),
            'worker_DNS': type.OptionalType(type.ListType(type.StringType())),
            'master_DNS_search_domains': type.OptionalType(type.ListType(type.StringType())),
            'master_NTP_servers': type.OptionalType(type.ListType(type.StringType())),
            'master_storage_policy': type.OptionalType(type.IdType()),
            'ephemeral_storage_policy': type.OptionalType(type.IdType()),
            'login_banner': type.OptionalType(type.StringType()),
            'image_storage': type.OptionalType(type.ReferenceType(__name__, 'Clusters.ImageStorageSpec')),
            'default_image_registry': type.OptionalType(type.ReferenceType(__name__, 'Clusters.ImageRegistry')),
            'default_image_repository': type.OptionalType(type.StringType()),
            'tls_endpoint_certificate': type.OptionalType(type.StringType()),
            'default_kubernetes_service_content_library': type.OptionalType(type.IdType()),
        },
        UpdateSpec,
        False,
        None))


    class SetSpec(VapiStruct):
        """
        The ``Clusters.SetSpec`` class contains the specification required to set a
        new configuration on the Cluster. This class is applied in entirety,
        replacing the current specification fully.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'network_provider',
                {
                    'NSXT_CONTAINER_PLUGIN' : [('ncp_cluster_network_spec', True)],
                }
            ),
        ]


        _canonical_to_pep_names = {
                                'master_DNS': 'master_dns',
                                'worker_DNS': 'worker_dns',
                                'master_DNS_search_domains': 'master_dns_search_domains',
                                'master_NTP_servers': 'master_ntp_servers',
                                }

        def __init__(self,
                     size_hint=None,
                     network_provider=None,
                     ncp_cluster_network_spec=None,
                     master_dns=None,
                     worker_dns=None,
                     master_dns_search_domains=None,
                     master_ntp_servers=None,
                     master_storage_policy=None,
                     ephemeral_storage_policy=None,
                     login_banner=None,
                     image_storage=None,
                     default_image_registry=None,
                     default_image_repository=None,
                     default_kubernetes_service_content_library=None,
                    ):
            """
            :type  size_hint: :class:`SizingHint`
            :param size_hint: This affects the size and resources allocated to the Kubernetes API
                server.
            :type  network_provider: :class:`Clusters.NetworkProvider`
            :param network_provider: The provider of cluster networking for this vSphere Namespaces
                cluster.
            :type  ncp_cluster_network_spec: :class:`Clusters.NCPClusterNetworkSetSpec`
            :param ncp_cluster_network_spec: Specification for the NSX Container Plugin cluster network.
                This attribute is optional and it is only relevant when the value
                of ``networkProvider`` is
                :attr:`Clusters.NetworkProvider.NSXT_CONTAINER_PLUGIN`.
            :type  master_dns: :class:`list` of :class:`str` or ``None``
            :param master_dns: List of DNS server IP addresses to use on Kubernetes API server,
                specified in order of preference.
                If None, DNS servers set on Kubernetes API server will be cleared.
            :type  worker_dns: :class:`list` of :class:`str` or ``None``
            :param worker_dns: List of DNS server IP addresses to use on the worker nodes,
                specified in order of preference.
                If None, DNS servers set on worker nodes will be cleared.
            :type  master_dns_search_domains: :class:`list` of :class:`str` or ``None``
            :param master_dns_search_domains: List of domains (for example "vmware.com") to be searched when
                trying to lookup a host name on Kubernetes API server, specified in
                order of preference.
                If None, DNS search domains set on Kubernetes API server will be
                cleared.
            :type  master_ntp_servers: :class:`list` of :class:`str` or ``None``
            :param master_ntp_servers: List of NTP server DNS names or IP addresses to use on Kubernetes
                API server, specified in order of preference.
                If None, VMware Tools based time synchronization is enabled and any
                set NTP servers are cleared.
            :type  master_storage_policy: :class:`str`
            :param master_storage_policy: Identifier of storage policy associated with Kubernetes API server.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``SpsStorageProfile``. When methods return a value of this class as
                a return value, the attribute will be an identifier for the
                resource type: ``SpsStorageProfile``.
            :type  ephemeral_storage_policy: :class:`str`
            :param ephemeral_storage_policy: Identifier of storage policy associated with ephemeral disks of all
                the Kubernetes Pods in the cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``SpsStorageProfile``. When methods return a value of this class as
                a return value, the attribute will be an identifier for the
                resource type: ``SpsStorageProfile``.
            :type  login_banner: :class:`str` or ``None``
            :param login_banner: Disclaimer to be displayed prior to login via the Kubectl plugin.
                If None, disclaimer to be displayed prior to login via the Kubectl
                plugin will be cleared.
            :type  image_storage: :class:`Clusters.ImageStorageSpec`
            :param image_storage: Specification for storage to be used for container images.
            :type  default_image_registry: :class:`Clusters.ImageRegistry` or ``None``
            :param default_image_registry: Default image registry to use when Kubernetes Pod container
                specification does not specify it as part of the container image
                name.
                If None, default image registry will be set to Docker Hub.
            :type  default_image_repository: :class:`str` or ``None``
            :param default_image_repository: Default image repository to use when Kubernetes Pod container
                specification does not specify it as part of the container image
                name.
                If None, default image repository will be set to Docker Hub
                official repository in case of Docker Hub image registry, otherwise
                will be set to empty string.
            :type  default_kubernetes_service_content_library: :class:`str` or ``None``
            :param default_kubernetes_service_content_library: Identifier of the Content Library which holds the VM Images for
                vSphere Kubernetes Service. This Content Library should be
                subscribed to VMware's hosted vSphere Kubernetes Service
                Repository. Modifying or clearing the Content Library identifier
                will not affect existing vSphere Kubernetes Service clusters.
                However, upgrades or scale-out of existing clusters may be affected
                if the new Content Library doesn't have the necessary VM Images.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.Library``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.content.Library``.
                If None, the Content Library identifier will be cleared.
            """
            self.size_hint = size_hint
            self.network_provider = network_provider
            self.ncp_cluster_network_spec = ncp_cluster_network_spec
            self.master_dns = master_dns
            self.worker_dns = worker_dns
            self.master_dns_search_domains = master_dns_search_domains
            self.master_ntp_servers = master_ntp_servers
            self.master_storage_policy = master_storage_policy
            self.ephemeral_storage_policy = ephemeral_storage_policy
            self.login_banner = login_banner
            self.image_storage = image_storage
            self.default_image_registry = default_image_registry
            self.default_image_repository = default_image_repository
            self.default_kubernetes_service_content_library = default_kubernetes_service_content_library
            VapiStruct.__init__(self)


    SetSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.clusters.set_spec', {
            'size_hint': type.ReferenceType(__name__, 'SizingHint'),
            'network_provider': type.ReferenceType(__name__, 'Clusters.NetworkProvider'),
            'ncp_cluster_network_spec': type.OptionalType(type.ReferenceType(__name__, 'Clusters.NCPClusterNetworkSetSpec')),
            'master_DNS': type.OptionalType(type.ListType(type.StringType())),
            'worker_DNS': type.OptionalType(type.ListType(type.StringType())),
            'master_DNS_search_domains': type.OptionalType(type.ListType(type.StringType())),
            'master_NTP_servers': type.OptionalType(type.ListType(type.StringType())),
            'master_storage_policy': type.IdType(resource_types='SpsStorageProfile'),
            'ephemeral_storage_policy': type.IdType(resource_types='SpsStorageProfile'),
            'login_banner': type.OptionalType(type.StringType()),
            'image_storage': type.ReferenceType(__name__, 'Clusters.ImageStorageSpec'),
            'default_image_registry': type.OptionalType(type.ReferenceType(__name__, 'Clusters.ImageRegistry')),
            'default_image_repository': type.OptionalType(type.StringType()),
            'default_kubernetes_service_content_library': type.OptionalType(type.IdType()),
        },
        SetSpec,
        False,
        None))



    def enable(self,
               cluster,
               spec,
               ):
        """
        Enable vSphere Namespaces on the cluster. This operation sets up
        Kubernetes instance for the cluster along with worker nodes.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster on which vSphere Namespaces will be
            enabled.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`Clusters.EnableSpec`
        :param spec: Specification for setting up the Kubernetes API server and the
            worker nodes.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the cluster already has vSphere Namespaces enabled.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if resources/objects could not be located.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if ``spec`` contain any errors.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if the specified cluster is not licensed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have Namespaces.Manage privilege.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the specified cluster is not supported for vSphere Namespaces,
            the cluster's hosts do not have the required ESX version, or for
            any other incompatibilities.
        """
        return self._invoke('enable',
                            {
                            'cluster': cluster,
                            'spec': spec,
                            })

    def disable(self,
                cluster,
                ):
        """
        Disable vSphere Namespaces on the cluster. This operation tears down
        the Kubernetes instance and the worker nodes associated with vSphere
        Namespaces enabled cluster.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster for which vSphere Namespaces will be
            disabled.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if cluster could not be located.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have Namespaces.Manage privilege.
        """
        return self._invoke('disable',
                            {
                            'cluster': cluster,
                            })

    def get(self,
            cluster,
            ):
        """
        Returns information about a specific cluster.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster on which vSphere Namespaces are enabled.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`Clusters.Info`
        :return: Information about the desired state of the specified cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if cluster could not be located.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the specified cluster does not have vSphere Namespaces enabled.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })

    def list(self):
        """
        Returns information about all clusters on which vSphere Namespaces are
        enabled on this vCenter.


        :rtype: :class:`list` of :class:`Clusters.Summary`
        :return: List of summary of all clusters with vSphere Namespaces enabled.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('list', None)

    def set(self,
            cluster,
            spec,
            ):
        """
        Set a new configuration on the cluster object. The specified
        configuration is applied in entirety and will replace the current
        configuration fully.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster on which vSphere Namespaces is enabled.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`Clusters.SetSpec`
        :param spec: New specification for the cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if ``spec`` contain any errors.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if vSphere Namespaces is being disabled on this cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if cluster could not be located.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have Namespaces.Manage privilege.
        """
        return self._invoke('set',
                            {
                            'cluster': cluster,
                            'spec': spec,
                            })

    def update(self,
               cluster,
               spec,
               ):
        """
        Update configuration on the cluster object. The specified configuration
        is applied partially and None fields in ``spec`` will leave those parts
        of configuration as-is.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster on which vSphere Namespaces is enabled.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`Clusters.UpdateSpec`
        :param spec: New specification for the cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if ``spec`` contain any errors.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if vSphere Namespaces is being disabled on this cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if cluster could not be located.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have Namespaces.Manage privilege.
        """
        return self._invoke('update',
                            {
                            'cluster': cluster,
                            'spec': spec,
                            })

    def rotate_password(self,
                        cluster,
                        ):
        """
        Request a new root password for all control plane nodes in the cluster.
        This operation generates a new root password and configures every
        control plane node in the cluster to accept it for authentication.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster for which the password is being
            generated.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if cluster could not be located.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have Namespaces.Manage privilege.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the cluster is in the process of password rotation.
        """
        return self._invoke('rotate_password',
                            {
                            'cluster': cluster,
                            })
class HostsConfig(VapiInterface):
    """
    The ``Compatibility`` class provides methods to retrieve information about
    vSphere Namespaces support and licensing.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.hosts_config'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _HostsConfigStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``Compatibility`` class contains information about vSphere Namespaces
        support and licensing.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     namespaces_supported=None,
                     namespaces_licensed=None,
                    ):
            """
            :type  namespaces_supported: :class:`bool`
            :param namespaces_supported: True if vSphere Namespace feature is supported in this VC.
            :type  namespaces_licensed: :class:`bool`
            :param namespaces_licensed: True if vSphere Namespace feature is licensed on any hosts in this
                VC.
            """
            self.namespaces_supported = namespaces_supported
            self.namespaces_licensed = namespaces_licensed
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.hosts_config.info', {
            'namespaces_supported': type.BooleanType(),
            'namespaces_licensed': type.BooleanType(),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Returns support and licensing information about hosts under a VC.


        :rtype: :class:`HostsConfig.Info`
        :return: Compatibility structure containing information about vSphere
            Namespaces support and licensing.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('get', None)
class ClusterAvailableVersions(VapiInterface):
    """
    The {\\\\@name cluster-available-versions} class provides methods to
    retrieve available upgrade versions of WCP and detailed information about
    each upgrade.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.cluster_available_versions'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterAvailableVersionsStub)
        self._VAPI_OPERATION_IDS = {}

    class Summary(VapiStruct):
        """
        The ``ClusterAvailableVersions.Summary`` class contains the information
        about each available upgrade version.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     version=None,
                     name=None,
                     description=None,
                     release_date=None,
                     release_notes=None,
                    ):
            """
            :type  version: :class:`str`
            :param version: Version of the upgrade.
            :type  name: :class:`str`
            :param name: Name of the upgrade.
            :type  description: :class:`str`
            :param description: Description of the upgrade.
            :type  release_date: :class:`datetime.datetime`
            :param release_date: Release date of the upgrade.
            :type  release_notes: :class:`str`
            :param release_notes: Release details of the upgrade.
            """
            self.version = version
            self.name = name
            self.description = description
            self.release_date = release_date
            self.release_notes = release_notes
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.cluster_available_versions.summary', {
            'version': type.StringType(),
            'name': type.StringType(),
            'description': type.StringType(),
            'release_date': type.DateTimeType(),
            'release_notes': type.StringType(),
        },
        Summary,
        False,
        None))



    def list(self):
        """
        Get information about each available upgrade.


        :rtype: :class:`list` of :class:`ClusterAvailableVersions.Summary`
        :return: Information for each upgrade.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('list', None)
class ClusterCompatibility(VapiInterface):
    """
    The ``ClusterCompatibility`` class provides methods to get
    Namespace-related compatibility information for clusters in this vCenter.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.cluster_compatibility'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterCompatibilityStub)
        self._VAPI_OPERATION_IDS = {}

    class Summary(VapiStruct):
        """
        The ``ClusterCompatibility.Summary`` class contains the information about
        the compatibility of a cluster.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     cluster=None,
                     compatible=None,
                     incompatibility_reasons=None,
                    ):
            """
            :type  cluster: :class:`str`
            :param cluster: Identifier of the cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``ClusterComputeResource``.
            :type  compatible: :class:`bool`
            :param compatible: Compatibility of this cluster.
            :type  incompatibility_reasons: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param incompatibility_reasons: Reasons for incompatibility.
            """
            self.cluster = cluster
            self.compatible = compatible
            self.incompatibility_reasons = incompatibility_reasons
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.cluster_compatibility.summary', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'compatible': type.BooleanType(),
            'incompatibility_reasons': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``ClusterCompatibility.FilterSpec`` class contains attributes used to
        filter the results when listing clusters (see
        :func:`ClusterCompatibility.list`) and their compatibility information.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     compatible=None,
                    ):
            """
            :type  compatible: :class:`bool` or ``None``
            :param compatible: Compatibility criteria for matching the filter. If true, only
                clusters which are compatible for Namespaces match the filter. If
                false, all clusters match the filter.
                If None, both compatible and incompatible clusters match the
                filter.
            """
            self.compatible = compatible
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.cluster_compatibility.filter_spec', {
            'compatible': type.OptionalType(type.BooleanType()),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns Namespaces compatibility information for all clusters in
        vCenter matching the :class:`ClusterCompatibility.FilterSpec`. The
        result contains only visible (subject to permission checks) clusters.

        :type  filter: :class:`ClusterCompatibility.FilterSpec` or ``None``
        :param filter: Specification of matching clusters for which information should be
            returned.
            If None, the behavior is equivalent to a
            :class:`ClusterCompatibility.FilterSpec` with all attributes None
            which means all clusters match the filter.
        :rtype: :class:`list` of :class:`ClusterCompatibility.Summary`
        :return: Namespaces compatibility information for the clusters matching the
            the :class:`ClusterCompatibility.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            if the server reports an unknown internal error.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class ClusterSizeInfo(VapiInterface):
    """
    The {\\\\@name cluster-size-info} class provides methods to retrieve
    various sizes available for enabling Namespaces and information about each
    size.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.cluster_size_info'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterSizeInfoStub)
        self._VAPI_OPERATION_IDS = {}

    class VmInfo(VapiStruct):
        """
        The ``ClusterSizeInfo.VmInfo`` class contains the information about the
        configuration of the virtual machines which would be created for
        Namespaces.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     count=None,
                     cores_per_socket=None,
                     memory=None,
                     capacity=None,
                    ):
            """
            :type  count: :class:`long`
            :param count: Number of CPU cores.
            :type  cores_per_socket: :class:`long`
            :param cores_per_socket: Number of CPU cores per socket.
            :type  memory: :class:`long`
            :param memory: Memory size, in mebibytes.
            :type  capacity: :class:`long`
            :param capacity: Overall capacity of the disks in the virtual machine, in mebibytes.
            """
            self.count = count
            self.cores_per_socket = cores_per_socket
            self.memory = memory
            self.capacity = capacity
            VapiStruct.__init__(self)


    VmInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.cluster_size_info.vm_info', {
            'count': type.IntegerType(),
            'cores_per_socket': type.IntegerType(),
            'memory': type.IntegerType(),
            'capacity': type.IntegerType(),
        },
        VmInfo,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``ClusterSizeInfo.Info`` class contains the information about limits
        associated with a ``SizingHint``.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     num_supported_pods=None,
                     num_supported_services=None,
                     default_service_cidr=None,
                     default_pod_cidr=None,
                     master_vm_info=None,
                     worker_vm_info=None,
                    ):
            """
            :type  num_supported_pods: :class:`long`
            :param num_supported_pods: The maximum number of supported pods.
            :type  num_supported_services: :class:`long`
            :param num_supported_services: The maximum number of supported services.
            :type  default_service_cidr: :class:`Ipv4Cidr`
            :param default_service_cidr: Default CIDR range from which Kubernetes allocates service cluster
                IP addresses.
            :type  default_pod_cidr: :class:`Ipv4Cidr`
            :param default_pod_cidr: Default CIDR range from which Kubernetes allocates pod IP
                addresses.
            :type  master_vm_info: :class:`ClusterSizeInfo.VmInfo`
            :param master_vm_info: Information about Kubernetes API server virtual machine
                configuration.
            :type  worker_vm_info: :class:`ClusterSizeInfo.VmInfo` or ``None``
            :param worker_vm_info: Information about worker virtual machine configuration.
                If None, the configuration of the worker VM is not fixed.
            """
            self.num_supported_pods = num_supported_pods
            self.num_supported_services = num_supported_services
            self.default_service_cidr = default_service_cidr
            self.default_pod_cidr = default_pod_cidr
            self.master_vm_info = master_vm_info
            self.worker_vm_info = worker_vm_info
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.cluster_size_info.info', {
            'num_supported_pods': type.IntegerType(),
            'num_supported_services': type.IntegerType(),
            'default_service_cidr': type.ReferenceType(__name__, 'Ipv4Cidr'),
            'default_pod_cidr': type.ReferenceType(__name__, 'Ipv4Cidr'),
            'master_vm_info': type.ReferenceType(__name__, 'ClusterSizeInfo.VmInfo'),
            'worker_vm_info': type.OptionalType(type.ReferenceType(__name__, 'ClusterSizeInfo.VmInfo')),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Get information about the default values associated with various sizes.


        :rtype: :class:`dict` of :class:`SizingHint` and :class:`ClusterSizeInfo.Info`
        :return: Information for each size.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        """
        return self._invoke('get', None)
class DistributedSwitchCompatibility(VapiInterface):
    """
    The ``DistributedSwitchCompatibility`` class provides methods to get
    Namespaces compatibility information of Distributed Switches in this
    vCenter.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.distributed_switch_compatibility'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DistributedSwitchCompatibilityStub)
        self._VAPI_OPERATION_IDS = {}

    class Summary(VapiStruct):
        """
        The ``DistributedSwitchCompatibility.Summary`` class contains information
        about the compatibility of a vSphere Distributed Switch with the Namespaces
        feature.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     distributed_switch=None,
                     compatible=None,
                     incompatibility_reasons=None,
                    ):
            """
            :type  distributed_switch: :class:`str`
            :param distributed_switch: Identifier of the switch.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``vSphereDistributedSwitch``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``vSphereDistributedSwitch``.
            :type  compatible: :class:`bool`
            :param compatible: Compatibility of this switch with vSphere Namespaces.
            :type  incompatibility_reasons: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
            :param incompatibility_reasons: List of reasons for incompatibility.
                If None, this Distributed Switch is compatible.
            """
            self.distributed_switch = distributed_switch
            self.compatible = compatible
            self.incompatibility_reasons = incompatibility_reasons
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.distributed_switch_compatibility.summary', {
            'distributed_switch': type.IdType(resource_types='vSphereDistributedSwitch'),
            'compatible': type.BooleanType(),
            'incompatibility_reasons': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'))),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``DistributedSwitchCompatibility.FilterSpec`` class contains attributes
        used to filter the results when listing Distributed Switches (see
        :func:`DistributedSwitchCompatibility.list`) and their compatibility
        information.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     compatible=None,
                    ):
            """
            :type  compatible: :class:`bool` or ``None``
            :param compatible: Compatibility criteria for matching the filter. If true, only
                Distributed Switches which are compatible with vSphere Namespaces
                match the filter. If false, only Distributed Switches which are
                incompatible with vSphere Namespaces match the filter.
                If None, both compatible and incompatible Distributed Switches
                match the filter.
            """
            self.compatible = compatible
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.distributed_switch_compatibility.filter_spec', {
            'compatible': type.OptionalType(type.BooleanType()),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             cluster,
             filter=None,
             ):
        """
        Returns Namespaces compatibility information of Distributed Switches in
        vCenter associated with the vCenter cluster, matching the
        :class:`DistributedSwitchCompatibility.FilterSpec`.

        :type  cluster: :class:`str`
        :param cluster: Identifier of a vCenter Cluster. Only Distributed Switches
            associated with the vCenter Cluster will be considered by the
            filter.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  filter: :class:`DistributedSwitchCompatibility.FilterSpec` or ``None``
        :param filter: Specification of matching Distributed Switches for which
            information should be returned.
            If None, the behavior is equivalent to a
            :class:`DistributedSwitchCompatibility.FilterSpec` with all
            attributes None which means all Distributed Switches match the
            filter.
        :rtype: :class:`list` of :class:`DistributedSwitchCompatibility.Summary`
        :return: Namespaces compatibility information for Distributed Switches
            matching the the
            :class:`DistributedSwitchCompatibility.FilterSpec`.
        """
        return self._invoke('list',
                            {
                            'cluster': cluster,
                            'filter': filter,
                            })
class EdgeClusterCompatibility(VapiInterface):
    """
    The ``EdgeClusterCompatibility`` class provides methods to get Namespaces
    compatibility information of NSX Edge Clusters.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.edge_cluster_compatibility'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _EdgeClusterCompatibilityStub)
        self._VAPI_OPERATION_IDS = {}

    class Summary(VapiStruct):
        """
        The ``EdgeClusterCompatibility.Summary`` class contains information about
        an NSX-T Edge Cluster, including its compatibility with the vCenter
        Namespaces feature.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     edge_cluster=None,
                     display_name=None,
                     compatible=None,
                     incompatibility_reasons=None,
                    ):
            """
            :type  edge_cluster: :class:`str`
            :param edge_cluster: Identifier of the Edge Cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``NSXEdgeCluster``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``NSXEdgeCluster``.
            :type  display_name: :class:`str`
            :param display_name: Display name of the Edge Cluster.
            :type  compatible: :class:`bool`
            :param compatible: Compatibility of this Edge Cluster with Namespaces feature.
            :type  incompatibility_reasons: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
            :param incompatibility_reasons: List of reasons for incompatibility.
                If None, this Edge Cluster is compatible.
            """
            self.edge_cluster = edge_cluster
            self.display_name = display_name
            self.compatible = compatible
            self.incompatibility_reasons = incompatibility_reasons
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.edge_cluster_compatibility.summary', {
            'edge_cluster': type.IdType(resource_types='NSXEdgeCluster'),
            'display_name': type.StringType(),
            'compatible': type.BooleanType(),
            'incompatibility_reasons': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'))),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``EdgeClusterCompatibility.FilterSpec`` class contains attributes used
        to filter the results when listing Edge Clusters (see
        :func:`EdgeClusterCompatibility.list`) and their compatibility information.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     compatible=None,
                    ):
            """
            :type  compatible: :class:`bool` or ``None``
            :param compatible: Compatibility criteria for matching the filter. If true, only Edge
                Clusters which are compatible with vSphere Namespaces match the
                filter. If false, only Edge Clusters which are incompatible with
                vSphere Namespaces match the filter.
                If None, both compatible and incompatible Edge Clusters match the
                filter.
            """
            self.compatible = compatible
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.edge_cluster_compatibility.filter_spec', {
            'compatible': type.OptionalType(type.BooleanType()),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             cluster,
             distributed_switch,
             filter=None,
             ):
        """
        Returns Namespaces compatibility information of NSX-T Edge Clusters
        matching the :class:`EdgeClusterCompatibility.FilterSpec`.

        :type  cluster: :class:`str`
        :param cluster: Identifier of a vCenter Cluster. Only Edge Clusters that are
            associated with the particular vCenter Cluster will be considered
            by the filter.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  distributed_switch: :class:`str`
        :param distributed_switch: Identifier of a Distributed Switch. Only Edge Clusters that are
            associated with the particular Distributed Switch will be
            considered by the filter.
            The parameter must be an identifier for the resource type:
            ``vSphereDistributedSwitch``.
        :type  filter: :class:`EdgeClusterCompatibility.FilterSpec` or ``None``
        :param filter: Specification of matching Edge Clusters for which information
            should be returned.
            If None, the behavior is equivalent to a
            :class:`EdgeClusterCompatibility.FilterSpec` with all attributes
            None which means all Edge Clusters match the filter.
        :rtype: :class:`list` of :class:`EdgeClusterCompatibility.Summary`
        :return: List of summaries of Edge Clusters associated with the given
            vCenter Cluster and Distributed Switch matching the
            :class:`EdgeClusterCompatibility.FilterSpec`.
        """
        return self._invoke('list',
                            {
                            'cluster': cluster,
                            'distributed_switch': distributed_switch,
                            'filter': filter,
                            })
class SupportBundle(VapiInterface):
    """
    The ``SupportBundle`` class provides methods to retrieve the cluster's
    Namespaces-related support bundle download location.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.support_bundle'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SupportBundleStub)
        self._VAPI_OPERATION_IDS = {}

    class Token(VapiStruct):
        """
        The ``SupportBundle.Token`` class contains information about the token
        required in the HTTP GET request to generate the support bundle.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     token=None,
                     expiry=None,
                    ):
            """
            :type  token: :class:`str`
            :param token: A one-time, short-lived token required in the HTTP header of the
                request to the url. This token needs to be passed in as a header
                with the name "wcp-support-bundle-token".
            :type  expiry: :class:`str`
            :param expiry: Expiry time of the token
            """
            self.token = token
            self.expiry = expiry
            VapiStruct.__init__(self)


    Token._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.support_bundle.token', {
            'token': type.StringType(),
            'expiry': type.StringType(),
        },
        Token,
        False,
        None))


    class Location(VapiStruct):
        """
        The ``SupportBundle.Location`` class contains the URI location to download
        the per-cluster support bundle from, as well as a token required (as a
        header on the HTTP request) to get the bundle. The validity of the token is
        5 minutes. After the token expires, any attempt to call the URI with said
        token will fail.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     url=None,
                     wcp_support_bundle_token=None,
                    ):
            """
            :type  url: :class:`str`
            :param url: Support Bundle Download URL.
            :type  wcp_support_bundle_token: :class:`SupportBundle.Token`
            :param wcp_support_bundle_token: Information about the token required in the HTTP GET request to
                generate the support bundle.
            """
            self.url = url
            self.wcp_support_bundle_token = wcp_support_bundle_token
            VapiStruct.__init__(self)


    Location._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.support_bundle.location', {
            'url': type.StringType(),
            'wcp_support_bundle_token': type.ReferenceType(__name__, 'SupportBundle.Token'),
        },
        Location,
        False,
        None))



    def create(self,
               cluster,
               ):
        """
        Returns the location :class:`SupportBundle.Location` information for
        downloading the Namespaces-related support bundle for the specified
        cluster. 
        
         Retrieving a support bundle involves two steps: 
        
        * Step 1: Invoke method to provision a token and a URI.
        * Step 2: Make an HTTP GET request using URI and one time used token
          returned in step 1 to generate the support bundle and return it.
        
        There can only be one valid token per cluster at any given time. If
        this method is invoked again for the same cluster identifier while a
        token still valid, the API will return the same
        :class:`SupportBundle.Location` response. 
        
         The HTTP GET request will: 
        
        * return 401 (Not Authorized) if the download URL is recognized, but
          the token is invalid.
        * otherwise return 200 (OK), mark the token used (invalidating it for
          any future use), open a application/tar download stream for the client,
          and start the bundle process. As part of its work, the API will
          orchestrate support bundling on the worker nodes of a cluster. If a
          failure occurs during the collection of support bundle from worker
          node, the API will not abort the request, but will log a warning and
          move on to processing other worker nodes' bundles. The API will only
          abort its operation if the content of the stream has been corrupted.
          When the API has to abort its operation (and the response stream), it
          will not provide any indication of failures to the client. The client
          will need to verify validity of the resultant file based on the format
          specified in the response's Content-Disposition header.

        :type  cluster: :class:`str`
        :param cluster: Identifier of cluster for which the Namespaces-related support
            bundle should be generated.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`SupportBundle.Location`
        :return: the download location of the support bundle for the cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the specified cluster is not registered on this vCenter server.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('create',
                            {
                            'cluster': cluster,
                            })
class NamespaceResourceOptions(VapiInterface):
    """
    The ``NamespaceResourceOptions`` class provides methods to get the objects
    used to create and modify resource quotas on a namespace.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.namespace_management.namespace_resource_options'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NamespaceResourceOptionsStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``NamespaceResourceOptions.Info`` class contains the information about
        the objects used to set and update resource quota keys on a namespace.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     create_resource_quota_type=None,
                     update_resource_quota_type=None,
                    ):
            """
            :type  create_resource_quota_type: :class:`str`
            :param create_resource_quota_type: Identifier of the class used to set resource quotas on the
                namespace. See null and null.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.structure``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.structure``.
            :type  update_resource_quota_type: :class:`str`
            :param update_resource_quota_type: Identifier of the class used to update resource quotas on the
                namespace. See null.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.structure``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.structure``.
            """
            self.create_resource_quota_type = create_resource_quota_type
            self.update_resource_quota_type = update_resource_quota_type
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.namespace_management.namespace_resource_options.info', {
            'create_resource_quota_type': type.IdType(resource_types='com.vmware.vapi.structure'),
            'update_resource_quota_type': type.IdType(resource_types='com.vmware.vapi.structure'),
        },
        Info,
        False,
        None))



    def get(self,
            cluster,
            ):
        """
        Get the information about the objects used to set and update resource
        quota keys for version of Kubernetes running on {#link cluster}.

        :type  cluster: :class:`str`
        :param cluster: Identifier for the cluster hosting the namespace on which the
            resource quota needs to be set.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`NamespaceResourceOptions.Info`
        :return: Information about the structures representing the resource spec.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if cluster could not be located.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the specified cluster is not enabled for Namespaces.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })
class _ClustersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for enable operation
        enable_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.ReferenceType(__name__, 'Clusters.EnableSpec'),
        })
        enable_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        enable_input_value_validator_list = [
        ]
        enable_output_validator_list = [
        ]
        enable_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/namespace-management/clusters/{cluster}',
            request_body_parameter='spec',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'enable',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        # properties for disable operation
        disable_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        disable_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        disable_input_value_validator_list = [
        ]
        disable_output_validator_list = [
        ]
        disable_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/namespace-management/clusters/{cluster}',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'disable',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/clusters/{cluster}',
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

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/clusters',
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

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.ReferenceType(__name__, 'Clusters.SetSpec'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/vcenter/namespace-management/clusters/{cluster}',
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

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.ReferenceType(__name__, 'Clusters.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/namespace-management/clusters/{cluster}',
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

        # properties for rotate_password operation
        rotate_password_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        rotate_password_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        rotate_password_input_value_validator_list = [
        ]
        rotate_password_output_validator_list = [
        ]
        rotate_password_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/namespace-management/clusters/{cluster}',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'rotate_password',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        operations = {
            'enable': {
                'input_type': enable_input_type,
                'output_type': type.VoidType(),
                'errors': enable_error_dict,
                'input_value_validator_list': enable_input_value_validator_list,
                'output_validator_list': enable_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'disable': {
                'input_type': disable_input_type,
                'output_type': type.VoidType(),
                'errors': disable_error_dict,
                'input_value_validator_list': disable_input_value_validator_list,
                'output_validator_list': disable_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Clusters.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Clusters.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_value_validator_list': set_input_value_validator_list,
                'output_validator_list': set_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'rotate_password': {
                'input_type': rotate_password_input_type,
                'output_type': type.VoidType(),
                'errors': rotate_password_error_dict,
                'input_value_validator_list': rotate_password_input_value_validator_list,
                'output_validator_list': rotate_password_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'enable': enable_rest_metadata,
            'disable': disable_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'set': set_rest_metadata,
            'update': update_rest_metadata,
            'rotate_password': rotate_password_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.namespace_management.clusters',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _HostsConfigStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/capability',
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
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'HostsConfig.Info'),
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
            self, iface_name='com.vmware.vcenter.namespace_management.hosts_config',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ClusterAvailableVersionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/software/cluster-available-versions',
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'ClusterAvailableVersions.Summary')),
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
            self, iface_name='com.vmware.vcenter.namespace_management.cluster_available_versions',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ClusterCompatibilityStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'ClusterCompatibility.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/cluster-compatibility',
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'ClusterCompatibility.Summary')),
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
            self, iface_name='com.vmware.vcenter.namespace_management.cluster_compatibility',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ClusterSizeInfoStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/cluster-size-info',
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
            'get': {
                'input_type': get_input_type,
                'output_type': type.MapType(type.ReferenceType(__name__, 'SizingHint'), type.ReferenceType(__name__, 'ClusterSizeInfo.Info')),
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
            self, iface_name='com.vmware.vcenter.namespace_management.cluster_size_info',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _DistributedSwitchCompatibilityStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'filter': type.OptionalType(type.ReferenceType(__name__, 'DistributedSwitchCompatibility.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/distributed-switch-compatibility',
            path_variables={
            },
            query_parameters={
                'cluster': 'cluster',
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'DistributedSwitchCompatibility.Summary')),
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
            self, iface_name='com.vmware.vcenter.namespace_management.distributed_switch_compatibility',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _EdgeClusterCompatibilityStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'distributed_switch': type.IdType(resource_types='vSphereDistributedSwitch'),
            'filter': type.OptionalType(type.ReferenceType(__name__, 'EdgeClusterCompatibility.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/edge-cluster-compatibility',
            path_variables={
            },
            query_parameters={
                'cluster': 'cluster',
                'distributed_switch': 'distributed_switch',
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'EdgeClusterCompatibility.Summary')),
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
            self, iface_name='com.vmware.vcenter.namespace_management.edge_cluster_compatibility',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SupportBundleStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/namespace-management/clusters/{cluster}/support-bundle',
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

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType(__name__, 'SupportBundle.Location'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.namespace_management.support_bundle',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _NamespaceResourceOptionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/namespace-management/clusters/{cluster}/workload-resource-options',
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

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'NamespaceResourceOptions.Info'),
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
            self, iface_name='com.vmware.vcenter.namespace_management.namespace_resource_options',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Clusters': Clusters,
        'HostsConfig': HostsConfig,
        'ClusterAvailableVersions': ClusterAvailableVersions,
        'ClusterCompatibility': ClusterCompatibility,
        'ClusterSizeInfo': ClusterSizeInfo,
        'DistributedSwitchCompatibility': DistributedSwitchCompatibility,
        'EdgeClusterCompatibility': EdgeClusterCompatibility,
        'SupportBundle': SupportBundle,
        'NamespaceResourceOptions': NamespaceResourceOptions,
        'software': 'com.vmware.vcenter.namespace_management.software_client.StubFactory',
        'stats': 'com.vmware.vcenter.namespace_management.stats_client.StubFactory',
    }

