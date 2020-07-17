# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vm.guest.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.vm.guest_client`` module provides classes for dealing
with the guest operating system. This includes information about the state of
local file systems and network interfaces and methods to manipulate the guest
file system and processes.

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


class DnsAssignedValues(VapiStruct):
    """
    The {\\\\@name DnsAssignedValues) class describes values assigned by a
    Domain Name Server (DNS). This class was added in vSphere API 7.0.0.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 host_name=None,
                 domain_name=None,
                ):
        """
        :type  host_name: :class:`str`
        :param host_name: The host name portion of DNS name. For example, "esx01" part of
            esx01.example.com. This attribute was added in vSphere API 7.0.0.
        :type  domain_name: :class:`str`
        :param domain_name: The domain name portion of the DNS name. "example.com" part of
            esx01.example.com. This attribute was added in vSphere API 7.0.0.
        """
        self.host_name = host_name
        self.domain_name = domain_name
        VapiStruct.__init__(self)


DnsAssignedValues._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.guest.dns_assigned_values', {
        'host_name': type.StringType(),
        'domain_name': type.StringType(),
    },
    DnsAssignedValues,
    False,
    None))



class DnsConfigInfo(VapiStruct):
    """
    The ``DnsConfigInfo`` class describes the configuration of RFC 1034 DNS
    settings. This class was added in vSphere API 7.0.0.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 ip_addresses=None,
                 search_domains=None,
                ):
        """
        :type  ip_addresses: :class:`list` of :class:`str`
        :param ip_addresses: The IP addresses of the DNS servers in order of use. IPv4 addresses
            are specified using dotted decimal notation. For example,
            "192.0.2.1". IPv6 addresses are 128-bit addresses represented as
            eight fields of up to four hexadecimal digits. A colon separates
            each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The
            address can also consist of the symbol '::' to represent multiple
            16-bit groups of contiguous 0's only once in an address as
            described in RFC 2373. This attribute was added in vSphere API
            7.0.0.
        :type  search_domains: :class:`list` of :class:`str`
        :param search_domains: The domain in which to search for hosts, placed in order of
            preference. These are the domain name portion of the DNS names.
            This attribute was added in vSphere API 7.0.0.
        """
        self.ip_addresses = ip_addresses
        self.search_domains = search_domains
        VapiStruct.__init__(self)


DnsConfigInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.guest.dns_config_info', {
        'ip_addresses': type.ListType(type.StringType()),
        'search_domains': type.ListType(type.StringType()),
    },
    DnsConfigInfo,
    False,
    None))



class DhcpConfigInfo(VapiStruct):
    """
    The ``DhcpConfigInfo`` class specifies when Dynamic Host Configuration
    Protocol is enabled. This class was added in vSphere API 7.0.0.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 ipv4_enabled=None,
                 ipv6_enabled=None,
                ):
        """
        :type  ipv4_enabled: :class:`bool`
        :param ipv4_enabled: True if IPv4 DHCP is enabled, false otherwise. This attribute was
            added in vSphere API 7.0.0.
        :type  ipv6_enabled: :class:`bool`
        :param ipv6_enabled: True if IPv6 DHCP is enabled, false otherwise. This attribute was
            added in vSphere API 7.0.0.
        """
        self.ipv4_enabled = ipv4_enabled
        self.ipv6_enabled = ipv6_enabled
        VapiStruct.__init__(self)


DhcpConfigInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.guest.dhcp_config_info', {
        'ipv4_enabled': type.BooleanType(),
        'ipv6_enabled': type.BooleanType(),
    },
    DhcpConfigInfo,
    False,
    None))



class Customization(VapiInterface):
    """
    The ``Customization`` class provides methods to apply a customization
    specification to a virtual machine. This class was added in vSphere API
    7.0.0.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.vm.guest.customization'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CustomizationStub)
        self._VAPI_OPERATION_IDS = {}

    class SetSpec(VapiStruct):
        """
        The ``Customization.SetSpec`` class contains specification information that
        has to be applied to a virtual machine. This class was added in vSphere API
        7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     spec=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: The name of the customization specification that has be retrieved
                from the virtual center inventory and applied for the virtual
                machine. Either one of ``name`` or ``spec`` or none of them should
                be specified. This attribute was added in vSphere API 7.0.0.
                If None and ``spec`` is also None when executing
                :func:`Customization.set` operationg, then any pending
                customization for the virtual machine will be cleared.
            :type  spec: :class:`com.vmware.vcenter.guest_client.CustomizationSpec` or ``None``
            :param spec: The customization specification that has to be applied for the
                virtual machine. Either one of ``name`` or ``spec`` or none of them
                should be specified. This attribute was added in vSphere API 7.0.0.
                If None and ``name`` is also None when executing
                :func:`Customization.set` operationg, then any pending
                customization for the virtual machine will be cleared.
            """
            self.name = name
            self.spec = spec
            VapiStruct.__init__(self)


    SetSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.guest.customization.set_spec', {
            'name': type.OptionalType(type.StringType()),
            'spec': type.OptionalType(type.ReferenceType('com.vmware.vcenter.guest_client', 'CustomizationSpec')),
        },
        SetSpec,
        False,
        None))



    def set(self,
            vm,
            spec,
            ):
        """
        Applies a customization specification in ``spec`` on the virtual
        machine in ``vm``. This method only sets the specification settings for
        the virtual machine. The actual customization happens inside the guest
        when the virtual machine is powered on. If ``spec`` has None values,
        then any pending customization settings for the virtual machine are
        cleared. If there is a pending customization for the virtual machine
        and ``spec`` has valid content, then the existing customization setting
        will be overwritten with the new settings. This method was added in
        vSphere API 7.0.0.

        :type  vm: :class:`str`
        :param vm: The unique identifier of the virtual machine that needs to be
            customized.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Customization.SetSpec`
        :param spec: The customization settings to be applied to the guest operating
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the customization settings in ``spec`` are not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine ``vm`` is not in a powered off state.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a customization specification is not found with the unique name
            in ``spec``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the virtual machine ``vm`` is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('set',
                            {
                            'vm': vm,
                            'spec': spec,
                            })
class Identity(VapiInterface):
    """
    The ``Identity`` class provides methods for retrieving guest operating
    system identification information. This class was added in vSphere API 6.7.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.vm.guest.identity'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _IdentityStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``Identity.Info`` class contains information describing the guest
        operating system identification. This class was added in vSphere API 6.7.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     family=None,
                     full_name=None,
                     host_name=None,
                     ip_address=None,
                    ):
            """
            :type  name: :class:`com.vmware.vcenter.vm_client.GuestOS`
            :param name: Guest operating system identifier (short name). This attribute was
                added in vSphere API 6.7.
            :type  family: :class:`com.vmware.vcenter.vm_client.GuestOSFamily`
            :param family: Guest operating system family. This attribute was added in vSphere
                API 6.7.
            :type  full_name: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param full_name: Guest operating system full name. This attribute was added in
                vSphere API 6.7.
            :type  host_name: :class:`str`
            :param host_name: Hostname of the guest operating system. This attribute was added in
                vSphere API 6.7.
            :type  ip_address: :class:`str` or ``None``
            :param ip_address: IP address assigned by the guest operating system. This attribute
                was added in vSphere API 6.7.
                If None the guest does not have an IP address.
            """
            self.name = name
            self.family = family
            self.full_name = full_name
            self.host_name = host_name
            self.ip_address = ip_address
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.guest.identity.info', {
            'name': type.ReferenceType('com.vmware.vcenter.vm_client', 'GuestOS'),
            'family': type.ReferenceType('com.vmware.vcenter.vm_client', 'GuestOSFamily'),
            'full_name': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'host_name': type.StringType(),
            'ip_address': type.OptionalType(type.StringType()),
        },
        Info,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Return information about the guest. This method was added in vSphere
        API 6.7.

        :type  vm: :class:`str`
        :param vm: Identifier of the virtual machine.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`Identity.Info`
        :return: guest identification information.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if VMware Tools is not running.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if VMware Tools has not provided any data.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })
class LocalFilesystem(VapiInterface):
    """
    The ``LocalFilesystem`` class provides methods for retrieving information
    about the guest operating system local file systems. This class was added
    in vSphere API 6.7.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.vm.guest.local_filesystem'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LocalFilesystemStub)
        self._VAPI_OPERATION_IDS = {}

    class VirtualDiskMapping(VapiStruct):
        """
        Describes the virtual disk backing a local guest disk. This class was added
        in vSphere API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     disk=None,
                    ):
            """
            :type  disk: :class:`str`
            :param disk: The virtual disk. This attribute was added in vSphere API 7.0.0.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
            """
            self.disk = disk
            VapiStruct.__init__(self)


    VirtualDiskMapping._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.guest.local_filesystem.virtual_disk_mapping', {
            'disk': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Disk'),
        },
        VirtualDiskMapping,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``LocalFilesystem.Info`` class contains information about a local file
        system configured in the guest operating system. This class was added in
        vSphere API 6.7.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     capacity=None,
                     free_space=None,
                     filesystem=None,
                     mappings=None,
                    ):
            """
            :type  capacity: :class:`long`
            :param capacity: Total capacity of the file system, in bytes. This attribute was
                added in vSphere API 6.7.
            :type  free_space: :class:`long`
            :param free_space: Free space on the file system, in bytes. This attribute was added
                in vSphere API 6.7.
            :type  filesystem: :class:`str` or ``None``
            :param filesystem: Filesystem type, if known. For example, ext3 or NTFS. This
                attribute was added in vSphere API 7.0.0.
                :class:`set` if VMware Tools reports a value.
            :type  mappings: :class:`list` of :class:`LocalFilesystem.VirtualDiskMapping`
            :param mappings: VirtualDisks backing the guest partition, if known. This attribute
                was added in vSphere API 7.0.0.
                This attribute is optional because it was added in a newer version
                than its parent node.
            """
            self.capacity = capacity
            self.free_space = free_space
            self.filesystem = filesystem
            self.mappings = mappings
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.guest.local_filesystem.info', {
            'capacity': type.IntegerType(),
            'free_space': type.IntegerType(),
            'filesystem': type.OptionalType(type.StringType()),
            'mappings': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'LocalFilesystem.VirtualDiskMapping'))),
        },
        Info,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Returns details of the local file systems in the guest operating
        system. This method was added in vSphere API 6.7.

        :type  vm: :class:`str`
        :param vm: Identifier of the virtual machine.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`dict` of :class:`str` and :class:`LocalFilesystem.Info`
        :return: Information about the local file systems configured in the guest
            operating system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if VMware Tools is not running.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if VMware Tools has not provided any data.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })
class Networking(VapiInterface):
    """
    The ``Networking`` class provides methods for retrieving guest operating
    system network information. This class was added in vSphere API 7.0.0.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.vm.guest.networking'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NetworkingStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``Networking.Info`` class contains information about networking as
        configured in the guest operating system. This class was added in vSphere
        API 7.0.0.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     dns_values=None,
                     dns=None,
                    ):
            """
            :type  dns_values: :class:`DnsAssignedValues` or ``None``
            :param dns_values: Client DNS values. Data assigned by DNS. This attribute was added
                in vSphere API 7.0.0.
                If None no DNS assigned value exists.
            :type  dns: :class:`DnsConfigInfo` or ``None``
            :param dns: Client DNS configuration. How DNS queries are resolved. This
                attribute was added in vSphere API 7.0.0.
                If None no DNS assigned value exists.
            """
            self.dns_values = dns_values
            self.dns = dns
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.guest.networking.info', {
            'dns_values': type.OptionalType(type.ReferenceType(__name__, 'DnsAssignedValues')),
            'dns': type.OptionalType(type.ReferenceType(__name__, 'DnsConfigInfo')),
        },
        Info,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Returns information about the network configuration in the guest
        operating system. This method was added in vSphere API 7.0.0.

        :type  vm: :class:`str`
        :param vm: Virtual machine ID
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`Networking.Info`
        :return: Information about the networking configuration in the guest
            operating system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if VMware Tools is not running.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })
class Power(VapiInterface):
    """
    The ``Power`` class provides methods for managing the guest operating
    system power state of a virtual machine. This class was added in vSphere
    API 6.7.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.vm.guest.power'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PowerStub)
        self._VAPI_OPERATION_IDS = {}

    class State(Enum):
        """
        Possible guest power states. This enumeration was added in vSphere API 6.7.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        RUNNING = None
        """
        The guest OS is running. This class attribute was added in vSphere API 6.7.

        """
        SHUTTING_DOWN = None
        """
        The guest OS is shutting down. This class attribute was added in vSphere
        API 6.7.

        """
        RESETTING = None
        """
        The guest OS is resetting. This class attribute was added in vSphere API
        6.7.

        """
        STANDBY = None
        """
        The guest OS is in standby. This class attribute was added in vSphere API
        6.7.

        """
        NOT_RUNNING = None
        """
        The guest OS is not running. This class attribute was added in vSphere API
        6.7.

        """
        UNAVAILABLE = None
        """
        The guest OS power state is unknown. This class attribute was added in
        vSphere API 6.7.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`State` instance.
            """
            Enum.__init__(string)

    State._set_values([
        State('RUNNING'),
        State('SHUTTING_DOWN'),
        State('RESETTING'),
        State('STANDBY'),
        State('NOT_RUNNING'),
        State('UNAVAILABLE'),
    ])
    State._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.guest.power.state',
        State))


    class Info(VapiStruct):
        """
        Information about the guest operating system power state. This class was
        added in vSphere API 6.7.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     state=None,
                     operations_ready=None,
                    ):
            """
            :type  state: :class:`Power.State`
            :param state: The power state of the guest operating system. This attribute was
                added in vSphere API 6.7.
            :type  operations_ready: :class:`bool`
            :param operations_ready: Flag indicating if the virtual machine is ready to process soft
                power operations. This attribute was added in vSphere API 6.7.
            """
            self.state = state
            self.operations_ready = operations_ready
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.guest.power.info', {
            'state': type.ReferenceType(__name__, 'Power.State'),
            'operations_ready': type.BooleanType(),
        },
        Info,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Returns information about the guest operating system power state. This
        method was added in vSphere API 6.7.

        :type  vm: :class:`str`
        :param vm: Identifier of the virtual machine.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`Power.Info`
        :return: Guest OS powerstate information.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })

    def shutdown(self,
                 vm,
                 ):
        """
        Issues a request to the guest operating system asking it to perform a
        clean shutdown of all services. This request returns immediately and
        does not wait for the guest operating system to complete the operation.
        This method was added in vSphere API 6.7.

        :type  vm: :class:`str`
        :param vm: Identifier of the virtual machine.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if VMware Tools is not running.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the virtual machine does not support being powered on (e.g.
            marked as a template, serving as a fault-tolerance secondary
            virtual machine).
        """
        return self._invoke('shutdown',
                            {
                            'vm': vm,
                            })

    def reboot(self,
               vm,
               ):
        """
        Issues a request to the guest operating system asking it to perform a
        reboot. This request returns immediately and does not wait for the
        guest operating system to complete the operation. This method was added
        in vSphere API 6.7.

        :type  vm: :class:`str`
        :param vm: Identifier of the virtual machine.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if VMware Tools is not running.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the virtual machine does not support being powered on (e.g.
            marked as a template, serving as a fault-tolerance secondary
            virtual machine).
        """
        return self._invoke('reboot',
                            {
                            'vm': vm,
                            })

    def standby(self,
                vm,
                ):
        """
        Issues a request to the guest operating system asking it to perform a
        suspend operation. This method was added in vSphere API 6.7.

        :type  vm: :class:`str`
        :param vm: Identifier of the virtual machine.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual machine is suspended.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if VMware Tools is not running.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the virtual machine does not support being powered on (e.g.
            marked as a template, serving as a fault-tolerance secondary
            virtual machine).
        """
        return self._invoke('standby',
                            {
                            'vm': vm,
                            })
class _CustomizationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Customization.SetSpec'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
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
            url_template='/vcenter/vm/{vm}/guest/customization',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_value_validator_list': set_input_value_validator_list,
                'output_validator_list': set_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'set': set_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.guest.customization',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _IdentityStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/guest/identity',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Identity.Info'),
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
            self, iface_name='com.vmware.vcenter.vm.guest.identity',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _LocalFilesystemStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/guest/local-filesystem',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.MapType(type.StringType(), type.ReferenceType(__name__, 'LocalFilesystem.Info')),
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
            self, iface_name='com.vmware.vcenter.vm.guest.local_filesystem',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _NetworkingStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/guest/networking',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Networking.Info'),
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
            self, iface_name='com.vmware.vcenter.vm.guest.networking',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PowerStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/guest/power',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for shutdown operation
        shutdown_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        shutdown_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        shutdown_input_value_validator_list = [
        ]
        shutdown_output_validator_list = [
        ]
        shutdown_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/guest/power',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for reboot operation
        reboot_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        reboot_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        reboot_input_value_validator_list = [
        ]
        reboot_output_validator_list = [
        ]
        reboot_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/guest/power',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for standby operation
        standby_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        standby_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        standby_input_value_validator_list = [
        ]
        standby_output_validator_list = [
        ]
        standby_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/guest/power',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Power.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'shutdown': {
                'input_type': shutdown_input_type,
                'output_type': type.VoidType(),
                'errors': shutdown_error_dict,
                'input_value_validator_list': shutdown_input_value_validator_list,
                'output_validator_list': shutdown_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reboot': {
                'input_type': reboot_input_type,
                'output_type': type.VoidType(),
                'errors': reboot_error_dict,
                'input_value_validator_list': reboot_input_value_validator_list,
                'output_validator_list': reboot_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'standby': {
                'input_type': standby_input_type,
                'output_type': type.VoidType(),
                'errors': standby_error_dict,
                'input_value_validator_list': standby_input_value_validator_list,
                'output_validator_list': standby_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'shutdown': shutdown_rest_metadata,
            'reboot': reboot_rest_metadata,
            'standby': standby_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.guest.power',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Customization': Customization,
        'Identity': Identity,
        'LocalFilesystem': LocalFilesystem,
        'Networking': Networking,
        'Power': Power,
        'networking': 'com.vmware.vcenter.vm.guest.networking_client.StubFactory',
    }

