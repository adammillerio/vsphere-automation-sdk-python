# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.pbr.
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


class Sections(VapiInterface):
    """
    
    """
    CREATE_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Sections.create`.

    """
    CREATE_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Sections.create`.

    """
    CREATE_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Sections.create`.

    """
    CREATE_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Sections.create`.

    """
    CREATEWITHRULES_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Sections.createwithrules`.

    """
    CREATEWITHRULES_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Sections.createwithrules`.

    """
    CREATEWITHRULES_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Sections.createwithrules`.

    """
    CREATEWITHRULES_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Sections.createwithrules`.

    """
    LIST_EXCLUDE_APPLIED_TO_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``excludeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_EXCLUDE_APPLIED_TO_TYPE_LOGICALSWITCH = "LogicalSwitch"
    """
    Possible value for ``excludeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_EXCLUDE_APPLIED_TO_TYPE_LOGICALROUTER = "LogicalRouter"
    """
    Possible value for ``excludeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_EXCLUDE_APPLIED_TO_TYPE_LOGICALPORT = "LogicalPort"
    """
    Possible value for ``excludeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_FILTER_TYPE_FILTER = "FILTER"
    """
    Possible value for ``filterType`` of method :func:`Sections.list`.

    """
    LIST_FILTER_TYPE_SEARCH = "SEARCH"
    """
    Possible value for ``filterType`` of method :func:`Sections.list`.

    """
    LIST_INCLUDE_APPLIED_TO_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``includeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_INCLUDE_APPLIED_TO_TYPE_LOGICALSWITCH = "LogicalSwitch"
    """
    Possible value for ``includeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_INCLUDE_APPLIED_TO_TYPE_LOGICALROUTER = "LogicalRouter"
    """
    Possible value for ``includeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_INCLUDE_APPLIED_TO_TYPE_LOGICALPORT = "LogicalPort"
    """
    Possible value for ``includeAppliedToType`` of method :func:`Sections.list`.

    """
    REVISE_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Sections.revise`.

    """
    REVISE_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Sections.revise`.

    """
    REVISE_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Sections.revise`.

    """
    REVISE_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Sections.revise`.

    """
    REVISEWITHRULES_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Sections.revisewithrules`.

    """
    REVISEWITHRULES_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Sections.revisewithrules`.

    """
    REVISEWITHRULES_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Sections.revisewithrules`.

    """
    REVISEWITHRULES_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Sections.revisewithrules`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.pbr.sections'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SectionsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               p_br_section,
               id=None,
               operation=None,
               ):
        """
        Creates new empty PBR section in the system.

        :type  p_br_section: :class:`com.vmware.nsx.model_client.PBRSection`
        :param p_br_section: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSection`
        :return: com.vmware.nsx.model.PBRSection
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('create',
                            {
                            'p_br_section': p_br_section,
                            'id': id,
                            'operation': operation,
                            })

    def createwithrules(self,
                        p_br_section_rule_list,
                        id=None,
                        operation=None,
                        ):
        """
        Creates a new PBR section with rules. The limit on the number of rules
        is defined by maxItems in collection types for PBRRule (PBRRuleXXXList
        types). When invoked on a section with a large number of rules, this
        API is supported only at low rates of invocation (not more than 4-5
        times per minute). The typical latency of this API with about 1024
        rules is about 4-5 seconds. This API should not be invoked with large
        payloads at automation speeds. More than 50 rules with a large number
        of rule references is not supported. Instead, to create sections, use:
        POST /api/v1/pbr/sections To create rules, use: POST
        /api/v1/pbr/sections/<section-id>/rules

        :type  p_br_section_rule_list: :class:`com.vmware.nsx.model_client.PBRSectionRuleList`
        :param p_br_section_rule_list: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSectionRuleList`
        :return: com.vmware.nsx.model.PBRSectionRuleList
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('createwithrules',
                            {
                            'p_br_section_rule_list': p_br_section_rule_list,
                            'id': id,
                            'operation': operation,
                            })

    def delete(self,
               section_id,
               cascade=None,
               ):
        """
        Removes PBR section from the system. PBR section with rules can only be
        deleted by passing \"cascade=true\" parameter.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  cascade: :class:`bool` or ``None``
        :param cascade: Flag to cascade delete of this object to all it's child objects.
            (optional, default to false)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('delete',
                            {
                            'section_id': section_id,
                            'cascade': cascade,
                            })

    def get(self,
            section_id,
            ):
        """
        Returns information about PBR section for the identifier.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSection`
        :return: com.vmware.nsx.model.PBRSection
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'section_id': section_id,
                            })

    def list(self,
             applied_tos=None,
             cursor=None,
             destinations=None,
             exclude_applied_to_type=None,
             filter_type=None,
             include_applied_to_type=None,
             included_fields=None,
             page_size=None,
             services=None,
             sort_ascending=None,
             sort_by=None,
             sources=None,
             ):
        """
        List all PBR section in paginated form. A default page size is limited
        to 1000 PBR sections.

        :type  applied_tos: :class:`str` or ``None``
        :param applied_tos: AppliedTo's referenced by this section or section's Distributed
            Service Rules . (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  destinations: :class:`str` or ``None``
        :param destinations: Destinations referenced by this section's Distributed Service Rules
            . (optional)
        :type  exclude_applied_to_type: :class:`str` or ``None``
        :param exclude_applied_to_type: Resource type valid for use as AppliedTo filter in section API
            (optional)
        :type  filter_type: :class:`str` or ``None``
        :param filter_type: Filter type (optional, default to FILTER)
        :type  include_applied_to_type: :class:`str` or ``None``
        :param include_applied_to_type: Resource type valid for use as AppliedTo filter in section API
            (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  services: :class:`str` or ``None``
        :param services: NSService referenced by this section's Distributed Service Rules .
            (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  sources: :class:`str` or ``None``
        :param sources: Sources referenced by this section's Distributed Service Rules .
            (optional)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSectionListResult`
        :return: com.vmware.nsx.model.PBRSectionListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'applied_tos': applied_tos,
                            'cursor': cursor,
                            'destinations': destinations,
                            'exclude_applied_to_type': exclude_applied_to_type,
                            'filter_type': filter_type,
                            'include_applied_to_type': include_applied_to_type,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'services': services,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'sources': sources,
                            })

    def listwithrules(self,
                      section_id,
                      ):
        """
        Returns PBR section information with rules for a section identifier.
        When invoked on a section with a large number of rules, this API is
        supported only at low rates of invocation (not more than 4-5 times per
        minute). The typical latency of this API with about 1024 rules is about
        4-5 seconds. This API should not be invoked with large payloads at
        automation speeds. More than 50 rules with a large number rule
        references is not supported. Instead, to read PBR rules, use: GET
        /api/v1/pbr/sections/<section-id>/rules with the appropriate page_size.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSectionRuleList`
        :return: com.vmware.nsx.model.PBRSectionRuleList
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('listwithrules',
                            {
                            'section_id': section_id,
                            })

    def revise(self,
               section_id,
               p_br_section,
               id=None,
               operation=None,
               ):
        """
        Modifies an existing PBR section along with its relative position among
        other PBR sections in the system.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  p_br_section: :class:`com.vmware.nsx.model_client.PBRSection`
        :param p_br_section: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSection`
        :return: com.vmware.nsx.model.PBRSection
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('revise',
                            {
                            'section_id': section_id,
                            'p_br_section': p_br_section,
                            'id': id,
                            'operation': operation,
                            })

    def revisewithrules(self,
                        section_id,
                        p_br_section_rule_list,
                        id=None,
                        operation=None,
                        ):
        """
        Modifies an existing PBR section along with its relative position among
        other PBR sections with rules. When invoked on a large number of rules,
        this API is supported only at low rates of invocation (not more than 2
        times per minute). The typical latency of this API with about 1024
        rules is about 15 seconds in a cluster setup. This API should not be
        invoked with large payloads at automation speeds. Instead, to move a
        section above or below another section, use: POST
        /api/v1/pbr/sections/<section-id>?action=revise To modify rules, use:
        PUT /api/v1/pbr/sections/<section-id>/rules/<rule-id>

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  p_br_section_rule_list: :class:`com.vmware.nsx.model_client.PBRSectionRuleList`
        :param p_br_section_rule_list: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSectionRuleList`
        :return: com.vmware.nsx.model.PBRSectionRuleList
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('revisewithrules',
                            {
                            'section_id': section_id,
                            'p_br_section_rule_list': p_br_section_rule_list,
                            'id': id,
                            'operation': operation,
                            })

    def update(self,
               section_id,
               p_br_section,
               ):
        """
        Modifies the specified section, but does not modify the section's
        associated rules.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  p_br_section: :class:`com.vmware.nsx.model_client.PBRSection`
        :param p_br_section: (required)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSection`
        :return: com.vmware.nsx.model.PBRSection
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('update',
                            {
                            'section_id': section_id,
                            'p_br_section': p_br_section,
                            })

    def updatewithrules(self,
                        section_id,
                        p_br_section_rule_list,
                        ):
        """
        Modifies existing PBR section along with its association with rules.
        When invoked on a large number of rules, this API is supported only at
        low rates of invocation (not more than 2 times per minute). The typical
        latency of this API with about 1024 rules is about 15 seconds in a
        cluster setup. This API should not be invoked with large payloads at
        automation speeds. Instead, to update rule content, use: PUT
        /api/v1/pbr/sections/<section-id>/rules/<rule-id>

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  p_br_section_rule_list: :class:`com.vmware.nsx.model_client.PBRSectionRuleList`
        :param p_br_section_rule_list: (required)
        :rtype: :class:`com.vmware.nsx.model_client.PBRSectionRuleList`
        :return: com.vmware.nsx.model.PBRSectionRuleList
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('updatewithrules',
                            {
                            'section_id': section_id,
                            'p_br_section_rule_list': p_br_section_rule_list,
                            })
class _SectionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'p_BR_section': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSection'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/pbr/sections',
            request_body_parameter='p_BR_section',
            path_variables={
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for createwithrules operation
        createwithrules_input_type = type.StructType('operation-input', {
            'p_BR_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSectionRuleList'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        createwithrules_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        createwithrules_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        createwithrules_output_validator_list = [
            HasFieldsOfValidator()
        ]
        createwithrules_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/pbr/sections?action=create_with_rules',
            request_body_parameter='p_BR_section_rule_list',
            path_variables={
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'cascade': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/pbr/sections/{section-id}',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'cascade': 'cascade',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/pbr/sections/{section-id}',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'applied_tos': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'destinations': type.OptionalType(type.StringType()),
            'exclude_applied_to_type': type.OptionalType(type.StringType()),
            'filter_type': type.OptionalType(type.StringType()),
            'include_applied_to_type': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'services': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'sources': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/pbr/sections',
            path_variables={
            },
            query_parameters={
                'applied_tos': 'applied_tos',
                'cursor': 'cursor',
                'destinations': 'destinations',
                'exclude_applied_to_type': 'exclude_applied_to_type',
                'filter_type': 'filter_type',
                'include_applied_to_type': 'include_applied_to_type',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'services': 'services',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'sources': 'sources',
            },
            content_type='application/json'
        )

        # properties for listwithrules operation
        listwithrules_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
        })
        listwithrules_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        listwithrules_input_value_validator_list = [
        ]
        listwithrules_output_validator_list = [
            HasFieldsOfValidator()
        ]
        listwithrules_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/pbr/sections/{section-id}?action=list_with_rules',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for revise operation
        revise_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'p_BR_section': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSection'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        revise_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        revise_input_value_validator_list = [
        ]
        revise_output_validator_list = [
        ]
        revise_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/pbr/sections/{section-id}?action=revise',
            request_body_parameter='p_BR_section',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for revisewithrules operation
        revisewithrules_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'p_BR_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSectionRuleList'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        revisewithrules_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        revisewithrules_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        revisewithrules_output_validator_list = [
            HasFieldsOfValidator()
        ]
        revisewithrules_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/pbr/sections/{section-id}?action=revise_with_rules',
            request_body_parameter='p_BR_section_rule_list',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'p_BR_section': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSection'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/pbr/sections/{section-id}',
            request_body_parameter='p_BR_section',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for updatewithrules operation
        updatewithrules_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'p_BR_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSectionRuleList'),
        })
        updatewithrules_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        updatewithrules_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        updatewithrules_output_validator_list = [
            HasFieldsOfValidator()
        ]
        updatewithrules_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/pbr/sections/{section-id}?action=update_with_rules',
            request_body_parameter='p_BR_section_rule_list',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSection'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'createwithrules': {
                'input_type': createwithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSectionRuleList'),
                'errors': createwithrules_error_dict,
                'input_value_validator_list': createwithrules_input_value_validator_list,
                'output_validator_list': createwithrules_output_validator_list,
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSection'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSectionListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'listwithrules': {
                'input_type': listwithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSectionRuleList'),
                'errors': listwithrules_error_dict,
                'input_value_validator_list': listwithrules_input_value_validator_list,
                'output_validator_list': listwithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revise': {
                'input_type': revise_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSection'),
                'errors': revise_error_dict,
                'input_value_validator_list': revise_input_value_validator_list,
                'output_validator_list': revise_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revisewithrules': {
                'input_type': revisewithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSectionRuleList'),
                'errors': revisewithrules_error_dict,
                'input_value_validator_list': revisewithrules_input_value_validator_list,
                'output_validator_list': revisewithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSection'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'updatewithrules': {
                'input_type': updatewithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PBRSectionRuleList'),
                'errors': updatewithrules_error_dict,
                'input_value_validator_list': updatewithrules_input_value_validator_list,
                'output_validator_list': updatewithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'createwithrules': createwithrules_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'listwithrules': listwithrules_rest_metadata,
            'revise': revise_rest_metadata,
            'revisewithrules': revisewithrules_rest_metadata,
            'update': update_rest_metadata,
            'updatewithrules': updatewithrules_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.pbr.sections',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Sections': Sections,
        'sections': 'com.vmware.nsx.pbr.sections_client.StubFactory',
    }

