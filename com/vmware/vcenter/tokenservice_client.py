# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.tokenservice.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.tokenservice_client`` module provides Token classes.

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


class Error(VapiError):
    """
    The ``Error`` exception describes theattributes common to all standard
    exceptions. 
    
     This exception serves two purposes: 
    
    #. It is the exception that clients in many programming languages can catch
       to handle all standard exceptions. Typically those clients will display one
       or more of the localizable messages from :attr:`Error.messages` to a human.
    #. It is the exception that methods can report when they need to report
       some exception, but the exception doesn't fit into any other standard
       exception, and in fact the only reasonable way for a client to react to the
       exception is to display the message(s) to a human.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'Error'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            null, null, and null classes are intended as possible values for
            this attribute. :class:`com.vmware.vapi.std_client.DynamicID` may
            also be useful as a value for this attribute (although that is not
            its primary purpose). Some classes may provide their own specific
            classes for use as the value of this attribute when reporting
            exceptions from their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        self.messages = messages
        self.data = data
        VapiError.__init__(self)

Error._set_binding_type(type.ErrorType(
    'com.vmware.vcenter.tokenservice.error', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    Error))



class InvalidScope(Error):
    """
    The ``InvalidScope`` exception indicates requested scope is invalid,
    unknown, malformed, or exceeds the scope granted by the resource owner.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'InvalidScope'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            null, null, and null classes are intended as possible values for
            this attribute. :class:`com.vmware.vapi.std_client.DynamicID` may
            also be useful as a value for this attribute (although that is not
            its primary purpose). Some classes may provide their own specific
            classes for use as the value of this attribute when reporting
            exceptions from their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

InvalidScope._set_binding_type(type.ErrorType(
    'com.vmware.vcenter.tokenservice.invalid_scope', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InvalidScope))



class InvalidRequest(Error):
    """
    The ``InvalidRequest`` exception indicates that
    :class:`TokenExchange.ExchangeSpec` is missing a required parameter,
    includes an unsupported parameter value (other than
    :attr:`TokenExchange.ExchangeSpec.grant_type`)

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'InvalidRequest'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            null, null, and null classes are intended as possible values for
            this attribute. :class:`com.vmware.vapi.std_client.DynamicID` may
            also be useful as a value for this attribute (although that is not
            its primary purpose). Some classes may provide their own specific
            classes for use as the value of this attribute when reporting
            exceptions from their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

InvalidRequest._set_binding_type(type.ErrorType(
    'com.vmware.vcenter.tokenservice.invalid_request', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InvalidRequest))



class InvalidGrant(Error):
    """
    The ``InvalidGrant`` exception indicates that provided authorization grant
    (e.g., authorization code, resource owner credentials) or refresh token is
    invalid, expired, revoked, does not match the redirection URI used in the
    authorization request, or was issued to another client.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'InvalidGrant'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            null, null, and null classes are intended as possible values for
            this attribute. :class:`com.vmware.vapi.std_client.DynamicID` may
            also be useful as a value for this attribute (although that is not
            its primary purpose). Some classes may provide their own specific
            classes for use as the value of this attribute when reporting
            exceptions from their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

InvalidGrant._set_binding_type(type.ErrorType(
    'com.vmware.vcenter.tokenservice.invalid_grant', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InvalidGrant))



class TokenExchange(VapiInterface):
    """
    The ``TokenExchange`` interface provides possibility to exchange between
    different tokens types. Implementation of "OAuth 2.0 Token Exchange"
    standard (https://tools.ietf.org/html/draft-ietf-oauth-token-exchange-12).
    """
    TOKEN_EXCHANGE_GRANT = "urn:ietf:params:oauth:grant-type:token-exchange"
    """
    Class attribute indicates that token exchange grant type.

    """
    ACCESS_TOKEN_TYPE = "urn:ietf:params:oauth:token-type:access_token"
    """
    Class attribute indicates OAuth 2.0 access token type.

    """
    REFRESH_TOKEN_TYPE = "urn:ietf:params:oauth:token-type:refresh_token"
    """
    Class attribute indicates OAuth 2.0 refresh token type.

    """
    ID_TOKEN_TYPE = "urn:ietf:params:oauth:token-type:id_token"
    """
    Class attribute indicates OIDC ID token type.

    """
    SAML1_TOKEN_TYPE = "urn:ietf:params:oauth:token-type:saml1"
    """
    Class attribute indicates base64-encoded SAML 1.1 token type.

    """
    SAML2_TOKEN_TYPE = "urn:ietf:params:oauth:token-type:saml2"
    """
    Class attribute indicates base64-encoded SAML 2.0 token type.

    """
    BEARER_TOKEN_METHOD_TYPE = "Bearer"
    """
    Class attribute indicates that the security token is a bearer token.

    """
    N_A_TOKEN_METHOD_TYPE = "N_A"
    """
    Class attribute indicates :attr:`TokenExchange.Info.token_type` identifier is
    not applicable in that context.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.tokenservice.token_exchange'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TokenExchangeStub)
        self._VAPI_OPERATION_IDS = {}

    class ExchangeSpec(VapiStruct):
        """
        The ``TokenExchange.ExchangeSpec`` class contains arguments required for
        token exchange.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     grant_type=None,
                     resource=None,
                     audience=None,
                     scope=None,
                     requested_token_type=None,
                     subject_token=None,
                     subject_token_type=None,
                     actor_token=None,
                     actor_token_type=None,
                    ):
            """
            :type  grant_type: :class:`str`
            :param grant_type: The value of :attr:`TokenExchange.TOKEN_EXCHANGE_GRANT` indicates
                that a token exchange is being performed.
            :type  resource: :class:`str` or ``None``
            :param resource: Indicates the location of the target service or resource where the
                client intends to use the requested security token.
                if can be inferred from other arguments or not needed for specific
                case of exchange.
            :type  audience: :class:`str` or ``None``
            :param audience: The logical name of the target service where the client intends to
                use the requested security token. This serves a purpose similar to
                the :attr:`TokenExchange.ExchangeSpec.resource` parameter, but with
                the client providing a logical name rather than a location.
                if can be inferred from other arguments or not needed for specific
                case of exchange.
            :type  scope: :class:`str` or ``None``
            :param scope: A list of space-delimited, case-sensitive strings, that allow the
                client to specify the desired scope of the requested security token
                in the context of the service or resource where the token will be
                used.
                if can be inferred from other arguments or not needed for specific
                case of exchange.
            :type  requested_token_type: :class:`str` or ``None``
            :param requested_token_type: An identifier for the type of the requested security token. If the
                requested type is unspecified, the issued token type is at the
                discretion of the server and may be dictated by knowledge of the
                requirements of the service or resource indicated by the
                :attr:`TokenExchange.ExchangeSpec.resource` or
                :attr:`TokenExchange.ExchangeSpec.audience` parameter.
                if can be inferred from other arguments or not needed for specific
                case of exchange.
            :type  subject_token: :class:`str`
            :param subject_token: A security token that represents the identity of the party on
                behalf of whom exchange is being made. Typically, the subject of
                this token will be the subject of the security token issued. Token
                is base64-encoded.
            :type  subject_token_type: :class:`str`
            :param subject_token_type: An identifier, that indicates the type of the security token in the
                :attr:`TokenExchange.ExchangeSpec.subject_token` parameter.
            :type  actor_token: :class:`str` or ``None``
            :param actor_token: A security token that represents the identity of the acting party.
                Typically, this will be the party that is authorized to use the
                requested security token and act on behalf of the subject.
                if not needed for specific case of exchange.
            :type  actor_token_type: :class:`str` or ``None``
            :param actor_token_type: An identifier, that indicates the type of the security token in the
                :attr:`TokenExchange.ExchangeSpec.actor_token` parameter.
                if :attr:`TokenExchange.ExchangeSpec.actor_token` parameter is not
                present.
            """
            self.grant_type = grant_type
            self.resource = resource
            self.audience = audience
            self.scope = scope
            self.requested_token_type = requested_token_type
            self.subject_token = subject_token
            self.subject_token_type = subject_token_type
            self.actor_token = actor_token
            self.actor_token_type = actor_token_type
            VapiStruct.__init__(self)


    ExchangeSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.tokenservice.token_exchange.exchange_spec', {
            'grant_type': type.StringType(),
            'resource': type.OptionalType(type.StringType()),
            'audience': type.OptionalType(type.StringType()),
            'scope': type.OptionalType(type.StringType()),
            'requested_token_type': type.OptionalType(type.StringType()),
            'subject_token': type.StringType(),
            'subject_token_type': type.StringType(),
            'actor_token': type.OptionalType(type.StringType()),
            'actor_token_type': type.OptionalType(type.StringType()),
        },
        ExchangeSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``TokenExchange.Info`` class contains data that represents successful
        token exchange response.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     access_token=None,
                     issued_token_type=None,
                     token_type=None,
                     expires_in=None,
                     scope=None,
                     refresh_token=None,
                    ):
            """
            :type  access_token: :class:`str`
            :param access_token: The security token issued by the server in response to the token
                exchange request. Token is base64-encoded.
            :type  issued_token_type: :class:`str`
            :param issued_token_type: An identifier, that indicates the type of the security token in the
                :attr:`TokenExchange.Info.access_token` parameter.
            :type  token_type: :class:`str`
            :param token_type: A case-insensitive value specifying the method of using the access
                token issued.
            :type  expires_in: :class:`long` or ``None``
            :param expires_in: The validity lifetime, in seconds, of the token issued by the
                server.
                if not applicable for issued token.
            :type  scope: :class:`str` or ``None``
            :param scope: Scope of the issued security token.
                if the scope of the issued security token is identical to the scope
                requested by the client.
            :type  refresh_token: :class:`str` or ``None``
            :param refresh_token: A refresh token can be issued in cases where the client of the
                token exchange needs the ability to access a resource even when the
                original credential is no longer valid.
                if not needed for specific case of exchange.
            """
            self.access_token = access_token
            self.issued_token_type = issued_token_type
            self.token_type = token_type
            self.expires_in = expires_in
            self.scope = scope
            self.refresh_token = refresh_token
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.tokenservice.token_exchange.info', {
            'access_token': type.StringType(),
            'issued_token_type': type.StringType(),
            'token_type': type.StringType(),
            'expires_in': type.OptionalType(type.IntegerType()),
            'scope': type.OptionalType(type.StringType()),
            'refresh_token': type.OptionalType(type.StringType()),
        },
        Info,
        False,
        None))



    def exchange(self,
                 spec,
                 ):
        """
        Exchanges incoming token based on the spec and current client
        authorization data.

        :type  spec: :class:`TokenExchange.ExchangeSpec`
        :param spec: ``TokenExchange.ExchangeSpec`` class contains arguments that define
            exchange process.
        :rtype: :class:`TokenExchange.Info`
        :return: :class:`TokenExchange.Info` class that contains new token.
        :raise: :class:`InvalidGrant` 
            provided authorization grant (e.g., authorization code, resource
            owner credentials) or refresh token is invalid, expired, revoked,
            does not match the redirection URI used in the authorization
            request, or was issued to another client.
        :raise: :class:`InvalidScope` 
            If the server is unwilling or unable to issue a token for all the
            target services indicated by the
            :attr:`TokenExchange.ExchangeSpec.resource` or
            :attr:`TokenExchange.ExchangeSpec.audience` parameters.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if authorization is not given to a caller.
        """
        return self._invoke('exchange',
                            {
                            'spec': spec,
                            })
class _TokenExchangeStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for exchange operation
        exchange_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'TokenExchange.ExchangeSpec'),
        })
        exchange_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vcenter.tokenservice.invalid_request':
                type.ReferenceType(__name__, 'InvalidRequest'),
            'com.vmware.vcenter.tokenservice.invalid_grant':
                type.ReferenceType(__name__, 'InvalidGrant'),
            'com.vmware.vcenter.tokenservice.invalid_scope':
                type.ReferenceType(__name__, 'InvalidScope'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        exchange_input_value_validator_list = [
        ]
        exchange_output_validator_list = [
        ]
        exchange_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/tokenservice/token-exchange',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'exchange': {
                'input_type': exchange_input_type,
                'output_type': type.ReferenceType(__name__, 'TokenExchange.Info'),
                'errors': exchange_error_dict,
                'input_value_validator_list': exchange_input_value_validator_list,
                'output_validator_list': exchange_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'exchange': exchange_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.tokenservice.token_exchange',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'TokenExchange': TokenExchange,
    }

