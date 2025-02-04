# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.content.registries.harbor.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.content.registries.harbor_client`` module provides
classes and classes for managing Harbor registry in vCenter.

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


class Projects(VapiInterface):
    """
    The ``Projects`` class provides methods for managing the lifecycle of
    Harbor project that stores and distributes container repositories and
    images.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.content.registries.harbor.projects'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ProjectsStub)
        self._VAPI_OPERATION_IDS = {}

    class Scope(Enum):
        """
        The ``Projects.Scope`` class in a project defines access levels of the
        project.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        PUBLIC = None
        """
        A Harbor project can be accessed by everyone.

        """
        PRIVATE = None
        """
        A Harbor project can only be accessed by assigned users.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Scope` instance.
            """
            Enum.__init__(string)

    Scope._set_values([
        Scope('PUBLIC'),
        Scope('PRIVATE'),
    ])
    Scope._set_binding_type(type.EnumType(
        'com.vmware.vcenter.content.registries.harbor.projects.scope',
        Scope))


    class ConfigStatus(Enum):
        """
        The ``Projects.ConfigStatus`` class describes the status of reaching the
        desired configuration state for the Harbor project.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        PENDING = None
        """
        Harbor project is being created or the configuration is being applied to
        the project.

        """
        REMOVING = None
        """
        The configuration is being removed and Harbor project is being deleted.

        """
        ERROR = None
        """
        Failed to create Harbor project or apply the configuration to the project,
        user intervention needed.

        """
        READY = None
        """
        Harbor project is created or configured correctly.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ConfigStatus` instance.
            """
            Enum.__init__(string)

    ConfigStatus._set_values([
        ConfigStatus('PENDING'),
        ConfigStatus('REMOVING'),
        ConfigStatus('ERROR'),
        ConfigStatus('READY'),
    ])
    ConfigStatus._set_binding_type(type.EnumType(
        'com.vmware.vcenter.content.registries.harbor.projects.config_status',
        ConfigStatus))


    class CreateSpec(VapiStruct):
        """
        The ``Projects.CreateSpec`` class defines the information required to
        create a Harbor project.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     scope=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Name of the Harbor project. Should be between 2-63 characters long
                alphanumeric string and may contain the following characters:
                a-z,0-9, and '-'. Must be starting with characters or numbers, with
                the '-' character allowed anywhere except the first or last
                character.
            :type  scope: :class:`Projects.Scope`
            :param scope: Access type of a Harbor project.
            """
            self.name = name
            self.scope = scope
            VapiStruct.__init__(self)


    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.content.registries.harbor.projects.create_spec', {
            'name': type.StringType(),
            'scope': type.ReferenceType(__name__, 'Projects.Scope'),
        },
        CreateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Projects.Summary`` class contains basic information about a Harbor
        project.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     project=None,
                     name=None,
                     scope=None,
                    ):
            """
            :type  project: :class:`str`
            :param project: Identifier of the harbor project.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.content.Registry.Harbor.Project``. When
                methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type:
                ``com.vmware.vcenter.content.Registry.Harbor.Project``.
            :type  name: :class:`str`
            :param name: Name of the Harbor project. Should be between 2-63 characters long
                alphanumeric string and may contain the following characters:
                a-z,0-9, and '-'. Must be starting with characters or numbers, with
                the '-' character allowed anywhere except the first or last
                character.
            :type  scope: :class:`Projects.Scope`
            :param scope: Access type of a Harbor project.
            """
            self.project = project
            self.name = name
            self.scope = scope
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.content.registries.harbor.projects.summary', {
            'project': type.IdType(resource_types='com.vmware.vcenter.content.Registry.Harbor.Project'),
            'name': type.StringType(),
            'scope': type.ReferenceType(__name__, 'Projects.Scope'),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Projects.Info`` class contains detailed information about a Harbor
        project.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'config_status',
                {
                    'READY' : [('update_time', True), ('access_url', True)],
                    'ERROR' : [('message', True)],
                    'PENDING' : [],
                    'REMOVING' : [],
                }
            ),
        ]



        def __init__(self,
                     name=None,
                     config_status=None,
                     scope=None,
                     creation_time=None,
                     update_time=None,
                     access_url=None,
                     message=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Name of the Harbor project. Should be between 2-63 characters long
                alphanumeric string and may contain the following characters:
                a-z,0-9, and '-'. Must be starting with characters or numbers, with
                the '-' character allowed anywhere except the first or last
                character.
            :type  config_status: :class:`Projects.ConfigStatus`
            :param config_status: The status of the Harbor project.
            :type  scope: :class:`Projects.Scope`
            :param scope: The access type of a Harbor project.
            :type  creation_time: :class:`datetime.datetime`
            :param creation_time: The date and time when the harbor project creation API was
                triggered and project identifier generated.
            :type  update_time: :class:`datetime.datetime`
            :param update_time: The date and time when the harbor project purge API was triggered.
                In case no purge was triggered, ``updateTime`` is same as
                ``creationTime``.
                This attribute is optional and it is only relevant when the value
                of ``configStatus`` is :attr:`Projects.ConfigStatus.READY`.
            :type  access_url: :class:`str`
            :param access_url: URL to access the harbor project through docker client.
                This attribute is optional and it is only relevant when the value
                of ``configStatus`` is :attr:`Projects.ConfigStatus.READY`.
            :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param message: Details about the ERROR project status.
                This attribute is optional and it is only relevant when the value
                of ``configStatus`` is :attr:`Projects.ConfigStatus.ERROR`.
            """
            self.name = name
            self.config_status = config_status
            self.scope = scope
            self.creation_time = creation_time
            self.update_time = update_time
            self.access_url = access_url
            self.message = message
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.content.registries.harbor.projects.info', {
            'name': type.StringType(),
            'config_status': type.ReferenceType(__name__, 'Projects.ConfigStatus'),
            'scope': type.ReferenceType(__name__, 'Projects.Scope'),
            'creation_time': type.DateTimeType(),
            'update_time': type.OptionalType(type.DateTimeType()),
            'access_url': type.OptionalType(type.URIType()),
            'message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        Info,
        False,
        None))



    def create(self,
               registry,
               spec,
               ):
        """
        Creates a project in a Harbor registry using the supplied
        specification. In vSphere 7.0, a Harbor registry is deployed in a
        vSphere cluster with vSphere namespaces enabled. When a namespace is
        created, a project with same name as the namespace is created in the
        Harbor registry, so this method should not be called.

        :type  registry: :class:`str`
        :param registry: Identifier of the Registry.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry``.
        :type  spec: :class:`Projects.CreateSpec`
        :param spec: Information used to create the Harbor project.
        :rtype: :class:`str`
        :return: Identifier of the newly created Harbor project.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry.Harbor.Project``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if ``spec`` contains any error.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if Harbor registry is being deleted.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a registry specified by ``registry`` could not be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if a project with the same name already exists in the registry. In
            vSphere 7.0, the existing project could have been created
            automatically when a namespace with the same name is created.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have ContentLibrary.ManageRegistryProject
            privilege.
        """
        return self._invoke('create',
                            {
                            'registry': registry,
                            'spec': spec,
                            })

    def delete(self,
               registry,
               project,
               ):
        """
        Deletes the specified project from Harbor registry. Repositories and
        images in the project will be removed upon project deletion. Storage
        space of deleted images in the project will be reclaimed through next
        scheduled Harbor registry garbage collection. In vSphere 7.0, a Harbor
        registry is deployed in a vSphere cluster with vSphere namespaces
        enabled. When a namespace is deleted, a project with same name as the
        namespace is deleted from the Harbor registry, so this method should
        not be called.

        :type  registry: :class:`str`
        :param registry: Identifier of the registry.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry``.
        :type  project: :class:`str`
        :param project: Identifier of the Harbor project.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry.Harbor.Project``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if Harbor registry is being deleted.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``registry`` or ``project`` cannot be found. In vSphere 7.0, the
            existing project could have been deleted automatically when a
            namespace with the same name is deleted.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have ContentLibrary.ManageRegistryProject
            privilege.
        """
        return self._invoke('delete',
                            {
                            'registry': registry,
                            'project': project,
                            })

    def get(self,
            registry,
            project,
            ):
        """
        Returns detailed information about the specified Harbor project.

        :type  registry: :class:`str`
        :param registry: Identifier of the registry.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry``.
        :type  project: :class:`str`
        :param project: Identifier of the Harbor project.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry.Harbor.Project``.
        :rtype: :class:`Projects.Info`
        :return: Detailed information about the specified Harbor project.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``registry`` or ``project`` cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('get',
                            {
                            'registry': registry,
                            'project': project,
                            })

    def list(self,
             registry,
             ):
        """
        Returns basic information of all projects in a Harbor registry.

        :type  registry: :class:`str`
        :param registry: Identifier of the registry.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry``.
        :rtype: :class:`list` of :class:`Projects.Summary`
        :return: The list of summary information of all Harbor projects.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``registry`` cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have System.Read privilege.
        """
        return self._invoke('list',
                            {
                            'registry': registry,
                            })

    def purge(self,
              registry,
              project,
              ):
        """
        Remove all repositories, images and members in the project. Storage
        space of deleted images in the project will be reclaimed through next
        scheduled Harbor registry garbage collection.

        :type  registry: :class:`str`
        :param registry: Registry identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry``.
        :type  project: :class:`str`
        :param project: Identifier of the Harbor project.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.content.Registry.Harbor.Project``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``registry`` or ``project`` cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if Harbor registry is being deleted or the project is not in
            :attr:`Projects.ConfigStatus.READY` status.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have ContentLibrary.ManageRegistryProject
            privilege.
        """
        return self._invoke('purge',
                            {
                            'registry': registry,
                            'project': project,
                            })
class _ProjectsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'registry': type.IdType(resource_types='com.vmware.vcenter.content.Registry'),
            'spec': type.ReferenceType(__name__, 'Projects.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
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
            url_template='/vcenter/content/registries/harbor/{registry}/projects',
            path_variables={
                'registry': 'registry',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'registry': type.IdType(resource_types='com.vmware.vcenter.content.Registry'),
            'project': type.IdType(resource_types='com.vmware.vcenter.content.Registry.Harbor.Project'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/content/registries/harbor/{registry}/projects/{project}',
            path_variables={
                'registry': 'registry',
                'project': 'project',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'registry': type.IdType(resource_types='com.vmware.vcenter.content.Registry'),
            'project': type.IdType(resource_types='com.vmware.vcenter.content.Registry.Harbor.Project'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/content/registries/harbor/{registry}/projects/{project}',
            path_variables={
                'registry': 'registry',
                'project': 'project',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'registry': type.IdType(resource_types='com.vmware.vcenter.content.Registry'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/content/registries/harbor/{registry}/projects',
            path_variables={
                'registry': 'registry',
            },
            query_parameters={
            }
        )

        # properties for purge operation
        purge_input_type = type.StructType('operation-input', {
            'registry': type.IdType(resource_types='com.vmware.vcenter.content.Registry'),
            'project': type.IdType(resource_types='com.vmware.vcenter.content.Registry.Harbor.Project'),
        })
        purge_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        purge_input_value_validator_list = [
        ]
        purge_output_validator_list = [
        ]
        purge_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/content/registries/harbor/{registry}/projects/{project}?action=purge',
            path_variables={
                'registry': 'registry',
                'project': 'project',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.content.Registry.Harbor.Project'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Projects.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Projects.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'purge': {
                'input_type': purge_input_type,
                'output_type': type.VoidType(),
                'errors': purge_error_dict,
                'input_value_validator_list': purge_input_value_validator_list,
                'output_validator_list': purge_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'purge': purge_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.content.registries.harbor.projects',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Projects': Projects,
    }

