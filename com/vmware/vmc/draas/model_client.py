# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.draas.model.
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


class AbstractEntity(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'created': 'created',
                            'updated_by_user_id': 'updated_by_user_id',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 created=None,
                 updated_by_user_id=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: 
        """
        self.updated = updated
        self.user_id = user_id
        self.created = created
        self.updated_by_user_id = updated_by_user_id
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        VapiStruct.__init__(self)


AbstractEntity._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.abstract_entity', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'created': type.DateTimeType(),
        'updated_by_user_id': type.StringType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
    },
    AbstractEntity,
    False,
    None))



class ActivateSiteRecoveryConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'srm_extension_key_suffix': 'srm_extension_key_suffix',
                            }

    def __init__(self,
                 srm_extension_key_suffix=None,
                ):
        """
        :type  srm_extension_key_suffix: :class:`str` or ``None``
        :param srm_extension_key_suffix: Optional custom extension key suffix for SRM. If not specified,
            default extension key will be used. The custom extension suffix
            must contain 13 characters or less, be composed of letters,
            numbers, ., -, and _ characters. The extension suffix must begin
            and end with a letter or number. The suffix is appended to
            com.vmware.vcDr- to form the full extension key.
        """
        self.srm_extension_key_suffix = srm_extension_key_suffix
        VapiStruct.__init__(self)


ActivateSiteRecoveryConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.activate_site_recovery_config', {
        'srm_extension_key_suffix': type.OptionalType(type.StringType()),
    },
    ActivateSiteRecoveryConfig,
    False,
    None))



class ErrorResponse(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'status': 'status',
                            'path': 'path',
                            'retryable': 'retryable',
                            'error_code': 'error_code',
                            'error_messages': 'error_messages',
                            }

    def __init__(self,
                 status=None,
                 path=None,
                 retryable=None,
                 error_code=None,
                 error_messages=None,
                ):
        """
        :type  status: :class:`long`
        :param status: HTTP status code
        :type  path: :class:`str`
        :param path: Originating request URI
        :type  retryable: :class:`bool`
        :param retryable: If true, client should retry operation
        :type  error_code: :class:`str`
        :param error_code: unique error code
        :type  error_messages: :class:`list` of :class:`str`
        :param error_messages: localized error messages
        """
        self.status = status
        self.path = path
        self.retryable = retryable
        self.error_code = error_code
        self.error_messages = error_messages
        VapiStruct.__init__(self)


ErrorResponse._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.error_response', {
        'status': type.IntegerType(),
        'path': type.StringType(),
        'retryable': type.BooleanType(),
        'error_code': type.StringType(),
        'error_messages': type.ListType(type.StringType()),
    },
    ErrorResponse,
    False,
    None))



class ProvisionSrmConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'srm_extension_key_suffix': 'srm_extension_key_suffix',
                            }

    def __init__(self,
                 srm_extension_key_suffix=None,
                ):
        """
        :type  srm_extension_key_suffix: :class:`str` or ``None``
        :param srm_extension_key_suffix: Optional custom extension key suffix for SRM. If not specified,
            default extension key will be used.
        """
        self.srm_extension_key_suffix = srm_extension_key_suffix
        VapiStruct.__init__(self)


ProvisionSrmConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.provision_srm_config', {
        'srm_extension_key_suffix': type.OptionalType(type.StringType()),
    },
    ProvisionSrmConfig,
    False,
    None))



class ReplicaDisk(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'space_requirement': 'space_requirement',
                            'name': 'name',
                            'collection_id': 'collection_id',
                            'datastores_for_single_host_move': 'datastores_for_single_host_move',
                            'movable': 'movable',
                            'disk_id': 'disk_id',
                            'datastore_mo_id': 'datastore_mo_id',
                            }

    def __init__(self,
                 space_requirement=None,
                 name=None,
                 collection_id=None,
                 datastores_for_single_host_move=None,
                 movable=None,
                 disk_id=None,
                 datastore_mo_id=None,
                ):
        """
        :type  space_requirement: :class:`float` or ``None``
        :param space_requirement: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  collection_id: :class:`str` or ``None``
        :param collection_id: 
        :type  datastores_for_single_host_move: :class:`list` of :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param datastores_for_single_host_move: 
        :type  movable: :class:`bool` or ``None``
        :param movable: 
        :type  disk_id: :class:`str` or ``None``
        :param disk_id: 
        :type  datastore_mo_id: :class:`str` or ``None``
        :param datastore_mo_id: 
        """
        self.space_requirement = space_requirement
        self.name = name
        self.collection_id = collection_id
        self.datastores_for_single_host_move = datastores_for_single_host_move
        self.movable = movable
        self.disk_id = disk_id
        self.datastore_mo_id = datastore_mo_id
        VapiStruct.__init__(self)


ReplicaDisk._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.replica_disk', {
        'space_requirement': type.OptionalType(type.DoubleType()),
        'name': type.OptionalType(type.StringType()),
        'collection_id': type.OptionalType(type.StringType()),
        'datastores_for_single_host_move': type.OptionalType(type.ListType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct))),
        'movable': type.OptionalType(type.BooleanType()),
        'disk_id': type.OptionalType(type.StringType()),
        'datastore_mo_id': type.OptionalType(type.StringType()),
    },
    ReplicaDisk,
    False,
    None))



class ReplicaDiskCollection(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'collection_id': 'collection_id',
                            'generated': 'generated',
                            'disks': 'disks',
                            'placeholder_vm_mo_id': 'placeholder_vm_mo_id',
                            'name': 'name',
                            }

    def __init__(self,
                 collection_id=None,
                 generated=None,
                 disks=None,
                 placeholder_vm_mo_id=None,
                 name=None,
                ):
        """
        :type  collection_id: :class:`str` or ``None``
        :param collection_id: 
        :type  generated: :class:`datetime.datetime` or ``None``
        :param generated: 
        :type  disks: :class:`list` of :class:`ReplicaDisk` or ``None``
        :param disks: 
        :type  placeholder_vm_mo_id: :class:`str` or ``None``
        :param placeholder_vm_mo_id: 
        :type  name: :class:`str` or ``None``
        :param name: 
        """
        self.collection_id = collection_id
        self.generated = generated
        self.disks = disks
        self.placeholder_vm_mo_id = placeholder_vm_mo_id
        self.name = name
        VapiStruct.__init__(self)


ReplicaDiskCollection._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.replica_disk_collection', {
        'collection_id': type.OptionalType(type.StringType()),
        'generated': type.OptionalType(type.DateTimeType()),
        'disks': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ReplicaDisk'))),
        'placeholder_vm_mo_id': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
    },
    ReplicaDiskCollection,
    False,
    None))



class SiteRecovery(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    SITE_RECOVERY_STATE_ACTIVATING = "ACTIVATING"
    """


    """
    SITE_RECOVERY_STATE_ACTIVATED = "ACTIVATED"
    """


    """
    SITE_RECOVERY_STATE_DEACTIVATING = "DEACTIVATING"
    """


    """
    SITE_RECOVERY_STATE_DEACTIVATED = "DEACTIVATED"
    """


    """
    SITE_RECOVERY_STATE_FAILED = "FAILED"
    """


    """
    SITE_RECOVERY_STATE_CANCELED = "CANCELED"
    """


    """
    SITE_RECOVERY_STATE_DELETED = "DELETED"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'created': 'created',
                            'updated_by_user_id': 'updated_by_user_id',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'site_recovery_state': 'site_recovery_state',
                            'vr_node': 'vr_node',
                            'srm_nodes': 'srm_nodes',
                            'sddc_id': 'sddc_id',
                            'draas_h5_url': 'draas_h5_url',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 created=None,
                 updated_by_user_id=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 site_recovery_state=None,
                 vr_node=None,
                 srm_nodes=None,
                 sddc_id=None,
                 draas_h5_url=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: 
        :type  site_recovery_state: :class:`str` or ``None``
        :param site_recovery_state: Possible values are: 
            
            * :attr:`SiteRecovery.SITE_RECOVERY_STATE_ACTIVATING`
            * :attr:`SiteRecovery.SITE_RECOVERY_STATE_ACTIVATED`
            * :attr:`SiteRecovery.SITE_RECOVERY_STATE_DEACTIVATING`
            * :attr:`SiteRecovery.SITE_RECOVERY_STATE_DEACTIVATED`
            * :attr:`SiteRecovery.SITE_RECOVERY_STATE_FAILED`
            * :attr:`SiteRecovery.SITE_RECOVERY_STATE_CANCELED`
            * :attr:`SiteRecovery.SITE_RECOVERY_STATE_DELETED`
        :type  vr_node: :class:`SiteRecoveryNode` or ``None``
        :param vr_node: 
        :type  srm_nodes: :class:`list` of :class:`SiteRecoveryNode` or ``None``
        :param srm_nodes: 
        :type  sddc_id: :class:`str` or ``None``
        :param sddc_id: 
        :type  draas_h5_url: :class:`str` or ``None``
        :param draas_h5_url: 
        """
        self.updated = updated
        self.user_id = user_id
        self.created = created
        self.updated_by_user_id = updated_by_user_id
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.site_recovery_state = site_recovery_state
        self.vr_node = vr_node
        self.srm_nodes = srm_nodes
        self.sddc_id = sddc_id
        self.draas_h5_url = draas_h5_url
        VapiStruct.__init__(self)


SiteRecovery._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.site_recovery', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'created': type.DateTimeType(),
        'updated_by_user_id': type.StringType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'site_recovery_state': type.OptionalType(type.StringType()),
        'vr_node': type.OptionalType(type.ReferenceType(__name__, 'SiteRecoveryNode')),
        'srm_nodes': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SiteRecoveryNode'))),
        'sddc_id': type.OptionalType(type.StringType()),
        'draas_h5_url': type.OptionalType(type.StringType()),
    },
    SiteRecovery,
    False,
    None))



class SiteRecoveryNode(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATE_DEPLOYING = "DEPLOYING"
    """


    """
    STATE_PROVISIONED = "PROVISIONED"
    """


    """
    STATE_READY = "READY"
    """


    """
    STATE_DELETING = "DELETING"
    """


    """
    STATE_FAILED = "FAILED"
    """


    """
    STATE_CANCELED = "CANCELED"
    """


    """
    TYPE_VRMS = "VRMS"
    """


    """
    TYPE_SRM = "SRM"
    """


    """
    TYPE_VRS = "VRS"
    """


    """



    _canonical_to_pep_names = {
                            'vm_moref_id': 'vm_moref_id',
                            'ip_address': 'ip_address',
                            'hostname': 'hostname',
                            'id': 'id',
                            'state': 'state',
                            'type': 'type',
                            }

    def __init__(self,
                 vm_moref_id=None,
                 ip_address=None,
                 hostname=None,
                 id=None,
                 state=None,
                 type=None,
                ):
        """
        :type  vm_moref_id: :class:`str` or ``None``
        :param vm_moref_id: 
        :type  ip_address: :class:`str` or ``None``
        :param ip_address: 
        :type  hostname: :class:`str` or ``None``
        :param hostname: 
        :type  id: :class:`str` or ``None``
        :param id: 
        :type  state: :class:`str` or ``None``
        :param state: Possible values are: 
            
            * :attr:`SiteRecoveryNode.STATE_DEPLOYING`
            * :attr:`SiteRecoveryNode.STATE_PROVISIONED`
            * :attr:`SiteRecoveryNode.STATE_READY`
            * :attr:`SiteRecoveryNode.STATE_DELETING`
            * :attr:`SiteRecoveryNode.STATE_FAILED`
            * :attr:`SiteRecoveryNode.STATE_CANCELED`
        :type  type: :class:`str` or ``None``
        :param type: Possible values are: 
            
            * :attr:`SiteRecoveryNode.TYPE_VRMS`
            * :attr:`SiteRecoveryNode.TYPE_SRM`
            * :attr:`SiteRecoveryNode.TYPE_VRS`
        """
        self.vm_moref_id = vm_moref_id
        self.ip_address = ip_address
        self.hostname = hostname
        self.id = id
        self.state = state
        self.type = type
        VapiStruct.__init__(self)


SiteRecoveryNode._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.site_recovery_node', {
        'vm_moref_id': type.OptionalType(type.StringType()),
        'ip_address': type.OptionalType(type.StringType()),
        'hostname': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'state': type.OptionalType(type.StringType()),
        'type': type.OptionalType(type.StringType()),
    },
    SiteRecoveryNode,
    False,
    None))



class SiteRecoveryNodeVersion(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    VERSION_SOURCE_VAMICLI = "vamicli"
    """


    """
    VERSION_SOURCE_LS = "ls"
    """


    """
    NODE_TYPE_VRMS = "VRMS"
    """


    """
    NODE_TYPE_SRM = "SRM"
    """


    """
    NODE_TYPE_VRS = "VRS"
    """


    """



    _canonical_to_pep_names = {
                            'version_source': 'version_source',
                            'node_id': 'node_id',
                            'build_number': 'build_number',
                            'appliance_version': 'appliance_version',
                            'node_ip': 'node_ip',
                            'full_version': 'full_version',
                            'node_type': 'node_type',
                            }

    def __init__(self,
                 version_source=None,
                 node_id=None,
                 build_number=None,
                 appliance_version=None,
                 node_ip=None,
                 full_version=None,
                 node_type=None,
                ):
        """
        :type  version_source: :class:`str` or ``None``
        :param version_source: Possible values are: 
            
            * :attr:`SiteRecoveryNodeVersion.VERSION_SOURCE_VAMICLI`
            * :attr:`SiteRecoveryNodeVersion.VERSION_SOURCE_LS`
        :type  node_id: :class:`str` or ``None``
        :param node_id: 
        :type  build_number: :class:`str` or ``None``
        :param build_number: 
        :type  appliance_version: :class:`str` or ``None``
        :param appliance_version: 
        :type  node_ip: :class:`str` or ``None``
        :param node_ip: 
        :type  full_version: :class:`str` or ``None``
        :param full_version: 
        :type  node_type: :class:`str` or ``None``
        :param node_type: Possible values are: 
            
            * :attr:`SiteRecoveryNodeVersion.NODE_TYPE_VRMS`
            * :attr:`SiteRecoveryNodeVersion.NODE_TYPE_SRM`
            * :attr:`SiteRecoveryNodeVersion.NODE_TYPE_VRS`
        """
        self.version_source = version_source
        self.node_id = node_id
        self.build_number = build_number
        self.appliance_version = appliance_version
        self.node_ip = node_ip
        self.full_version = full_version
        self.node_type = node_type
        VapiStruct.__init__(self)


SiteRecoveryNodeVersion._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.site_recovery_node_version', {
        'version_source': type.OptionalType(type.StringType()),
        'node_id': type.OptionalType(type.StringType()),
        'build_number': type.OptionalType(type.StringType()),
        'appliance_version': type.OptionalType(type.StringType()),
        'node_ip': type.OptionalType(type.StringType()),
        'full_version': type.OptionalType(type.StringType()),
        'node_type': type.OptionalType(type.StringType()),
    },
    SiteRecoveryNodeVersion,
    False,
    None))



class SiteRecoveryVersions(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'generated': 'generated',
                            'sddc_id': 'sddc_id',
                            'node_versions': 'node_versions',
                            }

    def __init__(self,
                 generated=None,
                 sddc_id=None,
                 node_versions=None,
                ):
        """
        :type  generated: :class:`datetime.datetime` or ``None``
        :param generated: 
        :type  sddc_id: :class:`str` or ``None``
        :param sddc_id: 
        :type  node_versions: :class:`list` of :class:`SiteRecoveryNodeVersion` or ``None``
        :param node_versions: list of site recovery node version
        """
        self.generated = generated
        self.sddc_id = sddc_id
        self.node_versions = node_versions
        VapiStruct.__init__(self)


SiteRecoveryVersions._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.site_recovery_versions', {
        'generated': type.OptionalType(type.DateTimeType()),
        'sddc_id': type.OptionalType(type.StringType()),
        'node_versions': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SiteRecoveryNodeVersion'))),
    },
    SiteRecoveryVersions,
    False,
    None))



class Task(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATUS_STARTED = "STARTED"
    """


    """
    STATUS_CANCELING = "CANCELING"
    """


    """
    STATUS_FINISHED = "FINISHED"
    """


    """
    STATUS_FAILED = "FAILED"
    """


    """
    STATUS_CANCELED = "CANCELED"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'created': 'created',
                            'updated_by_user_id': 'updated_by_user_id',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'status': 'status',
                            'resource_id': 'resource_id',
                            'start_time': 'start_time',
                            'retries': 'retries',
                            'task_type': 'task_type',
                            'task_progress_phases': 'task_progress_phases',
                            'tenant_id': 'tenant_id',
                            'error_message': 'error_message',
                            'parent_task_id': 'parent_task_id',
                            'progress_percent': 'progress_percent',
                            'estimated_remaining_minutes': 'estimated_remaining_minutes',
                            'params': 'params',
                            'end_time': 'end_time',
                            'task_version': 'task_version',
                            'resource_type': 'resource_type',
                            'sub_status': 'sub_status',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 created=None,
                 updated_by_user_id=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 status=None,
                 resource_id=None,
                 start_time=None,
                 retries=None,
                 task_type=None,
                 task_progress_phases=None,
                 tenant_id=None,
                 error_message=None,
                 parent_task_id=None,
                 progress_percent=None,
                 estimated_remaining_minutes=None,
                 params=None,
                 end_time=None,
                 task_version=None,
                 resource_type=None,
                 sub_status=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: 
        :type  status: :class:`str` or ``None``
        :param status: Possible values are: 
            
            * :attr:`Task.STATUS_STARTED`
            * :attr:`Task.STATUS_CANCELING`
            * :attr:`Task.STATUS_FINISHED`
            * :attr:`Task.STATUS_FAILED`
            * :attr:`Task.STATUS_CANCELED`
        :type  resource_id: :class:`str` or ``None``
        :param resource_id: UUID of resources task is acting upon
        :type  start_time: :class:`str` or ``None``
        :param start_time: 
        :type  retries: :class:`long` or ``None``
        :param retries: 
        :type  task_type: :class:`str` or ``None``
        :param task_type: 
        :type  task_progress_phases: :class:`list` of :class:`TaskProgressPhase` or ``None``
        :param task_progress_phases: Task progress phases involved in current task execution
        :type  tenant_id: :class:`str` or ``None``
        :param tenant_id: 
        :type  error_message: :class:`str` or ``None``
        :param error_message: 
        :type  parent_task_id: :class:`str` or ``None``
        :param parent_task_id: 
        :type  progress_percent: :class:`long` or ``None``
        :param progress_percent: Estimated progress percentage the task executed format: int32
        :type  estimated_remaining_minutes: :class:`long` or ``None``
        :param estimated_remaining_minutes: Estimated remaining time in minute of the task execution, < 0 means
            no estimation for the task. format: int32
        :type  params: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param params: 
        :type  end_time: :class:`datetime.datetime` or ``None``
        :param end_time: 
        :type  task_version: :class:`str` or ``None``
        :param task_version: 
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: Type of resource being acted upon
        :type  sub_status: :class:`str` or ``None``
        :param sub_status: 
        """
        self.updated = updated
        self.user_id = user_id
        self.created = created
        self.updated_by_user_id = updated_by_user_id
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.status = status
        self.resource_id = resource_id
        self.start_time = start_time
        self.retries = retries
        self.task_type = task_type
        self.task_progress_phases = task_progress_phases
        self.tenant_id = tenant_id
        self.error_message = error_message
        self.parent_task_id = parent_task_id
        self.progress_percent = progress_percent
        self.estimated_remaining_minutes = estimated_remaining_minutes
        self.params = params
        self.end_time = end_time
        self.task_version = task_version
        self.resource_type = resource_type
        self.sub_status = sub_status
        VapiStruct.__init__(self)


Task._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.task', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'created': type.DateTimeType(),
        'updated_by_user_id': type.StringType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'status': type.OptionalType(type.StringType()),
        'resource_id': type.OptionalType(type.StringType()),
        'start_time': type.OptionalType(type.StringType()),
        'retries': type.OptionalType(type.IntegerType()),
        'task_type': type.OptionalType(type.StringType()),
        'task_progress_phases': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'TaskProgressPhase'))),
        'tenant_id': type.OptionalType(type.StringType()),
        'error_message': type.OptionalType(type.StringType()),
        'parent_task_id': type.OptionalType(type.StringType()),
        'progress_percent': type.OptionalType(type.IntegerType()),
        'estimated_remaining_minutes': type.OptionalType(type.IntegerType()),
        'params': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'end_time': type.OptionalType(type.DateTimeType()),
        'task_version': type.OptionalType(type.StringType()),
        'resource_type': type.OptionalType(type.StringType()),
        'sub_status': type.OptionalType(type.StringType()),
    },
    Task,
    False,
    None))



class TaskProgressPhase(VapiStruct):
    """
    A task progress can be (but does NOT have to be) divided to more meaningful
    progress phases.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'id': 'id',
                            'name': 'name',
                            'progress_percent': 'progress_percent',
                            }

    def __init__(self,
                 id=None,
                 name=None,
                 progress_percent=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The identifier of the task progress phase
        :type  name: :class:`str`
        :param name: The display name of the task progress phase
        :type  progress_percent: :class:`long`
        :param progress_percent: The percentage of the phase that has completed format: int32
        """
        self.id = id
        self.name = name
        self.progress_percent = progress_percent
        VapiStruct.__init__(self)


TaskProgressPhase._set_binding_type(type.StructType(
    'com.vmware.vmc.draas.model.task_progress_phase', {
        'id': type.StringType(),
        'name': type.StringType(),
        'progress_percent': type.IntegerType(),
    },
    TaskProgressPhase,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

