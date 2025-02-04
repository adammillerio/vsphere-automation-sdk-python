# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.settings.depot_content.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.settings.depot_content_client`` module provides classes to
retrieve contents from the depot.

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


class AddOns(VapiInterface):
    """
    The ``AddOns`` class provides methods to get OEM add-ons from the sync'ed
    and imported depots.
    """
    RESOURCE_TYPE = "com.vmware.esx.settings.add_on"
    """
    Resource type for add-on resource

    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.depot_content.add_ons'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _AddOnsStub)
        self._VAPI_OPERATION_IDS = {}

    class CategoryType(Enum):
        """
        The ``AddOns.CategoryType`` class defines possible values of categories for
        a OEM add-on.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SECURITY = None
        """
        Security

        """
        ENHANCEMENT = None
        """
        Enhancement

        """
        BUGFIX = None
        """
        Bugfix

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`CategoryType` instance.
            """
            Enum.__init__(string)

    CategoryType._set_values([
        CategoryType('SECURITY'),
        CategoryType('ENHANCEMENT'),
        CategoryType('BUGFIX'),
    ])
    CategoryType._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.depot_content.add_ons.category_type',
        CategoryType))


    class Summary(VapiStruct):
        """
        The ``AddOns.Summary`` class defines the summary information regarding a
        OEM add-on.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     display_name=None,
                     vendor=None,
                     versions=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Name of the OEM add-on.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.add_on``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.esx.settings.add_on``.
            :type  display_name: :class:`str`
            :param display_name: Display name of the OEM add-on.
            :type  vendor: :class:`str`
            :param vendor: Vendor of the OEM add-on.
            :type  versions: :class:`list` of :class:`AddOns.AddOnVersionSummary`
            :param versions: Summary information about the versions of this addon. These are
                sorted by the version.
            """
            self.name = name
            self.display_name = display_name
            self.vendor = vendor
            self.versions = versions
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depot_content.add_ons.summary', {
            'name': type.IdType(resource_types='com.vmware.esx.settings.add_on'),
            'display_name': type.StringType(),
            'vendor': type.StringType(),
            'versions': type.ListType(type.ReferenceType(__name__, 'AddOns.AddOnVersionSummary')),
        },
        Summary,
        False,
        None))


    class AddOnVersionSummary(VapiStruct):
        """
        The ``AddOns.AddOnVersionSummary`` class defines the summary information
        regarding a version of an OEM add-on.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     version=None,
                     display_version=None,
                     summary=None,
                     category=None,
                     kb=None,
                     release_date=None,
                    ):
            """
            :type  version: :class:`str`
            :param version: Version of the OEM add-on.
            :type  display_version: :class:`str`
            :param display_version: Human readable version of the OEM add-on.
            :type  summary: :class:`str`
            :param summary: Summary of the OEM add-on version.
            :type  category: :class:`AddOns.CategoryType`
            :param category: Category of the OEM add-on version.
            :type  kb: :class:`str`
            :param kb: Link to kb article related to this the OEM add-on version.
            :type  release_date: :class:`datetime.datetime`
            :param release_date: Release date of the OEM add-on version.
            """
            self.version = version
            self.display_version = display_version
            self.summary = summary
            self.category = category
            self.kb = kb
            self.release_date = release_date
            VapiStruct.__init__(self)


    AddOnVersionSummary._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depot_content.add_ons.add_on_version_summary', {
            'version': type.StringType(),
            'display_version': type.StringType(),
            'summary': type.StringType(),
            'category': type.ReferenceType(__name__, 'AddOns.CategoryType'),
            'kb': type.URIType(),
            'release_date': type.DateTimeType(),
        },
        AddOnVersionSummary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``AddOns.FilterSpec`` class contains attributes used to filter the
        results when listing OEM add-ons, see :func:`AddOns.list`).

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vendors=None,
                     names=None,
                     versions=None,
                     min_version=None,
                    ):
            """
            :type  vendors: :class:`set` of :class:`str` or ``None``
            :param vendors: Vendors that an add-on must have to match the filter.
                If None or empty, add-ons from any vendor will match the filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that an add-on must have to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.esx.settings.add_on``. When methods return a value of
                this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.esx.settings.add_on``.
                If None or empty, add-ons with any name will match the filter.
            :type  versions: :class:`set` of :class:`str` or ``None``
            :param versions: Versions that an add-on must have to match the filter.
                If None or empty, add-ons with any version will match the filter.
            :type  min_version: :class:`str` or ``None``
            :param min_version: Minimum version of an add-on that can match the filter.
                If :class:`set`, only OEM add-ons with version greater than or
                equal to this will be returned.
            """
            self.vendors = vendors
            self.names = names
            self.versions = versions
            self.min_version = min_version
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depot_content.add_ons.filter_spec', {
            'vendors': type.OptionalType(type.SetType(type.StringType())),
            'names': type.OptionalType(type.SetType(type.IdType())),
            'versions': type.OptionalType(type.SetType(type.StringType())),
            'min_version': type.OptionalType(type.StringType()),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns a list of currently available OEM add-ons in the depot.

        :type  filter: :class:`AddOns.FilterSpec` or ``None``
        :param filter: The specification of matching OEM add-ons.
            If None, the behavior is equivalent to a :class:`AddOns.FilterSpec`
            with all attributes None, which means all OEM add-ons match the
            filter.
        :rtype: :class:`list` of :class:`AddOns.Summary`
        :return: List of OEM add-ons in the depot.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is unknown internal error. The accompanying error message
            will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class BaseImages(VapiInterface):
    """
    The ``BaseImages`` class provides methods to get base-images from the
    sync'ed and imported depots.
    """
    RESOURCE_TYPE = "com.vmware.esx.settings.base_image"
    """
    Resource type for add-on resource

    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.depot_content.base_images'
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

    class CategoryType(Enum):
        """
        The ``BaseImages.CategoryType`` class defines possible values of categories
        for a base-image.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SECURITY = None
        """
        Security

        """
        ENHANCEMENT = None
        """
        Enhancement

        """
        BUGFIX = None
        """
        Bugfix

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`CategoryType` instance.
            """
            Enum.__init__(string)

    CategoryType._set_values([
        CategoryType('SECURITY'),
        CategoryType('ENHANCEMENT'),
        CategoryType('BUGFIX'),
    ])
    CategoryType._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.depot_content.base_images.category_type',
        CategoryType))


    class Summary(VapiStruct):
        """
        The ``BaseImages.Summary`` class defines the summary information regarding
        a base-image.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     display_name=None,
                     version=None,
                     display_version=None,
                     summary=None,
                     category=None,
                     kb=None,
                     release_date=None,
                    ):
            """
            :type  display_name: :class:`str`
            :param display_name: Display name of the base-image.
            :type  version: :class:`str`
            :param version: Version of the base-image.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.base_image``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.esx.settings.base_image``.
            :type  display_version: :class:`str`
            :param display_version: Human readable version of the base-image.
            :type  summary: :class:`str`
            :param summary: Summary of the base-image.
            :type  category: :class:`BaseImages.CategoryType`
            :param category: Category of the base-image.
            :type  kb: :class:`str`
            :param kb: Link to kb article related to this the base-image.
            :type  release_date: :class:`datetime.datetime`
            :param release_date: Release date of the base-image.
            """
            self.display_name = display_name
            self.version = version
            self.display_version = display_version
            self.summary = summary
            self.category = category
            self.kb = kb
            self.release_date = release_date
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depot_content.base_images.summary', {
            'display_name': type.StringType(),
            'version': type.IdType(resource_types='com.vmware.esx.settings.base_image'),
            'display_version': type.StringType(),
            'summary': type.StringType(),
            'category': type.ReferenceType(__name__, 'BaseImages.CategoryType'),
            'kb': type.URIType(),
            'release_date': type.DateTimeType(),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``BaseImages.FilterSpec`` class contains attributes used to filter the
        results when listing base-images, see :func:`BaseImages.list`).

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     min_version=None,
                    ):
            """
            :type  min_version: :class:`str` or ``None``
            :param min_version: Minimum version of a base-image that can match the filter.
                If :class:`set`, only base-images with version greater than or
                equal to this version will be returned.
            """
            self.min_version = min_version
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depot_content.base_images.filter_spec', {
            'min_version': type.OptionalType(type.StringType()),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns a list of currently available base-images in the depot.

        :type  filter: :class:`BaseImages.FilterSpec` or ``None``
        :param filter: The specification of matching base-images.
            If None, the behavior is equivalent to a
            :class:`BaseImages.FilterSpec` with all attributes None, which
            means all base-images match the filter.
        :rtype: :class:`list` of :class:`BaseImages.Summary`
        :return: List of base-images in the depot. These will be sorted by the
            version of the base-image.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is unknown internal error. The accompanying error message
            will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class Components(VapiInterface):
    """
    The ``Components`` class provides methods to get Components from the
    sync'ed and imported depots.
    """
    RESOURCE_TYPE = "com.vmware.esx.settings.component"
    """
    Resource type for add-on resource

    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.depot_content.components'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComponentsStub)
        self._VAPI_OPERATION_IDS = {}

    class CategoryType(Enum):
        """
        The ``Components.CategoryType`` class defines possible values of categories
        for a component.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SECURITY = None
        """
        Security

        """
        ENHANCEMENT = None
        """
        Enhancement

        """
        BUGFIX = None
        """
        Bugfix

        """
        RECALL = None
        """
        Recall

        """
        RECALL_FIX = None
        """
        Recall-fix

        """
        INFO = None
        """
        Info

        """
        MISC = None
        """
        Misc

        """
        GENERAL = None
        """
        General

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`CategoryType` instance.
            """
            Enum.__init__(string)

    CategoryType._set_values([
        CategoryType('SECURITY'),
        CategoryType('ENHANCEMENT'),
        CategoryType('BUGFIX'),
        CategoryType('RECALL'),
        CategoryType('RECALL_FIX'),
        CategoryType('INFO'),
        CategoryType('MISC'),
        CategoryType('GENERAL'),
    ])
    CategoryType._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.depot_content.components.category_type',
        CategoryType))


    class UrgencyType(Enum):
        """
        The ``Components.UrgencyType`` class defines possible values of urgencies
        for a component.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        CRITICAL = None
        """
        Critical

        """
        IMPORTANT = None
        """
        Important

        """
        MODERATE = None
        """
        Moderate

        """
        LOW = None
        """
        Low

        """
        GENERAL = None
        """
        General

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`UrgencyType` instance.
            """
            Enum.__init__(string)

    UrgencyType._set_values([
        UrgencyType('CRITICAL'),
        UrgencyType('IMPORTANT'),
        UrgencyType('MODERATE'),
        UrgencyType('LOW'),
        UrgencyType('GENERAL'),
    ])
    UrgencyType._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.depot_content.components.urgency_type',
        UrgencyType))


    class ComponentBundleType(Enum):
        """
        The ``Components.ComponentBundleType`` class defines possible ways
        components are bundled.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        INDEPENDENT = None
        """
        Components not bundled in base-images or add-ons

        """
        BASE_IMAGE = None
        """
        Components bundled in base-images

        """
        ADD_ON = None
        """
        Components bundled in add-ons

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ComponentBundleType` instance.
            """
            Enum.__init__(string)

    ComponentBundleType._set_values([
        ComponentBundleType('INDEPENDENT'),
        ComponentBundleType('BASE_IMAGE'),
        ComponentBundleType('ADD_ON'),
    ])
    ComponentBundleType._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.depot_content.components.component_bundle_type',
        ComponentBundleType))


    class Summary(VapiStruct):
        """
        The ``Components.Summary`` class defines the summary information regarding
        a component.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     display_name=None,
                     vendor=None,
                     versions=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Name of the Component.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.component``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.esx.settings.component``.
            :type  display_name: :class:`str`
            :param display_name: Display name of the component.
            :type  vendor: :class:`str`
            :param vendor: Vendor of the component.
            :type  versions: :class:`list` of :class:`Components.ComponentVersionSummary`
            :param versions: Summary information about the versions of this component. These are
                sorted by the version.
            """
            self.name = name
            self.display_name = display_name
            self.vendor = vendor
            self.versions = versions
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depot_content.components.summary', {
            'name': type.IdType(resource_types='com.vmware.esx.settings.component'),
            'display_name': type.StringType(),
            'vendor': type.StringType(),
            'versions': type.ListType(type.ReferenceType(__name__, 'Components.ComponentVersionSummary')),
        },
        Summary,
        False,
        None))


    class ComponentVersionSummary(VapiStruct):
        """
        The ``Components.ComponentVersionSummary`` class defines the summary
        information regarding a version of a component.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     version=None,
                     display_version=None,
                     summary=None,
                     category=None,
                     urgency=None,
                     kb=None,
                     release_date=None,
                    ):
            """
            :type  version: :class:`str`
            :param version: Version of the component.
            :type  display_version: :class:`str`
            :param display_version: Human readable version of the component.
            :type  summary: :class:`str`
            :param summary: Summary of the component version.
            :type  category: :class:`Components.CategoryType`
            :param category: Category of the component version.
            :type  urgency: :class:`Components.UrgencyType`
            :param urgency: Urgency of the component version.
            :type  kb: :class:`str`
            :param kb: Link to kb article related to this the component version.
            :type  release_date: :class:`datetime.datetime`
            :param release_date: Release date of the component version.
            """
            self.version = version
            self.display_version = display_version
            self.summary = summary
            self.category = category
            self.urgency = urgency
            self.kb = kb
            self.release_date = release_date
            VapiStruct.__init__(self)


    ComponentVersionSummary._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depot_content.components.component_version_summary', {
            'version': type.StringType(),
            'display_version': type.StringType(),
            'summary': type.StringType(),
            'category': type.ReferenceType(__name__, 'Components.CategoryType'),
            'urgency': type.ReferenceType(__name__, 'Components.UrgencyType'),
            'kb': type.URIType(),
            'release_date': type.DateTimeType(),
        },
        ComponentVersionSummary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Components.FilterSpec`` class contains attributes used to filter the
        results when listing components, see :func:`Components.list`).

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vendors=None,
                     names=None,
                     versions=None,
                     min_version=None,
                     bundle_types=None,
                    ):
            """
            :type  vendors: :class:`set` of :class:`str` or ``None``
            :param vendors: Vendors that a component must have to match the filter.
                If None or empty, components with any vendor name match the filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that a component must have to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.esx.settings.component``. When methods return a value
                of this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.esx.settings.component``.
                If None or empty, components with any name will match the filter.
            :type  versions: :class:`set` of :class:`str` or ``None``
            :param versions: Versions that a component must have to match the filter.
                If None or empty, components with any version will match the
                filter.
            :type  min_version: :class:`str` or ``None``
            :param min_version: Minimum version of the component that can match the filter.
                If :class:`set`, only components with version greater than or equal
                to the given version match the filter.
            :type  bundle_types: :class:`set` of :class:`Components.ComponentBundleType` or ``None``
            :param bundle_types: Component bundle types that a component must have to match the
                filter.
                If None or empty, all components will match the filter.
            """
            self.vendors = vendors
            self.names = names
            self.versions = versions
            self.min_version = min_version
            self.bundle_types = bundle_types
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depot_content.components.filter_spec', {
            'vendors': type.OptionalType(type.SetType(type.StringType())),
            'names': type.OptionalType(type.SetType(type.IdType())),
            'versions': type.OptionalType(type.SetType(type.StringType())),
            'min_version': type.OptionalType(type.StringType()),
            'bundle_types': type.OptionalType(type.SetType(type.ReferenceType(__name__, 'Components.ComponentBundleType'))),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns a list of currently available components in the depot.

        :type  filter: :class:`Components.FilterSpec` or ``None``
        :param filter: The specification of matching components.
            If None, the behavior is equivalent to a
            :class:`Components.FilterSpec` with all attributes None, which
            means ALL components match the filter.
        :rtype: :class:`list` of :class:`Components.Summary`
        :return: List of components in the depot.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is unknown internal error. The accompanying error message
            will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class _AddOnsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'AddOns.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/esx/settings/depot-content/add-ons',
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'AddOns.Summary')),
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
            self, iface_name='com.vmware.esx.settings.depot_content.add_ons',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _BaseImagesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'BaseImages.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/esx/settings/depot-content/base-images',
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'BaseImages.Summary')),
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
            self, iface_name='com.vmware.esx.settings.depot_content.base_images',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ComponentsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Components.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/esx/settings/depot-content/components',
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'Components.Summary')),
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
            self, iface_name='com.vmware.esx.settings.depot_content.components',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'AddOns': AddOns,
        'BaseImages': BaseImages,
        'Components': Components,
        'add_ons': 'com.vmware.esx.settings.depot_content.add_ons_client.StubFactory',
        'base_images': 'com.vmware.esx.settings.depot_content.base_images_client.StubFactory',
        'components': 'com.vmware.esx.settings.depot_content.components_client.StubFactory',
    }

