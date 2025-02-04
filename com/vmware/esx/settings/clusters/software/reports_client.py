# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.settings.clusters.software.reports.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.settings.clusters.software.reports_client`` module
provides classes to manage reports pertaining to the desired state software for
a cluster of ESXi hosts.

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
    COMPATIBLE = None
    """
    Target version is compliant with cluster hardware

    """
    INCOMPATIBLE = None
    """
    Target version is not compatible with the device present in one of the
    hosts part of this cluster.

    """
    HCL_DATA_UNAVAILABLE = None
    """
    HCL data can not be fetched to validate cluster hardware.

    """
    UNAVAILABLE = None
    """
    Hosts in cluster are not available to validate cluster hardware.

    """
    NO_FIRMWARE_PROVIDER = None
    """
    No Firmware HSM present in Software Spec to get Firmware Details null class

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`ComplianceStatus` instance.
        """
        Enum.__init__(string)

ComplianceStatus._set_values([
    ComplianceStatus('COMPATIBLE'),
    ComplianceStatus('INCOMPATIBLE'),
    ComplianceStatus('HCL_DATA_UNAVAILABLE'),
    ComplianceStatus('UNAVAILABLE'),
    ComplianceStatus('NO_FIRMWARE_PROVIDER'),
])
ComplianceStatus._set_binding_type(type.EnumType(
    'com.vmware.esx.settings.clusters.software.reports.compliance_status',
    ComplianceStatus))




class DriverFirmwareVersion(VapiStruct):
    """
    The ``DriverFirmwareVersion`` class contains information about device's
    driver and firmware version combination from Hardware Compatibility List.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 driver_version=None,
                 firmware_version=None,
                 driver_name=None,
                ):
        """
        :type  driver_version: :class:`str`
        :param driver_version: Compatible Driver Version.
        :type  firmware_version: :class:`str`
        :param firmware_version: Compatible Firmware Version.
        :type  driver_name: :class:`str`
        :param driver_name: Compatible Driver Name.
        """
        self.driver_version = driver_version
        self.firmware_version = firmware_version
        self.driver_name = driver_name
        VapiStruct.__init__(self)


DriverFirmwareVersion._set_binding_type(type.StructType(
    'com.vmware.esx.settings.clusters.software.reports.driver_firmware_version', {
        'driver_version': type.StringType(),
        'firmware_version': type.StringType(),
        'driver_name': type.StringType(),
    },
    DriverFirmwareVersion,
    False,
    None))



class PciDevice(VapiStruct):
    """
    The ``PciDevice`` class contains information about a PCI Device.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 display_name=None,
                 driver_name=None,
                 vendor=None,
                 vid=None,
                 did=None,
                 svid=None,
                 ssid=None,
                ):
        """
        :type  display_name: :class:`str`
        :param display_name: Display name of the device.
        :type  driver_name: :class:`str`
        :param driver_name: Driver Name of the device.
        :type  vendor: :class:`str`
        :param vendor: Vendor Name of the device.
        :type  vid: :class:`str`
        :param vid: PCI VID of the device.
        :type  did: :class:`str`
        :param did: PCI DID of the device.
        :type  svid: :class:`str`
        :param svid: PCI SVID of the device.
        :type  ssid: :class:`str`
        :param ssid: PCI SSID of the device.
        """
        self.display_name = display_name
        self.driver_name = driver_name
        self.vendor = vendor
        self.vid = vid
        self.did = did
        self.svid = svid
        self.ssid = ssid
        VapiStruct.__init__(self)


PciDevice._set_binding_type(type.StructType(
    'com.vmware.esx.settings.clusters.software.reports.pci_device', {
        'display_name': type.StringType(),
        'driver_name': type.StringType(),
        'vendor': type.StringType(),
        'vid': type.StringType(),
        'did': type.StringType(),
        'svid': type.StringType(),
        'ssid': type.StringType(),
    },
    PciDevice,
    False,
    None))



class PciDeviceComplianceInfo(VapiStruct):
    """
    The ``PciDeviceComplianceInfo`` class contains information that describe
    the compliance of a pci device with respect to the component present in the
    target software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 device=None,
                 compatible_versions=None,
                 host_info=None,
                 target=None,
                 supported=None,
                 compatibility_guide_link=None,
                 notifications=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Compliance status of the device.
        :type  device: :class:`PciDevice`
        :param device: Pci Device Details
        :type  compatible_versions: :class:`list` of :class:`str`
        :param compatible_versions: List of vSphere Versions compatible for this device. This field is
            populated only for device found INCOMPATIBLE
        :type  host_info: :class:`dict` of :class:`str` and :class:`com.vmware.esx.settings_client.HostInfo`
        :param host_info: Affected List of Host IDs where this device is found.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``HostSystem``. When methods return a value of this class as
            a return value, the key in the attribute :class:`dict` will be an
            identifier for the resource type: ``HostSystem``.
        :type  target: :class:`DriverFirmwareVersion`
        :param target: Driver and Firmware Version from Image Specification.
        :type  supported: :class:`list` of :class:`DriverFirmwareVersion`
        :param supported: List of Supported Driver and Firmware Version combination from
            Harware Compatibility List.
        :type  compatibility_guide_link: :class:`str` or ``None``
        :param compatibility_guide_link: Provides link to the VMware Compatibility Guide for further
            information on the compatibility.
            If None there is no VMware Compatibility link available as this is
            device used by VSAN.
        :type  notifications: :class:`com.vmware.esx.settings_client.Notifications` or ``None``
        :param notifications: Device Specific notifications describing the compliance result.
        """
        self.status = status
        self.device = device
        self.compatible_versions = compatible_versions
        self.host_info = host_info
        self.target = target
        self.supported = supported
        self.compatibility_guide_link = compatibility_guide_link
        self.notifications = notifications
        VapiStruct.__init__(self)


PciDeviceComplianceInfo._set_binding_type(type.StructType(
    'com.vmware.esx.settings.clusters.software.reports.pci_device_compliance_info', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'device': type.ReferenceType(__name__, 'PciDevice'),
        'compatible_versions': type.ListType(type.StringType()),
        'host_info': type.MapType(type.IdType(), type.ReferenceType('com.vmware.esx.settings_client', 'HostInfo')),
        'target': type.ReferenceType(__name__, 'DriverFirmwareVersion'),
        'supported': type.ListType(type.ReferenceType(__name__, 'DriverFirmwareVersion')),
        'compatibility_guide_link': type.OptionalType(type.URIType()),
        'notifications': type.OptionalType(type.ReferenceType('com.vmware.esx.settings_client', 'Notifications')),
    },
    PciDeviceComplianceInfo,
    False,
    None))



class PciDeviceCompliance(VapiStruct):
    """
    The ``PciDeviceCompliance`` class contains information that describe the
    compliance result of all pci device from all hosts in the clsuter with
    respect to the component present in the target software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 compatible_devices=None,
                 incompatible_devices=None,
                 incompatible_driver_firmware=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Over all Compliance status of PCI Devices in Cluster with
            respective to all hosts in the cluster.
        :type  compatible_devices: :class:`list` of :class:`PciDeviceComplianceInfo`
        :param compatible_devices: Compatible Device Compliance result for all devices present on all
            hosts in the cluster compared with the corresponding component in
            the software specification. The key is the DeviceName and value is
            the PciDeviceComplianceInfo object.
        :type  incompatible_devices: :class:`list` of :class:`PciDeviceComplianceInfo`
        :param incompatible_devices: Incompatible Device Compliance result for all devices present on
            all hosts in the cluster compared with the corresponding component
            in the software specification. The key is the DeviceName and value
            is the PciDeviceComplianceInfo object.
        :type  incompatible_driver_firmware: :class:`list` of :class:`PciDeviceComplianceInfo`
        :param incompatible_driver_firmware: Incompatible Driver Firmware combination Compliance result for all
            devices present on hosts in the cluster compared with the
            corresponding component in the software specification. The key is
            the DeviceName and value is the PciDeviceComplianceInfo object.
        """
        self.status = status
        self.compatible_devices = compatible_devices
        self.incompatible_devices = incompatible_devices
        self.incompatible_driver_firmware = incompatible_driver_firmware
        VapiStruct.__init__(self)


PciDeviceCompliance._set_binding_type(type.StructType(
    'com.vmware.esx.settings.clusters.software.reports.pci_device_compliance', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'compatible_devices': type.ListType(type.ReferenceType(__name__, 'PciDeviceComplianceInfo')),
        'incompatible_devices': type.ListType(type.ReferenceType(__name__, 'PciDeviceComplianceInfo')),
        'incompatible_driver_firmware': type.ListType(type.ReferenceType(__name__, 'PciDeviceComplianceInfo')),
    },
    PciDeviceCompliance,
    False,
    None))



class CheckResult(VapiStruct):
    """
    The ``CheckResult`` class contains information to describe HCL compliance
    result of a cluster on target software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                 scan_time=None,
                 v_san_data_only=None,
                 commit=None,
                 base_image_version=None,
                 pci_device_compliance=None,
                 notifications=None,
                 note=None,
                ):
        """
        :type  status: :class:`ComplianceStatus`
        :param status: Overall compliance status of Cluster with respective to all hosts
            in the cluster.
        :type  scan_time: :class:`datetime.datetime`
        :param scan_time: HCL Validation check time.
        :type  v_san_data_only: :class:`bool` or ``None``
        :param v_san_data_only: HCL Validation Computed only for vSAN Clusters.
            None to show vSAN in UI
        :type  commit: :class:`str` or ``None``
        :param commit: Spec Identifier of the desired configuration on which the HCL scan
            is performed to generate this result, populated by the HCL
            validation.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.settings.commit``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.esx.settings.commit``.
            None if validation is performed with no spec
        :type  base_image_version: :class:`str`
        :param base_image_version: Target base image version E.g., version = BaseImageSpec->Version
            :attr:`com.vmware.esx.settings_client.BaseImageSpec.version` class
        :type  pci_device_compliance: :class:`PciDeviceCompliance` or ``None``
        :param pci_device_compliance: Compliance result for the Pci Devices that are present in all hosts
            of the cluster.
        :type  notifications: :class:`com.vmware.esx.settings_client.Notifications`
        :param notifications: Notifications returned by the HCL Validation operation.
        :type  note: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param note: Localizable disclaimer notice to show on the UI detailing the type
            of checks are done by the HCL Validaiton. Example : HCL Validation
            is only done on storage and network controllers.
        """
        self.status = status
        self.scan_time = scan_time
        self.v_san_data_only = v_san_data_only
        self.commit = commit
        self.base_image_version = base_image_version
        self.pci_device_compliance = pci_device_compliance
        self.notifications = notifications
        self.note = note
        VapiStruct.__init__(self)


CheckResult._set_binding_type(type.StructType(
    'com.vmware.esx.settings.clusters.software.reports.check_result', {
        'status': type.ReferenceType(__name__, 'ComplianceStatus'),
        'scan_time': type.DateTimeType(),
        'v_san_data_only': type.OptionalType(type.BooleanType()),
        'commit': type.OptionalType(type.IdType()),
        'base_image_version': type.StringType(),
        'pci_device_compliance': type.OptionalType(type.ReferenceType(__name__, 'PciDeviceCompliance')),
        'notifications': type.ReferenceType('com.vmware.esx.settings_client', 'Notifications'),
        'note': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
    },
    CheckResult,
    False,
    None))



class ApplyImpact(VapiInterface):
    """
    The ``ApplyImpact`` class provides methods to get the impact of an apply
    method on a cluster.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.clusters.software.reports.apply_impact'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ApplyImpactStub)
        self._VAPI_OPERATION_IDS = {}

    class ApplyImpactSpec(VapiStruct):
        """
        The ``ApplyImpact.ApplyImpactSpec`` class contains attributes that describe
        the specification to be used for getting the impact of an apply method on
        an ESXi cluster.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     hosts=None,
                    ):
            """
            :type  hosts: :class:`set` of :class:`str` or ``None``
            :param hosts: The specific hosts for which an impact is to be generated.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
                if None or empty impact is generated for all hosts within the
                cluster.
            """
            self.hosts = hosts
            VapiStruct.__init__(self)


    ApplyImpactSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.reports.apply_impact.apply_impact_spec', {
            'hosts': type.OptionalType(type.SetType(type.IdType())),
        },
        ApplyImpactSpec,
        False,
        None))


    class Impact(VapiStruct):
        """
        The ``ApplyImpact.Impact`` class contains attributes that describe what the
        impact is of a particular step during the apply method.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     message=None,
                    ):
            """
            :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param message: Description of the impact.
            """
            self.message = message
            VapiStruct.__init__(self)


    Impact._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.reports.apply_impact.impact', {
            'message': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        },
        Impact,
        False,
        None))


    class ClusterImpact(VapiStruct):
        """
        The ``ApplyImpact.ClusterImpact`` class contains attributes that describe
        the summary of how hosts within a cluster will be impacted during an apply
        method.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     impact=None,
                     host_impact=None,
                     commit=None,
                     host_info=None,
                    ):
            """
            :type  impact: :class:`list` of :class:`ApplyImpact.Impact`
            :param impact: Impact of steps performed during the setup and cleanup phase of the
                apply method.
            :type  host_impact: :class:`dict` of :class:`str` and :class:`list` of :class:`ApplyImpact.Impact`
            :param host_impact: Impact summary for each host within the clsuter.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``HostSystem``. When methods return a value of this class as
                a return value, the key in the attribute :class:`dict` will be an
                identifier for the resource type: ``HostSystem``.
            :type  commit: :class:`str`
            :param commit: Identifier of the commit on which the impact is generated.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.commit``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.esx.settings.commit``.
            :type  host_info: :class:`dict` of :class:`str` and :class:`com.vmware.esx.settings_client.HostInfo`
            :param host_info: Information of hosts within the cluster.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``HostSystem``. When methods return a value of this class as
                a return value, the key in the attribute :class:`dict` will be an
                identifier for the resource type: ``HostSystem``.
            """
            self.impact = impact
            self.host_impact = host_impact
            self.commit = commit
            self.host_info = host_info
            VapiStruct.__init__(self)


    ClusterImpact._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.reports.apply_impact.cluster_impact', {
            'impact': type.ListType(type.ReferenceType(__name__, 'ApplyImpact.Impact')),
            'host_impact': type.MapType(type.IdType(), type.ListType(type.ReferenceType(__name__, 'ApplyImpact.Impact'))),
            'commit': type.IdType(resource_types='com.vmware.esx.settings.commit'),
            'host_info': type.MapType(type.IdType(), type.ReferenceType('com.vmware.esx.settings_client', 'HostInfo')),
        },
        ClusterImpact,
        False,
        None))



    def get(self,
            cluster,
            spec=None,
            ):
        """
        Returns a summary of how hosts within the cluster will be impacted
        during an apply method. The impact is generated from the compliance
        information obtained from
        :func:`com.vmware.esx.settings.clusters.software_client.Compliance.get`

        :type  cluster: :class:`str`
        :param cluster: The cluster identifier.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :type  spec: :class:`ApplyImpact.ApplyImpactSpec` or ``None``
        :param spec: 
            Specification for how much information should be returned.
        :rtype: :class:`ApplyImpact.ClusterImpact`
        :return: Summary of how hosts will be impacted during an apply method
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is an unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSoftwareRemediation.Read``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires
              ``VcIntegrity.lifecycleSoftwareRemediation.Read``.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            'spec': spec,
                            })
class HardwareCompatibility(VapiInterface):
    """
    The ``HardwareCompatibility`` class provides methods to manage HCL
    Validation of a software specification of an ESX cluster.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.clusters.software.reports.hardware_compatibility'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _HardwareCompatibilityStub)
        self._VAPI_OPERATION_IDS = {}
        self._VAPI_OPERATION_IDS.update({'check_task': 'check$task'})

    class ComplianceStatus(Enum):
        """
        The ``HardwareCompatibility.ComplianceStatus`` class contains the possible
        different status of compliance with respect to target version.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        COMPATIBLE = None
        """
        Target version is compliant with cluster hardware.

        """
        INCOMPATIBLE = None
        """
        Target version is not compatible with the device present in one of the
        hosts which is part of this cluster.

        """
        HCL_DATA_UNAVAILABLE = None
        """
        HCL data can not be fetched to validate cluster hardware.

        """
        UNAVAILABLE = None
        """
        Hosts in cluster are not available to validate cluster hardware.

        """
        NO_FIRMWARE_PROVIDER = None
        """
        No Firmware HSM present in Software Spec to get Firmware Details null class

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ComplianceStatus` instance.
            """
            Enum.__init__(string)

    ComplianceStatus._set_values([
        ComplianceStatus('COMPATIBLE'),
        ComplianceStatus('INCOMPATIBLE'),
        ComplianceStatus('HCL_DATA_UNAVAILABLE'),
        ComplianceStatus('UNAVAILABLE'),
        ComplianceStatus('NO_FIRMWARE_PROVIDER'),
    ])
    ComplianceStatus._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.clusters.software.reports.hardware_compatibility.compliance_status',
        ComplianceStatus))


    class CheckSummary(VapiStruct):
        """
        The ``HardwareCompatibility.CheckSummary`` class contains information to
        describe the HCL compliance summary result of a cluster on target software
        specification.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     scan_time=None,
                     commit=None,
                     base_image_version=None,
                     summary_result=None,
                     notifications=None,
                    ):
            """
            :type  status: :class:`HardwareCompatibility.ComplianceStatus`
            :param status: Overall compliance state of HCL Validation on the host.
            :type  scan_time: :class:`datetime.datetime`
            :param scan_time: HCL Validation check time.
            :type  commit: :class:`str` or ``None``
            :param commit: Spec Identifier of the desired configuration on which the HCL scan
                is performed to generate this result, populated by the HCL
                validation.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.commit``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.esx.settings.commit``.
                None if validation is performed with no spec
            :type  base_image_version: :class:`str`
            :param base_image_version: Target base image version E.g., version = BaseImageSpec->Version
                :attr:`com.vmware.esx.settings_client.BaseImageSpec.version` class
            :type  summary_result: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param summary_result: Over all Compliance result for cluster for the software
                specification.
            :type  notifications: :class:`com.vmware.esx.settings_client.Notifications`
            :param notifications: Notifications returned by the HCL Validation operation.
            """
            self.status = status
            self.scan_time = scan_time
            self.commit = commit
            self.base_image_version = base_image_version
            self.summary_result = summary_result
            self.notifications = notifications
            VapiStruct.__init__(self)


    CheckSummary._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.reports.hardware_compatibility.check_summary', {
            'status': type.ReferenceType(__name__, 'HardwareCompatibility.ComplianceStatus'),
            'scan_time': type.DateTimeType(),
            'commit': type.OptionalType(type.IdType()),
            'base_image_version': type.StringType(),
            'summary_result': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'notifications': type.ReferenceType('com.vmware.esx.settings_client', 'Notifications'),
        },
        CheckSummary,
        False,
        None))



    def get(self,
            cluster,
            ):
        """
        Returns the hcl validation check summary.

        :type  cluster: :class:`str`
        :param cluster: identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`HardwareCompatibility.CheckSummary`
        :return: CheckSummary hcl validation summary.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some other unknown internal error. The accompanying
            error message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })


    def check_task(self,
              cluster,
              ):
        """
        Initiates a Cluster HCL Validation check for a given cluster. The
        result of this operation can be queried by calling the
        cis/tasks/{task-id} where the task-id is the response of this
        operation.

        :type  cluster: :class:`str`
        :param cluster: Identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some other unknown internal error. The accompanying
            error message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            If the caller is not authenticated.
        """
        task_id = self._invoke('check$task',
                                {
                                'cluster': cluster,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.ReferenceType(__name__, 'CheckResult'))
        return task_instance
class LastApplyResult(VapiInterface):
    """
    The ``LastApplyResult`` class provides methods to get the most recent
    available result of applying the desired software document to all hosts
    within a cluster.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.clusters.software.reports.last_apply_result'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LastApplyResultStub)
        self._VAPI_OPERATION_IDS = {}

    class ApplyStatus(VapiStruct):
        """
        The ``LastApplyResult.ApplyStatus`` class contains attributes that describe
        the status of an apply method.

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
            :type  status: :class:`LastApplyResult.ApplyStatus.Status`
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
            The ``LastApplyResult.ApplyStatus.Status`` class contains the possible
            different status codes that can be returned while trying to apply the
            desired software specification to hosts within the cluster.

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
            'com.vmware.esx.settings.clusters.software.reports.last_apply_result.apply_status.status',
            Status))

    ApplyStatus._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.reports.last_apply_result.apply_status', {
            'status': type.ReferenceType(__name__, 'LastApplyResult.ApplyStatus.Status'),
            'start_time': type.DateTimeType(),
            'end_time': type.DateTimeType(),
            'notifications': type.ReferenceType('com.vmware.esx.settings_client', 'Notifications'),
        },
        ApplyStatus,
        False,
        None))


    class ApplyResult(VapiStruct):
        """
        The ``LastApplyResult.ApplyResult`` class contains attributes that describe
        the result of an apply method.

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
            :type  status: :class:`LastApplyResult.ApplyStatus`
            :param status: Specifies the aggregated status of the apply method.
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
                :attr:`LastApplyResult.ApplyResult.commit` should be applied to.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``HostSystem``. When methods return a value of this class as
                a return value, the key in the attribute :class:`dict` will be an
                identifier for the resource type: ``HostSystem``.
            :type  host_status: :class:`dict` of :class:`str` and :class:`LastApplyResult.ApplyStatus`
            :param host_status: Status of the hosts in this cluster to which the desired software
                document specified by the
                :attr:`LastApplyResult.ApplyResult.commit` was applied to. Hosts on
                which the apply method was sucessful are specified by
                :attr:`LastApplyResult.ApplyResult.successful_hosts`. Hosts on
                which the apply method failed are specified by
                :attr:`LastApplyResult.ApplyResult.failed_hosts`. Hosts which were
                skipped by the apply method are specified by
                :attr:`LastApplyResult.ApplyResult.skipped_hosts`.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``HostSystem``. When methods return a value of this class as
                a return value, the key in the attribute :class:`dict` will be an
                identifier for the resource type: ``HostSystem``.
            :type  successful_hosts: :class:`set` of :class:`str`
            :param successful_hosts: Hosts in this cluster to which the desired software document
                specified by the :attr:`LastApplyResult.ApplyResult.commit` has
                been successfully applied to.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
            :type  failed_hosts: :class:`set` of :class:`str`
            :param failed_hosts: Hosts in this cluster to which the desired software document
                specified by the :attr:`LastApplyResult.ApplyResult.commit` failed
                to be applied to.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
            :type  skipped_hosts: :class:`set` of :class:`str`
            :param skipped_hosts: Hosts in this cluster that were skipped by the apply method.
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
        'com.vmware.esx.settings.clusters.software.reports.last_apply_result.apply_result', {
            'status': type.ReferenceType(__name__, 'LastApplyResult.ApplyStatus'),
            'commit': type.IdType(resource_types='com.vmware.esx.settings.commit'),
            'host_info': type.MapType(type.IdType(), type.ReferenceType('com.vmware.esx.settings_client', 'HostInfo')),
            'host_status': type.MapType(type.IdType(), type.ReferenceType(__name__, 'LastApplyResult.ApplyStatus')),
            'successful_hosts': type.SetType(type.IdType()),
            'failed_hosts': type.SetType(type.IdType()),
            'skipped_hosts': type.SetType(type.IdType()),
        },
        ApplyResult,
        False,
        None))



    def get(self,
            cluster,
            ):
        """
        Returns the most recent available result of applying the desired
        software document to all hosts within the cluster.

        :type  cluster: :class:`str`
        :param cluster: The cluster identifier.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`LastApplyResult.ApplyResult`
        :return: Most recent available result of applying the desired software
            document to all hosts within the cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is an unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system or
            if there is no result associated with the cluster ``cluster``
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSoftwareRemediation.Read``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires
              ``VcIntegrity.lifecycleSoftwareRemediation.Read``.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })
class LastCheckResult(VapiInterface):
    """
    The ``LastCheckResult`` class provides methods to get the most recent
    available result of the checks that have been run on a cluster before the
    application of the desired software document to all hosts within the
    cluster.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.clusters.software.reports.last_check_result'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LastCheckResultStub)
        self._VAPI_OPERATION_IDS = {}

    class Status(Enum):
        """
        The ``LastCheckResult.Status`` class defines the status result for a
        particular check.

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
        'com.vmware.esx.settings.clusters.software.reports.last_check_result.status',
        Status))


    class CheckInfo(VapiStruct):
        """
        The ``LastCheckResult.CheckInfo`` class contains attributes that describe a
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
        'com.vmware.esx.settings.clusters.software.reports.last_check_result.check_info', {
            'check': type.StringType(),
            'name': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        },
        CheckInfo,
        False,
        None))


    class CheckStatus(VapiStruct):
        """
        The ``LastCheckResult.CheckStatus`` class contains attributes that describe
        a check result.

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
            :type  check: :class:`LastCheckResult.CheckInfo`
            :param check: Information about this check.
            :type  status: :class:`LastCheckResult.Status`
            :param status: The status of this check.
            :type  issues: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param issues: The issues encountered while running this check.
            """
            self.check = check
            self.status = status
            self.issues = issues
            VapiStruct.__init__(self)


    CheckStatus._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.reports.last_check_result.check_status', {
            'check': type.ReferenceType(__name__, 'LastCheckResult.CheckInfo'),
            'status': type.ReferenceType(__name__, 'LastCheckResult.Status'),
            'issues': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        CheckStatus,
        False,
        None))


    class EntityCheckResult(VapiStruct):
        """
        The ``LastCheckResult.EntityCheckResult`` class contains attributes that
        describe aggregated status of all checks performed on a specific entity.

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
            :type  type: :class:`LastCheckResult.EntityCheckResult.EntityType`
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
                :attr:`LastCheckResult.EntityCheckResult.EntityType.CLUSTER`.
            :type  host: :class:`str`
            :param host: If the entity type is HOST then the host identifier for which the
                checks have been run.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`LastCheckResult.EntityCheckResult.EntityType.HOST`.
            :type  status: :class:`LastCheckResult.Status`
            :param status: Aggregated status from all checks performed on this entity.
            :type  check_statuses: :class:`list` of :class:`LastCheckResult.CheckStatus`
            :param check_statuses: List of ``LastCheckResult.CheckStatus`` for all checks performed.
            """
            self.type = type
            self.cluster = cluster
            self.host = host
            self.status = status
            self.check_statuses = check_statuses
            VapiStruct.__init__(self)


        class EntityType(Enum):
            """
            The ``LastCheckResult.EntityCheckResult.EntityType`` class contains the
            entitites on which checks can be performed.

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
            'com.vmware.esx.settings.clusters.software.reports.last_check_result.entity_check_result.entity_type',
            EntityType))

    EntityCheckResult._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.reports.last_check_result.entity_check_result', {
            'type': type.ReferenceType(__name__, 'LastCheckResult.EntityCheckResult.EntityType'),
            'cluster': type.OptionalType(type.IdType()),
            'host': type.OptionalType(type.IdType()),
            'status': type.ReferenceType(__name__, 'LastCheckResult.Status'),
            'check_statuses': type.ListType(type.ReferenceType(__name__, 'LastCheckResult.CheckStatus')),
        },
        EntityCheckResult,
        False,
        None))


    class CheckResult(VapiStruct):
        """
        The ``LastCheckResult.CheckResult`` class contains attributes that describe
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
            :type  status: :class:`LastCheckResult.Status`
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
            :type  entity_results: :class:`list` of :class:`LastCheckResult.EntityCheckResult`
            :param entity_results: List of ``LastCheckResult.EntityCheckResult`` for all entities for
                which checks have been run.
            """
            self.status = status
            self.start_time = start_time
            self.end_time = end_time
            self.commit = commit
            self.host_info = host_info
            self.entity_results = entity_results
            VapiStruct.__init__(self)


    CheckResult._set_binding_type(type.StructType(
        'com.vmware.esx.settings.clusters.software.reports.last_check_result.check_result', {
            'status': type.ReferenceType(__name__, 'LastCheckResult.Status'),
            'start_time': type.DateTimeType(),
            'end_time': type.DateTimeType(),
            'commit': type.IdType(resource_types='com.vmware.esx.settings.commit'),
            'host_info': type.MapType(type.IdType(), type.ReferenceType('com.vmware.esx.settings_client', 'HostInfo')),
            'entity_results': type.ListType(type.ReferenceType(__name__, 'LastCheckResult.EntityCheckResult')),
        },
        CheckResult,
        False,
        None))



    def get(self,
            cluster,
            ):
        """
        Returns the most recent available result of checks run on the cluster
        before the application of the desired software document to all hosts
        within the cluster.

        :type  cluster: :class:`str`
        :param cluster: The cluster identifier.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`LastCheckResult.CheckResult`
        :return: Most recent result available of the checks run on the cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is an unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no cluster associated with ``cluster`` in the system or
            if there is no result associated with the cluster ``cluster``
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSoftwareRemediation.Read``.
            * The resource ``ClusterComputeResource`` referenced by the
              parameter ``cluster`` requires
              ``VcIntegrity.lifecycleSoftwareRemediation.Read``.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })
class _ApplyImpactStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'spec': type.OptionalType(type.ReferenceType(__name__, 'ApplyImpact.ApplyImpactSpec')),
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
            url_template='/esx/settings/clusters/{cluster}/software/reports/apply-impact',
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
                'output_type': type.ReferenceType(__name__, 'ApplyImpact.ClusterImpact'),
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
            self, iface_name='com.vmware.esx.settings.clusters.software.reports.apply_impact',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _HardwareCompatibilityStub(ApiInterfaceStub):
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
            url_template='/esx/settings/clusters/{cluster}/software/reports/hardware-compatibility',
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

        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        check_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        check_input_value_validator_list = [
        ]
        check_output_validator_list = [
        ]
        check_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/clusters/{cluster}/software/reports/hardware-compatibility',
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
                'output_type': type.ReferenceType(__name__, 'HardwareCompatibility.CheckSummary'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
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
            'check': check_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.clusters.software.reports.hardware_compatibility',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _LastApplyResultStub(ApiInterfaceStub):
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
            url_template='/esx/settings/clusters/{cluster}/software/reports/last-apply-result',
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
                'output_type': type.ReferenceType(__name__, 'LastApplyResult.ApplyResult'),
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
            self, iface_name='com.vmware.esx.settings.clusters.software.reports.last_apply_result',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _LastCheckResultStub(ApiInterfaceStub):
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
            url_template='/esx/settings/clusters/{cluster}/software/reports/last-check-result',
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
                'output_type': type.ReferenceType(__name__, 'LastCheckResult.CheckResult'),
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
            self, iface_name='com.vmware.esx.settings.clusters.software.reports.last_check_result',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ApplyImpact': ApplyImpact,
        'HardwareCompatibility': HardwareCompatibility,
        'LastApplyResult': LastApplyResult,
        'LastCheckResult': LastCheckResult,
        'hardware_compatibility': 'com.vmware.esx.settings.clusters.software.reports.hardware_compatibility_client.StubFactory',
    }

