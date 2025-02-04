# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.hvc.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.hvc_client`` module provides classes to manage hybrid
links between a local and remote Platform Service Controller. Usage beyond
VMware Cloud on AWS is not supported.

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


class Links(VapiInterface):
    """
    The ``Links`` class provides methods to create, delete, get information,
    and list hybrid links between the local and foreign Platform Service
    Controller (PSC). Usage beyond VMware Cloud on AWS is not supported.
    **Warning:** This class is available as Technology Preview. These are early
    access APIs provided to test, automate and provide feedback on the feature.
    Since this can change based on feedback, VMware does not guarantee
    backwards compatibility and recommends against using them in production
    environments. Some Technology Preview APIs might only be applicable to
    specific environments.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.hvc.links'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LinksStub)
        self._VAPI_OPERATION_IDS = {}

    class Summary(VapiStruct):
        """
        The ``Links.Summary`` class contains information about the hybrid link.
        **Warning:** This class is available as Technology Preview. These are early
        access APIs provided to test, automate and provide feedback on the feature.
        Since this can change based on feedback, VMware does not guarantee
        backwards compatibility and recommends against using them in production
        environments. Some Technology Preview APIs might only be applicable to
        specific environments.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     link=None,
                     display_name=None,
                    ):
            """
            :type  link: :class:`str`
            :param link: Unique identifier for the link. **Warning:** This attribute is
                available as Technology Preview. These are early access APIs
                provided to test, automate and provide feedback on the feature.
                Since this can change based on feedback, VMware does not guarantee
                backwards compatibility and recommends against using them in
                production environments. Some Technology Preview APIs might only be
                applicable to specific environments.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.hvc.Links``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.vcenter.hvc.Links``.
            :type  display_name: :class:`str`
            :param display_name: The display name is set to the domain name which was set during
                create. **Warning:** This attribute is available as Technology
                Preview. These are early access APIs provided to test, automate and
                provide feedback on the feature. Since this can change based on
                feedback, VMware does not guarantee backwards compatibility and
                recommends against using them in production environments. Some
                Technology Preview APIs might only be applicable to specific
                environments.
            """
            self.link = link
            self.display_name = display_name
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.hvc.links.summary', {
            'link': type.IdType(resource_types='com.vmware.vcenter.hvc.Links'),
            'display_name': type.StringType(),
        },
        Summary,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Links.CreateSpec`` class is the specification used for the hybrid
        link creation. **Warning:** This class is available as Technology Preview.
        These are early access APIs provided to test, automate and provide feedback
        on the feature. Since this can change based on feedback, VMware does not
        guarantee backwards compatibility and recommends against using them in
        production environments. Some Technology Preview APIs might only be
        applicable to specific environments.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     psc_hostname=None,
                     port=None,
                     domain_name=None,
                     username=None,
                     password=None,
                     ssl_thumbprint=None,
                     admin_groups=None,
                    ):
            """
            :type  psc_hostname: :class:`str`
            :param psc_hostname: The PSC hostname for the domain to be linked. **Warning:** This
                attribute is available as Technology Preview. These are early
                access APIs provided to test, automate and provide feedback on the
                feature. Since this can change based on feedback, VMware does not
                guarantee backwards compatibility and recommends against using them
                in production environments. Some Technology Preview APIs might only
                be applicable to specific environments.
            :type  port: :class:`str` or ``None``
            :param port: The HTTPS port of the PSC to be linked. **Warning:** This attribute
                is available as Technology Preview. These are early access APIs
                provided to test, automate and provide feedback on the feature.
                Since this can change based on feedback, VMware does not guarantee
                backwards compatibility and recommends against using them in
                production environments. Some Technology Preview APIs might only be
                applicable to specific environments.
                If None 443 will be used as default.
            :type  domain_name: :class:`str`
            :param domain_name: The domain to which the PSC belongs. **Warning:** This attribute is
                available as Technology Preview. These are early access APIs
                provided to test, automate and provide feedback on the feature.
                Since this can change based on feedback, VMware does not guarantee
                backwards compatibility and recommends against using them in
                production environments. Some Technology Preview APIs might only be
                applicable to specific environments.
            :type  username: :class:`str`
            :param username: The administrator username of the PSC. **Warning:** This attribute
                is available as Technology Preview. These are early access APIs
                provided to test, automate and provide feedback on the feature.
                Since this can change based on feedback, VMware does not guarantee
                backwards compatibility and recommends against using them in
                production environments. Some Technology Preview APIs might only be
                applicable to specific environments.
            :type  password: :class:`str`
            :param password: The administrator password of the PSC. **Warning:** This attribute
                is available as Technology Preview. These are early access APIs
                provided to test, automate and provide feedback on the feature.
                Since this can change based on feedback, VMware does not guarantee
                backwards compatibility and recommends against using them in
                production environments. Some Technology Preview APIs might only be
                applicable to specific environments.
            :type  ssl_thumbprint: :class:`str` or ``None``
            :param ssl_thumbprint: The ssl thumbprint of the server. **Warning:** This attribute is
                available as Technology Preview. These are early access APIs
                provided to test, automate and provide feedback on the feature.
                Since this can change based on feedback, VMware does not guarantee
                backwards compatibility and recommends against using them in
                production environments. Some Technology Preview APIs might only be
                applicable to specific environments.
                if None no thumbprint is passed.
            :type  admin_groups: :class:`set` of :class:`str` or ``None``
            :param admin_groups: List of groups to be added to enable administrator access to.
                **Warning:** This attribute is available as Technology Preview.
                These are early access APIs provided to test, automate and provide
                feedback on the feature. Since this can change based on feedback,
                VMware does not guarantee backwards compatibility and recommends
                against using them in production environments. Some Technology
                Preview APIs might only be applicable to specific environments.
                if None administrator access will not be set.
            """
            self.psc_hostname = psc_hostname
            self.port = port
            self.domain_name = domain_name
            self.username = username
            self.password = password
            self.ssl_thumbprint = ssl_thumbprint
            self.admin_groups = admin_groups
            VapiStruct.__init__(self)


    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.hvc.links.create_spec', {
            'psc_hostname': type.StringType(),
            'port': type.OptionalType(type.StringType()),
            'domain_name': type.StringType(),
            'username': type.StringType(),
            'password': type.SecretType(),
            'ssl_thumbprint': type.OptionalType(type.StringType()),
            'admin_groups': type.OptionalType(type.SetType(type.StringType())),
        },
        CreateSpec,
        False,
        None))


    class CertificateInfo(VapiStruct):
        """
        The ``Links.CertificateInfo`` class contains information about the SSL
        certificate for a destination PSC endpoint. **Warning:** This class is
        available as Technology Preview. These are early access APIs provided to
        test, automate and provide feedback on the feature. Since this can change
        based on feedback, VMware does not guarantee backwards compatibility and
        recommends against using them in production environments. Some Technology
        Preview APIs might only be applicable to specific environments.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     ssl_thumbprint=None,
                    ):
            """
            :type  ssl_thumbprint: :class:`str`
            :param ssl_thumbprint: The SHA-256 thumbprint of the SSL certificate for the destination
                PSC endpoint. **Warning:** This attribute is available as
                Technology Preview. These are early access APIs provided to test,
                automate and provide feedback on the feature. Since this can change
                based on feedback, VMware does not guarantee backwards
                compatibility and recommends against using them in production
                environments. Some Technology Preview APIs might only be applicable
                to specific environments.
            """
            self.ssl_thumbprint = ssl_thumbprint
            VapiStruct.__init__(self)


    CertificateInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.hvc.links.certificate_info', {
            'ssl_thumbprint': type.StringType(),
        },
        CertificateInfo,
        False,
        None))


    class Credentials(VapiStruct):
        """
        The ``Links.Credentials`` class specifies user credentials to make a
        successful connection to remote endpoint. **Warning:** This class is
        available as Technology Preview. These are early access APIs provided to
        test, automate and provide feedback on the feature. Since this can change
        based on feedback, VMware does not guarantee backwards compatibility and
        recommends against using them in production environments. Some Technology
        Preview APIs might only be applicable to specific environments.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     user_name=None,
                     password=None,
                    ):
            """
            :type  user_name: :class:`str`
            :param user_name: Name of the user to authenticate. **Warning:** This attribute is
                available as Technology Preview. These are early access APIs
                provided to test, automate and provide feedback on the feature.
                Since this can change based on feedback, VMware does not guarantee
                backwards compatibility and recommends against using them in
                production environments. Some Technology Preview APIs might only be
                applicable to specific environments.
            :type  password: :class:`str`
            :param password: Password for the user. **Warning:** This attribute is available as
                Technology Preview. These are early access APIs provided to test,
                automate and provide feedback on the feature. Since this can change
                based on feedback, VMware does not guarantee backwards
                compatibility and recommends against using them in production
                environments. Some Technology Preview APIs might only be applicable
                to specific environments.
            """
            self.user_name = user_name
            self.password = password
            VapiStruct.__init__(self)


    Credentials._set_binding_type(type.StructType(
        'com.vmware.vcenter.hvc.links.credentials', {
            'user_name': type.StringType(),
            'password': type.SecretType(),
        },
        Credentials,
        False,
        None))



    def create(self,
               spec,
               ):
        """
        Creates a new hybrid link between the local and foreign PSC. Usage
        beyond VMware Cloud on AWS is not supported. **Warning:** This method
        is available as Technology Preview. These are early access APIs
        provided to test, automate and provide feedback on the feature. Since
        this can change based on feedback, VMware does not guarantee backwards
        compatibility and recommends against using them in production
        environments. Some Technology Preview APIs might only be applicable to
        specific environments.

        :type  spec: :class:`Links.CreateSpec`
        :param spec: Specification for the new link to be created.
        :rtype: :class:`str`
        :return: The identifier of the newly linked domain.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.hvc.Links``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            If the link already exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the values of any of the attributes of the ``spec`` parameter
            are not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            If the PSC or the VC version is not supported.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user is not authorized.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnverifiedPeer` 
            If the SSL certificate of the foreign PSC cannot be validated by
            comparing with the thumbprint provided in
            :attr:`Links.CreateSpec.ssl_thumbprint` or if
            :attr:`Links.CreateSpec.ssl_thumbprint` is None. The value of the
            {\\\\@link UnverifiedPeer#data) attribute will be a class that
            contains all the attributes defined in
            :class:`Links.CertificateInfo`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })

    def delete(self,
               link,
               ):
        """
        Deletes an existing hybrid link. Usage beyond VMware Cloud on AWS is
        not supported. **Warning:** This method is available as Technology
        Preview. These are early access APIs provided to test, automate and
        provide feedback on the feature. Since this can change based on
        feedback, VMware does not guarantee backwards compatibility and
        recommends against using them in production environments. Some
        Technology Preview APIs might only be applicable to specific
        environments.

        :type  link: :class:`str`
        :param link: Identifier of the hybrid link.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.hvc.Links``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the hybrid link associated with ``link`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user is not authorized.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        """
        return self._invoke('delete',
                            {
                            'link': link,
                            })

    def list(self):
        """
        Enumerates the list of registered hybrid links. Usage beyond VMware
        Cloud on AWS is not supported. **Warning:** This method is available as
        Technology Preview. These are early access APIs provided to test,
        automate and provide feedback on the feature. Since this can change
        based on feedback, VMware does not guarantee backwards compatibility
        and recommends against using them in production environments. Some
        Technology Preview APIs might only be applicable to specific
        environments.


        :rtype: :class:`list` of :class:`Links.Summary`
        :return: The :class:`list` of hybrid link information.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        """
        return self._invoke('list', None)
class _LinksStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Links.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unverified_peer':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnverifiedPeer'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/hvc/links',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'link': type.IdType(resource_types='com.vmware.vcenter.hvc.Links'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/hvc/links/{link_id}',
            path_variables={
                'link': 'link_id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/hvc/links',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.hvc.Links'),
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
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Links.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.hvc.links',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Links': Links,
        'links': 'com.vmware.vcenter.hvc.links_client.StubFactory',
        'management': 'com.vmware.vcenter.hvc.management_client.StubFactory',
    }

