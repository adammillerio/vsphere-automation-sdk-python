# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.serviceinsertion.
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


class Excludelist(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.excludelist'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ExcludelistStub)
        self._VAPI_OPERATION_IDS = {}


    def addmember(self,
                  resource_reference,
                  ):
        """
        Add a new member in the exclude list

        :type  resource_reference: :class:`com.vmware.nsx.model_client.ResourceReference`
        :param resource_reference: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ResourceReference`
        :return: com.vmware.nsx.model.ResourceReference
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
        return self._invoke('addmember',
                            {
                            'resource_reference': resource_reference,
                            })

    def get(self):
        """
        Get list of members in exclude list


        :rtype: :class:`com.vmware.nsx.model_client.SIExcludeList`
        :return: com.vmware.nsx.model.SIExcludeList
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
        return self._invoke('get', None)

    def removemember(self,
                     object_id,
                     ):
        """
        Remove an existing object from the exclude list

        :type  object_id: :class:`str`
        :param object_id: Identifier of the object (required)
        :rtype: :class:`com.vmware.nsx.model_client.ResourceReference`
        :return: com.vmware.nsx.model.ResourceReference
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
        return self._invoke('removemember',
                            {
                            'object_id': object_id,
                            })

    def update(self,
               si_exclude_list,
               ):
        """
        Modify exclude list. This includes adding/removing members in the list.

        :type  si_exclude_list: :class:`com.vmware.nsx.model_client.SIExcludeList`
        :param si_exclude_list: (required)
        :rtype: :class:`com.vmware.nsx.model_client.SIExcludeList`
        :return: com.vmware.nsx.model.SIExcludeList
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
                            'si_exclude_list': si_exclude_list,
                            })
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
    LIST_TYPE_L3REDIRECT = "L3REDIRECT"
    """
    Possible value for ``type`` of method :func:`Sections.list`.

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

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.sections'
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
               service_insertion_section,
               id=None,
               operation=None,
               ):
        """
        Creates new empty Service Insertion section in the system.

        :type  service_insertion_section: :class:`com.vmware.nsx.model_client.ServiceInsertionSection`
        :param service_insertion_section: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSection`
        :return: com.vmware.nsx.model.ServiceInsertionSection
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
                            'service_insertion_section': service_insertion_section,
                            'id': id,
                            'operation': operation,
                            })

    def createwithrules(self,
                        service_insertion_section_rule_list,
                        id=None,
                        operation=None,
                        ):
        """
        Creates a new serviceinsertion section with rules. The limit on the
        number of rules is defined by maxItems in collection types for
        ServiceInsertionRule (ServiceInsertionRuleXXXList types). When invoked
        on a section with a large number of rules, this API is supported only
        at low rates of invocation (not more than 4-5 times per minute). The
        typical latency of this API with about 1024 rules is about 4-5 seconds.
        This API should not be invoked with large payloads at automation
        speeds. More than 50 rules are not supported. Instead, to create
        sections, use: POST /api/v1/serviceinsertion/sections To create rules,
        use: POST /api/v1/serviceinsertion/sections/<section-id>/rules

        :type  service_insertion_section_rule_list: :class:`com.vmware.nsx.model_client.ServiceInsertionSectionRuleList`
        :param service_insertion_section_rule_list: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSectionRuleList`
        :return: com.vmware.nsx.model.ServiceInsertionSectionRuleList
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
                            'service_insertion_section_rule_list': service_insertion_section_rule_list,
                            'id': id,
                            'operation': operation,
                            })

    def delete(self,
               section_id,
               cascade=None,
               ):
        """
        Removes serviceinsertion section from the system. ServiceInsertion
        section with rules can only be deleted by passing \"cascade=true\"
        parameter.

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
        Returns information about serviceinsertion section for the identifier.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSection`
        :return: com.vmware.nsx.model.ServiceInsertionSection
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
             type=None,
             ):
        """
        List all Service Insertion section in paginated form. A default page
        size is limited to 1000 sections. By default, the list of section is
        filtered by L3REDIRECT type.

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
        :type  type: :class:`str` or ``None``
        :param type: Section Type (optional, default to L3REDIRECT)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSectionListResult`
        :return: com.vmware.nsx.model.ServiceInsertionSectionListResult
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
                            'type': type,
                            })

    def listwithrules(self,
                      section_id,
                      ):
        """
        Returns serviceinsertion section information with rules for a section
        identifier. When invoked on a section with a large number of rules,
        this API is supported only at low rates of invocation (not more than
        4-5 times per minute). The typical latency of this API with about 1024
        rules is about 4-5 seconds. This API should not be invoked with large
        payloads at automation speeds. More than 50 rules are not supported.
        Instead, to read serviceinsertion rules, use: GET
        /api/v1/serviceinsertion/sections/<section-id>/rules with the
        appropriate page_size.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSectionRuleList`
        :return: com.vmware.nsx.model.ServiceInsertionSectionRuleList
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
               service_insertion_section,
               id=None,
               operation=None,
               ):
        """
        Modifies an existing serviceinsertion section along with its relative
        position among other serviceinsertion sections in the system.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  service_insertion_section: :class:`com.vmware.nsx.model_client.ServiceInsertionSection`
        :param service_insertion_section: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSection`
        :return: com.vmware.nsx.model.ServiceInsertionSection
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
                            'service_insertion_section': service_insertion_section,
                            'id': id,
                            'operation': operation,
                            })

    def revisewithrules(self,
                        section_id,
                        service_insertion_section_rule_list,
                        id=None,
                        operation=None,
                        ):
        """
        Modifies an existing serviceinsertion section along with its relative
        position among other serviceinsertion sections with rules. When invoked
        on a large number of rules, this API is supported only at low rates of
        invocation (not more than 2 times per minute). The typical latency of
        this API with about 1024 rules is about 15 seconds in a cluster setup.
        This API should not be invoked with large payloads at automation
        speeds. Instead, to move a section above or below another section, use:
        POST /api/v1/serviceinsertion/sections/<section-id>?action=revise To
        modify rules, use: PUT
        /api/v1/serviceinsertion/sections/<section-id>/rules/<rule-id>

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  service_insertion_section_rule_list: :class:`com.vmware.nsx.model_client.ServiceInsertionSectionRuleList`
        :param service_insertion_section_rule_list: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSectionRuleList`
        :return: com.vmware.nsx.model.ServiceInsertionSectionRuleList
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
                            'service_insertion_section_rule_list': service_insertion_section_rule_list,
                            'id': id,
                            'operation': operation,
                            })

    def update(self,
               section_id,
               service_insertion_section,
               ):
        """
        Modifies the specified section, but does not modify the section's
        associated rules.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  service_insertion_section: :class:`com.vmware.nsx.model_client.ServiceInsertionSection`
        :param service_insertion_section: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSection`
        :return: com.vmware.nsx.model.ServiceInsertionSection
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
                            'service_insertion_section': service_insertion_section,
                            })

    def updatewithrules(self,
                        section_id,
                        service_insertion_section_rule_list,
                        ):
        """
        Modifies existing serviceinsertion section along with its association
        with rules. When invoked on a large number of rules, this API is
        supported only at low rates of invocation (not more than 2 times per
        minute). The typical latency of this API with about 1024 rules is about
        15 seconds in a cluster setup. This API should not be invoked with
        large payloads at automation speeds. Instead, to update rule content,
        use: PUT /api/v1/serviceinsertion/sections/<section-id>/rules/<rule-id>

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  service_insertion_section_rule_list: :class:`com.vmware.nsx.model_client.ServiceInsertionSectionRuleList`
        :param service_insertion_section_rule_list: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionSectionRuleList`
        :return: com.vmware.nsx.model.ServiceInsertionSectionRuleList
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
                            'service_insertion_section_rule_list': service_insertion_section_rule_list,
                            })
class ServiceAttachments(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.service_attachments'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceAttachmentsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               service_attachment,
               ):
        """
        Adds a new Service attachment. A service attachment represents a point
        on NSX entity (Example: Logical Router) to which service instance can
        be connected through an InstanceEndpoint.

        :type  service_attachment: :class:`com.vmware.nsx.model_client.ServiceAttachment`
        :param service_attachment: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceAttachment`
        :return: com.vmware.nsx.model.ServiceAttachment
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
                            'service_attachment': service_attachment,
                            })

    def delete(self,
               service_attachment_id,
               ):
        """
        Delete existing service attachment from system. Before deletion, please
        make sure that, no instance endpoints are connected to this attachment.
        In turn no appliance should be connected to this attachment.

        :type  service_attachment_id: :class:`str`
        :param service_attachment_id: (required)
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
                            'service_attachment_id': service_attachment_id,
                            })

    def get(self,
            service_attachment_id,
            ):
        """
        Returns detailed Attachment information for a given service attachment.

        :type  service_attachment_id: :class:`str`
        :param service_attachment_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceAttachment`
        :return: com.vmware.nsx.model.ServiceAttachment
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
                            'service_attachment_id': service_attachment_id,
                            })

    def list(self):
        """
        Returns all Service-Attachement(s) present in the system.


        :rtype: :class:`com.vmware.nsx.model_client.ServiceAttachmentListResult`
        :return: com.vmware.nsx.model.ServiceAttachmentListResult
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
        return self._invoke('list', None)
class ServiceChains(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.service_chains'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceChainsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               service_chain,
               ):
        """
        Adds a new service chain. Service Chains is can contain profile
        belonging to same or different Service(s). It represents a redirection
        target for a Rule.

        :type  service_chain: :class:`com.vmware.nsx.model_client.ServiceChain`
        :param service_chain: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceChain`
        :return: com.vmware.nsx.model.ServiceChain
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
                            'service_chain': service_chain,
                            })

    def delete(self,
               service_chain_id,
               ):
        """
        Delete a particular service chain.

        :type  service_chain_id: :class:`str`
        :param service_chain_id: (required)
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
                            'service_chain_id': service_chain_id,
                            })

    def get(self,
            service_chain_id,
            ):
        """
        Returns detailed service chain information.

        :type  service_chain_id: :class:`str`
        :param service_chain_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceChain`
        :return: com.vmware.nsx.model.ServiceChain
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
                            'service_chain_id': service_chain_id,
                            })

    def list(self):
        """
        List all service chains in the system.


        :rtype: :class:`com.vmware.nsx.model_client.ServiceChainListResult`
        :return: com.vmware.nsx.model.ServiceChainListResult
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
        return self._invoke('list', None)
class ServiceInstances(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.service_instances'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceInstancesStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             deployed_to=None,
             service_deployment_id=None,
             ):
        """
        Returns all Service-Instance(s) of all Services present in system. When
        request parameter (deployed_to or service_deployment_id) is provided as
        a part of request, it will filter out Service-Instances accordingly.

        :type  deployed_to: :class:`str` or ``None``
        :param deployed_to: Deployed_to referenced by service instances present in system
            (optional)
        :type  service_deployment_id: :class:`str` or ``None``
        :param service_deployment_id: Service Deployment Id using which the instances were deployed
            (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInstanceListResult`
        :return: com.vmware.nsx.model.ServiceInstanceListResult
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
                            'deployed_to': deployed_to,
                            'service_deployment_id': service_deployment_id,
                            })
class ServiceManagers(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.service_managers'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceManagersStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               service_manager,
               ):
        """
        Register service-manager with NSX with basic details like name,
        username, password.

        :type  service_manager: :class:`com.vmware.nsx.model_client.ServiceManager`
        :param service_manager: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceManager`
        :return: com.vmware.nsx.model.ServiceManager
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
                            'service_manager': service_manager,
                            })

    def delete(self,
               service_manager_id,
               ):
        """
        Delete service-manager which is registered with NSX with basic details
        like name, username, password.

        :type  service_manager_id: :class:`str`
        :param service_manager_id: (required)
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
                            'service_manager_id': service_manager_id,
                            })

    def get(self,
            service_manager_id,
            ):
        """
        Retrieve service-manager details like name, username, password, vendor
        ID, thumbprint for a given ID.

        :type  service_manager_id: :class:`str`
        :param service_manager_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceManager`
        :return: com.vmware.nsx.model.ServiceManager
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
                            'service_manager_id': service_manager_id,
                            })

    def list(self):
        """
        List all service managers.


        :rtype: :class:`com.vmware.nsx.model_client.ServiceManagerListResult`
        :return: com.vmware.nsx.model.ServiceManagerListResult
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
        return self._invoke('list', None)

    def update(self,
               service_manager_id,
               service_manager,
               ):
        """
        Update service-manager which is registered with NSX with basic details
        like name, username, password.

        :type  service_manager_id: :class:`str`
        :param service_manager_id: (required)
        :type  service_manager: :class:`com.vmware.nsx.model_client.ServiceManager`
        :param service_manager: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceManager`
        :return: com.vmware.nsx.model.ServiceManager
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
                            'service_manager_id': service_manager_id,
                            'service_manager': service_manager,
                            })
class Services(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.services'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServicesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               service_definition,
               ):
        """
        Creates new Service-Insertion Service in the system.

        :type  service_definition: :class:`com.vmware.nsx.model_client.ServiceDefinition`
        :param service_definition: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceDefinition`
        :return: com.vmware.nsx.model.ServiceDefinition
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
                            'service_definition': service_definition,
                            })

    def delete(self,
               service_id,
               cascade=None,
               ):
        """
        Removes Service-Insertion Service from the system. A Service with
        Service-Instances can only be deleted by passing \"cascade=true\"
        parameter.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  cascade: :class:`bool` or ``None``
        :param cascade: Flag to cascade delete all the child objects, associated with it.
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
                            'service_id': service_id,
                            'cascade': cascade,
                            })

    def get(self,
            service_id,
            ):
        """
        Returns information about Service-Insertion Service with the given
        identifier.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceDefinition`
        :return: com.vmware.nsx.model.ServiceDefinition
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
                            'service_id': service_id,
                            })

    def list(self):
        """
        List all Service-Insertion Service Definitions.


        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionServiceListResult`
        :return: com.vmware.nsx.model.ServiceInsertionServiceListResult
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
        return self._invoke('list', None)

    def update(self,
               service_id,
               service_definition,
               ):
        """
        Modifies the specified Service.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_definition: :class:`com.vmware.nsx.model_client.ServiceDefinition`
        :param service_definition: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceDefinition`
        :return: com.vmware.nsx.model.ServiceDefinition
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
                            'service_id': service_id,
                            'service_definition': service_definition,
                            })
class SourceEntities(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.source_entities'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SourceEntitiesStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             source_node_value,
             ):
        """
        Service insertion data path inserts unique 'source node id' value into
        each packet. This API can be used to identify the source of the packet
        using this value. It can be resolved to multiple source entities.

        :type  source_node_value: :class:`str`
        :param source_node_value: value (required)
        :rtype: :class:`com.vmware.nsx.model_client.SourceEntityResult`
        :return: com.vmware.nsx.model.SourceEntityResult
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
                            'source_node_value': source_node_value,
                            })
class Status(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatusStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            context_type,
            ):
        """
        Get ServiceInsertion global status for a context

        :type  context_type: :class:`str`
        :param context_type: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionStatus`
        :return: com.vmware.nsx.model.ServiceInsertionStatus
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
                            'context_type': context_type,
                            })

    def list(self):
        """
        List all service insertion status for supported contexts


        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionStatusListResult`
        :return: com.vmware.nsx.model.ServiceInsertionStatusListResult
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
        return self._invoke('list', None)

    def update(self,
               context_type,
               service_insertion_status,
               ):
        """
        Update global ServiceInsertion status for a context

        :type  context_type: :class:`str`
        :param context_type: (required)
        :type  service_insertion_status: :class:`com.vmware.nsx.model_client.ServiceInsertionStatus`
        :param service_insertion_status: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionStatus`
        :return: com.vmware.nsx.model.ServiceInsertionStatus
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
                            'context_type': context_type,
                            'service_insertion_status': service_insertion_status,
                            })
class _ExcludelistStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for addmember operation
        addmember_input_type = type.StructType('operation-input', {
            'resource_reference': type.ReferenceType('com.vmware.nsx.model_client', 'ResourceReference'),
        })
        addmember_error_dict = {
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
        addmember_input_value_validator_list = [
        ]
        addmember_output_validator_list = [
        ]
        addmember_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/excludelist?action=add_member',
            request_body_parameter='resource_reference',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
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
            url_template='/api/v1/serviceinsertion/excludelist',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for removemember operation
        removemember_input_type = type.StructType('operation-input', {
            'object_id': type.StringType(),
        })
        removemember_error_dict = {
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
        removemember_input_value_validator_list = [
        ]
        removemember_output_validator_list = [
        ]
        removemember_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/excludelist?action=remove_member',
            path_variables={
            },
            query_parameters={
                'object_id': 'object_id',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'si_exclude_list': type.ReferenceType('com.vmware.nsx.model_client', 'SIExcludeList'),
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
            url_template='/api/v1/serviceinsertion/excludelist',
            request_body_parameter='si_exclude_list',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'addmember': {
                'input_type': addmember_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ResourceReference'),
                'errors': addmember_error_dict,
                'input_value_validator_list': addmember_input_value_validator_list,
                'output_validator_list': addmember_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'SIExcludeList'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'removemember': {
                'input_type': removemember_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ResourceReference'),
                'errors': removemember_error_dict,
                'input_value_validator_list': removemember_input_value_validator_list,
                'output_validator_list': removemember_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'SIExcludeList'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'addmember': addmember_rest_metadata,
            'get': get_rest_metadata,
            'removemember': removemember_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.excludelist',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SectionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'service_insertion_section': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSection'),
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
            url_template='/api/v1/serviceinsertion/sections',
            request_body_parameter='service_insertion_section',
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
            'service_insertion_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSectionRuleList'),
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
            url_template='/api/v1/serviceinsertion/sections?action=create_with_rules',
            request_body_parameter='service_insertion_section_rule_list',
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
            url_template='/api/v1/serviceinsertion/sections/{section-id}',
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
            url_template='/api/v1/serviceinsertion/sections/{section-id}',
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
            'type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/serviceinsertion/sections',
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
                'type': 'type',
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
            url_template='/api/v1/serviceinsertion/sections/{section-id}?action=list_with_rules',
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
            'service_insertion_section': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSection'),
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
            url_template='/api/v1/serviceinsertion/sections/{section-id}?action=revise',
            request_body_parameter='service_insertion_section',
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
            'service_insertion_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSectionRuleList'),
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
            url_template='/api/v1/serviceinsertion/sections/{section-id}?action=revise_with_rules',
            request_body_parameter='service_insertion_section_rule_list',
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
            'service_insertion_section': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSection'),
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
            url_template='/api/v1/serviceinsertion/sections/{section-id}',
            request_body_parameter='service_insertion_section',
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
            'service_insertion_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSectionRuleList'),
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
            url_template='/api/v1/serviceinsertion/sections/{section-id}?action=update_with_rules',
            request_body_parameter='service_insertion_section_rule_list',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSection'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'createwithrules': {
                'input_type': createwithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSectionRuleList'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSection'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSectionListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'listwithrules': {
                'input_type': listwithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSectionRuleList'),
                'errors': listwithrules_error_dict,
                'input_value_validator_list': listwithrules_input_value_validator_list,
                'output_validator_list': listwithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revise': {
                'input_type': revise_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSection'),
                'errors': revise_error_dict,
                'input_value_validator_list': revise_input_value_validator_list,
                'output_validator_list': revise_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revisewithrules': {
                'input_type': revisewithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSectionRuleList'),
                'errors': revisewithrules_error_dict,
                'input_value_validator_list': revisewithrules_input_value_validator_list,
                'output_validator_list': revisewithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSection'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'updatewithrules': {
                'input_type': updatewithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionSectionRuleList'),
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
            self, iface_name='com.vmware.nsx.serviceinsertion.sections',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ServiceAttachmentsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'service_attachment': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceAttachment'),
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
            url_template='/api/v1/serviceinsertion/service-attachments',
            request_body_parameter='service_attachment',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'service_attachment_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/service-attachments/{service-attachment-id}',
            path_variables={
                'service_attachment_id': 'service-attachment-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_attachment_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/service-attachments/{service-attachment-id}',
            path_variables={
                'service_attachment_id': 'service-attachment-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/api/v1/serviceinsertion/service-attachments',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceAttachment'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceAttachment'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceAttachmentListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.service_attachments',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ServiceChainsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'service_chain': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceChain'),
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
            url_template='/api/v1/serviceinsertion/service-chains',
            request_body_parameter='service_chain',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'service_chain_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/service-chains/{service-chain-id}',
            path_variables={
                'service_chain_id': 'service-chain-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_chain_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/service-chains/{service-chain-id}',
            path_variables={
                'service_chain_id': 'service-chain-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/api/v1/serviceinsertion/service-chains',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceChain'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceChain'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceChainListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.service_chains',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ServiceInstancesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'deployed_to': type.OptionalType(type.StringType()),
            'service_deployment_id': type.OptionalType(type.StringType()),
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/serviceinsertion/service-instances',
            path_variables={
            },
            query_parameters={
                'deployed_to': 'deployed_to',
                'service_deployment_id': 'service_deployment_id',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInstanceListResult'),
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
            self, iface_name='com.vmware.nsx.serviceinsertion.service_instances',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ServiceManagersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'service_manager': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceManager'),
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
            url_template='/api/v1/serviceinsertion/service-managers',
            request_body_parameter='service_manager',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'service_manager_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/service-managers/{service-manager-id}',
            path_variables={
                'service_manager_id': 'service-manager-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_manager_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/service-managers/{service-manager-id}',
            path_variables={
                'service_manager_id': 'service-manager-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/api/v1/serviceinsertion/service-managers',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'service_manager_id': type.StringType(),
            'service_manager': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceManager'),
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
            url_template='/api/v1/serviceinsertion/service-managers/{service-manager-id}',
            request_body_parameter='service_manager',
            path_variables={
                'service_manager_id': 'service-manager-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceManager'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceManager'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceManagerListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceManager'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.service_managers',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ServicesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'service_definition': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceDefinition'),
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
            url_template='/api/v1/serviceinsertion/services',
            request_body_parameter='service_definition',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/services/{service-id}',
            path_variables={
                'service_id': 'service-id',
            },
            query_parameters={
                'cascade': 'cascade',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/services/{service-id}',
            path_variables={
                'service_id': 'service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/api/v1/serviceinsertion/services',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_definition': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceDefinition'),
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
            url_template='/api/v1/serviceinsertion/services/{service-id}',
            request_body_parameter='service_definition',
            path_variables={
                'service_id': 'service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceDefinition'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceDefinition'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionServiceListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceDefinition'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.services',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SourceEntitiesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'source_node_value': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/source-entities',
            path_variables={
            },
            query_parameters={
                'source_node_value': 'source_node_value',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'SourceEntityResult'),
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
            self, iface_name='com.vmware.nsx.serviceinsertion.source_entities',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'context_type': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/status/{context-type}',
            path_variables={
                'context_type': 'context-type',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/api/v1/serviceinsertion/status',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'context_type': type.StringType(),
            'service_insertion_status': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionStatus'),
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
            url_template='/api/v1/serviceinsertion/status/{context-type}',
            request_body_parameter='service_insertion_status',
            path_variables={
                'context_type': 'context-type',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionStatus'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionStatusListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionStatus'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Excludelist': Excludelist,
        'Sections': Sections,
        'ServiceAttachments': ServiceAttachments,
        'ServiceChains': ServiceChains,
        'ServiceInstances': ServiceInstances,
        'ServiceManagers': ServiceManagers,
        'Services': Services,
        'SourceEntities': SourceEntities,
        'Status': Status,
        'sections': 'com.vmware.nsx.serviceinsertion.sections_client.StubFactory',
        'service_chains': 'com.vmware.nsx.serviceinsertion.service_chains_client.StubFactory',
        'services': 'com.vmware.nsx.serviceinsertion.services_client.StubFactory',
    }

