# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.upgrade.
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


class Bundles(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.bundles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BundlesStub)
        self._VAPI_OPERATION_IDS = {}


    def cancelupload(self,
                     bundle_id,
                     ):
        """
        Cancel upload of upgrade bundle. This API works only when bundle upload
        is in-progress and will not work during post-processing of upgrade
        bundle. If bundle upload is in-progress, then the API call returns http
        OK response after cancelling the upload and deleting partially uploaded
        bundle.

        :type  bundle_id: :class:`str`
        :param bundle_id: (required)
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
        return self._invoke('cancelupload',
                            {
                            'bundle_id': bundle_id,
                            })

    def create(self,
               upgrade_bundle_fetch_request,
               ):
        """
        

        :type  upgrade_bundle_fetch_request: :class:`com.vmware.nsx.model_client.UpgradeBundleFetchRequest`
        :param upgrade_bundle_fetch_request: (required)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeBundleId`
        :return: com.vmware.nsx.model.UpgradeBundleId
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
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('create',
                            {
                            'upgrade_bundle_fetch_request': upgrade_bundle_fetch_request,
                            })

    def get(self,
            bundle_id,
            ):
        """
        Get uploaded upgrade bundle information

        :type  bundle_id: :class:`str`
        :param bundle_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeBundleInfo`
        :return: com.vmware.nsx.model.UpgradeBundleInfo
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
                            'bundle_id': bundle_id,
                            })
class FunctionalState(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.functional_state'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FunctionalStateStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Get the functional state of the upgrade coordinator.


        :rtype: :class:`com.vmware.nsx.model_client.UcFunctionalState`
        :return: com.vmware.nsx.model.UcFunctionalState
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
class History(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.history'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _HistoryStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self):
        """
        Get upgrade history


        :rtype: :class:`com.vmware.nsx.model_client.UpgradeHistoryList`
        :return: com.vmware.nsx.model.UpgradeHistoryList
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
class Nodes(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.nodes'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NodesStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             component_type=None,
             component_version=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Get list of nodes. If request parameter component type is specified,
        then all nodes for that component will be returned. If request
        parameter component version is specified, then all nodes at that
        version will be returned.

        :type  component_type: :class:`str` or ``None``
        :param component_type: Component type based on which nodes will be filtered (optional)
        :type  component_version: :class:`str` or ``None``
        :param component_version: Component version based on which nodes will be filtered (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.NodeInfoListResult`
        :return: com.vmware.nsx.model.NodeInfoListResult
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
                            'component_type': component_type,
                            'component_version': component_version,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class NodesSummary(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.nodes_summary'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NodesSummaryStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Get summary of nodes, which includes node count for each type and
        component version.


        :rtype: :class:`com.vmware.nsx.model_client.NodeSummaryList`
        :return: com.vmware.nsx.model.NodeSummaryList
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
class Plan(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.plan'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PlanStub)
        self._VAPI_OPERATION_IDS = {}


    def continue_(self,
                  component_type=None,
                  skip=None,
                  ):
        """
        Continue the upgrade. Resumes the upgrade from the point where it was
        paused.

        :type  component_type: :class:`str` or ``None``
        :param component_type: Component to upgrade. (optional)
        :type  skip: :class:`bool` or ``None``
        :param skip: Skip to upgrade of next component. (optional, default to false)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('continue',
                            {
                            'component_type': component_type,
                            'skip': skip,
                            })

    def pause(self):
        """
        Pause the upgrade. Upgrade will be paused after upgrade of all the
        nodes currently in progress is completed either successfully or with
        failure. User can make changes in the upgrade plan when the upgrade is
        paused.


        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('pause', None)

    def reset(self,
              component_type,
              ):
        """
        Reset the upgrade plan to default plan. User has an option to change
        the default plan. But if after making changes, user wants to go back to
        the default plan, this is the way to do so.

        :type  component_type: :class:`str`
        :param component_type: Component type (required)
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
        return self._invoke('reset',
                            {
                            'component_type': component_type,
                            })

    def start(self):
        """
        Start the upgrade. Upgrade will start as per the upgrade plan.


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
        return self._invoke('start', None)

    def upgradeselectedunits(self,
                             upgrade_unit_list,
                             ):
        """
        Upgrades, Resumes the upgrade of a selected set of units.

        :type  upgrade_unit_list: :class:`com.vmware.nsx.model_client.UpgradeUnitList`
        :param upgrade_unit_list: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('upgradeselectedunits',
                            {
                            'upgrade_unit_list': upgrade_unit_list,
                            })
class StatusSummary(VapiInterface):
    """
    
    """
    GET_SELECTION_STATUS_SELECTED = "SELECTED"
    """
    Possible value for ``selectionStatus`` of method :func:`StatusSummary.get`.

    """
    GET_SELECTION_STATUS_DESELECTED = "DESELECTED"
    """
    Possible value for ``selectionStatus`` of method :func:`StatusSummary.get`.

    """
    GET_SELECTION_STATUS_ALL = "ALL"
    """
    Possible value for ``selectionStatus`` of method :func:`StatusSummary.get`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.status_summary'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatusSummaryStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            component_type=None,
            selection_status=None,
            show_history=None,
            ):
        """
        Get upgrade status summary

        :type  component_type: :class:`str` or ``None``
        :param component_type: Component type based on which upgrade units to be filtered
            (optional)
        :type  selection_status: :class:`str` or ``None``
        :param selection_status: Flag to indicate whether to return status for only selected, only
            deselected or both type of upgrade units (optional, default to ALL)
        :type  show_history: :class:`bool` or ``None``
        :param show_history: Get upgrade activity for a given component (optional)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeStatus`
        :return: com.vmware.nsx.model.UpgradeStatus
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
                            'component_type': component_type,
                            'selection_status': selection_status,
                            'show_history': show_history,
                            })
class Summary(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.summary'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SummaryStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Get upgrade summary


        :rtype: :class:`com.vmware.nsx.model_client.UpgradeSummary`
        :return: com.vmware.nsx.model.UpgradeSummary
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
class UcUpgradeStatus(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.uc_upgrade_status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UcUpgradeStatusStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Get upgrade-coordinator upgrade status


        :rtype: :class:`com.vmware.nsx.model_client.UcUpgradeStatus`
        :return: com.vmware.nsx.model.UcUpgradeStatus
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
class UpgradeChecksInfo(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.upgrade_checks_info'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpgradeChecksInfoStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             component_type=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information of pre-upgrade and post-upgrade checks. If request
        parameter component type is specified, then returns information about
        all pre-upgrade and post-upgrade for the component. Otherwise returns
        information of checks across all component types.

        :type  component_type: :class:`str` or ``None``
        :param component_type: Component type based on which upgrade checks are to be filtered
            (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ComponentUpgradeChecksInfoListResult`
        :return: com.vmware.nsx.model.ComponentUpgradeChecksInfoListResult
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
                            'component_type': component_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class UpgradeUnitGroups(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.upgrade_unit_groups'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpgradeUnitGroupsStub)
        self._VAPI_OPERATION_IDS = {}


    def addupgradeunits(self,
                        group_id,
                        upgrade_unit_list,
                        ):
        """
        Add upgrade units to specified upgrade unit group. The upgrade units
        will be added at the end of the upgrade unit list.

        :type  group_id: :class:`str`
        :param group_id: (required)
        :type  upgrade_unit_list: :class:`com.vmware.nsx.model_client.UpgradeUnitList`
        :param upgrade_unit_list: (required)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnitList`
        :return: com.vmware.nsx.model.UpgradeUnitList
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
        return self._invoke('addupgradeunits',
                            {
                            'group_id': group_id,
                            'upgrade_unit_list': upgrade_unit_list,
                            })

    def create(self,
               upgrade_unit_group,
               ):
        """
        Create a group of upgrade units.

        :type  upgrade_unit_group: :class:`com.vmware.nsx.model_client.UpgradeUnitGroup`
        :param upgrade_unit_group: (required)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnitGroup`
        :return: com.vmware.nsx.model.UpgradeUnitGroup
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
                            'upgrade_unit_group': upgrade_unit_group,
                            })

    def delete(self,
               group_id,
               ):
        """
        Delete the specified group. NOTE - A group can be deleted only if it is
        empty. If user tries to delete a group containing one or more upgrade
        units, the operation will fail and an error will be returned.

        :type  group_id: :class:`str`
        :param group_id: (required)
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
                            'group_id': group_id,
                            })

    def get(self,
            group_id,
            summary=None,
            ):
        """
        Returns information about a specific upgrade unit group in the upgrade
        plan. If request parameter summary is set to true, then only count of
        upgrade units will be returned, upgrade units list will be empty.

        :type  group_id: :class:`str`
        :param group_id: (required)
        :type  summary: :class:`bool` or ``None``
        :param summary: Flag indicating whether to return the summary (optional, default to
            false)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnitGroup`
        :return: com.vmware.nsx.model.UpgradeUnitGroup
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
                            'group_id': group_id,
                            'summary': summary,
                            })

    def list(self,
             component_type=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             summary=None,
             sync=None,
             ):
        """
        Return information of all upgrade unit groups in the upgrade plan. If
        request parameter summary is set to true, then only count of upgrade
        units will be returned, upgrade units list will be empty. If request
        parameter component type is specified, then all upgrade unit groups for
        that component will be returned.

        :type  component_type: :class:`str` or ``None``
        :param component_type: Component type based on which upgrade unit groups to be filtered
            (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  summary: :class:`bool` or ``None``
        :param summary: Flag indicating whether to return summary (optional, default to
            false)
        :type  sync: :class:`bool` or ``None``
        :param sync: Synchronize before returning upgrade unit groups (optional, default
            to false)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnitGroupListResult`
        :return: com.vmware.nsx.model.UpgradeUnitGroupListResult
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
                            'component_type': component_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'summary': summary,
                            'sync': sync,
                            })

    def reorder(self,
                group_id,
                reorder_request,
                ):
        """
        Reorder an upgrade unit group by placing it before/after the specified
        upgrade unit group.

        :type  group_id: :class:`str`
        :param group_id: (required)
        :type  reorder_request: :class:`com.vmware.nsx.model_client.ReorderRequest`
        :param reorder_request: (required)
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
        return self._invoke('reorder',
                            {
                            'group_id': group_id,
                            'reorder_request': reorder_request,
                            })

    def update(self,
               group_id,
               upgrade_unit_group,
               ):
        """
        Update the specified upgrade unit group. Removal of upgrade units from
        the group using this is not allowed. An error will be returned in that
        case. Following extended_configuration is supported: Key: upgrade_mode
        Supported values: maintenance_mode,in_place Default: maintenance_mode
        Key: maintenance_mode_config_vsan_mode Supported values:
        evacuate_all_data, ensure_object_accessibility, no_action Default:
        ensure_object_accessibility Key:
        maintenance_mode_config_evacuate_powered_off_vms Supported values:
        true, false Default: false Key: rebootless_upgrade Supported values:
        true, false Default: true

        :type  group_id: :class:`str`
        :param group_id: (required)
        :type  upgrade_unit_group: :class:`com.vmware.nsx.model_client.UpgradeUnitGroup`
        :param upgrade_unit_group: (required)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnitGroup`
        :return: com.vmware.nsx.model.UpgradeUnitGroup
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
                            'group_id': group_id,
                            'upgrade_unit_group': upgrade_unit_group,
                            })
class UpgradeUnitGroupsStatus(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.upgrade_unit_groups_status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpgradeUnitGroupsStatusStub)
        self._VAPI_OPERATION_IDS = {}


    def getall(self,
               component_type=None,
               cursor=None,
               included_fields=None,
               page_size=None,
               sort_ascending=None,
               sort_by=None,
               ):
        """
        Get upgrade status for upgrade unit groups

        :type  component_type: :class:`str` or ``None``
        :param component_type: Component type on which the action is performed or on which the
            results are filtered (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnitGroupStatusListResult`
        :return: com.vmware.nsx.model.UpgradeUnitGroupStatusListResult
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
        return self._invoke('getall',
                            {
                            'component_type': component_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class UpgradeUnits(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.upgrade_units'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpgradeUnitsStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            upgrade_unit_id,
            ):
        """
        Get a specific upgrade unit

        :type  upgrade_unit_id: :class:`str`
        :param upgrade_unit_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnit`
        :return: com.vmware.nsx.model.UpgradeUnit
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
                            'upgrade_unit_id': upgrade_unit_id,
                            })

    def list(self,
             component_type=None,
             current_version=None,
             cursor=None,
             group_id=None,
             has_warnings=None,
             included_fields=None,
             metadata=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             upgrade_unit_type=None,
             ):
        """
        Get upgrade units

        :type  component_type: :class:`str` or ``None``
        :param component_type: Component type based on which upgrade units to be filtered
            (optional)
        :type  current_version: :class:`str` or ``None``
        :param current_version: Current version of upgrade unit based on which upgrade units to be
            filtered (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  group_id: :class:`str` or ``None``
        :param group_id: UUID of group based on which upgrade units to be filtered
            (optional)
        :type  has_warnings: :class:`bool` or ``None``
        :param has_warnings: Flag to indicate whether to return only upgrade units with warnings
            (optional, default to false)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  metadata: :class:`str` or ``None``
        :param metadata: Metadata about upgrade unit to filter on (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  upgrade_unit_type: :class:`str` or ``None``
        :param upgrade_unit_type: Upgrade unit type based on which upgrade units to be filtered
            (optional)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnitListResult`
        :return: com.vmware.nsx.model.UpgradeUnitListResult
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
                            'component_type': component_type,
                            'current_version': current_version,
                            'cursor': cursor,
                            'group_id': group_id,
                            'has_warnings': has_warnings,
                            'included_fields': included_fields,
                            'metadata': metadata,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'upgrade_unit_type': upgrade_unit_type,
                            })
class UpgradeUnitsStats(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.upgrade_units_stats'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpgradeUnitsStatsStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             sync=None,
             ):
        """
        Get upgrade units stats

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  sync: :class:`bool` or ``None``
        :param sync: Synchronize before returning upgrade unit stats (optional, default
            to false)
        :rtype: :class:`com.vmware.nsx.model_client.UpgradeUnitTypeStatsList`
        :return: com.vmware.nsx.model.UpgradeUnitTypeStatsList
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
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'sync': sync,
                            })
class VersionWhitelist(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade.version_whitelist'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VersionWhitelistStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            component_type,
            ):
        """
        Get whitelist of versions for a component. Component can include HOST,
        EDGE, CCP, MP

        :type  component_type: :class:`str`
        :param component_type: (required)
        :rtype: :class:`com.vmware.nsx.model_client.AcceptableComponentVersion`
        :return: com.vmware.nsx.model.AcceptableComponentVersion
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
                            'component_type': component_type,
                            })

    def list(self):
        """
        Get whitelist of versions for different components


        :rtype: :class:`com.vmware.nsx.model_client.AcceptableComponentVersionList`
        :return: com.vmware.nsx.model.AcceptableComponentVersionList
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
               component_type,
               version_list,
               ):
        """
        Update the version whitelist for the specified component type (HOST,
        EDGE, CCP, MP).

        :type  component_type: :class:`str`
        :param component_type: (required)
        :type  version_list: :class:`com.vmware.nsx.model_client.VersionList`
        :param version_list: (required)
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
                            'component_type': component_type,
                            'version_list': version_list,
                            })
class _BundlesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for cancelupload operation
        cancelupload_input_type = type.StructType('operation-input', {
            'bundle_id': type.StringType(),
        })
        cancelupload_error_dict = {
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
        cancelupload_input_value_validator_list = [
        ]
        cancelupload_output_validator_list = [
        ]
        cancelupload_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/bundles/{bundle-id}?action=cancel_upload',
            path_variables={
                'bundle_id': 'bundle-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'upgrade_bundle_fetch_request': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeBundleFetchRequest'),
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
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/bundles',
            request_body_parameter='upgrade_bundle_fetch_request',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'bundle_id': type.StringType(),
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
            url_template='/api/v1/upgrade/bundles/{bundle-id}',
            path_variables={
                'bundle_id': 'bundle-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'cancelupload': {
                'input_type': cancelupload_input_type,
                'output_type': type.VoidType(),
                'errors': cancelupload_error_dict,
                'input_value_validator_list': cancelupload_input_value_validator_list,
                'output_validator_list': cancelupload_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeBundleId'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeBundleInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'cancelupload': cancelupload_rest_metadata,
            'create': create_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.upgrade.bundles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _FunctionalStateStub(ApiInterfaceStub):
    def __init__(self, config):
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
            url_template='/api/v1/upgrade/functional-state',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UcFunctionalState'),
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
            self, iface_name='com.vmware.nsx.upgrade.functional_state',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _HistoryStub(ApiInterfaceStub):
    def __init__(self, config):
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
            url_template='/api/v1/upgrade/history',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeHistoryList'),
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
            self, iface_name='com.vmware.nsx.upgrade.history',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NodesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'component_version': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/upgrade/nodes',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
                'component_version': 'component_version',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NodeInfoListResult'),
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
            self, iface_name='com.vmware.nsx.upgrade.nodes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NodesSummaryStub(ApiInterfaceStub):
    def __init__(self, config):
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
            url_template='/api/v1/upgrade/nodes-summary',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NodeSummaryList'),
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
            self, iface_name='com.vmware.nsx.upgrade.nodes_summary',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _PlanStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for continue operation
        continue_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'skip': type.OptionalType(type.BooleanType()),
        })
        continue_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        continue_input_value_validator_list = [
        ]
        continue_output_validator_list = [
        ]
        continue_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/plan?action=continue',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
                'skip': 'skip',
            },
            content_type='application/json'
        )

        # properties for pause operation
        pause_input_type = type.StructType('operation-input', {})
        pause_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        pause_input_value_validator_list = [
        ]
        pause_output_validator_list = [
        ]
        pause_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/plan?action=pause',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for reset operation
        reset_input_type = type.StructType('operation-input', {
            'component_type': type.StringType(),
        })
        reset_error_dict = {
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
        reset_input_value_validator_list = [
        ]
        reset_output_validator_list = [
        ]
        reset_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/plan?action=reset',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
            },
            content_type='application/json'
        )

        # properties for start operation
        start_input_type = type.StructType('operation-input', {})
        start_error_dict = {
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
        start_input_value_validator_list = [
        ]
        start_output_validator_list = [
        ]
        start_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/plan?action=start',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for upgradeselectedunits operation
        upgradeselectedunits_input_type = type.StructType('operation-input', {
            'upgrade_unit_list': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitList'),
        })
        upgradeselectedunits_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        upgradeselectedunits_input_value_validator_list = [
        ]
        upgradeselectedunits_output_validator_list = [
        ]
        upgradeselectedunits_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/plan?action=upgrade_selected_units',
            request_body_parameter='upgrade_unit_list',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'continue': {
                'input_type': continue_input_type,
                'output_type': type.VoidType(),
                'errors': continue_error_dict,
                'input_value_validator_list': continue_input_value_validator_list,
                'output_validator_list': continue_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'pause': {
                'input_type': pause_input_type,
                'output_type': type.VoidType(),
                'errors': pause_error_dict,
                'input_value_validator_list': pause_input_value_validator_list,
                'output_validator_list': pause_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reset': {
                'input_type': reset_input_type,
                'output_type': type.VoidType(),
                'errors': reset_error_dict,
                'input_value_validator_list': reset_input_value_validator_list,
                'output_validator_list': reset_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'start': {
                'input_type': start_input_type,
                'output_type': type.VoidType(),
                'errors': start_error_dict,
                'input_value_validator_list': start_input_value_validator_list,
                'output_validator_list': start_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'upgradeselectedunits': {
                'input_type': upgradeselectedunits_input_type,
                'output_type': type.VoidType(),
                'errors': upgradeselectedunits_error_dict,
                'input_value_validator_list': upgradeselectedunits_input_value_validator_list,
                'output_validator_list': upgradeselectedunits_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'continue': continue_rest_metadata,
            'pause': pause_rest_metadata,
            'reset': reset_rest_metadata,
            'start': start_rest_metadata,
            'upgradeselectedunits': upgradeselectedunits_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.upgrade.plan',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatusSummaryStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'selection_status': type.OptionalType(type.StringType()),
            'show_history': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/upgrade/status-summary',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
                'selection_status': 'selection_status',
                'show_history': 'show_history',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeStatus'),
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
            self, iface_name='com.vmware.nsx.upgrade.status_summary',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SummaryStub(ApiInterfaceStub):
    def __init__(self, config):
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
            url_template='/api/v1/upgrade/summary',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeSummary'),
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
            self, iface_name='com.vmware.nsx.upgrade.summary',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _UcUpgradeStatusStub(ApiInterfaceStub):
    def __init__(self, config):
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
            url_template='/api/v1/upgrade/uc-upgrade-status',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UcUpgradeStatus'),
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
            self, iface_name='com.vmware.nsx.upgrade.uc_upgrade_status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _UpgradeChecksInfoStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/upgrade/upgrade-checks-info',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComponentUpgradeChecksInfoListResult'),
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
            self, iface_name='com.vmware.nsx.upgrade.upgrade_checks_info',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _UpgradeUnitGroupsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for addupgradeunits operation
        addupgradeunits_input_type = type.StructType('operation-input', {
            'group_id': type.StringType(),
            'upgrade_unit_list': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitList'),
        })
        addupgradeunits_error_dict = {
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
        addupgradeunits_input_value_validator_list = [
        ]
        addupgradeunits_output_validator_list = [
        ]
        addupgradeunits_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/upgrade-unit-groups/{group-id}?action=add_upgrade_units',
            request_body_parameter='upgrade_unit_list',
            path_variables={
                'group_id': 'group-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'upgrade_unit_group': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitGroup'),
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
            url_template='/api/v1/upgrade/upgrade-unit-groups',
            request_body_parameter='upgrade_unit_group',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'group_id': type.StringType(),
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
            url_template='/api/v1/upgrade/upgrade-unit-groups/{group-id}',
            path_variables={
                'group_id': 'group-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'group_id': type.StringType(),
            'summary': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/upgrade/upgrade-unit-groups/{group-id}',
            path_variables={
                'group_id': 'group-id',
            },
            query_parameters={
                'summary': 'summary',
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'summary': type.OptionalType(type.BooleanType()),
            'sync': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/upgrade/upgrade-unit-groups',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'summary': 'summary',
                'sync': 'sync',
            },
            content_type='application/json'
        )

        # properties for reorder operation
        reorder_input_type = type.StructType('operation-input', {
            'group_id': type.StringType(),
            'reorder_request': type.ReferenceType('com.vmware.nsx.model_client', 'ReorderRequest'),
        })
        reorder_error_dict = {
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
        reorder_input_value_validator_list = [
        ]
        reorder_output_validator_list = [
        ]
        reorder_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/upgrade-unit-groups/{group-id}?action=reorder',
            request_body_parameter='reorder_request',
            path_variables={
                'group_id': 'group-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'group_id': type.StringType(),
            'upgrade_unit_group': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitGroup'),
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
            url_template='/api/v1/upgrade/upgrade-unit-groups/{group-id}',
            request_body_parameter='upgrade_unit_group',
            path_variables={
                'group_id': 'group-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'addupgradeunits': {
                'input_type': addupgradeunits_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitList'),
                'errors': addupgradeunits_error_dict,
                'input_value_validator_list': addupgradeunits_input_value_validator_list,
                'output_validator_list': addupgradeunits_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitGroup'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitGroup'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitGroupListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reorder': {
                'input_type': reorder_input_type,
                'output_type': type.VoidType(),
                'errors': reorder_error_dict,
                'input_value_validator_list': reorder_input_value_validator_list,
                'output_validator_list': reorder_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitGroup'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'addupgradeunits': addupgradeunits_rest_metadata,
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'reorder': reorder_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.upgrade.upgrade_unit_groups',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _UpgradeUnitGroupsStatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for getall operation
        getall_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
        })
        getall_error_dict = {
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
        getall_input_value_validator_list = [
        ]
        getall_output_validator_list = [
        ]
        getall_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/upgrade/upgrade-unit-groups-status',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'getall': {
                'input_type': getall_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitGroupStatusListResult'),
                'errors': getall_error_dict,
                'input_value_validator_list': getall_input_value_validator_list,
                'output_validator_list': getall_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'getall': getall_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.upgrade.upgrade_unit_groups_status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _UpgradeUnitsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'upgrade_unit_id': type.StringType(),
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
            url_template='/api/v1/upgrade/upgrade-units/{upgrade-unit-id}',
            path_variables={
                'upgrade_unit_id': 'upgrade-unit-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'current_version': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'group_id': type.OptionalType(type.StringType()),
            'has_warnings': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'metadata': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'upgrade_unit_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/upgrade/upgrade-units',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
                'current_version': 'current_version',
                'cursor': 'cursor',
                'group_id': 'group_id',
                'has_warnings': 'has_warnings',
                'included_fields': 'included_fields',
                'metadata': 'metadata',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'upgrade_unit_type': 'upgrade_unit_type',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnit'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.upgrade.upgrade_units',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _UpgradeUnitsStatsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'sync': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/upgrade/upgrade-units-stats',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'sync': 'sync',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'UpgradeUnitTypeStatsList'),
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
            self, iface_name='com.vmware.nsx.upgrade.upgrade_units_stats',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _VersionWhitelistStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'component_type': type.StringType(),
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
            url_template='/api/v1/upgrade/version-whitelist/{component_type}',
            path_variables={
                'component_type': 'component_type',
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
            url_template='/api/v1/upgrade/version-whitelist',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'component_type': type.StringType(),
            'version_list': type.ReferenceType('com.vmware.nsx.model_client', 'VersionList'),
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
            url_template='/api/v1/upgrade/version-whitelist/{component_type}',
            request_body_parameter='version_list',
            path_variables={
                'component_type': 'component_type',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'AcceptableComponentVersion'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'AcceptableComponentVersionList'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
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
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.upgrade.version_whitelist',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Bundles': Bundles,
        'FunctionalState': FunctionalState,
        'History': History,
        'Nodes': Nodes,
        'NodesSummary': NodesSummary,
        'Plan': Plan,
        'StatusSummary': StatusSummary,
        'Summary': Summary,
        'UcUpgradeStatus': UcUpgradeStatus,
        'UpgradeChecksInfo': UpgradeChecksInfo,
        'UpgradeUnitGroups': UpgradeUnitGroups,
        'UpgradeUnitGroupsStatus': UpgradeUnitGroupsStatus,
        'UpgradeUnits': UpgradeUnits,
        'UpgradeUnitsStats': UpgradeUnitsStats,
        'VersionWhitelist': VersionWhitelist,
        'bundles': 'com.vmware.nsx.upgrade.bundles_client.StubFactory',
        'eula': 'com.vmware.nsx.upgrade.eula_client.StubFactory',
        'plan': 'com.vmware.nsx.upgrade.plan_client.StubFactory',
        'upgrade_unit_groups': 'com.vmware.nsx.upgrade.upgrade_unit_groups_client.StubFactory',
        'upgrade_units': 'com.vmware.nsx.upgrade.upgrade_units_client.StubFactory',
    }

