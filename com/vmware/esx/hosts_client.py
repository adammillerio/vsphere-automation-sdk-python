# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.hosts.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.hosts_client`` module provides classes to manage ESX host.

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


class ComponentInfo(VapiStruct):
    """
    The ``ComponentInfo`` class contains attributes that describe a specific
    component version in a software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 display_name=None,
                 display_version=None,
                 vendor=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the component.
        :type  display_name: :class:`str`
        :param display_name: Display name of the component.
        :type  display_version: :class:`str`
        :param display_version: Human readable version of the component.
        :type  vendor: :class:`str`
        :param vendor: Vendor of the component.
        """
        self.version = version
        self.display_name = display_name
        self.display_version = display_version
        self.vendor = vendor
        VapiStruct.__init__(self)


ComponentInfo._set_binding_type(type.StructType(
    'com.vmware.esx.hosts.component_info', {
        'version': type.StringType(),
        'display_name': type.StringType(),
        'display_version': type.StringType(),
        'vendor': type.StringType(),
    },
    ComponentInfo,
    False,
    None))



class SolutionInfo(VapiStruct):
    """
    The ``SolutionInfo`` class contains attributes that describe solution
    registered in the software specification.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 display_name=None,
                 components=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the solution.
        :type  display_name: :class:`str`
        :param display_name: Display name of the solution.
        :type  components: :class:`dict` of :class:`str` and :class:`ComponentInfo`
        :param components: Components registered by the solution.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.hosts.component``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.hosts.component``.
        """
        self.version = version
        self.display_name = display_name
        self.components = components
        VapiStruct.__init__(self)


SolutionInfo._set_binding_type(type.StructType(
    'com.vmware.esx.hosts.solution_info', {
        'version': type.StringType(),
        'display_name': type.StringType(),
        'components': type.MapType(type.IdType(), type.ReferenceType(__name__, 'ComponentInfo')),
    },
    SolutionInfo,
    False,
    None))



class BaseImageInfo(VapiStruct):
    """
    The ``BaseImageInfo`` class contains attributes that describe a specific
    ESX base-image.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 display_name=None,
                 display_version=None,
                 release_date=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the base-image.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.hosts.base_image``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.esx.hosts.base_image``.
        :type  display_name: :class:`str`
        :param display_name: Display name of the base-image.
        :type  display_version: :class:`str`
        :param display_version: Human readable version of the base-image.
        :type  release_date: :class:`datetime.datetime`
        :param release_date: Release date of the base-image.
        """
        self.version = version
        self.display_name = display_name
        self.display_version = display_version
        self.release_date = release_date
        VapiStruct.__init__(self)


BaseImageInfo._set_binding_type(type.StructType(
    'com.vmware.esx.hosts.base_image_info', {
        'version': type.IdType(resource_types='com.vmware.esx.hosts.base_image'),
        'display_name': type.StringType(),
        'display_version': type.StringType(),
        'release_date': type.DateTimeType(),
    },
    BaseImageInfo,
    False,
    None))



class AddOnInfo(VapiStruct):
    """
    The ``AddOnInfo`` class contains attributes that describe a specific OEM
    customization add-on.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 version=None,
                 display_name=None,
                 vendor=None,
                 display_version=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the add-on
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.hosts.add_on``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.esx.hosts.add_on``.
        :type  version: :class:`str`
        :param version: Version of the add-on
        :type  display_name: :class:`str`
        :param display_name: Display name of the OEM add-on.
        :type  vendor: :class:`str`
        :param vendor: Vendor of the OEM add-on.
        :type  display_version: :class:`str`
        :param display_version: Human readable version of the OEM add-on.
        """
        self.name = name
        self.version = version
        self.display_name = display_name
        self.vendor = vendor
        self.display_version = display_version
        VapiStruct.__init__(self)


AddOnInfo._set_binding_type(type.StructType(
    'com.vmware.esx.hosts.add_on_info', {
        'name': type.IdType(resource_types='com.vmware.esx.hosts.add_on'),
        'version': type.StringType(),
        'display_name': type.StringType(),
        'vendor': type.StringType(),
        'display_version': type.StringType(),
    },
    AddOnInfo,
    False,
    None))



class SoftwareInfo(VapiStruct):
    """
    The ``SoftwareInfo`` class contains attributes that describe desired
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
                ):
        """
        :type  base_image: :class:`BaseImageInfo`
        :param base_image: Base image of the ESX.
        :type  add_on: :class:`AddOnInfo` or ``None``
        :param add_on: OEM customization on top of given base-image. The components in
            this customization override the components in the base base-image.
            If None, no OEM customization will be applied.
        :type  components: :class:`dict` of :class:`str` and (:class:`ComponentInfo` or ``None``)
        :param components: Map of components in an ESX image. The key is the component name
            and value is the information about specific version of the
            component.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.hosts.component``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.hosts.component``.
        :type  solutions: :class:`dict` of :class:`str` and :class:`SolutionInfo`
        :param solutions: Map of software solutions in an ESX image. The key is the solution
            name and value is the specification detailing components registered
            by that solution.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.esx.hosts.solution``. When methods return a
            value of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.esx.hosts.solution``.
        """
        self.base_image = base_image
        self.add_on = add_on
        self.components = components
        self.solutions = solutions
        VapiStruct.__init__(self)


SoftwareInfo._set_binding_type(type.StructType(
    'com.vmware.esx.hosts.software_info', {
        'base_image': type.ReferenceType(__name__, 'BaseImageInfo'),
        'add_on': type.OptionalType(type.ReferenceType(__name__, 'AddOnInfo')),
        'components': type.MapType(type.IdType(), type.OptionalType(type.ReferenceType(__name__, 'ComponentInfo'))),
        'solutions': type.MapType(type.IdType(), type.ReferenceType(__name__, 'SolutionInfo')),
    },
    SoftwareInfo,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
        'software': 'com.vmware.esx.hosts.software_client.StubFactory',
    }

