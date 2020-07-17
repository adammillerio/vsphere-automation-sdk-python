# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.settings.depots.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.settings.depots_client`` module provides classes to manage
VUM compatible ESX Depots.

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


class Offline(VapiInterface):
    """
    The ``Offline`` class provides methods to manage Offline Software Depots
    used during ESX lifecycle management.
    """
    RESOURCE_TYPE = "com.vmware.esx.settings.depots.offline"
    """
    Resource type for depots resource

    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.depots.offline'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OfflineStub)
        self._VAPI_OPERATION_IDS = {}
        self._VAPI_OPERATION_IDS.update({'create_task': 'create$task'})

    class SourceType(Enum):
        """
        The ``Offline.SourceType`` class defines possible values of sources for the
        offline depot.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        PULL = None
        """
        Content is pulled from the URL location. The URL scheme of the value in
        {\\\\@link #pullLocation) can be http, https or file.

        """
        PUSH = None
        """
        Content was previously uploaded using the file upload enpoint present on
        vCenter appliance. This endpoint is present at
        https://VCENTERFQDN:9087/vum-fileupload URL.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SourceType` instance.
            """
            Enum.__init__(string)

    SourceType._set_values([
        SourceType('PULL'),
        SourceType('PUSH'),
    ])
    SourceType._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.depots.offline.source_type',
        SourceType))


    class CreateSpec(VapiStruct):
        """
        The ``Offline.CreateSpec`` class defines the information used to create a
        depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'source_type',
                {
                    'PULL' : [('location', True)],
                    'PUSH' : [('file_id', True)],
                }
            ),
        ]



        def __init__(self,
                     description=None,
                     source_type=None,
                     location=None,
                     file_id=None,
                    ):
            """
            :type  description: :class:`str` or ``None``
            :param description: Description of the depot.
                If None, the description will be empty.
            :type  source_type: :class:`Offline.SourceType`
            :param source_type: Type of the source from which offline bundle is obtained.
            :type  location: :class:`str`
            :param location: Location of the depot from which content should be retrieved.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`Offline.SourceType.PULL`.
            :type  file_id: :class:`str`
            :param file_id: File identifier returned by the file upload endpoint after file is
                uploaded.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`Offline.SourceType.PUSH`.
            """
            self.description = description
            self.source_type = source_type
            self.location = location
            self.file_id = file_id
            VapiStruct.__init__(self)


    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.offline.create_spec', {
            'description': type.OptionalType(type.StringType()),
            'source_type': type.ReferenceType(__name__, 'Offline.SourceType'),
            'location': type.OptionalType(type.URIType()),
            'file_id': type.OptionalType(type.StringType()),
        },
        CreateSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Offline.Info`` class defines the information regarding an Offline
        Depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'source_type',
                {
                    'PULL' : [('location', True)],
                    'PUSH' : [('file_id', True)],
                }
            ),
        ]



        def __init__(self,
                     description=None,
                     source_type=None,
                     location=None,
                     file_id=None,
                     create_time=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: Description of the Depot. If not set during import, it will be
                empty.
            :type  source_type: :class:`Offline.SourceType`
            :param source_type: Type of the source from which Offline Depot is obtained.
            :type  location: :class:`str`
            :param location: Location of the depot from which content is retrieved.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`Offline.SourceType.PULL`.
            :type  file_id: :class:`str`
            :param file_id: File identifier returned by the file upload endpoint after file is
                uploaded.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`Offline.SourceType.PUSH`.
            :type  create_time: :class:`datetime.datetime`
            :param create_time: Time when the depot was created.
            """
            self.description = description
            self.source_type = source_type
            self.location = location
            self.file_id = file_id
            self.create_time = create_time
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.offline.info', {
            'description': type.StringType(),
            'source_type': type.ReferenceType(__name__, 'Offline.SourceType'),
            'location': type.OptionalType(type.URIType()),
            'file_id': type.OptionalType(type.StringType()),
            'create_time': type.DateTimeType(),
        },
        Info,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Offline.Summary`` class defines the summary information regarding an
        Offline Depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'source_type',
                {
                    'PULL' : [('location', True)],
                    'PUSH' : [('file_id', True)],
                }
            ),
        ]



        def __init__(self,
                     description=None,
                     source_type=None,
                     location=None,
                     file_id=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: Description of the Depot. If not set during import, it will be
                empty.
            :type  source_type: :class:`Offline.SourceType`
            :param source_type: Type of the source from which Offline Depot is obtained.
            :type  location: :class:`str`
            :param location: Location of the depot from which content is retrieved.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`Offline.SourceType.PULL`.
            :type  file_id: :class:`str`
            :param file_id: File identifier returned by the file upload endpoint after file is
                uploaded.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`Offline.SourceType.PUSH`.
            """
            self.description = description
            self.source_type = source_type
            self.location = location
            self.file_id = file_id
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.offline.summary', {
            'description': type.StringType(),
            'source_type': type.ReferenceType(__name__, 'Offline.SourceType'),
            'location': type.OptionalType(type.URIType()),
            'file_id': type.OptionalType(type.StringType()),
        },
        Summary,
        False,
        None))


    class CreateResult(VapiStruct):
        """
        The ``Offline.CreateResult`` class defines the result information for a new
        Offline Depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     depot=None,
                    ):
            """
            :type  depot: :class:`str`
            :param depot: ID of the Offline Depot.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.esx.settings.depots.offline``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.esx.settings.depots.offline``.
            """
            self.depot = depot
            VapiStruct.__init__(self)


    CreateResult._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.offline.create_result', {
            'depot': type.IdType(resource_types='com.vmware.esx.settings.depots.offline'),
        },
        CreateResult,
        False,
        None))



    def get(self,
            depot,
            ):
        """
        Gets the information about an imported offline software depot.

        :type  depot: :class:`str`
        :param depot: Identifier for the depot.
            The parameter must be an identifier for the resource type:
            ``com.vmware.esx.settings.depots.offline``.
        :rtype: :class:`Offline.Info`
        :return: Information about the imported offline software depot.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no depot with given identifier ``depot`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('get',
                            {
                            'depot': depot,
                            })

    def list(self):
        """
        Returns currently imported offline software depots.


        :rtype: :class:`dict` of :class:`str` and :class:`Offline.Summary`
        :return: Map of currently imported offline software depots keyed by their
            identifier.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``com.vmware.esx.settings.depots.offline``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('list', None)


    def create_task(self,
               spec,
               ):
        """
        Imports a new offline software depot. This will also import the
        metadata and payloads from this offline depot. The returned task will
        fail and no Offline Depot would be created if there are any issues
        during import. The result of this operation can be queried by calling
        the cis/tasks/{task-id} where the task-id is the response of this
        operation.

        :type  spec: :class:`Offline.CreateSpec`
        :param spec: Depot specification to import an offline depot.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If an invalid pullLocation is provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            If the depot content of ``CreateSpec`` already exists. The value of
            the data attribute of
            :class:`com.vmware.vapi.std.errors_client.Error` will be a class
            that contains existing depot content id as part of depot attribute
            defined in :class:`Offline.CreateResult`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        """
        task_id = self._invoke('create$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.ReferenceType(__name__, 'Offline.CreateResult'))
        return task_instance

    def delete(self,
               depot,
               ):
        """
        Removes a depot from the list of imported offline software depots.

        :type  depot: :class:`str`
        :param depot: Identifier of the depot to be removed.
            The parameter must be an identifier for the resource type:
            ``com.vmware.esx.settings.depots.offline``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no depot associated with parameter ``depot`` in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('delete',
                            {
                            'depot': depot,
                            })
class Online(VapiInterface):
    """
    The ``Online`` class provides methods to manage Online Software Depots used
    during ESX lifecycle management.
    """
    RESOURCE_TYPE = "com.vmware.esx.settings.depots.online"
    """
    Resource type for depots resource

    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.depots.online'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OnlineStub)
        self._VAPI_OPERATION_IDS = {}

    class CreateSpec(VapiStruct):
        """
        The ``Online.CreateSpec`` class defines the information used to create a
        depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     description=None,
                     location=None,
                     enabled=None,
                    ):
            """
            :type  description: :class:`str` or ``None``
            :param description: Description of the Depot.
                If None, the description will be empty.
            :type  location: :class:`str`
            :param location: Location of the Depot. It should be the location to the index.xml
                for that depot.
            :type  enabled: :class:`bool` or ``None``
            :param enabled: Flag indicating whether this depot is enabled or not. Disabling the
                depot doesn't delete its cached metadata and payloads. It will not
                be refreshed next time depots are re-synced.
                If None the depot will be enabled.
            """
            self.description = description
            self.location = location
            self.enabled = enabled
            VapiStruct.__init__(self)


    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.online.create_spec', {
            'description': type.OptionalType(type.StringType()),
            'location': type.URIType(),
            'enabled': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Online.Info`` class defines the information regarding a Depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     description=None,
                     location=None,
                     enabled=None,
                     system_defined=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: Description of the Depot. It will be an empty string if no
                description was provided during create.
            :type  location: :class:`str`
            :param location: Location of the Depot.
            :type  enabled: :class:`bool`
            :param enabled: Flag indicating whether this depot is enabled or not.
            :type  system_defined: :class:`bool`
            :param system_defined: Flag to indicate if the depot is system defined. System defined
                depot can not be deleted.
            """
            self.description = description
            self.location = location
            self.enabled = enabled
            self.system_defined = system_defined
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.online.info', {
            'description': type.StringType(),
            'location': type.URIType(),
            'enabled': type.BooleanType(),
            'system_defined': type.BooleanType(),
        },
        Info,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Online.Summary`` class defines the summary information regarding a
        Depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     description=None,
                     location=None,
                     enabled=None,
                     system_defined=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: Description of the Depot. It will be an empty string if no
                description was provided during create.
            :type  location: :class:`str`
            :param location: Location of the Depot.
            :type  enabled: :class:`bool`
            :param enabled: Flag indicating whether this depot is enabled or not.
            :type  system_defined: :class:`bool`
            :param system_defined: Flag to indicate if the depot is system defined. System defined
                depot can not be deleted.
            """
            self.description = description
            self.location = location
            self.enabled = enabled
            self.system_defined = system_defined
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.online.summary', {
            'description': type.StringType(),
            'location': type.URIType(),
            'enabled': type.BooleanType(),
            'system_defined': type.BooleanType(),
        },
        Summary,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Online.UpdateSpec`` class defines the information used to update the
        depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     enabled=None,
                     description=None,
                    ):
            """
            :type  enabled: :class:`bool` or ``None``
            :param enabled: Flag indicating whether this depot is enabled or not. Disabling the
                depot doesn't delete its cached metadata and payloads. It will not
                be refreshed next time depots are re-synced.
                If None, enabled flag is not updated.
            :type  description: :class:`str` or ``None``
            :param description: Description of the Depot.
                If None, description is not updated.
            """
            self.enabled = enabled
            self.description = description
            VapiStruct.__init__(self)


    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.online.update_spec', {
            'enabled': type.OptionalType(type.BooleanType()),
            'description': type.OptionalType(type.StringType()),
        },
        UpdateSpec,
        False,
        None))



    def list(self):
        """
        Returns a list of currently configured online software depots.


        :rtype: :class:`dict` of :class:`str` and :class:`Online.Summary`
        :return: Map of currently configured online software depots keyed by their
            identifiers.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``com.vmware.esx.settings.depots.online``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('list', None)

    def get(self,
            depot,
            ):
        """
        Gets the information about a currently configured online software
        depot.

        :type  depot: :class:`str`
        :param depot: Identifier for the depot.
            The parameter must be an identifier for the resource type:
            ``com.vmware.esx.settings.depots.online``.
        :rtype: :class:`Online.Info`
        :return: Information of the currently configured online software depot.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no depot with given identifier ``depot`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('get',
                            {
                            'depot': depot,
                            })

    def create(self,
               spec,
               ):
        """
        Adds a new online software depot to the list of currently configured
        online software depots.

        :type  spec: :class:`Online.CreateSpec`
        :param spec: Depot information.
        :rtype: :class:`str`
        :return: Identifier of the currently configured online software depot.
            The return value will be an identifier for the resource type:
            ``com.vmware.esx.settings.depots.online``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If an invalid location is provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if depot with given location already exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })

    def delete(self,
               depot,
               ):
        """
        Removes a depot from the list of currently configured online software
        depots. It will not remove the downloaded metadata and payloads from
        that depot.

        :type  depot: :class:`str`
        :param depot: Identifier of the depot to be removed.
            The parameter must be an identifier for the resource type:
            ``com.vmware.esx.settings.depots.online``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If given depot is system defined.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no depot associated with ``depot`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('delete',
                            {
                            'depot': depot,
                            })

    def update(self,
               depot,
               spec,
               ):
        """
        Updates the configuration of a currently configured online software
        depot.

        :type  depot: :class:`str`
        :param depot: Identifier of the depot to be updated.
            The parameter must be an identifier for the resource type:
            ``com.vmware.esx.settings.depots.online``.
        :type  spec: :class:`Online.UpdateSpec`
        :param spec: Update specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If given depot is system defined.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no depot associated with parameter ``depot`` in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('update',
                            {
                            'depot': depot,
                            'spec': spec,
                            })
class SyncSchedule(VapiInterface):
    """
    The ``SyncSchedule`` class provides methods to manage Schedule of Online
    Software Depot sync.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.depots.sync_schedule'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SyncScheduleStub)
        self._VAPI_OPERATION_IDS = {}

    class Recurrence(Enum):
        """
        The ``SyncSchedule.Recurrence`` class contains the supported values for how
        often to sync from online or UMDS depots.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        HOURLY = None
        """
        Hourly.

        """
        DAILY = None
        """
        Daily.

        """
        WEEKLY = None
        """
        Weekly.

        """
        MONTHLY_BY_DAY = None
        """
        Monthly by day.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Recurrence` instance.
            """
            Enum.__init__(string)

    Recurrence._set_values([
        Recurrence('HOURLY'),
        Recurrence('DAILY'),
        Recurrence('WEEKLY'),
        Recurrence('MONTHLY_BY_DAY'),
    ])
    Recurrence._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.depots.sync_schedule.recurrence',
        Recurrence))


    class DayOfWeek(Enum):
        """
        The ``SyncSchedule.DayOfWeek`` class contains the supported days of the
        week.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SUNDAY = None
        """
        Sunday.

        """
        MONDAY = None
        """
        Monday.

        """
        TUESDAY = None
        """
        Tuesday.

        """
        WEDNESDAY = None
        """
        Wednesday.

        """
        THURSDAY = None
        """
        Thursday.

        """
        FRIDAY = None
        """
        Friday.

        """
        SATURDAY = None
        """
        Saturday.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`DayOfWeek` instance.
            """
            Enum.__init__(string)

    DayOfWeek._set_values([
        DayOfWeek('SUNDAY'),
        DayOfWeek('MONDAY'),
        DayOfWeek('TUESDAY'),
        DayOfWeek('WEDNESDAY'),
        DayOfWeek('THURSDAY'),
        DayOfWeek('FRIDAY'),
        DayOfWeek('SATURDAY'),
    ])
    DayOfWeek._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.depots.sync_schedule.day_of_week',
        DayOfWeek))


    class Schedule(VapiStruct):
        """
        The ``SyncSchedule.Schedule`` class defines a schedule.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'HOURLY' : [('skip', False), ('minute', True)],
                    'DAILY' : [('skip', False), ('minute', True), ('hour', True)],
                    'WEEKLY' : [('skip', False), ('minute', True), ('hour', True), ('day_of_week', True)],
                    'MONTHLY_BY_DAY' : [('skip', False), ('minute', True), ('hour', True), ('day_of_month', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     skip=None,
                     minute=None,
                     hour=None,
                     day_of_month=None,
                     day_of_week=None,
                    ):
            """
            :type  type: :class:`SyncSchedule.Recurrence`
            :param type: Frequency of the schedule.
            :type  skip: :class:`long` or ``None``
            :param skip: This determines the units of ``SyncSchedule.Recurrence`` to skip
                before the scheduled task runs again. For example, value of 1 for
                HOURLY type means the scheduled task runs every 2 hours. The value
                must be within the range 0 to 998.
                If None, no unit is skipped.
            :type  minute: :class:`long`
            :param minute: Minute at which schedule should be run. The value must be within
                the range 0 to 59.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`SyncSchedule.Recurrence.HOURLY`,
                :attr:`SyncSchedule.Recurrence.DAILY`,
                :attr:`SyncSchedule.Recurrence.WEEKLY`, or
                :attr:`SyncSchedule.Recurrence.MONTHLY_BY_DAY`.
            :type  hour: :class:`long`
            :param hour: Hour at which schedule should be run. The value must be within the
                range 0 to 23.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`SyncSchedule.Recurrence.DAILY`,
                :attr:`SyncSchedule.Recurrence.WEEKLY`, or
                :attr:`SyncSchedule.Recurrence.MONTHLY_BY_DAY`.
            :type  day_of_month: :class:`long`
            :param day_of_month: Day at which schedule should be run. The value must be within the
                range 1 to 31. If the value exceeds the total number of days in the
                month, the schedule will run on the last day of the month.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`SyncSchedule.Recurrence.MONTHLY_BY_DAY`.
            :type  day_of_week: :class:`SyncSchedule.DayOfWeek`
            :param day_of_week: Day of the week when schedule should be run
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`SyncSchedule.Recurrence.WEEKLY`.
            """
            self.type = type
            self.skip = skip
            self.minute = minute
            self.hour = hour
            self.day_of_month = day_of_month
            self.day_of_week = day_of_week
            VapiStruct.__init__(self)


    Schedule._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.sync_schedule.schedule', {
            'type': type.ReferenceType(__name__, 'SyncSchedule.Recurrence'),
            'skip': type.OptionalType(type.IntegerType()),
            'minute': type.OptionalType(type.IntegerType()),
            'hour': type.OptionalType(type.IntegerType()),
            'day_of_month': type.OptionalType(type.IntegerType()),
            'day_of_week': type.OptionalType(type.ReferenceType(__name__, 'SyncSchedule.DayOfWeek')),
        },
        Schedule,
        False,
        None))


    class Spec(VapiStruct):
        """
        The ``SyncSchedule.Spec`` class defines the information regarding the sync
        schedule.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     enabled=None,
                     schedule=None,
                     email_addresses=None,
                    ):
            """
            :type  enabled: :class:`bool`
            :param enabled: Flag indicating whether automatic sync is enabled or not
            :type  schedule: :class:`SyncSchedule.Schedule` or ``None``
            :param schedule: The schedule to check for new updates.
                If None the schedule must be disabled.
            :type  email_addresses: :class:`list` of :class:`str`
            :param email_addresses: Email addresses to which the notification will be sent. If empty,
                no notification is sent.
            """
            self.enabled = enabled
            self.schedule = schedule
            self.email_addresses = email_addresses
            VapiStruct.__init__(self)


    Spec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.sync_schedule.spec', {
            'enabled': type.BooleanType(),
            'schedule': type.OptionalType(type.ReferenceType(__name__, 'SyncSchedule.Schedule')),
            'email_addresses': type.ListType(type.StringType()),
        },
        Spec,
        False,
        None))



    def get(self):
        """
        Returns the currently configured software depot sync schedule.


        :rtype: :class:`SyncSchedule.Spec`
        :return: Currently configured sync schedule.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown error. The accompanying error message will
            give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('get', None)

    def set(self,
            spec=None,
            ):
        """
        Sets the software depot sync schedule.

        :type  spec: :class:`SyncSchedule.Spec` or ``None``
        :param spec: Information of the software depot sync schedule.
            If None, it will be reset to the default schedule, which is daily
            at a random hour chosen when this API is called.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If :attr:`SyncSchedule.Spec.schedule` is unset while
            :attr:`SyncSchedule.Spec.enabled` is set to true or if any of the
            values is not within valid range.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown error. The accompanying error message will
            give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('set',
                            {
                            'spec': spec,
                            })
class Umds(VapiInterface):
    """
    The ``Umds`` class provides methods to manage VMware vSphere Update Manager
    Download Service (UMDS) software depots used during ESX lifecycle
    management. This is the depot downloaded using UMDS.
    
    If a UMDS depot is specified then online depots are ignored and data is
    downloaded only from the UMDS depot.
    """

    _VAPI_SERVICE_ID = 'com.vmware.esx.settings.depots.umds'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UmdsStub)
        self._VAPI_OPERATION_IDS = {}

    class SetSpec(VapiStruct):
        """
        The ``Umds.SetSpec`` class defines the information of an UMDS depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     description=None,
                     enabled=None,
                     location=None,
                    ):
            """
            :type  description: :class:`str` or ``None``
            :param description: Description of the Depot.
                If None, the description will be empty.
            :type  enabled: :class:`bool` or ``None``
            :param enabled: Flag indicating whether or not this depot should be enabled.
                Disabling the depot doesn't delete its cached metadata and
                payloads. It will not be refreshed next time depots are re-synced.
                If None the depot will be enabled.
            :type  location: :class:`str`
            :param location: Location of the Depot. It should be the location to the index.xml
                for that depot.
            """
            self.description = description
            self.enabled = enabled
            self.location = location
            VapiStruct.__init__(self)


    SetSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.umds.set_spec', {
            'description': type.OptionalType(type.StringType()),
            'enabled': type.OptionalType(type.BooleanType()),
            'location': type.URIType(),
        },
        SetSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Umds.Info`` class defines the information regarding an UMDS Depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     description=None,
                     enabled=None,
                     location=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: Description of the Depot. It will be an empty string if no
                description was provided during create.
            :type  enabled: :class:`bool`
            :param enabled: Flag indicating whether or not this depot is enabled.
            :type  location: :class:`str`
            :param location: Location of the Depot.
            """
            self.description = description
            self.enabled = enabled
            self.location = location
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.umds.info', {
            'description': type.StringType(),
            'enabled': type.BooleanType(),
            'location': type.URIType(),
        },
        Info,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Umds.UpdateSpec`` class defines the information used to update the
        UMDS depot.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     enabled=None,
                     description=None,
                    ):
            """
            :type  enabled: :class:`bool` or ``None``
            :param enabled: Flag indicating whether or not this depot is enabled. Disabling the
                depot doesn't delete its cached metadata and payloads. It will not
                be refreshed next time depots are re-synced.
                If None, the enabled flag is not updated.
            :type  description: :class:`str` or ``None``
            :param description: Description of the Depot.
                If None, the description is not updated.
            """
            self.enabled = enabled
            self.description = description
            VapiStruct.__init__(self)


    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.esx.settings.depots.umds.update_spec', {
            'enabled': type.OptionalType(type.BooleanType()),
            'description': type.OptionalType(type.StringType()),
        },
        UpdateSpec,
        False,
        None))



    def get(self):
        """
        Gets the information about a currently configured UMDS software depot.


        :rtype: :class:`Umds.Info`
        :return: Information of the currently configured UMDS software depot.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no UMDS software depot set.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``VcIntegrity.lifecycleSettings.Read``.
        """
        return self._invoke('get', None)

    def set(self,
            spec,
            ):
        """
        Sets or overwrites information about an UMDS software depot.

        :type  spec: :class:`Umds.SetSpec`
        :param spec: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If an invalid location is provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('set',
                            {
                            'spec': spec,
                            })

    def delete(self):
        """
        Removes the configured UMDS software depot. It will not remove the
        downloaded metadata and payloads from that depot.


        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no UMDS software depot set.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('delete', None)

    def update(self,
               spec,
               ):
        """
        Updates the configuration of a currently configured UMDS software
        depot.

        :type  spec: :class:`Umds.UpdateSpec`
        :param spec: Update specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If there is no UMDS depot configured.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If there is some unknown internal error. The accompanying error
            message will give more details about the failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            If the service is not available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``VcIntegrity.lifecycleSettings.Write``.
        """
        return self._invoke('update',
                            {
                            'spec': spec,
                            })
class _OfflineStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'depot': type.IdType(resource_types='com.vmware.esx.settings.depots.offline'),
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
            url_template='/esx/settings/depots/offline/{depot}',
            path_variables={
                'depot': 'depot',
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
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/esx/settings/depots/offline',
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

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Offline.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/depots/offline',
            request_body_parameter='spec',
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

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'depot': type.IdType(resource_types='com.vmware.esx.settings.depots.offline'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/esx/settings/depots/offline/{depot}',
            path_variables={
                'depot': 'depot',
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
                'output_type': type.ReferenceType(__name__, 'Offline.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.MapType(type.IdType(), type.ReferenceType(__name__, 'Offline.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create$task': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.depots.offline',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _OnlineStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/esx/settings/depots/online',
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

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'depot': type.IdType(resource_types='com.vmware.esx.settings.depots.online'),
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
            url_template='/esx/settings/depots/online/{depot}',
            path_variables={
                'depot': 'depot',
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

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Online.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/esx/settings/depots/online',
            request_body_parameter='spec',
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

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'depot': type.IdType(resource_types='com.vmware.esx.settings.depots.online'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/esx/settings/depots/online/{depot}',
            path_variables={
                'depot': 'depot',
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
            'depot': type.IdType(resource_types='com.vmware.esx.settings.depots.online'),
            'spec': type.ReferenceType(__name__, 'Online.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/esx/settings/depots/online/{depot}',
            request_body_parameter='spec',
            path_variables={
                'depot': 'depot',
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
                'output_type': type.MapType(type.IdType(), type.ReferenceType(__name__, 'Online.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Online.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.esx.settings.depots.online'),
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
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.depots.online',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SyncScheduleStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
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
            url_template='/esx/settings/depots/sync-schedule',
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
            'spec': type.OptionalType(type.ReferenceType(__name__, 'SyncSchedule.Spec')),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/esx/settings/depots/sync-schedule',
            request_body_parameter='spec',
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
                'output_type': type.ReferenceType(__name__, 'SyncSchedule.Spec'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'set': set_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.depots.sync_schedule',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _UmdsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
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
            url_template='/esx/settings/depots/umds',
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
            'spec': type.ReferenceType(__name__, 'Umds.SetSpec'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/esx/settings/depots/umds',
            request_body_parameter='spec',
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

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {})
        delete_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/esx/settings/depots/umds',
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

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Umds.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/esx/settings/depots/umds',
            request_body_parameter='spec',
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
                'output_type': type.ReferenceType(__name__, 'Umds.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
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
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'set': set_rest_metadata,
            'delete': delete_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.esx.settings.depots.umds',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Offline': Offline,
        'Online': Online,
        'SyncSchedule': SyncSchedule,
        'Umds': Umds,
    }

