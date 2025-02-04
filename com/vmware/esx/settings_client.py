# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.settings.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.settings_client`` module provides classes to manage ESX
settings.

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

class ComplianceImpact(Enum):
    """
    The ``ComplianceImpact`` class contains information about the impact of
    applying the target state in case of non compliance.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    NO_IMPACT = None
    """
    Host has no impact.

    """
    MAINTENANCE_MODE_REQUIRED = None
    """
    Host requires maintenance mode to reach this target state.

    """
    REBOOT_REQUIRED = None
    """
    Host requires reboot to reach this target state.

    """
    UNKNOWN = None
    """
    Impact is unknown.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`ComplianceImpact` instance.
        """
        Enum.__init__(string)

ComplianceImpact._set_values([
    ComplianceImpact('NO_IMPACT'),
    ComplianceImpact('MAINTENANCE_MODE_REQUIRED'),
    ComplianceImpact('REBOOT_REQUIRED'),
    ComplianceImpact('UNKNOWN'),
])
ComplianceImpact._set_binding_type(type.EnumType(
    'com.vmware.esx.settings.compliance_impact',
    ComplianceImpact))



class ComplianceStatus(Enum):
    """
    The ``ComplianceStatus`` class contains the possible different status of
    compliance with respect to target version.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    COMPLIANT = None
    """
    Target version is same as current version.

    """
    NON_COMPLIANT = None
    """
    Target version is greater than current version.

    """
    INCOMPATIBLE = None
    """
    Target state cannot be applied due to conflict or missing dependencies or
    the target state is lesser than the current version.

    """
    UNAVAILABLE = None
    """
    Drift check failed due to unknown error or check hasn't happened yet and
    results are not available.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`ComplianceStatus` instance.
        """
        Enum.__init__(string)

ComplianceStatus._set_values([
    ComplianceStatus('COMPLIANT'),
    ComplianceStatus('NON_COMPLIANT'),
    ComplianceStatus('INCOMPATIBLE'),
    ComplianceStatus('UNAVAILABLE'),
])
ComplianceStatus._set_binding_type(type.EnumType(
    'com.vmware.esx.settings.compliance_status',
    ComplianceStatus))



class HardwareModuleClass(Enum):
    """
    The ``HardwareModuleClass`` class contains the module's source information.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    SYSTEM_BIOS = None
    """
    System BIOS

    """
    PCI_DEVICE = None
    """
    PCI device

    """
    OTHER = None
    """
    Other (non-PCI) hardware

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`HardwareModuleClass` instance.
        """
        Enum.__init__(string)

HardwareModuleClass._set_values([
    HardwareModuleClass('SYSTEM_BIOS'),
    HardwareModuleClass('PCI_DEVICE'),
    HardwareModuleClass('OTHER'),
])
HardwareModuleClass._set_binding_type(type.EnumType(
    'com.vmware.esx.settings.hardware_module_class',
    HardwareModuleClass))



class ComponentSource(Enum):
    """
    The ``ComponentSource`` class contains the component's source information.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    BASE_IMAGE = None
    """
    Base image is the source for this component

    """
    ADD_ON = None
    """
    Addon is the source for this component

    """
    USER = None
    """
    User is the source for this component

    """
    SOLUTION = None
    """
    Solution is the source for this component

    """
    HARDWARE_SUPPORT_PACKAGE = None
    """
    Hardware Support Package (HSP) is the source for this component

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`ComponentSource` instance.
        """
        Enum.__init__(string)

ComponentSource._set_values([
    ComponentSource('BASE_IMAGE'),
    ComponentSource('ADD_ON'),
    ComponentSource('USER'),
    ComponentSource('SOLUTION'),
    ComponentSource('HARDWARE_SUPPORT_PACKAGE'),
])
ComponentSource._set_binding_type(type.EnumType(
    'com.vmware.esx.settings.component_source',
    ComponentSource))




class ClusterCompliance(VapiStruct):
    """
    The ``ClusterCompliance`` class contains attributes to describe the
    compliance result of a cluster.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 impact=None,
                 status=None,
                 notifications=None,
                 scan_time=None,
                 commit=None,
                 compliant_hosts=None,
                 non_compliant_hosts=None,
                 incompatible_hosts=None,
                 unavailable_hosts=None,
                 hosts=None,
                 host_info=None,
                ):
        """
        :type  impact: :class:`ComplianceImpact`
        :param impact: Overall impact.
        :type  status: :class:`ComplianceStatus`
        :param status: Overall compliance state of the host.
        :type  notifications: :class:`Notifications`
        :param notifications: Notifications returned by the scan operation.
        :type  scan_time: :class:`datetime.datetime`
        :param scan_time: Scan completion time.
        :type  commit: :class:`str` or ``None``
        :param commit: Identifier of the commit on which the scan is run to generate this
            result.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.settings.commit``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.esx.settings.commit``.
            None if operation is performed on a draft.
        :type  compliant_hosts: :class:`set` of :class:`str`
        :param compliant_hosts: Identifiers of compliant hosts.
            When clients pass a value of this class as a parameter, the
            attribute must contain identifiers for the resource type:
            ``HostSystem``. When methods return a value of this class as a
            return value, the attribute will contain identifiers for the
            resource type: ``HostSystem``.
        :type  non_compliant_hosts: :class:`set` of :class:`str`
        :param non_compliant_hosts: Identifiers of non-compliant hosts.
            When clients pass a value of this class as a parameter, the
            attribute must contain identifiers for the resource type:
            ``HostSystem``. When methods return a value of this class as a
            return value, the attribute will contain identifiers for the
            resource type: ``HostSystem``.
        :type  incompatible_hosts: :class:`set` of :class:`str`
        :param incompatible_hosts: Identifiers of incompatible hosts.
            When clients pass a value of this class as a parameter, the
            attribute must contain identifiers for the resource type:
            ``HostSystem``. When methods return a value of this class as a
            return value, the attribute will contain identifiers for the
            resource type: ``HostSystem``.
        :type  unavailable_hosts: :class:`set` of :class:`str`
        :param unavailable_hosts: Identifiers of unavailable hosts. There will not be compliance
            details for these hosts in :attr:`ClusterCompliance.hosts`.
            When clients pass a value of this class as a parameter, the
            attribute must contain identifiers for the resource type:
            ``HostSystem``. When methods return a value of this class as a
            return value, the attribute will contain identifiers for the
            resource type: ``HostSystem``.
        :type  hosts: :class:`dict` of :class:`str` and :class:`HostCompliance`
        :param hosts: Mapping from host identifier to the compliance information for the
            host.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``HostSystem``. When methods return a value of this class as
            a return value, the key in the attribute :class:`dict` will be an
            identifier for the resource type: ``HostSystem``.
        :type  host_info: :class:`dict` of :class:`str` and :class:`HostInfo`
        :param host_info: Auxillary information about the hosts. This gives some additional
            information about the hosts referenced in this result.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``HostSystem``. When methods return a value of this class as
            a return value, the key in the attribute :class:`dict` will be an
            identifier for the resource type: ``HostSystem``.
        """
        self.impact = impact
        self.status = status
        self.notifications = notifications
        self.scan_time = scan_time
        self.commit = commit
        self.compliant_hosts = compliant_hosts
        self.non_compliant_hosts = non_compliant_hosts
        self.incompatible_hosts = incompatible_hosts
        self.unavailable_hosts = unavailable_hosts
        self.hosts = hosts
        self.host_info = host_info
        VapiStruct.__init__(self)


ClusterCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.cluster_compliance', {
        'impact': type.ReferenceType(__name__, 'ComplianceImpact'),
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'notifications': type.ReferenceType(__name__, 'Notifications'),
        'scan_time': type.DateTimeType(),
        'commit': type.OptionalType(type.IdType()),
        'compliant_hosts': type.SetType(type.IdType()),
        'non_compliant_hosts': type.SetType(type.IdType()),
        'incompatible_hosts': type.SetType(type.IdType()),
        'unavailable_hosts': type.SetType(type.IdType()),
        'hosts': type.MapType(type.IdType(), type.ReferenceType(__name__, 'HostCompliance')),
        'host_info': type.MapType(type.IdType(), type.ReferenceType(__name__, 'HostInfo')),
    },
    ClusterCompliance,
    False,
    None))



class BaseImageCompliance(VapiStruct):
    """
    The ``BaseImageCompliance`` class contains information that describe the
    compliance of ESX base image with respect to the base image present in the
    target software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 current=None,
                 target=None,
                 notifications=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Compliance status of the base image.
        :type  current: :class:`BaseImageInfo`
        :param current: Current base image information on the host.
        :type  target: :class:`BaseImageInfo`
        :param target: Target base image information present in the software
            specification.
        :type  notifications: :class:`Notifications`
        :param notifications: Notifications describing the compliance result.
        """
        self.status = status
        self.current = current
        self.target = target
        self.notifications = notifications
        VapiStruct.__init__(self)


BaseImageCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.base_image_compliance', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'current': type.ReferenceType(__name__, 'BaseImageInfo'),
        'target': type.ReferenceType(__name__, 'BaseImageInfo'),
        'notifications': type.ReferenceType(__name__, 'Notifications'),
    },
    BaseImageCompliance,
    False,
    None))



class AddOnCompliance(VapiStruct):
    """
    The ``AddOnCompliance`` class contains information that describe the
    compliance of the OEM add-on with respect to the add-on present in the
    target software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 current=None,
                 target=None,
                 notifications=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Compliance status of the OEM add-on.
        :type  current: :class:`AddOnInfo` or ``None``
        :param current: Current OEM add-on present on the host.
            None if OEM add-on is not present on the host.
        :type  target: :class:`AddOnInfo` or ``None``
        :param target: Target OEM add-on present in the software specification.
            None if OEM add-on is not present in the software specification.
        :type  notifications: :class:`Notifications`
        :param notifications: Notifications describing the compliance result.
        """
        self.status = status
        self.current = current
        self.target = target
        self.notifications = notifications
        VapiStruct.__init__(self)


AddOnCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.add_on_compliance', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'current': type.OptionalType(type.ReferenceType(__name__, 'AddOnInfo')),
        'target': type.OptionalType(type.ReferenceType(__name__, 'AddOnInfo')),
        'notifications': type.ReferenceType(__name__, 'Notifications'),
    },
    AddOnCompliance,
    False,
    None))



class ComponentCompliance(VapiStruct):
    """
    The ``ComponentCompliance`` class contains information that describe the
    compliance of a component with respect to the component present in the
    target software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 current=None,
                 target=None,
                 current_source=None,
                 target_source=None,
                 notifications=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Compliance status of the component.
        :type  current: :class:`ComponentInfo` or ``None``
        :param current: Current version of the component present on the host.
            None if component is not present on the host.
        :type  target: :class:`ComponentInfo` or ``None``
        :param target: Target version of the component present in the software
            specification.
            None if component is not present in the software specification.
        :type  current_source: :class:`ComponentSource` or ``None``
        :param current_source: Source of the component on the host.
            None if component is not present on the host.
        :type  target_source: :class:`ComponentSource` or ``None``
        :param target_source: Source of the component in the software specification.
            None if component is not present in the software specification.
        :type  notifications: :class:`Notifications`
        :param notifications: Notifications describing the compliance result.
        """
        self.status = status
        self.current = current
        self.target = target
        self.current_source = current_source
        self.target_source = target_source
        self.notifications = notifications
        VapiStruct.__init__(self)


ComponentCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.component_compliance', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'current': type.OptionalType(type.ReferenceType(__name__, 'ComponentInfo')),
        'target': type.OptionalType(type.ReferenceType(__name__, 'ComponentInfo')),
        'current_source': type.OptionalType(type.ReferenceType(__name__, 'ComponentSource')),
        'target_source': type.OptionalType(type.ReferenceType(__name__, 'ComponentSource')),
        'notifications': type.ReferenceType(__name__, 'Notifications'),
    },
    ComponentCompliance,
    False,
    None))



class SolutionCompliance(VapiStruct):
    """
    The ``SolutionCompliance`` class contains information that describe the
    compliance result of a host with respect to given solution present in the
    target software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 current=None,
                 target=None,
                 notifications=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Compliance status of the solution.
        :type  current: :class:`SolutionInfo` or ``None``
        :param current: Current solution present on the host.
            None if the solution is not present on the host.
        :type  target: :class:`SolutionInfo` or ``None``
        :param target: Target solution present in the software specification.
            None if solution is not present in the software specification.
        :type  notifications: :class:`Notifications`
        :param notifications: Notifications describing the compliance result.
        """
        self.status = status
        self.current = current
        self.target = target
        self.notifications = notifications
        VapiStruct.__init__(self)


SolutionCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.solution_compliance', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'current': type.OptionalType(type.ReferenceType(__name__, 'SolutionInfo')),
        'target': type.OptionalType(type.ReferenceType(__name__, 'SolutionInfo')),
        'notifications': type.ReferenceType(__name__, 'Notifications'),
    },
    SolutionCompliance,
    False,
    None))



class HardwareModuleDetails(VapiStruct):
    """
    The ``HardwareModuleDetails`` class contains information that provide more
    details about the a hardware module (e.g. BIOS, PCI device).

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 component_class=None,
                 description=None,
                ):
        """
        :type  component_class: :class:`HardwareModuleClass`
        :param component_class: Class of module (BIOS, PCI Device, non-PCI hardware, etc.)
        :type  description: :class:`str` or ``None``
        :param description: Descipription of the hardware module (e.g. "System BIOS" or
            "Frobozz 100Gb NIC").
            None if description is not specified.
        """
        self.component_class = component_class
        self.description = description
        VapiStruct.__init__(self)


HardwareModuleDetails._set_binding_type(type.StructType(
    'com.vmware.esx.settings.hardware_module_details', {
        'component_class': type.ReferenceType(__name__, 'HardwareModuleClass'),
        'description': type.OptionalType(type.StringType()),
    },
    HardwareModuleDetails,
    False,
    None))



class HardwareModuleFirmwareInfo(VapiStruct):
    """
    The ``HardwareModuleFirmwareInfo`` class contains information to describe
    the firmware on a hardware component or module (e.g. BIOS, PCI device).

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the hardware module firmware.
        """
        self.version = version
        VapiStruct.__init__(self)


HardwareModuleFirmwareInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.hardware_module_firmware_info', {
        'version': type.StringType(),
    },
    HardwareModuleFirmwareInfo,
    False,
    None))



class HardwareModuleFirmwareCompliance(VapiStruct):
    """
    The ``HardwareModuleFirmwareCompliance`` class contains information that
    describe the compliance of firmware of a particular hardware module (e.g.
    BIOS, PCI device) on the host with respect to the firmware present in the
    target Hardware Support Package (HSP) specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 details=None,
                 current=None,
                 target=None,
                 notifications=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Compliance status of the hardware module's firmware.
        :type  details: :class:`HardwareModuleDetails` or ``None``
        :param details: Additional details about the hardware module itself
            None if no further info was provided by HSM.
        :type  current: :class:`HardwareModuleFirmwareInfo` or ``None``
        :param current: Current version of the firmware present on the host hardware
            module.
            None if version of firmware on the hardware module on the host
            cannot be determined.
        :type  target: :class:`HardwareModuleFirmwareInfo` or ``None``
        :param target: Target version of the firmware present in the Hardware Support
            Package (HSP).
            None if component is not present in the software specification.
        :type  notifications: :class:`Notifications`
        :param notifications: Notifications describing the compliance result.
        """
        self.status = status
        self.details = details
        self.current = current
        self.target = target
        self.notifications = notifications
        VapiStruct.__init__(self)


HardwareModuleFirmwareCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.hardware_module_firmware_compliance', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'details': type.OptionalType(type.ReferenceType(__name__, 'HardwareModuleDetails')),
        'current': type.OptionalType(type.ReferenceType(__name__, 'HardwareModuleFirmwareInfo')),
        'target': type.OptionalType(type.ReferenceType(__name__, 'HardwareModuleFirmwareInfo')),
        'notifications': type.ReferenceType(__name__, 'Notifications'),
    },
    HardwareModuleFirmwareCompliance,
    False,
    None))



class HardwareSupportPackageCompliance(VapiStruct):
    """
    The ``HardwareSupportPackageCompliance`` class contains information that
    describe compliance of the Hardware Support Package (HSP) on the host with
    respect to the Hardware support Package (HSP) present in the target
    software image specification, if any.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 current=None,
                 target=None,
                 hardware_modules=None,
                 notifications=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Compliance status of the Hardware Support Package (HSP).
        :type  current: :class:`HardwareSupportPackageInfo` or ``None``
        :param current: Current version of the Hardware Support Package present on the
            host.
            None if there is no known Hardware Support Package on the host.
        :type  target: :class:`HardwareSupportPackageInfo` or ``None``
        :param target: Target version of the Hardware Support Package present in the
            software specification.
            None if current desired image includes a Hardware Support Manager
            (HSM) but no target Hardware Support Package (HSP).
        :type  hardware_modules: :class:`dict` of :class:`str` and :class:`HardwareModuleFirmwareCompliance`
        :param hardware_modules: Compliance result for individual hardware module on the host. The
            key is the module identifier and value is the
            HardwareModuleFirmwareCompliance for the device. NOTE: if no
            individual hardware module compliance is returned by the, Hardware
            Support Manager (HSM), this map may have no entries even if
            ComplianceStatus = NON_COMPLIANT
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.setting.hardware_module``. When methods
            return a value of this class as a return value, the key in the
            attribute :class:`dict` will be an identifier for the resource
            type: ``com.vmware.esx.setting.hardware_module``.
        :type  notifications: :class:`Notifications`
        :param notifications: Notifications describing the compliance result.
        """
        self.status = status
        self.current = current
        self.target = target
        self.hardware_modules = hardware_modules
        self.notifications = notifications
        VapiStruct.__init__(self)


HardwareSupportPackageCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.hardware_support_package_compliance', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'current': type.OptionalType(type.ReferenceType(__name__, 'HardwareSupportPackageInfo')),
        'target': type.OptionalType(type.ReferenceType(__name__, 'HardwareSupportPackageInfo')),
        'hardware_modules': type.MapType(type.IdType(), type.ReferenceType(__name__, 'HardwareModuleFirmwareCompliance')),
        'notifications': type.ReferenceType(__name__, 'Notifications'),
    },
    HardwareSupportPackageCompliance,
    False,
    None))



class HostCompliance(VapiStruct):
    """
    The ``HostCompliance`` class contains information to describe the
    compliance result of a host with respect to given target software
    specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 impact=None,
                 status=None,
                 notifications=None,
                 scan_time=None,
                 commit=None,
                 base_image=None,
                 add_on=None,
                 hardware_support=None,
                 components=None,
                 solutions=None,
                ):
        """
        :type  impact: :class:`ComplianceImpact`
        :param impact: Overall impact.
        :type  status: :class:`ComplianceStatus`
        :param status: Overall compliance state of the host.
        :type  notifications: :class:`Notifications`
        :param notifications: Notifications returned by the scan operation.
        :type  scan_time: :class:`datetime.datetime`
        :param scan_time: Scan completion time.
        :type  commit: :class:`str` or ``None``
        :param commit: Identifier of the commit on which the scan is run to generate this
            result.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.settings.commit``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.esx.settings.commit``.
            None if operation is performed on a working copy document.
        :type  base_image: :class:`BaseImageCompliance`
        :param base_image: Compliance result for the base image.
        :type  add_on: :class:`AddOnCompliance`
        :param add_on: Compliance result for the OEM add-on.
        :type  hardware_support: :class:`dict` of :class:`str` and :class:`HardwareSupportPackageCompliance`
        :param hardware_support: Compliance result for hardware support (both Hardware Support
            Package or HSP and individual hardware module firmware) for every
            HSP configured, keyed by Hardware Support Manager (HSM).
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.setting.hardware_support.manager``. When
            methods return a value of this class as a return value, the key in
            the attribute :class:`dict` will be an identifier for the resource
            type: ``com.vmware.esx.setting.hardware_support.manager``.
            This attribute is optional because it was added in a newer version
            than its parent node.
        :type  components: :class:`dict` of :class:`str` and :class:`ComponentCompliance`
        :param components: Compliance result for all the effective components and all the
            components present on the host. The key is the component name and
            value is the ComponentCompliance.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.settings.component``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.settings.component``.
        :type  solutions: :class:`dict` of :class:`str` and :class:`SolutionCompliance`
        :param solutions: Compliance result for solutions. The key is the solution name and
            value is the SolutionCompliance.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.settings.solution``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.settings.solution``.
        """
        self.impact = impact
        self.status = status
        self.notifications = notifications
        self.scan_time = scan_time
        self.commit = commit
        self.base_image = base_image
        self.add_on = add_on
        self.hardware_support = hardware_support
        self.components = components
        self.solutions = solutions
        VapiStruct.__init__(self)


HostCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.host_compliance', {
        'impact': type.ReferenceType(__name__, 'ComplianceImpact'),
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'notifications': type.ReferenceType(__name__, 'Notifications'),
        'scan_time': type.DateTimeType(),
        'commit': type.OptionalType(type.IdType()),
        'base_image': type.ReferenceType(__name__, 'BaseImageCompliance'),
        'add_on': type.ReferenceType(__name__, 'AddOnCompliance'),
        'hardware_support': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'HardwareSupportPackageCompliance'))),
        'components': type.MapType(type.IdType(), type.ReferenceType(__name__, 'ComponentCompliance')),
        'solutions': type.MapType(type.IdType(), type.ReferenceType(__name__, 'SolutionCompliance')),
    },
    HostCompliance,
    False,
    None))



class HostInfo(VapiStruct):
    """
    The ``HostInfo`` class contains attributes to describe some details
    regarding a host in the inventory.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the host.
        """
        self.name = name
        VapiStruct.__init__(self)


HostInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.host_info', {
        'name': type.StringType(),
    },
    HostInfo,
    False,
    None))



class Notification(VapiStruct):
    """
    The ``Notification`` class contains attributes to describe any
    info/warning/error messages that Tasks can raise.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 time=None,
                 message=None,
                 resolution=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The notification id.
        :type  time: :class:`datetime.datetime`
        :param time: The time the notification was raised/found.
        :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param message: The notification message.
        :type  resolution: :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
        :param resolution: The resolution message, if any.
            Only :class:`set` if there is a resolution available for this
            notification.
        """
        self.id = id
        self.time = time
        self.message = message
        self.resolution = resolution
        VapiStruct.__init__(self)


Notification._set_binding_type(type.StructType(
    'com.vmware.esx.settings.notification', {
        'id': type.StringType(),
        'time': type.DateTimeType(),
        'message': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'resolution': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
    },
    Notification,
    False,
    None))



class Notifications(VapiStruct):
    """
    The ``Notifications`` class contains info/warning/error messages that can
    be reported be the task.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 info=None,
                 warnings=None,
                 errors=None,
                ):
        """
        :type  info: :class:`list` of :class:`Notification` or ``None``
        :param info: Info notification messages reported.
            Only :class:`set` if an info was reported by the task.
        :type  warnings: :class:`list` of :class:`Notification` or ``None``
        :param warnings: Warning notification messages reported.
            Only :class:`set` if an warning was reported by the task.
        :type  errors: :class:`list` of :class:`Notification` or ``None``
        :param errors: Error notification messages reported.
            Only :class:`set` if an error was reported by the task.
        """
        self.info = info
        self.warnings = warnings
        self.errors = errors
        VapiStruct.__init__(self)


Notifications._set_binding_type(type.StructType(
    'com.vmware.esx.settings.notifications', {
        'info': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Notification'))),
        'warnings': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Notification'))),
        'errors': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Notification'))),
    },
    Notifications,
    False,
    None))



class ComponentOverrideInfo(VapiStruct):
    """
    The ``ComponentOverrideInfo`` class contains fields that describe how the
    component was overridden.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 display_version=None,
                 source=None,
                 note=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the component override.
        :type  display_version: :class:`str`
        :param display_version: Human readable version of the component override.
        :type  source: :class:`ComponentSource`
        :param source: Source of the component override.
        :type  note: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param note: Note explaining the override.
        """
        self.version = version
        self.display_version = display_version
        self.source = source
        self.note = note
        VapiStruct.__init__(self)


ComponentOverrideInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.component_override_info', {
        'version': type.StringType(),
        'display_version': type.StringType(),
        'source': type.ReferenceType(__name__, 'ComponentSource'),
        'note': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
    },
    ComponentOverrideInfo,
    False,
    None))



class EffectiveComponentDetails(VapiStruct):
    """
    The ``EffectiveComponentDetails`` class contains information that provide
    more details about the component from the depot.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 display_name=None,
                 display_version=None,
                 vendor=None,
                 source=None,
                 note=None,
                 overridden_components=None,
                ):
        """
        :type  display_name: :class:`str`
        :param display_name: Display name of the component.
        :type  display_version: :class:`str`
        :param display_version: Human readable version of the component.
        :type  vendor: :class:`str`
        :param vendor: Vendor of the component.
        :type  source: :class:`ComponentSource`
        :param source: Final effective source of the component.
        :type  note: :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
        :param note: Note assosicated with this component.
            If None, note is present for this component.
        :type  overridden_components: :class:`list` of :class:`ComponentOverrideInfo`
        :param overridden_components: List of other component versions present in base-image, add-ons or
            solutions that this component is overriding. For example, if a
            component version-1 was implicitly present in the base-image, but
            user wants it to be changed to version-2. In that case,
            :attr:`EffectiveComponentDetails.source` would be USER and there
            will be one entry in this list indicating base-image component
            version-1 is being overridden.
        """
        self.display_name = display_name
        self.display_version = display_version
        self.vendor = vendor
        self.source = source
        self.note = note
        self.overridden_components = overridden_components
        VapiStruct.__init__(self)


EffectiveComponentDetails._set_binding_type(type.StructType(
    'com.vmware.esx.settings.effective_component_details', {
        'display_name': type.StringType(),
        'display_version': type.StringType(),
        'vendor': type.StringType(),
        'source': type.ReferenceType(__name__, 'ComponentSource'),
        'note': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'overridden_components': type.ListType(type.ReferenceType(__name__, 'ComponentOverrideInfo')),
    },
    EffectiveComponentDetails,
    False,
    None))



class EffectiveComponentInfo(VapiStruct):
    """
    The ``EffectiveComponentInfo`` class contains information that describe a
    component and how that component appeared in the software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 details=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the component.
        :type  details: :class:`EffectiveComponentDetails` or ``None``
        :param details: Details about the effective component.
            None if component is not present in the depot.
        """
        self.version = version
        self.details = details
        VapiStruct.__init__(self)


EffectiveComponentInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.effective_component_info', {
        'version': type.StringType(),
        'details': type.OptionalType(type.ReferenceType(__name__, 'EffectiveComponentDetails')),
    },
    EffectiveComponentInfo,
    False,
    None))



class ComponentDetails(VapiStruct):
    """
    The ``ComponentDetails`` class contains information that provide more
    details about the component from the depot.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 display_name=None,
                 vendor=None,
                 display_version=None,
                ):
        """
        :type  display_name: :class:`str`
        :param display_name: Display name of the component.
        :type  vendor: :class:`str`
        :param vendor: Vendor of the component.
        :type  display_version: :class:`str` or ``None``
        :param display_version: Human readable version of the component.
            None if no version is provided for the component.
        """
        self.display_name = display_name
        self.vendor = vendor
        self.display_version = display_version
        VapiStruct.__init__(self)


ComponentDetails._set_binding_type(type.StructType(
    'com.vmware.esx.settings.component_details', {
        'display_name': type.StringType(),
        'vendor': type.StringType(),
        'display_version': type.OptionalType(type.StringType()),
    },
    ComponentDetails,
    False,
    None))



class ComponentInfo(VapiStruct):
    """
    The ``ComponentInfo`` class contains information that describe a specific
    component version in a software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 details=None,
                ):
        """
        :type  version: :class:`str` or ``None``
        :param version: Version of the component.
            None if version is not specified.
        :type  details: :class:`ComponentDetails` or ``None``
        :param details: Details about the component.
            None if component is not present in the depot.
        """
        self.version = version
        self.details = details
        VapiStruct.__init__(self)


ComponentInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.component_info', {
        'version': type.OptionalType(type.StringType()),
        'details': type.OptionalType(type.ReferenceType(__name__, 'ComponentDetails')),
    },
    ComponentInfo,
    False,
    None))



class SolutionComponentDetails(VapiStruct):
    """
    The ``SolutionComponentDetails`` class contains information that provide
    more details about component registered by the solution from depot.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 component=None,
                 display_name=None,
                 display_version=None,
                 vendor=None,
                ):
        """
        :type  component: :class:`str`
        :param component: Identifier of the component.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.settings.component``. When methods return a value
            of this class as a return value, the attribute will be an
            identifier for the resource type:
            ``com.vmware.esx.settings.component``.
        :type  display_name: :class:`str`
        :param display_name: Display name of the component.
        :type  display_version: :class:`str` or ``None``
        :param display_version: Human readable version of the component.
            None if no version is provided for the component.
        :type  vendor: :class:`str`
        :param vendor: Vendor of the component.
        """
        self.component = component
        self.display_name = display_name
        self.display_version = display_version
        self.vendor = vendor
        VapiStruct.__init__(self)


SolutionComponentDetails._set_binding_type(type.StructType(
    'com.vmware.esx.settings.solution_component_details', {
        'component': type.IdType(resource_types='com.vmware.esx.settings.component'),
        'display_name': type.StringType(),
        'display_version': type.OptionalType(type.StringType()),
        'vendor': type.StringType(),
    },
    SolutionComponentDetails,
    False,
    None))



class SolutionDetails(VapiStruct):
    """
    The ``SolutionDetails`` class contains information that provide more
    details about the solution from the depot.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 display_name=None,
                 display_version=None,
                 components=None,
                ):
        """
        :type  display_name: :class:`str`
        :param display_name: Display name of the solution.
        :type  display_version: :class:`str`
        :param display_version: Display version of the solution.
        :type  components: :class:`list` of :class:`SolutionComponentDetails`
        :param components: Components registered by the solution. If the component is not
            present in the depot, then corresponding details are absent from
            the list.
        """
        self.display_name = display_name
        self.display_version = display_version
        self.components = components
        VapiStruct.__init__(self)


SolutionDetails._set_binding_type(type.StructType(
    'com.vmware.esx.settings.solution_details', {
        'display_name': type.StringType(),
        'display_version': type.StringType(),
        'components': type.ListType(type.ReferenceType(__name__, 'SolutionComponentDetails')),
    },
    SolutionDetails,
    False,
    None))



class SolutionInfo(VapiStruct):
    """
    The ``SolutionInfo`` class contains information that describe solution
    registered in the software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 details=None,
                 version=None,
                 components=None,
                ):
        """
        :type  details: :class:`SolutionDetails` or ``None``
        :param details: Details about the solution from the depot.
            None if solution is not present in the depot.
        :type  version: :class:`str`
        :param version: Version of the solution.
        :type  components: :class:`list` of :class:`SolutionComponentSpec`
        :param components: Components registered by the solution.
        """
        self.details = details
        self.version = version
        self.components = components
        VapiStruct.__init__(self)


SolutionInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.solution_info', {
        'details': type.OptionalType(type.ReferenceType(__name__, 'SolutionDetails')),
        'version': type.StringType(),
        'components': type.ListType(type.ReferenceType(__name__, 'SolutionComponentSpec')),
    },
    SolutionInfo,
    False,
    None))



class BaseImageDetails(VapiStruct):
    """
    The ``BaseImageDetails`` class contains information that provide more
    details about the base image from the depot.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 display_name=None,
                 display_version=None,
                 release_date=None,
                ):
        """
        :type  display_name: :class:`str`
        :param display_name: Display name of the base-image.
        :type  display_version: :class:`str`
        :param display_version: Human readable version of the base-image.
        :type  release_date: :class:`datetime.datetime`
        :param release_date: Release date of the base-image.
        """
        self.display_name = display_name
        self.display_version = display_version
        self.release_date = release_date
        VapiStruct.__init__(self)


BaseImageDetails._set_binding_type(type.StructType(
    'com.vmware.esx.settings.base_image_details', {
        'display_name': type.StringType(),
        'display_version': type.StringType(),
        'release_date': type.DateTimeType(),
    },
    BaseImageDetails,
    False,
    None))



class BaseImageInfo(VapiStruct):
    """
    The ``BaseImageInfo`` class contains information that describe a specific
    ESX base-image.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 details=None,
                 version=None,
                ):
        """
        :type  details: :class:`BaseImageDetails` or ``None``
        :param details: Details about the base-image.
            None if base-image is not present in the depot.
        :type  version: :class:`str`
        :param version: Version of the base-image
        """
        self.details = details
        self.version = version
        VapiStruct.__init__(self)


BaseImageInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.base_image_info', {
        'details': type.OptionalType(type.ReferenceType(__name__, 'BaseImageDetails')),
        'version': type.StringType(),
    },
    BaseImageInfo,
    False,
    None))



class AddOnDetails(VapiStruct):
    """
    The ``AddOnDetails`` class contains information that provide more details
    about the add-on from the depot.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 display_name=None,
                 vendor=None,
                 display_version=None,
                ):
        """
        :type  display_name: :class:`str`
        :param display_name: Display name of the OEM add-on.
        :type  vendor: :class:`str`
        :param vendor: Vendor of the OEM add-on.
        :type  display_version: :class:`str`
        :param display_version: Human readable version of the OEM add-on.
        """
        self.display_name = display_name
        self.vendor = vendor
        self.display_version = display_version
        VapiStruct.__init__(self)


AddOnDetails._set_binding_type(type.StructType(
    'com.vmware.esx.settings.add_on_details', {
        'display_name': type.StringType(),
        'vendor': type.StringType(),
        'display_version': type.StringType(),
    },
    AddOnDetails,
    False,
    None))



class AddOnInfo(VapiStruct):
    """
    The ``AddOnInfo`` class contains information that describe a specific OEM
    customization add-on.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 details=None,
                 name=None,
                 version=None,
                ):
        """
        :type  details: :class:`AddOnDetails` or ``None``
        :param details: Details about the add-on.
            None if add-on is not present in the depot.
        :type  name: :class:`str`
        :param name: Name of the add-on
        :type  version: :class:`str`
        :param version: Version of the add-on
        """
        self.details = details
        self.name = name
        self.version = version
        VapiStruct.__init__(self)


AddOnInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.add_on_info', {
        'details': type.OptionalType(type.ReferenceType(__name__, 'AddOnDetails')),
        'name': type.StringType(),
        'version': type.StringType(),
    },
    AddOnInfo,
    False,
    None))



class HardwareSupportPackageInfo(VapiStruct):
    """
    The ``HardwareSupportPackageInfo`` class contains information to describe
    the desired Hardware Support Package (HSP) configured for a single device
    or distinct group of devices (typically the OEM's, including BIOS and
    device firmware).

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 pkg=None,
                 version=None,
                ):
        """
        :type  pkg: :class:`str`
        :param pkg: Identifier of Hardware Support Package (HSP) selected
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.setting.hardware_support.package``. When methods
            return a value of this class as a return value, the attribute will
            be an identifier for the resource type:
            ``com.vmware.esx.setting.hardware_support.package``.
        :type  version: :class:`str`
        :param version: Version of the Hardware Support Package (HSP) selected (e.g.
            "20180128.1" or "v42")
        """
        self.pkg = pkg
        self.version = version
        VapiStruct.__init__(self)


HardwareSupportPackageInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.hardware_support_package_info', {
        'pkg': type.IdType(resource_types='com.vmware.esx.setting.hardware_support.package'),
        'version': type.StringType(),
    },
    HardwareSupportPackageInfo,
    False,
    None))



class HardwareSupportInfo(VapiStruct):
    """
    The ``HardwareSupportInfo`` class contains information to describe the
    desired Hardware Support Package (HSP) configured for a cluster.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 packages=None,
                ):
        """
        :type  packages: :class:`dict` of :class:`str` and :class:`HardwareSupportPackageInfo`
        :param packages: Map of Hardware Support Packages (HSPs) for the cluster. The key is
            the Hardware Support Manager (HSM) identifier and the value is the
            specification detailing the HSP configured for that HSM.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.setting.hardware_support.manager``. When
            methods return a value of this class as a return value, the key in
            the attribute :class:`dict` will be an identifier for the resource
            type: ``com.vmware.esx.setting.hardware_support.manager``.
        """
        self.packages = packages
        VapiStruct.__init__(self)


HardwareSupportInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.hardware_support_info', {
        'packages': type.MapType(type.IdType(), type.ReferenceType(__name__, 'HardwareSupportPackageInfo')),
    },
    HardwareSupportInfo,
    False,
    None))



class SoftwareInfo(VapiStruct):
    """
    The ``SoftwareInfo`` class contains information that describes the desired
    software specification for an ESX host.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 base_image=None,
                 add_on=None,
                 components=None,
                 solutions=None,
                 hardware_support=None,
                ):
        """
        :type  base_image: :class:`BaseImageInfo`
        :param base_image: Base image of the ESX.
        :type  add_on: :class:`AddOnInfo` or ``None``
        :param add_on: OEM customization on top of given base-image. The components in
            this customization override the components in the base base-image.
            If None, no OEM customization will be applied.
        :type  components: :class:`dict` of :class:`str` and :class:`ComponentInfo`
        :param components: Information about the components in the software specification.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.settings.component``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.settings.component``.
        :type  solutions: :class:`dict` of :class:`str` and :class:`SolutionInfo`
        :param solutions: Information about the solutions in the software specification.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.settings.solution``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.settings.solution``.
        :type  hardware_support: :class:`HardwareSupportInfo` or ``None``
        :param hardware_support: Information about the Hardware Support Packages (HSP) configured.
            If None, no Hardware Support Package (HSP) is specified for the
            cluster.
        """
        self.base_image = base_image
        self.add_on = add_on
        self.components = components
        self.solutions = solutions
        self.hardware_support = hardware_support
        VapiStruct.__init__(self)


SoftwareInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.software_info', {
        'base_image': type.ReferenceType(__name__, 'BaseImageInfo'),
        'add_on': type.OptionalType(type.ReferenceType(__name__, 'AddOnInfo')),
        'components': type.MapType(type.IdType(), type.ReferenceType(__name__, 'ComponentInfo')),
        'solutions': type.MapType(type.IdType(), type.ReferenceType(__name__, 'SolutionInfo')),
        'hardware_support': type.OptionalType(type.ReferenceType(__name__, 'HardwareSupportInfo')),
    },
    SoftwareInfo,
    False,
    None))



class SolutionComponentSpec(VapiStruct):
    """
    The ``SolutionComponentSpec`` class contains attributes that describe a
    component registered by a software solution.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 component=None,
                ):
        """
        :type  component: :class:`str`
        :param component: Identifier of the component.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.settings.component``. When methods return a value
            of this class as a return value, the attribute will be an
            identifier for the resource type:
            ``com.vmware.esx.settings.component``.
        """
        self.component = component
        VapiStruct.__init__(self)


SolutionComponentSpec._set_binding_type(type.StructType(
    'com.vmware.esx.settings.solution_component_spec', {
        'component': type.IdType(resource_types='com.vmware.esx.settings.component'),
    },
    SolutionComponentSpec,
    False,
    None))



class SolutionSpec(VapiStruct):
    """
    The ``SolutionSpec`` class contains attributes that describe solution
    registered in the software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 components=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the solution.
        :type  components: :class:`list` of :class:`SolutionComponentSpec`
        :param components: Components registered by the solution.
        """
        self.version = version
        self.components = components
        VapiStruct.__init__(self)


SolutionSpec._set_binding_type(type.StructType(
    'com.vmware.esx.settings.solution_spec', {
        'version': type.StringType(),
        'components': type.ListType(type.ReferenceType(__name__, 'SolutionComponentSpec')),
    },
    SolutionSpec,
    False,
    None))



class BaseImageSpec(VapiStruct):
    """
    The ``BaseImageSpec`` class contains attributes that describe a specific
    ESX base-image.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the base-image
        """
        self.version = version
        VapiStruct.__init__(self)


BaseImageSpec._set_binding_type(type.StructType(
    'com.vmware.esx.settings.base_image_spec', {
        'version': type.StringType(),
    },
    BaseImageSpec,
    False,
    None))



class AddOnSpec(VapiStruct):
    """
    The ``AddOnSpec`` class contains attributes that describe a specific OEM
    customization add-on.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 version=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the add-on
        :type  version: :class:`str`
        :param version: Version of the add-on
        """
        self.name = name
        self.version = version
        VapiStruct.__init__(self)


AddOnSpec._set_binding_type(type.StructType(
    'com.vmware.esx.settings.add_on_spec', {
        'name': type.StringType(),
        'version': type.StringType(),
    },
    AddOnSpec,
    False,
    None))



class HardwareSupportPackageSpec(VapiStruct):
    """
    The ``HardwareSupportPackageSpec`` class contains attributes to describe
    the desired Hardware Support Package (HSP) configured for a single device
    or distinct group of devices (typically the OEM's, including BIOS, device
    firmware and OEM-supplied driver or agent components).

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 pkg=None,
                 version=None,
                ):
        """
        :type  pkg: :class:`str` or ``None``
        :param pkg: Hardware Support Package (HSP) selected
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.setting.hardware_support.package``. When methods
            return a value of this class as a return value, the attribute will
            be an identifier for the resource type:
            ``com.vmware.esx.setting.hardware_support.package``.
        :type  version: :class:`str` or ``None``
        :param version: Version of the Hardware Support Package (HSP) selected (e.g.
            "20180128.1" or "v42")
            If None, the system will use an empty string as the version.
        """
        self.pkg = pkg
        self.version = version
        VapiStruct.__init__(self)


HardwareSupportPackageSpec._set_binding_type(type.StructType(
    'com.vmware.esx.settings.hardware_support_package_spec', {
        'pkg': type.OptionalType(type.IdType()),
        'version': type.OptionalType(type.StringType()),
    },
    HardwareSupportPackageSpec,
    False,
    None))



class HardwareSupportSpec(VapiStruct):
    """
    The ``HardwareSupportSpec`` class contains attributes to describe the
    desired Hardware Support Package (HSP) configured for a cluster.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 packages=None,
                ):
        """
        :type  packages: :class:`dict` of :class:`str` and :class:`HardwareSupportPackageSpec`
        :param packages: Map of Hardware Support Packages (HSPs) for the cluster. The key is
            the Hardware Support Manager (HSM) name and the value is the
            specification detailing the HSP configured for that HSM.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.setting.hardware_support.manager``. When
            methods return a value of this class as a return value, the key in
            the attribute :class:`dict` will be an identifier for the resource
            type: ``com.vmware.esx.setting.hardware_support.manager``.
        """
        self.packages = packages
        VapiStruct.__init__(self)


HardwareSupportSpec._set_binding_type(type.StructType(
    'com.vmware.esx.settings.hardware_support_spec', {
        'packages': type.MapType(type.IdType(), type.ReferenceType(__name__, 'HardwareSupportPackageSpec')),
    },
    HardwareSupportSpec,
    False,
    None))



class SoftwareSpec(VapiStruct):
    """
    The ``SoftwareSpec`` class contains attributes that describe desired
    software specification for an ESX host.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 base_image=None,
                 add_on=None,
                 components=None,
                 solutions=None,
                 hardware_support=None,
                ):
        """
        :type  base_image: :class:`BaseImageSpec`
        :param base_image: Base image of the ESX.
        :type  add_on: :class:`AddOnSpec` or ``None``
        :param add_on: OEM customization on top of given base-image. The components in
            this customization override the components in the base base-image.
            If None, no OEM customization will be applied.
        :type  components: (:class:`dict` of :class:`str` and (:class:`str` or ``None``)) or ``None``
        :param components: Additional components which should be part of the software
            specification. If value is not given for a particular component
            then version for that component will be picked from the
            constraints. These override the components present in
            :attr:`SoftwareSpec.add_on` and :attr:`SoftwareSpec.base_image`.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.settings.component``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.settings.component``.
            If None, no additional components will be installed.
        :type  solutions: (:class:`dict` of :class:`str` and :class:`SolutionSpec`) or ``None``
        :param solutions: Mapping from solution identifier to the solution specification. The
            key is the solution name and the value is the specification
            detailing components registered by that solution.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.settings.solution``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.settings.solution``.
            If None, no solutions will be part of the software specification.
        :type  hardware_support: :class:`HardwareSupportSpec` or ``None``
        :param hardware_support: Information about the Hardware Support Package (HSP) configured in
            the software specification.
            If None or empty, no firmware compliance checking or remediation
            will be done.
        """
        self.base_image = base_image
        self.add_on = add_on
        self.components = components
        self.solutions = solutions
        self.hardware_support = hardware_support
        VapiStruct.__init__(self)


SoftwareSpec._set_binding_type(type.StructType(
    'com.vmware.esx.settings.software_spec', {
        'base_image': type.ReferenceType(__name__, 'BaseImageSpec'),
        'add_on': type.OptionalType(type.ReferenceType(__name__, 'AddOnSpec')),
        'components': type.OptionalType(type.MapType(type.IdType(), type.OptionalType(type.StringType()))),
        'solutions': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'SolutionSpec'))),
        'hardware_support': type.OptionalType(type.ReferenceType(__name__, 'HardwareSupportSpec')),
    },
    SoftwareSpec,
    False,
    None))



class TaskInfo(VapiStruct):
    """
    The ``TaskInfo`` class contains information about a task and its subtasks
    of which it consists.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'status',
            {
                'RUNNING' : [('progress', True), ('result', False), ('start_time', True)],
                'BLOCKED' : [('progress', True), ('result', False), ('start_time', True)],
                'SUCCEEDED' : [('progress', True), ('result', False), ('start_time', True), ('end_time', True)],
                'FAILED' : [('progress', True), ('result', False), ('error', False), ('start_time', True), ('end_time', True)],
                'PENDING' : [],
            }
        ),
    ]



    def __init__(self,
                 progress=None,
                 subtasks=None,
                 notifications=None,
                 result=None,
                 description=None,
                 service=None,
                 operation=None,
                 parent=None,
                 target=None,
                 status=None,
                 cancelable=None,
                 error=None,
                 start_time=None,
                 end_time=None,
                 user=None,
                ):
        """
        :type  progress: :class:`com.vmware.cis.task_client.Progress`
        :param progress: Progress of the operation.
            This attribute is optional and it is only relevant when the value
            of ``#status`` is one of
            :attr:`com.vmware.cis.task_client.Status.RUNNING`,
            :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
            :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
            :attr:`com.vmware.cis.task_client.Status.FAILED`.
        :type  subtasks: (:class:`dict` of :class:`str` and :class:`TaskInfo`) or ``None``
        :param subtasks: Information about the subtasks that this task contains.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.cis.task``. When methods return a value of this
            class as a return value, the key in the attribute :class:`dict`
            will be an identifier for the resource type:
            ``com.vmware.cis.task``.
            This attribute will be None if the task has no subtasks.
        :type  notifications: :class:`Notifications` or ``None``
        :param notifications: Notifications to the user
            Only :class:`set` if the notifications were reported by this
            particular task.
        :type  result: :class:`DataValue` or ``None``
        :param result: Task result.
            This attribute will be None if the task has no result.
        :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param description: Description of the operation associated with the task.
        :type  service: :class:`str`
        :param service: Identifier of the service containing the operation.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vapi.service``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vapi.service``.
        :type  operation: :class:`str`
        :param operation: Identifier of the operation associated with the task.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vapi.operation``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vapi.operation``.
        :type  parent: :class:`str` or ``None``
        :param parent: Parent of the current task.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.cis.task``. When methods return a value of this class
            as a return value, the attribute will be an identifier for the
            resource type: ``com.vmware.cis.task``.
            This attribute will be None if the task has no parent.
        :type  target: :class:`com.vmware.vapi.std_client.DynamicID` or ``None``
        :param target: Identifier of the target created by the operation or an existing
            one the operation performed on.
            This attribute will be None if the operation has no target or
            multiple targets.
        :type  status: :class:`com.vmware.cis.task_client.Status`
        :param status: Status of the operation associated with the task.
        :type  cancelable: :class:`bool`
        :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
            value may change as the operation progresses.
        :type  error: :class:`Exception` or ``None``
        :param error: Description of the error if the operation status is "FAILED".
            If None the description of why the operation failed will be
            included in the result of the operation (see
            :attr:`com.vmware.cis.task_client.Info.result`).
        :type  start_time: :class:`datetime.datetime`
        :param start_time: Time when the operation is started.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of
            :attr:`com.vmware.cis.task_client.Status.RUNNING`,
            :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
            :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
            :attr:`com.vmware.cis.task_client.Status.FAILED`.
        :type  end_time: :class:`datetime.datetime`
        :param end_time: Time when the operation is completed.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of
            :attr:`com.vmware.cis.task_client.Status.SUCCEEDED` or
            :attr:`com.vmware.cis.task_client.Status.FAILED`.
        :type  user: :class:`str` or ``None``
        :param user: Name of the user who performed the operation.
            This attribute will be None if the operation is performed by the
            system.
        """
        self.progress = progress
        self.subtasks = subtasks
        self.notifications = notifications
        self.result = result
        self.description = description
        self.service = service
        self.operation = operation
        self.parent = parent
        self.target = target
        self.status = status
        self.cancelable = cancelable
        self.error = error
        self.start_time = start_time
        self.end_time = end_time
        self.user = user
        VapiStruct.__init__(self)


TaskInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.task_info', {
        'progress': type.OptionalType(type.ReferenceType('com.vmware.cis.task_client', 'Progress')),
        'subtasks': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'TaskInfo'))),
        'notifications': type.OptionalType(type.ReferenceType(__name__, 'Notifications')),
        'result': type.OptionalType(type.OpaqueType()),
        'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'service': type.IdType(resource_types='com.vmware.vapi.service'),
        'operation': type.IdType(resource_types='com.vmware.vapi.operation'),
        'parent': type.OptionalType(type.IdType()),
        'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        'status': type.ReferenceType('com.vmware.cis.task_client', 'Status'),
        'cancelable': type.BooleanType(),
        'error': type.OptionalType(type.AnyErrorType()),
        'start_time': type.OptionalType(type.DateTimeType()),
        'end_time': type.OptionalType(type.DateTimeType()),
        'user': type.OptionalType(type.StringType()),
    },
    TaskInfo,
    False,
    None))



class Depots(VapiInterface):
    """
    The ``Depots`` class provides methods to manage Software Depots used during
    ESX lifecycle management.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.depots'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DepotsStub)
        self._VAPI_OPERATION_IDS = {}
        self._VAPI_OPERATION_IDS.update({'sync_task': 'sync$task'})



    def sync_task(self):
        """
        Syncs the metadata from the currently configured online or umds depots.
        If any umds depot is set, then metadata is downloaded from that depot
        else metadata is downloaded from the online depots. The result of this
        operation can be queried by calling the cis/tasks/{task-id} where the
        task-id is the response of this operation.


        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
            if the service is timed out.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        """
        task_id = self._invoke('sync$task',
                                None)
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance
class _DepotsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for sync operation
        sync_input_type = type.StructType('operation-input', {})
        sync_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        sync_input_value_validator_list = [
        ]
        sync_output_validator_list = [
        ]
        sync_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/depots',
            path_variables={
            },
            query_parameters={
            },
            dispatch_parameters={
                'action': 'sync',
            },
            header_parameters={
            },
            dispatch_header_parameters={
            }
        )

        operations = {
            'sync$task': {
                'input_type': sync_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': sync_error_dict,
                'input_value_validator_list': sync_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'sync': sync_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.depots',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Depots': Depots,
        'clusters': 'com.vmware.esx.settings.clusters_client.StubFactory',
        'defaults': 'com.vmware.esx.settings.defaults_client.StubFactory',
        'depot_content': 'com.vmware.esx.settings.depot_content_client.StubFactory',
        'depots': 'com.vmware.esx.settings.depots_client.StubFactory',
        'hosts': 'com.vmware.esx.settings.hosts_client.StubFactory',
    }

