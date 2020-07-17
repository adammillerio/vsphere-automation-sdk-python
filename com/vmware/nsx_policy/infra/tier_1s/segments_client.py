# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.tier_1s.segments.
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


class Ports(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_1s.segments.ports'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PortsStub)
        self._VAPI_OPERATION_IDS = {}


    def delete(self,
               tier1_id,
               segment_id,
               port_id,
               ):
        """
        Delete a Tier-1 segment port by giving ID.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :type  port_id: :class:`str`
        :param port_id: (required)
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'port_id': port_id,
                            })

    def get(self,
            tier1_id,
            segment_id,
            port_id,
            ):
        """
        Get detail information on a Tier-1 segment port by giving ID.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :type  port_id: :class:`str`
        :param port_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.SegmentPort`
        :return: com.vmware.nsx_policy.model.SegmentPort
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'port_id': port_id,
                            })

    def list(self,
             tier1_id,
             segment_id,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List all the ports for a Tier-1 segment.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_mark_for_delete_objects: :class:`bool` or ``None``
        :param include_mark_for_delete_objects: Include objects that are marked for deletion in results (optional,
            default to false)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.SegmentPortListResult`
        :return: com.vmware.nsx_policy.model.SegmentPortListResult
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier1_id,
              segment_id,
              port_id,
              segment_port,
              ):
        """
        Create a Tier-1 segment port if it does not exist based on the IDs, or
        update existing port information by replacing the port object fields
        which presents in the request body.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :type  port_id: :class:`str`
        :param port_id: (required)
        :type  segment_port: :class:`com.vmware.nsx_policy.model_client.SegmentPort`
        :param segment_port: (required)
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
        return self._invoke('patch',
                            {
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'port_id': port_id,
                            'segment_port': segment_port,
                            })

    def update(self,
               tier1_id,
               segment_id,
               port_id,
               segment_port,
               ):
        """
        Create a Tier-1 segment port if it does not exist based on the IDs, or
        update existing port information by replacing the port object already
        exists.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :type  port_id: :class:`str`
        :param port_id: (required)
        :type  segment_port: :class:`com.vmware.nsx_policy.model_client.SegmentPort`
        :param segment_port: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.SegmentPort`
        :return: com.vmware.nsx_policy.model.SegmentPort
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'port_id': port_id,
                            'segment_port': segment_port,
                            })
class SegmentMonitoringProfileBindingMaps(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_1s.segments.segment_monitoring_profile_binding_maps'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SegmentMonitoringProfileBindingMapsStub)
        self._VAPI_OPERATION_IDS = {}


    def delete(self,
               tier1_id,
               segment_id,
               segment_monitoring_profile_binding_map_id,
               ):
        """
        API will delete Segment Monitoring Profile Binding Profile.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  segment_id: :class:`str`
        :param segment_id: Segment ID (required)
        :type  segment_monitoring_profile_binding_map_id: :class:`str`
        :param segment_monitoring_profile_binding_map_id: Segment Monitoring Profile Binding Map ID (required)
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'segment_monitoring_profile_binding_map_id': segment_monitoring_profile_binding_map_id,
                            })

    def get(self,
            tier1_id,
            segment_id,
            segment_monitoring_profile_binding_map_id,
            ):
        """
        API will get Segment Monitoring Profile Binding Map.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  segment_id: :class:`str`
        :param segment_id: Segment ID (required)
        :type  segment_monitoring_profile_binding_map_id: :class:`str`
        :param segment_monitoring_profile_binding_map_id: Segment Monitoring Profile Binding Map ID (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.SegmentMonitoringProfileBindingMap`
        :return: com.vmware.nsx_policy.model.SegmentMonitoringProfileBindingMap
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'segment_monitoring_profile_binding_map_id': segment_monitoring_profile_binding_map_id,
                            })

    def list(self,
             tier1_id,
             segment_id,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        API will list all Segment Monitoring Profile Binding Maps in current
        segment id.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_mark_for_delete_objects: :class:`bool` or ``None``
        :param include_mark_for_delete_objects: Include objects that are marked for deletion in results (optional,
            default to false)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.SegmentMonitoringProfileBindingMapListResult`
        :return: com.vmware.nsx_policy.model.SegmentMonitoringProfileBindingMapListResult
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier1_id,
              segment_id,
              segment_monitoring_profile_binding_map_id,
              segment_monitoring_profile_binding_map,
              ):
        """
        API will create segment monitoring profile binding map.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  segment_id: :class:`str`
        :param segment_id: Segment ID (required)
        :type  segment_monitoring_profile_binding_map_id: :class:`str`
        :param segment_monitoring_profile_binding_map_id: Segment Monitoring Profile Binding Map ID (required)
        :type  segment_monitoring_profile_binding_map: :class:`com.vmware.nsx_policy.model_client.SegmentMonitoringProfileBindingMap`
        :param segment_monitoring_profile_binding_map: (required)
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
        return self._invoke('patch',
                            {
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'segment_monitoring_profile_binding_map_id': segment_monitoring_profile_binding_map_id,
                            'segment_monitoring_profile_binding_map': segment_monitoring_profile_binding_map,
                            })

    def update(self,
               tier1_id,
               segment_id,
               segment_monitoring_profile_binding_map_id,
               segment_monitoring_profile_binding_map,
               ):
        """
        API will update Segment Monitoring Profile Binding Map.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  segment_id: :class:`str`
        :param segment_id: Segment ID (required)
        :type  segment_monitoring_profile_binding_map_id: :class:`str`
        :param segment_monitoring_profile_binding_map_id: Segment Monitoring Profile Binding Map ID (required)
        :type  segment_monitoring_profile_binding_map: :class:`com.vmware.nsx_policy.model_client.SegmentMonitoringProfileBindingMap`
        :param segment_monitoring_profile_binding_map: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.SegmentMonitoringProfileBindingMap`
        :return: com.vmware.nsx_policy.model.SegmentMonitoringProfileBindingMap
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'segment_monitoring_profile_binding_map_id': segment_monitoring_profile_binding_map_id,
                            'segment_monitoring_profile_binding_map': segment_monitoring_profile_binding_map,
                            })
class StaticArp(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_1s.segments.static_arp'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StaticArpStub)
        self._VAPI_OPERATION_IDS = {}


    def delete(self,
               tier1_id,
               segment_id,
               ):
        """
        Delete static ARP config

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            })

    def get(self,
            tier1_id,
            segment_id,
            ):
        """
        Read static ARP config

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.StaticARPConfig`
        :return: com.vmware.nsx_policy.model.StaticARPConfig
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            })

    def patch(self,
              tier1_id,
              segment_id,
              static_arp_config,
              ):
        """
        Create static ARP config with Tier-1 and segment IDs provided if it
        doesn't exist, update with provided config if it's already created.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :type  static_arp_config: :class:`com.vmware.nsx_policy.model_client.StaticARPConfig`
        :param static_arp_config: (required)
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
        return self._invoke('patch',
                            {
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'static_arp_config': static_arp_config,
                            })

    def update(self,
               tier1_id,
               segment_id,
               static_arp_config,
               ):
        """
        Create static ARP config with Tier-1 and segment IDs provided if it
        doesn't exist, update with provided config if it's already created.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segment_id: :class:`str`
        :param segment_id: (required)
        :type  static_arp_config: :class:`com.vmware.nsx_policy.model_client.StaticARPConfig`
        :param static_arp_config: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.StaticARPConfig`
        :return: com.vmware.nsx_policy.model.StaticARPConfig
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
                            'tier1_id': tier1_id,
                            'segment_id': segment_id,
                            'static_arp_config': static_arp_config,
                            })
class Statistics(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_1s.segments.statistics'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatisticsStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            tier1_id,
            segments_id,
            cursor=None,
            edge_path=None,
            enforcement_point_path=None,
            include_mark_for_delete_objects=None,
            included_fields=None,
            page_size=None,
            sort_ascending=None,
            sort_by=None,
            ):
        """
        Get tier1 segment statistics information.

        :type  tier1_id: :class:`str`
        :param tier1_id: (required)
        :type  segments_id: :class:`str`
        :param segments_id: (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  edge_path: :class:`str` or ``None``
        :param edge_path: Policy path of edge node (optional)
        :type  enforcement_point_path: :class:`str` or ``None``
        :param enforcement_point_path: String Path of the enforcement point (optional)
        :type  include_mark_for_delete_objects: :class:`bool` or ``None``
        :param include_mark_for_delete_objects: Include objects that are marked for deletion in results (optional,
            default to false)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.SegmentStatistics`
        :return: com.vmware.nsx_policy.model.SegmentStatistics
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
                            'tier1_id': tier1_id,
                            'segments_id': segments_id,
                            'cursor': cursor,
                            'edge_path': edge_path,
                            'enforcement_point_path': enforcement_point_path,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class _PortsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'port_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
                'port_id': 'port-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'port_id': type.StringType(),
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
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
                'port_id': 'port-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'include_mark_for_delete_objects': type.OptionalType(type.BooleanType()),
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'include_mark_for_delete_objects': 'include_mark_for_delete_objects',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'port_id': type.StringType(),
            'segment_port': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentPort'),
        })
        patch_error_dict = {
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
        patch_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}',
            request_body_parameter='segment_port',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
                'port_id': 'port-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'port_id': type.StringType(),
            'segment_port': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentPort'),
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
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}',
            request_body_parameter='segment_port',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
                'port_id': 'port-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentPort'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentPortListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentPort'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_1s.segments.ports',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SegmentMonitoringProfileBindingMapsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'segment_monitoring_profile_binding_map_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-monitoring-profile-binding-maps/{segment-monitoring-profile-binding-map-id}',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
                'segment_monitoring_profile_binding_map_id': 'segment-monitoring-profile-binding-map-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'segment_monitoring_profile_binding_map_id': type.StringType(),
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
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-monitoring-profile-binding-maps/{segment-monitoring-profile-binding-map-id}',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
                'segment_monitoring_profile_binding_map_id': 'segment-monitoring-profile-binding-map-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'include_mark_for_delete_objects': type.OptionalType(type.BooleanType()),
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-monitoring-profile-binding-maps',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'include_mark_for_delete_objects': 'include_mark_for_delete_objects',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'segment_monitoring_profile_binding_map_id': type.StringType(),
            'segment_monitoring_profile_binding_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentMonitoringProfileBindingMap'),
        })
        patch_error_dict = {
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
        patch_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-monitoring-profile-binding-maps/{segment-monitoring-profile-binding-map-id}',
            request_body_parameter='segment_monitoring_profile_binding_map',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
                'segment_monitoring_profile_binding_map_id': 'segment-monitoring-profile-binding-map-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'segment_monitoring_profile_binding_map_id': type.StringType(),
            'segment_monitoring_profile_binding_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentMonitoringProfileBindingMap'),
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
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-monitoring-profile-binding-maps/{segment-monitoring-profile-binding-map-id}',
            request_body_parameter='segment_monitoring_profile_binding_map',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
                'segment_monitoring_profile_binding_map_id': 'segment-monitoring-profile-binding-map-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentMonitoringProfileBindingMap'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentMonitoringProfileBindingMapListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentMonitoringProfileBindingMap'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_1s.segments.segment_monitoring_profile_binding_maps',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StaticArpStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/static-arp',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
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
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/static-arp',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'static_ARP_config': type.ReferenceType('com.vmware.nsx_policy.model_client', 'StaticARPConfig'),
        })
        patch_error_dict = {
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
        patch_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/static-arp',
            request_body_parameter='static_ARP_config',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segment_id': type.StringType(),
            'static_ARP_config': type.ReferenceType('com.vmware.nsx_policy.model_client', 'StaticARPConfig'),
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
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/static-arp',
            request_body_parameter='static_ARP_config',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'StaticARPConfig'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'StaticARPConfig'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_1s.segments.static_arp',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatisticsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'segments_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'edge_path': type.OptionalType(type.StringType()),
            'enforcement_point_path': type.OptionalType(type.StringType()),
            'include_mark_for_delete_objects': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
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
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segments-id}/statistics',
            path_variables={
                'tier1_id': 'tier-1-id',
                'segments_id': 'segments-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'edge_path': 'edge_path',
                'enforcement_point_path': 'enforcement_point_path',
                'include_mark_for_delete_objects': 'include_mark_for_delete_objects',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SegmentStatistics'),
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
            self, iface_name='com.vmware.nsx_policy.infra.tier_1s.segments.statistics',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Ports': Ports,
        'SegmentMonitoringProfileBindingMaps': SegmentMonitoringProfileBindingMaps,
        'StaticArp': StaticArp,
        'Statistics': Statistics,
        'ports': 'com.vmware.nsx_policy.infra.tier_1s.segments.ports_client.StubFactory',
    }

