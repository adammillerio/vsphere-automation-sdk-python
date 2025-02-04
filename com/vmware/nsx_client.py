# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.
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


class Associations(VapiInterface):
    """
    
    """
    LIST_ASSOCIATED_RESOURCE_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``associatedResourceType`` of method
    :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_IPSET = "IPSet"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_MACSET = "MACSet"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_LOGICALSWITCH = "LogicalSwitch"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_LOGICALPORT = "LogicalPort"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_VIRTUALMACHINE = "VirtualMachine"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_DIRECTORYGROUP = "DirectoryGroup"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_VIRTUALNETWORKINTERFACE = "VirtualNetworkInterface"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """
    LIST_RESOURCE_TYPE_TRANSPORTNODE = "TransportNode"
    """
    Possible value for ``resourceType`` of method :func:`Associations.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.associations'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _AssociationsStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             associated_resource_type,
             resource_id,
             resource_type,
             cursor=None,
             fetch_ancestors=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about resources that are associated with the given
        resource. Id and type of the resource for which associated resources
        are to be fetched are to be specified as query parameter in the URI.
        Resource type of the associated resources must be specified as query
        parameter.

        :type  associated_resource_type: :class:`str`
        :param associated_resource_type: Resource type valid for use as target in association API (required)
        :type  resource_id: :class:`str`
        :param resource_id: The resource for which associated resources are to be fetched
            (required)
        :type  resource_type: :class:`str`
        :param resource_type: Resource type valid for use as source in association API (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  fetch_ancestors: :class:`bool` or ``None``
        :param fetch_ancestors: Fetch complete list of associated resources considering containment
            and nesting (optional, default to false)
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
        :rtype: :class:`com.vmware.nsx.model_client.AssociationListResult`
        :return: com.vmware.nsx.model.AssociationListResult
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
                            'associated_resource_type': associated_resource_type,
                            'resource_id': resource_id,
                            'resource_type': resource_type,
                            'cursor': cursor,
                            'fetch_ancestors': fetch_ancestors,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class Batch(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.batch'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BatchStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               batch_request,
               atomic=None,
               ):
        """
        Enables you to make multiple API requests using a single request. The
        batch API takes in an array of logical HTTP requests represented as
        JSON arrays. Each request has a method (GET, PUT, POST, or DELETE), a
        relative_url (the portion of the URL after https://<nsx-mgr>/api/),
        optional headers array (corresponding to HTTP headers) and an optional
        body (for POST and PUT requests). The batch API returns an array of
        logical HTTP responses represented as JSON arrays. Each response has a
        status code, an optional headers array and an optional body (which is a
        JSON-encoded string).

        :type  batch_request: :class:`com.vmware.nsx.model_client.BatchRequest`
        :param batch_request: (required)
        :type  atomic: :class:`bool` or ``None``
        :param atomic: transactional atomicity for the batch of requests embedded in the
            batch list (optional, default to false)
        :rtype: :class:`com.vmware.nsx.model_client.BatchResponse`
        :return: com.vmware.nsx.model.BatchResponse
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
                            'batch_request': batch_request,
                            'atomic': atomic,
                            })
class BridgeClusters(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.bridge_clusters'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BridgeClustersStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               bridge_cluster,
               ):
        """
        Creates a bridge cluster. It is collection of transport nodes that will
        do the bridging for overlay network to vlan networks. Bridge cluster
        may have one or more transport nodes

        :type  bridge_cluster: :class:`com.vmware.nsx.model_client.BridgeCluster`
        :param bridge_cluster: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeCluster`
        :return: com.vmware.nsx.model.BridgeCluster
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
                            'bridge_cluster': bridge_cluster,
                            })

    def delete(self,
               bridgecluster_id,
               ):
        """
        Removes the specified Bridge Cluster.

        :type  bridgecluster_id: :class:`str`
        :param bridgecluster_id: (required)
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
                            'bridgecluster_id': bridgecluster_id,
                            })

    def get(self,
            bridgecluster_id,
            ):
        """
        Returns information about a specified bridge cluster.

        :type  bridgecluster_id: :class:`str`
        :param bridgecluster_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeCluster`
        :return: com.vmware.nsx.model.BridgeCluster
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
                            'bridgecluster_id': bridgecluster_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all configured bridge clusters

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
        :rtype: :class:`com.vmware.nsx.model_client.BridgeClusterListResult`
        :return: com.vmware.nsx.model.BridgeClusterListResult
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
                            })

    def update(self,
               bridgecluster_id,
               bridge_cluster,
               ):
        """
        Modifies a existing bridge cluster. One of more transport nodes can be
        added or removed from the bridge cluster using this API.

        :type  bridgecluster_id: :class:`str`
        :param bridgecluster_id: (required)
        :type  bridge_cluster: :class:`com.vmware.nsx.model_client.BridgeCluster`
        :param bridge_cluster: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeCluster`
        :return: com.vmware.nsx.model.BridgeCluster
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
                            'bridgecluster_id': bridgecluster_id,
                            'bridge_cluster': bridge_cluster,
                            })
class BridgeEndpointProfiles(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.bridge_endpoint_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BridgeEndpointProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               bridge_endpoint_profile,
               ):
        """
        Creates a Bridge Endpoint Profile. Profile contains edge cluster id,
        indexes of the member nodes, fialover mode and high availability mode
        for a Bridge EndPoint

        :type  bridge_endpoint_profile: :class:`com.vmware.nsx.model_client.BridgeEndpointProfile`
        :param bridge_endpoint_profile: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeEndpointProfile`
        :return: com.vmware.nsx.model.BridgeEndpointProfile
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
                            'bridge_endpoint_profile': bridge_endpoint_profile,
                            })

    def delete(self,
               bridgeendpointprofile_id,
               ):
        """
        Deletes the specified Bridge Endpoint Profile.

        :type  bridgeendpointprofile_id: :class:`str`
        :param bridgeendpointprofile_id: (required)
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
                            'bridgeendpointprofile_id': bridgeendpointprofile_id,
                            })

    def get(self,
            bridgeendpointprofile_id,
            ):
        """
        Returns information about a specified bridge endpoint profile.

        :type  bridgeendpointprofile_id: :class:`str`
        :param bridgeendpointprofile_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeEndpointProfile`
        :return: com.vmware.nsx.model.BridgeEndpointProfile
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
                            'bridgeendpointprofile_id': bridgeendpointprofile_id,
                            })

    def list(self,
             cursor=None,
             edge_cluster_id=None,
             failover_mode=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all configured bridge endoint profiles

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  edge_cluster_id: :class:`str` or ``None``
        :param edge_cluster_id: Edge Cluster Identifier (optional)
        :type  failover_mode: :class:`str` or ``None``
        :param failover_mode: (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.BridgeEndpointProfileListResult`
        :return: com.vmware.nsx.model.BridgeEndpointProfileListResult
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
                            'edge_cluster_id': edge_cluster_id,
                            'failover_mode': failover_mode,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               bridgeendpointprofile_id,
               bridge_endpoint_profile,
               ):
        """
        Modifies a existing bridge endpoint profile.

        :type  bridgeendpointprofile_id: :class:`str`
        :param bridgeendpointprofile_id: (required)
        :type  bridge_endpoint_profile: :class:`com.vmware.nsx.model_client.BridgeEndpointProfile`
        :param bridge_endpoint_profile: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeEndpointProfile`
        :return: com.vmware.nsx.model.BridgeEndpointProfile
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
                            'bridgeendpointprofile_id': bridgeendpointprofile_id,
                            'bridge_endpoint_profile': bridge_endpoint_profile,
                            })
class BridgeEndpoints(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.bridge_endpoints'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BridgeEndpointsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               bridge_endpoint,
               ):
        """
        Creates a Bridge Endpoint. It describes the physical attributes of the
        bridge like vlan. A logical port can be attached to a vif providing
        bridging functionality from the logical overlay network to the physical
        vlan network

        :type  bridge_endpoint: :class:`com.vmware.nsx.model_client.BridgeEndpoint`
        :param bridge_endpoint: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeEndpoint`
        :return: com.vmware.nsx.model.BridgeEndpoint
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
                            'bridge_endpoint': bridge_endpoint,
                            })

    def delete(self,
               bridgeendpoint_id,
               ):
        """
        Deletes the specified Bridge Endpoint.

        :type  bridgeendpoint_id: :class:`str`
        :param bridgeendpoint_id: (required)
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
                            'bridgeendpoint_id': bridgeendpoint_id,
                            })

    def get(self,
            bridgeendpoint_id,
            ):
        """
        Returns information about a specified bridge endpoint.

        :type  bridgeendpoint_id: :class:`str`
        :param bridgeendpoint_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeEndpoint`
        :return: com.vmware.nsx.model.BridgeEndpoint
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
                            'bridgeendpoint_id': bridgeendpoint_id,
                            })

    def list(self,
             bridge_cluster_id=None,
             bridge_endpoint_profile_id=None,
             cursor=None,
             included_fields=None,
             logical_switch_id=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             vlan_transport_zone_id=None,
             ):
        """
        Returns information about all configured bridge endoints

        :type  bridge_cluster_id: :class:`str` or ``None``
        :param bridge_cluster_id: Bridge Cluster Identifier (optional)
        :type  bridge_endpoint_profile_id: :class:`str` or ``None``
        :param bridge_endpoint_profile_id: Bridge endpoint profile used by the edge cluster (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  logical_switch_id: :class:`str` or ``None``
        :param logical_switch_id: Logical Switch Identifier (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  vlan_transport_zone_id: :class:`str` or ``None``
        :param vlan_transport_zone_id: VLAN transport zone id used by the edge cluster (optional)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeEndpointListResult`
        :return: com.vmware.nsx.model.BridgeEndpointListResult
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
                            'bridge_cluster_id': bridge_cluster_id,
                            'bridge_endpoint_profile_id': bridge_endpoint_profile_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'logical_switch_id': logical_switch_id,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'vlan_transport_zone_id': vlan_transport_zone_id,
                            })

    def update(self,
               bridgeendpoint_id,
               bridge_endpoint,
               ):
        """
        Modifies a existing bridge endpoint.

        :type  bridgeendpoint_id: :class:`str`
        :param bridgeendpoint_id: (required)
        :type  bridge_endpoint: :class:`com.vmware.nsx.model_client.BridgeEndpoint`
        :param bridge_endpoint: (required)
        :rtype: :class:`com.vmware.nsx.model_client.BridgeEndpoint`
        :return: com.vmware.nsx.model.BridgeEndpoint
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
                            'bridgeendpoint_id': bridgeendpoint_id,
                            'bridge_endpoint': bridge_endpoint,
                            })
class Cluster(VapiInterface):
    """
    
    """
    REMOVENODE_FORCE_TRUE = "true"
    """
    Possible value for ``force`` of method :func:`Cluster.removenode`.

    """
    REMOVENODE_FORCE_FALSE = "false"
    """
    Possible value for ``force`` of method :func:`Cluster.removenode`.

    """
    REMOVENODE_GRACEFUL_SHUTDOWN_TRUE = "true"
    """
    Possible value for ``gracefulShutdown`` of method :func:`Cluster.removenode`.

    """
    REMOVENODE_GRACEFUL_SHUTDOWN_FALSE = "false"
    """
    Possible value for ``gracefulShutdown`` of method :func:`Cluster.removenode`.

    """
    REMOVENODE_IGNORE_REPOSITORY_IP_CHECK_TRUE = "true"
    """
    Possible value for ``ignoreRepositoryIpCheck`` of method
    :func:`Cluster.removenode`.

    """
    REMOVENODE_IGNORE_REPOSITORY_IP_CHECK_FALSE = "false"
    """
    Possible value for ``ignoreRepositoryIpCheck`` of method
    :func:`Cluster.removenode`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.cluster'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterStub)
        self._VAPI_OPERATION_IDS = {}


    def backuptoremote(self):
        """
        Request one-time backup. The backup will be uploaded using the same
        server configuration as for automatic backup.


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
        return self._invoke('backuptoremote', None)

    def create(self,
               target_node_id,
               target_uri,
               ):
        """
        Invoke POST request on target cluster node

        :type  target_node_id: :class:`str`
        :param target_node_id: Target node UUID or keyword self (required)
        :type  target_uri: :class:`str`
        :param target_uri: URI of API to invoke on target node (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
             Gateway Timeout
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
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def delete(self,
               target_node_id,
               target_uri,
               ):
        """
        Invoke DELETE request on target cluster node

        :type  target_node_id: :class:`str`
        :param target_node_id: Target node UUID or keyword self (required)
        :type  target_uri: :class:`str`
        :param target_uri: URI of API to invoke on target node (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
             Gateway Timeout
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
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def get(self):
        """
        Returns information about the NSX cluster configuration. An NSX cluster
        has two functions or purposes, commonly referred to as \"roles.\" These
        two roles are control and management. Each NSX installation has a
        single cluster. Separate NSX clusters do not share data. In other
        words, a given data-plane node is attached to only one cluster, not to
        multiple clusters.


        :rtype: :class:`com.vmware.nsx.model_client.ClusterConfig`
        :return: com.vmware.nsx.model.ClusterConfig
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

    def get_0(self,
              node_id,
              ):
        """
        Returns information about the specified NSX cluster node.

        :type  node_id: :class:`str`
        :param node_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ClusterNodeInfo`
        :return: com.vmware.nsx.model.ClusterNodeInfo
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
        return self._invoke('get_0',
                            {
                            'node_id': node_id,
                            })

    def get_1(self,
              target_node_id,
              target_uri,
              ):
        """
        Invoke GET request on target cluster node

        :type  target_node_id: :class:`str`
        :param target_node_id: Target node UUID or keyword self (required)
        :type  target_uri: :class:`str`
        :param target_uri: URI of API to invoke on target node (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
             Gateway Timeout
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
        return self._invoke('get_1',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def joincluster(self,
                    join_cluster_parameters,
                    ):
        """
        Join this node to a NSX Cluster

        :type  join_cluster_parameters: :class:`com.vmware.nsx.model_client.JoinClusterParameters`
        :param join_cluster_parameters: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ClusterConfiguration`
        :return: com.vmware.nsx.model.ClusterConfiguration
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
        return self._invoke('joincluster',
                            {
                            'join_cluster_parameters': join_cluster_parameters,
                            })

    def removenode(self,
                   node_id,
                   force=None,
                   graceful_shutdown=None,
                   ignore_repository_ip_check=None,
                   ):
        """
        Detach a node from the Cluster

        :type  node_id: :class:`str`
        :param node_id: UUID of the node (required)
        :type  force: :class:`str` or ``None``
        :param force: (optional)
        :type  graceful_shutdown: :class:`str` or ``None``
        :param graceful_shutdown: (optional, default to false)
        :type  ignore_repository_ip_check: :class:`str` or ``None``
        :param ignore_repository_ip_check: (optional, default to false)
        :rtype: :class:`com.vmware.nsx.model_client.ClusterConfiguration`
        :return: com.vmware.nsx.model.ClusterConfiguration
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
        return self._invoke('removenode',
                            {
                            'node_id': node_id,
                            'force': force,
                            'graceful_shutdown': graceful_shutdown,
                            'ignore_repository_ip_check': ignore_repository_ip_check,
                            })

    def summarizeinventorytoremote(self):
        """
        Request one-time inventory summary. The backup will be uploaded using
        the same server configuration as for an automatic backup.


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
        return self._invoke('summarizeinventorytoremote', None)

    def update(self,
               target_node_id,
               target_uri,
               ):
        """
        Invoke PUT request on target cluster node

        :type  target_node_id: :class:`str`
        :param target_node_id: Target node UUID or keyword self (required)
        :type  target_uri: :class:`str`
        :param target_uri: URI of API to invoke on target node (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
             Gateway Timeout
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
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })
class ClusterProfiles(VapiInterface):
    """
    
    """
    LIST_RESOURCE_TYPE_EDGEHIGHAVAILABILITYPROFILE = "EdgeHighAvailabilityProfile"
    """
    Possible value for ``resourceType`` of method :func:`ClusterProfiles.list`.

    """
    LIST_RESOURCE_TYPE_BRIDGEHIGHAVAILABILITYCLUSTERPROFILE = "BridgeHighAvailabilityClusterProfile"
    """
    Possible value for ``resourceType`` of method :func:`ClusterProfiles.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.cluster_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               cluster_profile,
               ):
        """
        Create a cluster profile. The resource_type is required.

        :type  cluster_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param cluster_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.ClusterProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.ClusterProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.ClusterProfile`.
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
                            'cluster_profile': cluster_profile,
                            })

    def delete(self,
               cluster_profile_id,
               ):
        """
        Delete a specified cluster profile.

        :type  cluster_profile_id: :class:`str`
        :param cluster_profile_id: (required)
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
                            'cluster_profile_id': cluster_profile_id,
                            })

    def get(self,
            cluster_profile_id,
            ):
        """
        Returns information about a specified cluster profile.

        :type  cluster_profile_id: :class:`str`
        :param cluster_profile_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.ClusterProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.ClusterProfile`.
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
                            'cluster_profile_id': cluster_profile_id,
                            })

    def list(self,
             cursor=None,
             include_system_owned=None,
             included_fields=None,
             page_size=None,
             resource_type=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns paginated list of cluster profiles Cluster profiles define
        policies for edge cluster and bridge cluster.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_system_owned: :class:`bool` or ``None``
        :param include_system_owned: Whether the list result contains system resources (optional,
            default to true)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: Supported cluster profiles. (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ClusterProfileListResult`
        :return: com.vmware.nsx.model.ClusterProfileListResult
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
                            'include_system_owned': include_system_owned,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'resource_type': resource_type,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               cluster_profile_id,
               cluster_profile,
               ):
        """
        Modifie a specified cluster profile. The body of the PUT request must
        include the resource_type.

        :type  cluster_profile_id: :class:`str`
        :param cluster_profile_id: (required)
        :type  cluster_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param cluster_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.ClusterProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.ClusterProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.ClusterProfile`.
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
                            'cluster_profile_id': cluster_profile_id,
                            'cluster_profile': cluster_profile,
                            })
class ComputeCollectionTransportNodeTemplates(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.compute_collection_transport_node_templates'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComputeCollectionTransportNodeTemplatesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               compute_collection_transport_node_template,
               ):
        """
        If automated transport node creation is configured on compute
        collection, this template will serve as the default setting for
        transport node creation. Note- transport node templates APIs are
        deprecated and user is recommended to use transport node profiles APIs
        instead.

        :type  compute_collection_transport_node_template: :class:`com.vmware.nsx.model_client.ComputeCollectionTransportNodeTemplate`
        :param compute_collection_transport_node_template: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollectionTransportNodeTemplate`
        :return: com.vmware.nsx.model.ComputeCollectionTransportNodeTemplate
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
                            'compute_collection_transport_node_template': compute_collection_transport_node_template,
                            })

    def delete(self,
               template_id,
               ):
        """
        Delete the specified compute collection transport node template. Note-
        transport node templates APIs are deprecated and user is recommended to
        use transport node profiles APIs instead.

        :type  template_id: :class:`str`
        :param template_id: (required)
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
                            'template_id': template_id,
                            })

    def get(self,
            template_id,
            ):
        """
        Returns compute collection transportnode template by id Note- transport
        node templates APIs are deprecated and user is recommended to use
        transport node profiles APIs instead.

        :type  template_id: :class:`str`
        :param template_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollectionTransportNodeTemplate`
        :return: com.vmware.nsx.model.ComputeCollectionTransportNodeTemplate
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
                            'template_id': template_id,
                            })

    def list(self,
             compute_collection_id=None,
             ):
        """
        Returns all eligible compute collection transportnode templates Note-
        transport node templates APIs are deprecated and user is recommended to
        use transport node profiles APIs instead.

        :type  compute_collection_id: :class:`str` or ``None``
        :param compute_collection_id: Compute collection id (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeTemplateListResult`
        :return: com.vmware.nsx.model.TransportNodeTemplateListResult
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
                            'compute_collection_id': compute_collection_id,
                            })

    def update(self,
               template_id,
               compute_collection_transport_node_template,
               ):
        """
        Update configuration of compute collection transportnode template.
        Compute_collection_id isn't allowed to be changed since it represents
        the association between ComputeCollection and this template. This is
        determined when ComputeCollectionTransportNodeTemplate got created.
        Note- transport node templates APIs are deprecated and user is
        recommended to use transport node profiles APIs instead.

        :type  template_id: :class:`str`
        :param template_id: (required)
        :type  compute_collection_transport_node_template: :class:`com.vmware.nsx.model_client.ComputeCollectionTransportNodeTemplate`
        :param compute_collection_transport_node_template: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollectionTransportNodeTemplate`
        :return: com.vmware.nsx.model.ComputeCollectionTransportNodeTemplate
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
                            'template_id': template_id,
                            'compute_collection_transport_node_template': compute_collection_transport_node_template,
                            })
class EdgeClusters(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.edge_clusters'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _EdgeClustersStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               edge_cluster,
               ):
        """
        Creates a new edge cluster. It only supports homogeneous members. The
        TransportNodes backed by EdgeNode are only allowed in cluster members.
        DeploymentType (VIRTUAL_MACHINE|PHYSICAL_MACHINE) of these EdgeNodes is
        recommended to be the same. EdgeCluster supports members of different
        deployment types.

        :type  edge_cluster: :class:`com.vmware.nsx.model_client.EdgeCluster`
        :param edge_cluster: (required)
        :rtype: :class:`com.vmware.nsx.model_client.EdgeCluster`
        :return: com.vmware.nsx.model.EdgeCluster
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
                            'edge_cluster': edge_cluster,
                            })

    def delete(self,
               edge_cluster_id,
               ):
        """
        Deletes the specified edge cluster.

        :type  edge_cluster_id: :class:`str`
        :param edge_cluster_id: (required)
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
                            'edge_cluster_id': edge_cluster_id,
                            })

    def get(self,
            edge_cluster_id,
            ):
        """
        Returns information about the specified edge cluster.

        :type  edge_cluster_id: :class:`str`
        :param edge_cluster_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.EdgeCluster`
        :return: com.vmware.nsx.model.EdgeCluster
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
                            'edge_cluster_id': edge_cluster_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about the configured edge clusters, which enable
        you to group together transport nodes of the type EdgeNode and apply
        fabric profiles to all members of the edge cluster. Each edge node can
        participate in only one edge cluster.

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
        :rtype: :class:`com.vmware.nsx.model_client.EdgeClusterListResult`
        :return: com.vmware.nsx.model.EdgeClusterListResult
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
                            })

    def replacetransportnode(self,
                             edge_cluster_id,
                             edge_cluster_member_transport_node,
                             ):
        """
        Replace the transport node in the specified member of the edge-cluster.
        This is a disruptive action. This will move all the
        LogicalRouterPorts(uplink and routerLink) host on the old
        transport_node to the new transport_node. The transportNode cannot be
        present in another member of any edgeClusters.

        :type  edge_cluster_id: :class:`str`
        :param edge_cluster_id: (required)
        :type  edge_cluster_member_transport_node: :class:`com.vmware.nsx.model_client.EdgeClusterMemberTransportNode`
        :param edge_cluster_member_transport_node: (required)
        :rtype: :class:`com.vmware.nsx.model_client.EdgeCluster`
        :return: com.vmware.nsx.model.EdgeCluster
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
        return self._invoke('replacetransportnode',
                            {
                            'edge_cluster_id': edge_cluster_id,
                            'edge_cluster_member_transport_node': edge_cluster_member_transport_node,
                            })

    def update(self,
               edge_cluster_id,
               edge_cluster,
               ):
        """
        Modifies the specified edge cluster. Modifiable parameters include the
        description, display_name, transport-node-id. If the optional
        fabric_profile_binding is included, resource_type and profile_id are
        required. User should do a GET on the edge-cluster and obtain the
        payload and retain the member_index of the existing members as
        returning in the GET output. For new member additions, the member_index
        cannot be defined by the user, user can read the system allocated index
        to the new member in the output of this API call or by doing a GET
        call. User cannot use this PUT api to replace the transport_node of an
        existing member because this is a disruption action, we have exposed a
        explicit API for doing so, refer to
        \"ReplaceEdgeClusterMemberTransportNode\" EdgeCluster only supports
        homogeneous members. The TransportNodes backed by EdgeNode are only
        allowed in cluster members. DeploymentType
        (VIRTUAL_MACHINE|PHYSICAL_MACHINE) of these EdgeNodes is recommended to
        be the same. EdgeCluster supports members of different deployment
        types.

        :type  edge_cluster_id: :class:`str`
        :param edge_cluster_id: (required)
        :type  edge_cluster: :class:`com.vmware.nsx.model_client.EdgeCluster`
        :param edge_cluster: (required)
        :rtype: :class:`com.vmware.nsx.model_client.EdgeCluster`
        :return: com.vmware.nsx.model.EdgeCluster
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
                            'edge_cluster_id': edge_cluster_id,
                            'edge_cluster': edge_cluster,
                            })
class ErrorResolver(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.error_resolver'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ErrorResolverStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            error_id,
            ):
        """
        Returns some metadata about the given error_id. This includes
        information of whether there is a resolver present for the given
        error_id and its associated user input data

        :type  error_id: :class:`str`
        :param error_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ErrorResolverInfo`
        :return: com.vmware.nsx.model.ErrorResolverInfo
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
                            'error_id': error_id,
                            })

    def list(self):
        """
        Returns a list of metadata for all the error resolvers registered.


        :rtype: :class:`com.vmware.nsx.model_client.ErrorResolverInfoList`
        :return: com.vmware.nsx.model.ErrorResolverInfoList
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

    def resolveerror(self,
                     error_resolver_metadata_list,
                     ):
        """
        Invokes the corresponding error resolver for the given error(s) present
        in the payload

        :type  error_resolver_metadata_list: :class:`com.vmware.nsx.model_client.ErrorResolverMetadataList`
        :param error_resolver_metadata_list: (required)
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
        return self._invoke('resolveerror',
                            {
                            'error_resolver_metadata_list': error_resolver_metadata_list,
                            })
class FailureDomains(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.failure_domains'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FailureDomainsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               failure_domain,
               ):
        """
        Creates a new failure domain.

        :type  failure_domain: :class:`com.vmware.nsx.model_client.FailureDomain`
        :param failure_domain: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FailureDomain`
        :return: com.vmware.nsx.model.FailureDomain
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
                            'failure_domain': failure_domain,
                            })

    def delete(self,
               failure_domain_id,
               ):
        """
        Deletes an existing failure domain. You can not delete system generated
        default failure domain.

        :type  failure_domain_id: :class:`str`
        :param failure_domain_id: (required)
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
                            'failure_domain_id': failure_domain_id,
                            })

    def get(self,
            failure_domain_id,
            ):
        """
        Returns information about a single failure domain.

        :type  failure_domain_id: :class:`str`
        :param failure_domain_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FailureDomain`
        :return: com.vmware.nsx.model.FailureDomain
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
                            'failure_domain_id': failure_domain_id,
                            })

    def list(self):
        """
        Returns information about configured failure domains.


        :rtype: :class:`com.vmware.nsx.model_client.FailureDomainListResult`
        :return: com.vmware.nsx.model.FailureDomainListResult
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
               failure_domain_id,
               failure_domain,
               ):
        """
        Updates an existing failure domain. Modifiable parameters are
        display_name, preferred_active_edge_services flag.

        :type  failure_domain_id: :class:`str`
        :param failure_domain_id: (required)
        :type  failure_domain: :class:`com.vmware.nsx.model_client.FailureDomain`
        :param failure_domain: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FailureDomain`
        :return: com.vmware.nsx.model.FailureDomain
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
                            'failure_domain_id': failure_domain_id,
                            'failure_domain': failure_domain,
                            })
class GlobalConfigs(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.global_configs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _GlobalConfigsStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            config_type,
            ):
        """
        Returns global configurations that belong to the config type

        :type  config_type: :class:`str`
        :param config_type: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.GlobalConfigs
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.GlobalConfigs`.
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
                            'config_type': config_type,
                            })

    def list(self):
        """
        Returns global configurations of a NSX domain grouped by the config
        types. These global configurations are valid across NSX domain for
        their respective types unless they are overridden by a more granular
        configurations.


        :rtype: :class:`com.vmware.nsx.model_client.GlobalConfigsListResult`
        :return: com.vmware.nsx.model.GlobalConfigsListResult
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

    def resyncconfig(self,
                     config_type,
                     global_configs,
                     ):
        """
        It is similar to update global configurations but this request would
        trigger update even if the configs are unmodified. However, the
        realization of the new configurations is config-type specific. Refer to
        config-type specific documentation for details about the configuration
        push state.

        :type  config_type: :class:`str`
        :param config_type: (required)
        :type  global_configs: :class:`vmware.vapi.struct.VapiStruct`
        :param global_configs: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.GlobalConfigs`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.GlobalConfigs
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.GlobalConfigs`.
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
        return self._invoke('resyncconfig',
                            {
                            'config_type': config_type,
                            'global_configs': global_configs,
                            })

    def update(self,
               config_type,
               global_configs,
               ):
        """
        

        :type  config_type: :class:`str`
        :param config_type: (required)
        :type  global_configs: :class:`vmware.vapi.struct.VapiStruct`
        :param global_configs: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.GlobalConfigs`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.GlobalConfigs
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.GlobalConfigs`.
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
                            'config_type': config_type,
                            'global_configs': global_configs,
                            })
class HostSwitchProfiles(VapiInterface):
    """
    
    """
    LIST_HOSTSWITCH_PROFILE_TYPE_UPLINKHOSTSWITCHPROFILE = "UplinkHostSwitchProfile"
    """
    Possible value for ``hostswitchProfileType`` of method
    :func:`HostSwitchProfiles.list`.

    """
    LIST_HOSTSWITCH_PROFILE_TYPE_LLDPHOSTSWITCHPROFILE = "LldpHostSwitchProfile"
    """
    Possible value for ``hostswitchProfileType`` of method
    :func:`HostSwitchProfiles.list`.

    """
    LIST_HOSTSWITCH_PROFILE_TYPE_NIOCPROFILE = "NiocProfile"
    """
    Possible value for ``hostswitchProfileType`` of method
    :func:`HostSwitchProfiles.list`.

    """
    LIST_HOSTSWITCH_PROFILE_TYPE_EXTRACONFIGHOSTSWITCHPROFILE = "ExtraConfigHostSwitchProfile"
    """
    Possible value for ``hostswitchProfileType`` of method
    :func:`HostSwitchProfiles.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.host_switch_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _HostSwitchProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               base_host_switch_profile,
               ):
        """
        Creates a hostswitch profile. The resource_type is required. For uplink
        profiles, the teaming and policy parameters are required. By default,
        the mtu is 1600 and the transport_vlan is 0. The supported MTU range is
        1280 through (uplink_mtu_threshold). (uplink_mtu_threshold) is 9000 by
        default. Range can be extended by modifying (uplink_mtu_threshold) in
        SwitchingGlobalConfig to the required upper threshold.

        :type  base_host_switch_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param base_host_switch_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseHostSwitchProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.BaseHostSwitchProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseHostSwitchProfile`.
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
                            'base_host_switch_profile': base_host_switch_profile,
                            })

    def delete(self,
               host_switch_profile_id,
               ):
        """
        Deletes a specified hostswitch profile.

        :type  host_switch_profile_id: :class:`str`
        :param host_switch_profile_id: (required)
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
                            'host_switch_profile_id': host_switch_profile_id,
                            })

    def get(self,
            host_switch_profile_id,
            ):
        """
        Returns information about a specified hostswitch profile.

        :type  host_switch_profile_id: :class:`str`
        :param host_switch_profile_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.BaseHostSwitchProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseHostSwitchProfile`.
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
                            'host_switch_profile_id': host_switch_profile_id,
                            })

    def list(self,
             cursor=None,
             hostswitch_profile_type=None,
             include_system_owned=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             uplink_teaming_policy_name=None,
             ):
        """
        Returns information about the configured hostswitch profiles.
        Hostswitch profiles define networking policies for hostswitches
        (sometimes referred to as bridges in OVS). Currently, only uplink
        teaming is supported. Uplink teaming allows NSX to load balance traffic
        across different physical NICs (PNICs) on the hypervisor hosts.
        Multiple teaming policies are supported, including LACP active, LACP
        passive, load balancing based on source ID, and failover order.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  hostswitch_profile_type: :class:`str` or ``None``
        :param hostswitch_profile_type: Supported HostSwitch profiles. (optional)
        :type  include_system_owned: :class:`bool` or ``None``
        :param include_system_owned: Whether the list result contains system resources (optional,
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
        :type  uplink_teaming_policy_name: :class:`str` or ``None``
        :param uplink_teaming_policy_name: The host switch profile's uplink teaming policy name (optional)
        :rtype: :class:`com.vmware.nsx.model_client.HostSwitchProfilesListResult`
        :return: com.vmware.nsx.model.HostSwitchProfilesListResult
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
                            'hostswitch_profile_type': hostswitch_profile_type,
                            'include_system_owned': include_system_owned,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'uplink_teaming_policy_name': uplink_teaming_policy_name,
                            })

    def update(self,
               host_switch_profile_id,
               base_host_switch_profile,
               ):
        """
        Modifies a specified hostswitch profile. The body of the PUT request
        must include the resource_type. For uplink profiles, the put request
        must also include teaming parameters. Modifiable attributes include
        display_name, mtu, and transport_vlan. For uplink teaming policies,
        uplink_name and policy are also modifiable.

        :type  host_switch_profile_id: :class:`str`
        :param host_switch_profile_id: (required)
        :type  base_host_switch_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param base_host_switch_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseHostSwitchProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.BaseHostSwitchProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseHostSwitchProfile`.
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
                            'host_switch_profile_id': host_switch_profile_id,
                            'base_host_switch_profile': base_host_switch_profile,
                            })
class IpSets(VapiInterface):
    """
    
    """
    CREATE_0_ACTION_ADD_IP = "add_ip"
    """
    Possible value for ``action`` of method :func:`IpSets.create_0`.

    """
    CREATE_0_ACTION_REMOVE_IP = "remove_ip"
    """
    Possible value for ``action`` of method :func:`IpSets.create_0`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ip_sets'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _IpSetsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               ip_set,
               ):
        """
        Creates a new IPSet that can group either IPv4 or IPv6 individual ip
        addresses, ranges or subnets.

        :type  ip_set: :class:`com.vmware.nsx.model_client.IPSet`
        :param ip_set: (required)
        :rtype: :class:`com.vmware.nsx.model_client.IPSet`
        :return: com.vmware.nsx.model.IPSet
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
                            'ip_set': ip_set,
                            })

    def create_0(self,
                 ip_set_id,
                 ip_address_element,
                 action,
                 ):
        """
        Add/Remove an individual IP address to an IPSet

        :type  ip_set_id: :class:`str`
        :param ip_set_id: IP Set Id (required)
        :type  ip_address_element: :class:`com.vmware.nsx.model_client.IPAddressElement`
        :param ip_address_element: (required)
        :type  action: :class:`str`
        :param action: Specifies addition or removal action (required)
        :rtype: :class:`com.vmware.nsx.model_client.IPAddressElement`
        :return: com.vmware.nsx.model.IPAddressElement
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
        return self._invoke('create_0',
                            {
                            'ip_set_id': ip_set_id,
                            'ip_address_element': ip_address_element,
                            'action': action,
                            })

    def delete(self,
               ip_set_id,
               force=None,
               ):
        """
        Deletes the specified IPSet. By default, if the IPSet is added to an
        NSGroup, it won't be deleted. In such situations, pass \"force=true\"
        as query param to force delete the IPSet.

        :type  ip_set_id: :class:`str`
        :param ip_set_id: IPSet Id (required)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
            (optional, default to false)
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
        return self._invoke('delete',
                            {
                            'ip_set_id': ip_set_id,
                            'force': force,
                            })

    def get(self,
            ip_set_id,
            ):
        """
        Returns information about the specified IPSet

        :type  ip_set_id: :class:`str`
        :param ip_set_id: IPSet Id (required)
        :rtype: :class:`com.vmware.nsx.model_client.IPSet`
        :return: com.vmware.nsx.model.IPSet
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
                            'ip_set_id': ip_set_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns paginated list of IPSets

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
        :rtype: :class:`com.vmware.nsx.model_client.IPSetListResult`
        :return: com.vmware.nsx.model.IPSetListResult
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
                            })

    def update(self,
               ip_set_id,
               ip_set,
               ):
        """
        Updates the specified IPSet. Modifiable parameters include description,
        display_name and ip_addresses.

        :type  ip_set_id: :class:`str`
        :param ip_set_id: IPSet Id (required)
        :type  ip_set: :class:`com.vmware.nsx.model_client.IPSet`
        :param ip_set: (required)
        :rtype: :class:`com.vmware.nsx.model_client.IPSet`
        :return: com.vmware.nsx.model.IPSet
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
                            'ip_set_id': ip_set_id,
                            'ip_set': ip_set,
                            })
class IpfixCollectorProfiles(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ipfix_collector_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _IpfixCollectorProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               ipfix_collector_upm_profile,
               ):
        """
        Create a new IPFIX collector profile with essential properties.

        :type  ipfix_collector_upm_profile: :class:`com.vmware.nsx.model_client.IpfixCollectorUpmProfile`
        :param ipfix_collector_upm_profile: (required)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixCollectorUpmProfile`
        :return: com.vmware.nsx.model.IpfixCollectorUpmProfile
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
                            'ipfix_collector_upm_profile': ipfix_collector_upm_profile,
                            })

    def delete(self,
               ipfix_collector_profile_id,
               ):
        """
        Delete an existing IPFIX collector profile by ID.

        :type  ipfix_collector_profile_id: :class:`str`
        :param ipfix_collector_profile_id: (required)
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
                            'ipfix_collector_profile_id': ipfix_collector_profile_id,
                            })

    def get(self,
            ipfix_collector_profile_id,
            ):
        """
        Get an existing IPFIX collector profile by profile ID.

        :type  ipfix_collector_profile_id: :class:`str`
        :param ipfix_collector_profile_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixCollectorUpmProfile`
        :return: com.vmware.nsx.model.IpfixCollectorUpmProfile
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
                            'ipfix_collector_profile_id': ipfix_collector_profile_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             profile_types=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Query IPFIX collector profiles with list parameters. List result can be
        filtered by profile type defined by IpfixCollectorUpmProfileType.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  profile_types: :class:`str` or ``None``
        :param profile_types: IPFIX Collector Profile Type List (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixCollectorUpmProfileListResult`
        :return: com.vmware.nsx.model.IpfixCollectorUpmProfileListResult
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
                            'profile_types': profile_types,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               ipfix_collector_profile_id,
               ipfix_collector_upm_profile,
               ):
        """
        Update an existing IPFIX collector profile with profile ID and modified
        properties.

        :type  ipfix_collector_profile_id: :class:`str`
        :param ipfix_collector_profile_id: (required)
        :type  ipfix_collector_upm_profile: :class:`com.vmware.nsx.model_client.IpfixCollectorUpmProfile`
        :param ipfix_collector_upm_profile: (required)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixCollectorUpmProfile`
        :return: com.vmware.nsx.model.IpfixCollectorUpmProfile
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
                            'ipfix_collector_profile_id': ipfix_collector_profile_id,
                            'ipfix_collector_upm_profile': ipfix_collector_upm_profile,
                            })
class IpfixObsPoints(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ipfix_obs_points'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _IpfixObsPointsStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self):
        """
        Deprecated - Please use /ipfix-profiles for switch IPFIX profile and
        /ipfix-collector-profiles for IPFIX collector profile.


        :rtype: :class:`com.vmware.nsx.model_client.IpfixObsPointsListResult`
        :return: com.vmware.nsx.model.IpfixObsPointsListResult
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
class IpfixProfiles(VapiInterface):
    """
    
    """
    LIST_APPLIED_TO_ENTITY_TYPE_LOGICALPORT = "LogicalPort"
    """
    Possible value for ``appliedToEntityType`` of method
    :func:`IpfixProfiles.list`.

    """
    LIST_APPLIED_TO_ENTITY_TYPE_LOGICALSWITCH = "LogicalSwitch"
    """
    Possible value for ``appliedToEntityType`` of method
    :func:`IpfixProfiles.list`.

    """
    LIST_APPLIED_TO_ENTITY_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``appliedToEntityType`` of method
    :func:`IpfixProfiles.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ipfix_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _IpfixProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               ipfix_upm_profile,
               ):
        """
        Create a new IPFIX profile with essential properties.

        :type  ipfix_upm_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param ipfix_upm_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixUpmProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.IpfixUpmProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixUpmProfile`.
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
                            'ipfix_upm_profile': ipfix_upm_profile,
                            })

    def delete(self,
               ipfix_profile_id,
               ):
        """
        Delete an existing IPFIX profile by ID.

        :type  ipfix_profile_id: :class:`str`
        :param ipfix_profile_id: (required)
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
                            'ipfix_profile_id': ipfix_profile_id,
                            })

    def get(self,
            ipfix_profile_id,
            ):
        """
        Get an existing IPFIX profile by profile ID.

        :type  ipfix_profile_id: :class:`str`
        :param ipfix_profile_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.IpfixUpmProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixUpmProfile`.
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
                            'ipfix_profile_id': ipfix_profile_id,
                            })

    def list(self,
             applied_to_entity_id=None,
             applied_to_entity_type=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             profile_types=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Query IPFIX profiles with list parameters. List result can be filtered
        by profile type defined by IpfixUpmProfileType.

        :type  applied_to_entity_id: :class:`str` or ``None``
        :param applied_to_entity_id: ID of Entity Applied with Profile (optional)
        :type  applied_to_entity_type: :class:`str` or ``None``
        :param applied_to_entity_type: Supported Entity Types (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  profile_types: :class:`str` or ``None``
        :param profile_types: IPFIX Profile Type List (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.IpfixUpmProfileListResult`
        :return: com.vmware.nsx.model.IpfixUpmProfileListResult
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
                            'applied_to_entity_id': applied_to_entity_id,
                            'applied_to_entity_type': applied_to_entity_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'profile_types': profile_types,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               ipfix_profile_id,
               ipfix_upm_profile,
               ):
        """
        Update an existing IPFIX profile with profile ID and modified
        properties.

        :type  ipfix_profile_id: :class:`str`
        :param ipfix_profile_id: (required)
        :type  ipfix_upm_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param ipfix_upm_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixUpmProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.IpfixUpmProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.IpfixUpmProfile`.
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
                            'ipfix_profile_id': ipfix_profile_id,
                            'ipfix_upm_profile': ipfix_upm_profile,
                            })
class Licenses(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.licenses'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LicensesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               license,
               ):
        """
        This will add a license key to the system. The API supports adding only
        one license key for each license edition type - Standard, Advanced or
        Enterprise. If a new license key is tried to add for an edition for
        which the license key already exists, then this API will return an
        error.

        :type  license: :class:`com.vmware.nsx.model_client.License`
        :param license: (required)
        :rtype: :class:`com.vmware.nsx.model_client.License`
        :return: com.vmware.nsx.model.License
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
                            'license': license,
                            })

    def delete(self,
               license_key,
               ):
        """
        Deprecated. Use POST /licenses?action=delete API instead.

        :type  license_key: :class:`str`
        :param license_key: (required)
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
                            'license_key': license_key,
                            })

    def delete_0(self,
                 license,
                 ):
        """
        This will delete the license key identified in the request body by
        \"license_key\" and its properties from the system. Attempting to
        delete the last license key will result in an error.

        :type  license: :class:`com.vmware.nsx.model_client.License`
        :param license: (required)
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
        return self._invoke('delete_0',
                            {
                            'license': license,
                            })

    def get(self):
        """
        Deprecated. Use the GET /licenses API instead.


        :rtype: :class:`com.vmware.nsx.model_client.License`
        :return: com.vmware.nsx.model.License
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

    def getlicensebykey(self,
                        license_key,
                        ):
        """
        Deprecated. Use GET /licenses API instead.

        :type  license_key: :class:`str`
        :param license_key: (required)
        :rtype: :class:`com.vmware.nsx.model_client.License`
        :return: com.vmware.nsx.model.License
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
        return self._invoke('getlicensebykey',
                            {
                            'license_key': license_key,
                            })

    def list(self):
        """
        Returns all licenses.


        :rtype: :class:`com.vmware.nsx.model_client.LicensesListResult`
        :return: com.vmware.nsx.model.LicensesListResult
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
               license,
               ):
        """
        Deprecated. Use the POST /licenses API instead

        :type  license: :class:`com.vmware.nsx.model_client.License`
        :param license: (required)
        :rtype: :class:`com.vmware.nsx.model_client.License`
        :return: com.vmware.nsx.model.License
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
                            'license': license,
                            })
class LogicalPorts(VapiInterface):
    """
    
    """
    LIST_ATTACHMENT_TYPE_VIF = "VIF"
    """
    Possible value for ``attachmentType`` of method :func:`LogicalPorts.list`.

    """
    LIST_ATTACHMENT_TYPE_LOGICALROUTER = "LOGICALROUTER"
    """
    Possible value for ``attachmentType`` of method :func:`LogicalPorts.list`.

    """
    LIST_ATTACHMENT_TYPE_BRIDGEENDPOINT = "BRIDGEENDPOINT"
    """
    Possible value for ``attachmentType`` of method :func:`LogicalPorts.list`.

    """
    LIST_ATTACHMENT_TYPE_DHCP_SERVICE = "DHCP_SERVICE"
    """
    Possible value for ``attachmentType`` of method :func:`LogicalPorts.list`.

    """
    LIST_ATTACHMENT_TYPE_METADATA_PROXY = "METADATA_PROXY"
    """
    Possible value for ``attachmentType`` of method :func:`LogicalPorts.list`.

    """
    LIST_ATTACHMENT_TYPE_L2VPN_SESSION = "L2VPN_SESSION"
    """
    Possible value for ``attachmentType`` of method :func:`LogicalPorts.list`.

    """
    LIST_ATTACHMENT_TYPE_NONE = "NONE"
    """
    Possible value for ``attachmentType`` of method :func:`LogicalPorts.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.logical_ports'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LogicalPortsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               logical_port,
               ):
        """
        Creates a new logical switch port. The required parameters are the
        associated logical_switch_id and admin_state (UP or DOWN). Optional
        parameters are the attachment and switching_profile_ids. If you don't
        specify switching_profile_ids, default switching profiles are assigned
        to the port. If you don't specify an attachment, the switch port
        remains empty. To configure an attachment, you must specify an id, and
        optionally you can specify an attachment_type (VIF or LOGICALROUTER).
        The attachment_type is VIF by default.

        :type  logical_port: :class:`com.vmware.nsx.model_client.LogicalPort`
        :param logical_port: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPort`
        :return: com.vmware.nsx.model.LogicalPort
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
                            'logical_port': logical_port,
                            })

    def delete(self,
               lport_id,
               detach=None,
               ):
        """
        Deletes the specified logical switch port. By default, if logical port
        has attachments, or it is added to any NSGroup, the deletion will be
        failed. Option detach could be used for deleting logical port forcibly.

        :type  lport_id: :class:`str`
        :param lport_id: (required)
        :type  detach: :class:`bool` or ``None``
        :param detach: force delete even if attached or referenced by a group (optional,
            default to false)
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
                            'lport_id': lport_id,
                            'detach': detach,
                            })

    def get(self,
            lport_id,
            ):
        """
        Returns information about a specified logical port.

        :type  lport_id: :class:`str`
        :param lport_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPort`
        :return: com.vmware.nsx.model.LogicalPort
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
                            'lport_id': lport_id,
                            })

    def list(self,
             attachment_id=None,
             attachment_type=None,
             bridge_cluster_id=None,
             container_ports_only=None,
             cursor=None,
             diagnostic=None,
             included_fields=None,
             logical_switch_id=None,
             page_size=None,
             parent_vif_id=None,
             sort_ascending=None,
             sort_by=None,
             switching_profile_id=None,
             transport_node_id=None,
             transport_zone_id=None,
             ):
        """
        Returns information about all configured logical switch ports. Logical
        switch ports connect to VM virtual network interface cards (NICs). Each
        logical port is associated with one logical switch.

        :type  attachment_id: :class:`str` or ``None``
        :param attachment_id: Logical Port attachment Id (optional)
        :type  attachment_type: :class:`str` or ``None``
        :param attachment_type: Type of attachment for logical port; for query only. (optional)
        :type  bridge_cluster_id: :class:`str` or ``None``
        :param bridge_cluster_id: Bridge Cluster identifier (optional)
        :type  container_ports_only: :class:`bool` or ``None``
        :param container_ports_only: Only container VIF logical ports will be returned if true
            (optional, default to false)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  diagnostic: :class:`bool` or ``None``
        :param diagnostic: Flag to enable showing of transit logical port. (optional, default
            to false)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  logical_switch_id: :class:`str` or ``None``
        :param logical_switch_id: Logical Switch identifier (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  parent_vif_id: :class:`str` or ``None``
        :param parent_vif_id: ID of the VIF of type PARENT (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  switching_profile_id: :class:`str` or ``None``
        :param switching_profile_id: Network Profile identifier (optional)
        :type  transport_node_id: :class:`str` or ``None``
        :param transport_node_id: Transport node identifier (optional)
        :type  transport_zone_id: :class:`str` or ``None``
        :param transport_zone_id: Transport zone identifier (optional)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPortListResult`
        :return: com.vmware.nsx.model.LogicalPortListResult
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
                            'attachment_id': attachment_id,
                            'attachment_type': attachment_type,
                            'bridge_cluster_id': bridge_cluster_id,
                            'container_ports_only': container_ports_only,
                            'cursor': cursor,
                            'diagnostic': diagnostic,
                            'included_fields': included_fields,
                            'logical_switch_id': logical_switch_id,
                            'page_size': page_size,
                            'parent_vif_id': parent_vif_id,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'switching_profile_id': switching_profile_id,
                            'transport_node_id': transport_node_id,
                            'transport_zone_id': transport_zone_id,
                            })

    def update(self,
               lport_id,
               logical_port,
               ):
        """
        Modifies an existing logical switch port. Parameters that can be
        modified include attachment_type (LOGICALROUTER, VIF), admin_state (UP
        or DOWN), attachment id and switching_profile_ids. You cannot modify
        the logical_switch_id. In other words, you cannot move an existing port
        from one switch to another switch.

        :type  lport_id: :class:`str`
        :param lport_id: (required)
        :type  logical_port: :class:`com.vmware.nsx.model_client.LogicalPort`
        :param logical_port: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPort`
        :return: com.vmware.nsx.model.LogicalPort
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
                            'lport_id': lport_id,
                            'logical_port': logical_port,
                            })
class LogicalRouterPorts(VapiInterface):
    """
    
    """
    LIST_RESOURCE_TYPE_LOGICALROUTERUPLINKPORT = "LogicalRouterUpLinkPort"
    """
    Possible value for ``resourceType`` of method :func:`LogicalRouterPorts.list`.

    """
    LIST_RESOURCE_TYPE_LOGICALROUTERDOWNLINKPORT = "LogicalRouterDownLinkPort"
    """
    Possible value for ``resourceType`` of method :func:`LogicalRouterPorts.list`.

    """
    LIST_RESOURCE_TYPE_LOGICALROUTERLINKPORTONTIER0 = "LogicalRouterLinkPortOnTIER0"
    """
    Possible value for ``resourceType`` of method :func:`LogicalRouterPorts.list`.

    """
    LIST_RESOURCE_TYPE_LOGICALROUTERLINKPORTONTIER1 = "LogicalRouterLinkPortOnTIER1"
    """
    Possible value for ``resourceType`` of method :func:`LogicalRouterPorts.list`.

    """
    LIST_RESOURCE_TYPE_LOGICALROUTERLOOPBACKPORT = "LogicalRouterLoopbackPort"
    """
    Possible value for ``resourceType`` of method :func:`LogicalRouterPorts.list`.

    """
    LIST_RESOURCE_TYPE_LOGICALROUTERIPTUNNELPORT = "LogicalRouterIPTunnelPort"
    """
    Possible value for ``resourceType`` of method :func:`LogicalRouterPorts.list`.

    """
    LIST_RESOURCE_TYPE_LOGICALROUTERCENTRALIZEDSERVICEPORT = "LogicalRouterCentralizedServicePort"
    """
    Possible value for ``resourceType`` of method :func:`LogicalRouterPorts.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.logical_router_ports'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LogicalRouterPortsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               logical_router_port,
               ):
        """
        Creates a logical router port. The required parameters include
        resource_type (LogicalRouterUpLinkPort, LogicalRouterDownLinkPort,
        LogicalRouterLinkPort, LogicalRouterLoopbackPort,
        LogicalRouterCentralizedServicePort); and logical_router_id (the router
        to which each logical router port is assigned). The service_bindings
        parameter is optional.

        :type  logical_router_port: :class:`vmware.vapi.struct.VapiStruct`
        :param logical_router_port: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.LogicalRouterPort`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.LogicalRouterPort
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.LogicalRouterPort`.
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
                            'logical_router_port': logical_router_port,
                            })

    def delete(self,
               logical_router_port_id,
               cascade_delete_linked_ports=None,
               force=None,
               ):
        """
        Deletes the specified logical router port. You must delete logical
        router ports before you can delete the associated logical router. To
        Delete Tier0 router link port you must have to delete attached tier1
        router link port, otherwise pass \"force=true\" as query param to force
        delete the Tier0 router link port.

        :type  logical_router_port_id: :class:`str`
        :param logical_router_port_id: (required)
        :type  cascade_delete_linked_ports: :class:`bool` or ``None``
        :param cascade_delete_linked_ports: Flag to specify whether to delete related logical switch ports
            (optional, default to false)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
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
                            'logical_router_port_id': logical_router_port_id,
                            'cascade_delete_linked_ports': cascade_delete_linked_ports,
                            'force': force,
                            })

    def get(self,
            logical_router_port_id,
            ):
        """
        Returns information about the specified logical router port.

        :type  logical_router_port_id: :class:`str`
        :param logical_router_port_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.LogicalRouterPort
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.LogicalRouterPort`.
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
                            'logical_router_port_id': logical_router_port_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             logical_router_id=None,
             logical_switch_id=None,
             page_size=None,
             resource_type=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all logical router ports. Information
        includes the resource_type (LogicalRouterUpLinkPort,
        LogicalRouterDownLinkPort, LogicalRouterLinkPort,
        LogicalRouterLoopbackPort, LogicalRouterCentralizedServicePort);
        logical_router_id (the router to which each logical router port is
        assigned); and any service_bindings (such as DHCP relay service). The
        GET request can include a query parameter (logical_router_id or
        logical_switch_id).

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  logical_router_id: :class:`str` or ``None``
        :param logical_router_id: Logical Router identifier (optional)
        :type  logical_switch_id: :class:`str` or ``None``
        :param logical_switch_id: Logical Switch identifier (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: Resource types of logical router port (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalRouterPortListResult`
        :return: com.vmware.nsx.model.LogicalRouterPortListResult
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
                            'logical_router_id': logical_router_id,
                            'logical_switch_id': logical_switch_id,
                            'page_size': page_size,
                            'resource_type': resource_type,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               logical_router_port_id,
               logical_router_port,
               ):
        """
        Modifies the specified logical router port. Required parameters include
        the resource_type and logical_router_id. Modifiable parameters include
        the resource_type (LogicalRouterUpLinkPort, LogicalRouterDownLinkPort,
        LogicalRouterLinkPort, LogicalRouterLoopbackPort,
        LogicalRouterCentralizedServicePort), logical_router_id (to reassign
        the port to a different router), and service_bindings.

        :type  logical_router_port_id: :class:`str`
        :param logical_router_port_id: (required)
        :type  logical_router_port: :class:`vmware.vapi.struct.VapiStruct`
        :param logical_router_port: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.LogicalRouterPort`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.LogicalRouterPort
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.LogicalRouterPort`.
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
                            'logical_router_port_id': logical_router_port_id,
                            'logical_router_port': logical_router_port,
                            })
class LogicalRouters(VapiInterface):
    """
    
    """
    LIST_ROUTER_TYPE_TIER0 = "TIER0"
    """
    Possible value for ``routerType`` of method :func:`LogicalRouters.list`.

    """
    LIST_ROUTER_TYPE_TIER1 = "TIER1"
    """
    Possible value for ``routerType`` of method :func:`LogicalRouters.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.logical_routers'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LogicalRoutersStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               logical_router,
               ):
        """
        Creates a logical router. The required parameters are router_type
        (TIER0 or TIER1) and edge_cluster_id (TIER0 only). Optional parameters
        include internal and external transit network addresses.

        :type  logical_router: :class:`com.vmware.nsx.model_client.LogicalRouter`
        :param logical_router: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalRouter`
        :return: com.vmware.nsx.model.LogicalRouter
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
                            'logical_router': logical_router,
                            })

    def delete(self,
               logical_router_id,
               cascade_delete_linked_ports=None,
               force=None,
               ):
        """
        Deletes the specified logical router. You must delete associated
        logical router ports before you can delete a logical router. Otherwise
        use force delete which will delete all related ports and other entities
        associated with that LR. To force delete logical router pass force=true
        in query param.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  cascade_delete_linked_ports: :class:`bool` or ``None``
        :param cascade_delete_linked_ports: Flag to specify whether to delete related logical switch ports
            (optional, default to false)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
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
                            'logical_router_id': logical_router_id,
                            'cascade_delete_linked_ports': cascade_delete_linked_ports,
                            'force': force,
                            })

    def get(self,
            logical_router_id,
            ):
        """
        Returns information about the specified logical router.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalRouter`
        :return: com.vmware.nsx.model.LogicalRouter
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
                            'logical_router_id': logical_router_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             router_type=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all logical routers, including the UUID,
        internal and external transit network addresses, and the router type
        (TIER0 or TIER1). You can get information for only TIER0 routers or
        only the TIER1 routers by including the router_type query parameter.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  router_type: :class:`str` or ``None``
        :param router_type: Type of Logical Router (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalRouterListResult`
        :return: com.vmware.nsx.model.LogicalRouterListResult
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
                            'router_type': router_type,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def reallocate(self,
                   logical_router_id,
                   service_router_allocation_config,
                   ):
        """
        API to re allocate edge node placement for TIER1 logical router. You
        can re-allocate service routers of TIER1 in same edge cluster or
        different edge cluster. You can also place edge nodes manually and
        provide maximum two indices for HA mode ACTIVE_STANDBY. To re-allocate
        on new edge cluster you must have existing edge cluster for TIER1
        logical router. This will be disruptive operation and all existing
        statistics of logical router will be remove.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  service_router_allocation_config: :class:`com.vmware.nsx.model_client.ServiceRouterAllocationConfig`
        :param service_router_allocation_config: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalRouter`
        :return: com.vmware.nsx.model.LogicalRouter
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
        return self._invoke('reallocate',
                            {
                            'logical_router_id': logical_router_id,
                            'service_router_allocation_config': service_router_allocation_config,
                            })

    def reprocess(self,
                  logical_router_id,
                  ):
        """
        Reprocess logical router configuration and configuration of related
        entities like logical router ports, static routing, etc. Any missing
        Updates are published to controller.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
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
        return self._invoke('reprocess',
                            {
                            'logical_router_id': logical_router_id,
                            })

    def update(self,
               logical_router_id,
               logical_router,
               ):
        """
        Modifies the specified logical router. Modifiable attributes include
        the internal_transit_network, external_transit_networks, and
        edge_cluster_id (for TIER0 routers).

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  logical_router: :class:`com.vmware.nsx.model_client.LogicalRouter`
        :param logical_router: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalRouter`
        :return: com.vmware.nsx.model.LogicalRouter
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
                            'logical_router_id': logical_router_id,
                            'logical_router': logical_router,
                            })
class LogicalSwitches(VapiInterface):
    """
    
    """
    LIST_TRANSPORT_TYPE_OVERLAY = "OVERLAY"
    """
    Possible value for ``transportType`` of method :func:`LogicalSwitches.list`.

    """
    LIST_TRANSPORT_TYPE_VLAN = "VLAN"
    """
    Possible value for ``transportType`` of method :func:`LogicalSwitches.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.logical_switches'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LogicalSwitchesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               logical_switch,
               ):
        """
        Creates a new logical switch. The request must include the
        transport_zone_id, display_name, and admin_state (UP or DOWN). The
        replication_mode (MTEP or SOURCE) is required for overlay logical
        switches, but not for VLAN-based logical switches. A vlan needs to be
        provided for VLAN-based logical switches

        :type  logical_switch: :class:`com.vmware.nsx.model_client.LogicalSwitch`
        :param logical_switch: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalSwitch`
        :return: com.vmware.nsx.model.LogicalSwitch
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
                            'logical_switch': logical_switch,
                            })

    def delete(self,
               lswitch_id,
               cascade=None,
               detach=None,
               ):
        """
        Removes a logical switch from the associated overlay or VLAN transport
        zone. By default, a logical switch cannot be deleted if there are
        logical ports on the switch, or it is added to a NSGroup. Cascade
        option can be used to delete all ports and the logical switch. Detach
        option can be used to delete the logical switch forcibly.

        :type  lswitch_id: :class:`str`
        :param lswitch_id: (required)
        :type  cascade: :class:`bool` or ``None``
        :param cascade: Delete a Logical Switch and all the logical ports in it, if none of
            the logical ports have any attachment. (optional, default to false)
        :type  detach: :class:`bool` or ``None``
        :param detach: Force delete a logical switch (optional, default to false)
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
                            'lswitch_id': lswitch_id,
                            'cascade': cascade,
                            'detach': detach,
                            })

    def get(self,
            lswitch_id,
            ):
        """
        Returns information about the specified logical switch Id.

        :type  lswitch_id: :class:`str`
        :param lswitch_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalSwitch`
        :return: com.vmware.nsx.model.LogicalSwitch
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
                            'lswitch_id': lswitch_id,
                            })

    def list(self,
             cursor=None,
             diagnostic=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             switching_profile_id=None,
             transport_type=None,
             transport_zone_id=None,
             uplink_teaming_policy_name=None,
             vlan=None,
             vni=None,
             ):
        """
        Returns information about all configured logical switches.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  diagnostic: :class:`bool` or ``None``
        :param diagnostic: Flag to enable showing of transit logical switch. (optional,
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
        :type  switching_profile_id: :class:`str` or ``None``
        :param switching_profile_id: Switching Profile identifier (optional)
        :type  transport_type: :class:`str` or ``None``
        :param transport_type: Mode of transport supported in the transport zone for this logical
            switch (optional)
        :type  transport_zone_id: :class:`str` or ``None``
        :param transport_zone_id: Transport zone identifier (optional)
        :type  uplink_teaming_policy_name: :class:`str` or ``None``
        :param uplink_teaming_policy_name: The logical switch's uplink teaming policy name (optional)
        :type  vlan: :class:`long` or ``None``
        :param vlan: Virtual Local Area Network Identifier (optional)
        :type  vni: :class:`long` or ``None``
        :param vni: VNI of the OVERLAY LogicalSwitch(es) to return. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalSwitchListResult`
        :return: com.vmware.nsx.model.LogicalSwitchListResult
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
                            'diagnostic': diagnostic,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'switching_profile_id': switching_profile_id,
                            'transport_type': transport_type,
                            'transport_zone_id': transport_zone_id,
                            'uplink_teaming_policy_name': uplink_teaming_policy_name,
                            'vlan': vlan,
                            'vni': vni,
                            })

    def update(self,
               lswitch_id,
               logical_switch,
               ):
        """
        Modifies attributes of an existing logical switch. Modifiable
        attributes include admin_state, replication_mode, switching_profile_ids
        and VLAN spec. You cannot modify the original transport_zone_id.

        :type  lswitch_id: :class:`str`
        :param lswitch_id: (required)
        :type  logical_switch: :class:`com.vmware.nsx.model_client.LogicalSwitch`
        :param logical_switch: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalSwitch`
        :return: com.vmware.nsx.model.LogicalSwitch
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
                            'lswitch_id': lswitch_id,
                            'logical_switch': logical_switch,
                            })
class MacSets(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.mac_sets'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MacSetsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               m_ac_set,
               ):
        """
        Creates a new MACSet that can group individual MAC addresses.

        :type  m_ac_set: :class:`com.vmware.nsx.model_client.MACSet`
        :param m_ac_set: (required)
        :rtype: :class:`com.vmware.nsx.model_client.MACSet`
        :return: com.vmware.nsx.model.MACSet
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
                            'm_ac_set': m_ac_set,
                            })

    def delete(self,
               mac_set_id,
               force=None,
               ):
        """
        Deletes the specified MACSet. By default, if the MACSet is added to an
        NSGroup, it won't be deleted. In such situations, pass \"force=true\"
        as query param to force delete the MACSet.

        :type  mac_set_id: :class:`str`
        :param mac_set_id: MACSet Id (required)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
            (optional, default to false)
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
        return self._invoke('delete',
                            {
                            'mac_set_id': mac_set_id,
                            'force': force,
                            })

    def get(self,
            mac_set_id,
            ):
        """
        Returns information about the specified MACSet

        :type  mac_set_id: :class:`str`
        :param mac_set_id: MACSet Id (required)
        :rtype: :class:`com.vmware.nsx.model_client.MACSet`
        :return: com.vmware.nsx.model.MACSet
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
                            'mac_set_id': mac_set_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns paginated list of MACSets

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
        :rtype: :class:`com.vmware.nsx.model_client.MACSetListResult`
        :return: com.vmware.nsx.model.MACSetListResult
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
                            })

    def update(self,
               mac_set_id,
               m_ac_set,
               ):
        """
        Updates the specified MACSet. Modifiable parameters include the
        description, display_name and mac_addresses.

        :type  mac_set_id: :class:`str`
        :param mac_set_id: MACSet Id (required)
        :type  m_ac_set: :class:`com.vmware.nsx.model_client.MACSet`
        :param m_ac_set: (required)
        :rtype: :class:`com.vmware.nsx.model_client.MACSet`
        :return: com.vmware.nsx.model.MACSet
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
                            'mac_set_id': mac_set_id,
                            'm_ac_set': m_ac_set,
                            })
class ManualHealthChecks(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.manual_health_checks'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ManualHealthChecksStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               manual_health_check,
               ):
        """
        Create a new manual health check request with essential properties.
        It's disallowed to create new one until the count of in-progress manual
        health check is less than 50. A manual health check will be deleted
        automatically after finished for 24 hours.

        :type  manual_health_check: :class:`com.vmware.nsx.model_client.ManualHealthCheck`
        :param manual_health_check: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ManualHealthCheck`
        :return: com.vmware.nsx.model.ManualHealthCheck
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
                            'manual_health_check': manual_health_check,
                            })

    def delete(self,
               manual_health_check_id,
               ):
        """
        Delete an existing manual health check by ID.

        :type  manual_health_check_id: :class:`str`
        :param manual_health_check_id: (required)
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
                            'manual_health_check_id': manual_health_check_id,
                            })

    def get(self,
            manual_health_check_id,
            ):
        """
        Get an existing manual health check by health check ID.

        :type  manual_health_check_id: :class:`str`
        :param manual_health_check_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ManualHealthCheck`
        :return: com.vmware.nsx.model.ManualHealthCheck
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
                            'manual_health_check_id': manual_health_check_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Query manual health checks with list parameters.

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
        :rtype: :class:`com.vmware.nsx.model_client.ManualHealthCheckListResult`
        :return: com.vmware.nsx.model.ManualHealthCheckListResult
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
                            })
class MdProxies(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.md_proxies'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MdProxiesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               metadata_proxy,
               ):
        """
        Create a metadata proxy

        :type  metadata_proxy: :class:`com.vmware.nsx.model_client.MetadataProxy`
        :param metadata_proxy: (required)
        :rtype: :class:`com.vmware.nsx.model_client.MetadataProxy`
        :return: com.vmware.nsx.model.MetadataProxy
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
                            'metadata_proxy': metadata_proxy,
                            })

    def delete(self,
               proxy_id,
               ):
        """
        Delete a metadata proxy

        :type  proxy_id: :class:`str`
        :param proxy_id: (required)
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
                            'proxy_id': proxy_id,
                            })

    def get(self,
            proxy_id,
            ):
        """
        Get a metadata proxy

        :type  proxy_id: :class:`str`
        :param proxy_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.MetadataProxy`
        :return: com.vmware.nsx.model.MetadataProxy
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
                            'proxy_id': proxy_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Get a paginated list of metadata proxies

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
        :rtype: :class:`com.vmware.nsx.model_client.MetadataProxyListResult`
        :return: com.vmware.nsx.model.MetadataProxyListResult
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
                            })

    def update(self,
               proxy_id,
               metadata_proxy,
               ):
        """
        Update a metadata proxy

        :type  proxy_id: :class:`str`
        :param proxy_id: (required)
        :type  metadata_proxy: :class:`com.vmware.nsx.model_client.MetadataProxy`
        :param metadata_proxy: (required)
        :rtype: :class:`com.vmware.nsx.model_client.MetadataProxy`
        :return: com.vmware.nsx.model.MetadataProxy
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
                            'proxy_id': proxy_id,
                            'metadata_proxy': metadata_proxy,
                            })
class MirrorSessions(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.mirror_sessions'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MirrorSessionsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               port_mirroring_session,
               ):
        """
        Create a mirror session

        :type  port_mirroring_session: :class:`com.vmware.nsx.model_client.PortMirroringSession`
        :param port_mirroring_session: (required)
        :rtype: :class:`com.vmware.nsx.model_client.PortMirroringSession`
        :return: com.vmware.nsx.model.PortMirroringSession
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
                            'port_mirroring_session': port_mirroring_session,
                            })

    def delete(self,
               mirror_session_id,
               ):
        """
        Delete the mirror session

        :type  mirror_session_id: :class:`str`
        :param mirror_session_id: (required)
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
                            'mirror_session_id': mirror_session_id,
                            })

    def get(self,
            mirror_session_id,
            ):
        """
        Get the mirror session

        :type  mirror_session_id: :class:`str`
        :param mirror_session_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.PortMirroringSession`
        :return: com.vmware.nsx.model.PortMirroringSession
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
                            'mirror_session_id': mirror_session_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List all mirror sessions

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
        :rtype: :class:`com.vmware.nsx.model_client.PortMirroringSessionListResult`
        :return: com.vmware.nsx.model.PortMirroringSessionListResult
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
                            })

    def update(self,
               mirror_session_id,
               port_mirroring_session,
               ):
        """
        Update the mirror session

        :type  mirror_session_id: :class:`str`
        :param mirror_session_id: (required)
        :type  port_mirroring_session: :class:`com.vmware.nsx.model_client.PortMirroringSession`
        :param port_mirroring_session: (required)
        :rtype: :class:`com.vmware.nsx.model_client.PortMirroringSession`
        :return: com.vmware.nsx.model.PortMirroringSession
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
                            'mirror_session_id': mirror_session_id,
                            'port_mirroring_session': port_mirroring_session,
                            })

    def verify(self,
               mirror_session_id,
               ):
        """
        Verify whether all participants are on the same transport node

        :type  mirror_session_id: :class:`str`
        :param mirror_session_id: (required)
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
        return self._invoke('verify',
                            {
                            'mirror_session_id': mirror_session_id,
                            })
class NetworkMigrationSpecs(VapiInterface):
    """
    
    """
    LIST_TYPE_HOSTPROFILENETWORKMIGRATIONSPEC = "HostProfileNetworkMigrationSpec"
    """
    Possible value for ``type`` of method :func:`NetworkMigrationSpecs.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.network_migration_specs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NetworkMigrationSpecsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               network_migration_spec,
               ):
        """
        Network migration specification once created and can be used as a
        template to indicate associated component which networks should be
        migrated and where. Currently migration template can be associated with
        compute collections which are managed by vCenter host profiles, to
        trigger automatic migration of networks for Stateless ESX hosts.
        Currently we only support creation of HostProfileNetworkMigrationSpec
        type of specification. Note- transport node templates APIs are
        deprecated and user is recommended to use transport node profiles APIs
        instead.

        :type  network_migration_spec: :class:`vmware.vapi.struct.VapiStruct`
        :param network_migration_spec: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.NetworkMigrationSpec`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.NetworkMigrationSpec
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.NetworkMigrationSpec`.
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
                            'network_migration_spec': network_migration_spec,
                            })

    def delete(self,
               template_id,
               ):
        """
        Delete the specified network migration specification template. Delete
        will fail if this is a HostProfileNetworkMigrationSpec and is
        associated with certain compute collection. Note- transport node
        templates APIs are deprecated and user is recommended to use transport
        node profiles APIs instead.

        :type  template_id: :class:`str`
        :param template_id: (required)
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
                            'template_id': template_id,
                            })

    def get(self,
            template_id,
            ):
        """
        Network migration specification once created and can be used as a
        template to indicate associated component which networks should be
        migrated and where. Currently migration template can be associated with
        compute collections which are managed by vCenter host profiles, to
        trigger automatic migration of networks for Stateless ESX hosts.
        Currently we only support creation of HostProfileNetworkMigrationSpec
        type of specification. Note- transport node templates APIs are
        deprecated and user is recommended to use transport node profiles APIs
        instead.

        :type  template_id: :class:`str`
        :param template_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.NetworkMigrationSpec
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.NetworkMigrationSpec`.
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
                            'template_id': template_id,
                            })

    def list(self,
             cursor=None,
             include_system_owned=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             type=None,
             ):
        """
        Network migration specification once created and can be used as a
        template to indicate associated component which networks should be
        migrated and where. Currently migration template can be associated with
        compute collections which are managed by vCenter host profiles, to
        trigger automatic migration of networks for Stateless ESX hosts.
        Currently we only support creation of HostProfileNetworkMigrationSpec
        type of specification. Note- transport node templates APIs are
        deprecated and user is recommended to use transport node profiles APIs
        instead.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_system_owned: :class:`bool` or ``None``
        :param include_system_owned: Whether the list result contains system resources (optional,
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
        :type  type: :class:`str` or ``None``
        :param type: Supported network migration specification types. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.NetworkMigrationSpecListResult`
        :return: com.vmware.nsx.model.NetworkMigrationSpecListResult
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
                            'include_system_owned': include_system_owned,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'type': type,
                            })

    def update(self,
               template_id,
               network_migration_spec,
               ):
        """
        Network migration specification once created and can be used as a
        template to indicate associated component which networks should be
        migrated and where. Currently migration template can be associated with
        compute collections which are managed by vCenter host profiles, to
        trigger automatic migration of networks for Stateless ESX hosts.
        Currently we only support creation of HostProfileNetworkMigrationSpec
        type of specification. For a HostProfileNetworkMigrationSpec which is
        already associated with a compute collection, updating it would mean
        next time the system needs to trigger migration for hosts managed by
        compute collection, it will use the updated migration specification.
        Note- transport node templates APIs are deprecated and user is
        recommended to use transport node profiles APIs instead.

        :type  template_id: :class:`str`
        :param template_id: (required)
        :type  network_migration_spec: :class:`vmware.vapi.struct.VapiStruct`
        :param network_migration_spec: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.NetworkMigrationSpec`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.NetworkMigrationSpec
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.NetworkMigrationSpec`.
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
                            'template_id': template_id,
                            'network_migration_spec': network_migration_spec,
                            })
class Node(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.node'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NodeStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Returns information about the NSX appliance. Information includes
        release number, time zone, system time, kernel version, message of the
        day (motd), and host name.


        :rtype: :class:`com.vmware.nsx.model_client.NodeProperties`
        :return: com.vmware.nsx.model.NodeProperties
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

    def restart(self):
        """
        Restarts or shuts down the NSX appliance.


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
        return self._invoke('restart', None)

    def setsystemtime(self,
                      node_time,
                      ):
        """
        Set the node system time to the given time in UTC in the RFC3339 format
        'yyyy-mm-ddThh:mm:ssZ'.

        :type  node_time: :class:`com.vmware.nsx.model_client.NodeTime`
        :param node_time: (required)
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
        return self._invoke('setsystemtime',
                            {
                            'node_time': node_time,
                            })

    def shutdown(self):
        """
        Restarts or shuts down the NSX appliance.


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
        return self._invoke('shutdown', None)

    def update(self,
               node_properties,
               ):
        """
        Modifies NSX appliance properties. Modifiable properties include the
        timezone, message of the day (motd), and hostname. The NSX appliance
        node_version, system_time, and kernel_version are read only and cannot
        be modified with this method.

        :type  node_properties: :class:`com.vmware.nsx.model_client.NodeProperties`
        :param node_properties: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NodeProperties`
        :return: com.vmware.nsx.model.NodeProperties
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
                            'node_properties': node_properties,
                            })
class Normalizations(VapiInterface):
    """
    
    """
    LIST_PREFERRED_NORMALIZATION_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``preferredNormalizationType`` of method
    :func:`Normalizations.list`.

    """
    LIST_PREFERRED_NORMALIZATION_TYPE_IPSET = "IPSet"
    """
    Possible value for ``preferredNormalizationType`` of method
    :func:`Normalizations.list`.

    """
    LIST_PREFERRED_NORMALIZATION_TYPE_MACSET = "MACSet"
    """
    Possible value for ``preferredNormalizationType`` of method
    :func:`Normalizations.list`.

    """
    LIST_PREFERRED_NORMALIZATION_TYPE_LOGICALSWITCH = "LogicalSwitch"
    """
    Possible value for ``preferredNormalizationType`` of method
    :func:`Normalizations.list`.

    """
    LIST_PREFERRED_NORMALIZATION_TYPE_LOGICALPORT = "LogicalPort"
    """
    Possible value for ``preferredNormalizationType`` of method
    :func:`Normalizations.list`.

    """
    LIST_PREFERRED_NORMALIZATION_TYPE_DIRECTORYGROUP = "DirectoryGroup"
    """
    Possible value for ``preferredNormalizationType`` of method
    :func:`Normalizations.list`.

    """
    LIST_RESOURCE_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``resourceType`` of method :func:`Normalizations.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.normalizations'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NormalizationsStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             preferred_normalization_type,
             resource_id,
             resource_type,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns the list of normalized resources based on the query parameters.
        Id and Type of the resource on which the normalizations is to be
        performed, are to be specified as query parameters in the URI. The
        target resource types to which normalization is to be done should also
        be specified as query parameter.

        :type  preferred_normalization_type: :class:`str`
        :param preferred_normalization_type: Resource type valid for use as target in normalization API.
            (required)
        :type  resource_id: :class:`str`
        :param resource_id: Identifier of the resource on which normalization is to be
            performed (required)
        :type  resource_type: :class:`str`
        :param resource_type: Resource type valid for use as source in normalization API.
            (required)
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
        :rtype: :class:`com.vmware.nsx.model_client.NormalizedResourceListResult`
        :return: com.vmware.nsx.model.NormalizedResourceListResult
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
                            'preferred_normalization_type': preferred_normalization_type,
                            'resource_id': resource_id,
                            'resource_type': resource_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class NotificationWatchers(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.notification_watchers'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NotificationWatchersStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               notification_watcher,
               ):
        """
        Add a new notification watcher.

        :type  notification_watcher: :class:`com.vmware.nsx.model_client.NotificationWatcher`
        :param notification_watcher: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NotificationWatcher`
        :return: com.vmware.nsx.model.NotificationWatcher
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
                            'notification_watcher': notification_watcher,
                            })

    def delete(self,
               watcher_id,
               ):
        """
        Delete notification watcher.

        :type  watcher_id: :class:`str`
        :param watcher_id: (required)
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
                            'watcher_id': watcher_id,
                            })

    def get(self,
            watcher_id,
            ):
        """
        Returns notification watcher by watcher id.

        :type  watcher_id: :class:`str`
        :param watcher_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NotificationWatcher`
        :return: com.vmware.nsx.model.NotificationWatcher
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
                            'watcher_id': watcher_id,
                            })

    def list(self):
        """
        Returns a list of registered notification watchers.


        :rtype: :class:`com.vmware.nsx.model_client.NotificationWatcherListResult`
        :return: com.vmware.nsx.model.NotificationWatcherListResult
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
               watcher_id,
               notification_watcher,
               ):
        """
        Update notification watcher.

        :type  watcher_id: :class:`str`
        :param watcher_id: (required)
        :type  notification_watcher: :class:`com.vmware.nsx.model_client.NotificationWatcher`
        :param notification_watcher: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NotificationWatcher`
        :return: com.vmware.nsx.model.NotificationWatcher
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
                            'watcher_id': watcher_id,
                            'notification_watcher': notification_watcher,
                            })
class NsGroups(VapiInterface):
    """
    
    """
    ADDORREMOVEEXPRESSION_ACTION_ADD_MEMBERS = "ADD_MEMBERS"
    """
    Possible value for ``action`` of method :func:`NsGroups.addorremoveexpression`.

    """
    ADDORREMOVEEXPRESSION_ACTION_REMOVE_MEMBERS = "REMOVE_MEMBERS"
    """
    Possible value for ``action`` of method :func:`NsGroups.addorremoveexpression`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ns_groups'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NsGroupsStub)
        self._VAPI_OPERATION_IDS = {}


    def addorremoveexpression(self,
                              ns_group_id,
                              ns_group_expression_list,
                              action,
                              ):
        """
        Add/remove the expressions passed in the request body to/from the
        NSGroup

        :type  ns_group_id: :class:`str`
        :param ns_group_id: NSGroup Id (required)
        :type  ns_group_expression_list: :class:`com.vmware.nsx.model_client.NSGroupExpressionList`
        :param ns_group_expression_list: (required)
        :type  action: :class:`str`
        :param action: Specifies addition or removal action (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSGroup`
        :return: com.vmware.nsx.model.NSGroup
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
        return self._invoke('addorremoveexpression',
                            {
                            'ns_group_id': ns_group_id,
                            'ns_group_expression_list': ns_group_expression_list,
                            'action': action,
                            })

    def create(self,
               ns_group,
               ):
        """
        Creates a new NSGroup that can group NSX resources - VIFs, Lports and
        LSwitches as well as the grouping objects - IPSet, MACSet and other
        NSGroups. For NSGroups containing VM criteria(both static and dynamic),
        system VMs will not be included as members. This filter applies at VM
        level only. Exceptions are as follows: 1. LogicalPorts and VNI of
        System VMs will be included in NSGroup if the criteria is based on
        LogicalPort, LogicalSwitch or VNI directly.

        :type  ns_group: :class:`com.vmware.nsx.model_client.NSGroup`
        :param ns_group: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSGroup`
        :return: com.vmware.nsx.model.NSGroup
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
                            'ns_group': ns_group,
                            })

    def delete(self,
               ns_group_id,
               force=None,
               ):
        """
        Deletes the specified NSGroup. By default, if the NSGroup is added to
        another NSGroup, it won't be deleted. In such situations, pass
        \"force=true\" as query param to force delete the NSGroup.

        :type  ns_group_id: :class:`str`
        :param ns_group_id: NSGroup Id (required)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
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
                            'ns_group_id': ns_group_id,
                            'force': force,
                            })

    def get(self,
            ns_group_id,
            populate_references=None,
            ):
        """
        Returns information about the specified NSGroup.

        :type  ns_group_id: :class:`str`
        :param ns_group_id: NSGroup Id (required)
        :type  populate_references: :class:`bool` or ``None``
        :param populate_references: Populate metadata of resource referenced by NSGroupExpressions
            (optional, default to false)
        :rtype: :class:`com.vmware.nsx.model_client.NSGroup`
        :return: com.vmware.nsx.model.NSGroup
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
                            'ns_group_id': ns_group_id,
                            'populate_references': populate_references,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             member_types=None,
             page_size=None,
             populate_references=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List the NSGroups in a paginated format. The page size is restricted to
        50 NSGroups so that the size of the response remains small even in the
        worst case. Optionally, specify valid member types as request parameter
        to filter NSGroups.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  member_types: :class:`str` or ``None``
        :param member_types: Specify member types to filter corresponding NSGroups (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  populate_references: :class:`bool` or ``None``
        :param populate_references: Populate metadata of resource referenced by NSGroupExpressions
            (optional, default to false)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.NSGroupListResult`
        :return: com.vmware.nsx.model.NSGroupListResult
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
                            'member_types': member_types,
                            'page_size': page_size,
                            'populate_references': populate_references,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               ns_group_id,
               ns_group,
               ):
        """
        Updates the specified NSGroup. Modifiable parameters include the
        description, display_name and members. For NSGroups containing VM
        criteria(both static and dynamic), system VMs will not be included as
        members. This filter applies at VM level only. Exceptions are as
        follows. 1. LogicalPorts and VNI of system VMs will be included in
        NSGroup if the criteria is based on LogicalPort, LogicalSwitch or VNI
        directly.

        :type  ns_group_id: :class:`str`
        :param ns_group_id: NSGroup Id (required)
        :type  ns_group: :class:`com.vmware.nsx.model_client.NSGroup`
        :param ns_group: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSGroup`
        :return: com.vmware.nsx.model.NSGroup
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
                            'ns_group_id': ns_group_id,
                            'ns_group': ns_group,
                            })
class NsProfiles(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ns_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NsProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               ns_profile,
               ):
        """
        Creates a new NSProfile which allows users to encapsulate attribute and
        sub-attributes of network services. Rules for using attributes and
        sub-attributes in single NSProfile 1. One type of attribute can't have
        multiple occurrences. ( Example - Attribute type APP_ID can be used
        only once per NSProfile.) 2. Values for an attribute are mentioned as
        array of strings. ( Example - For type APP_ID , values can be mentioned
        as [\"SSL\",\"FTP\"].) 3. If sub-attribtes are mentioned for an
        attribute, then only single value is allowed for that attribute. 4. To
        get a list of supported attributes and sub-attributes fire the
        following REST API GET https://<nsx-mgr>/api/v1/ns-profiles/attributes

        :type  ns_profile: :class:`com.vmware.nsx.model_client.NSProfile`
        :param ns_profile: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSProfile`
        :return: com.vmware.nsx.model.NSProfile
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
                            'ns_profile': ns_profile,
                            })

    def delete(self,
               ns_profile_id,
               force=None,
               ):
        """
        Deletes the specified NSProfile. By default, if the NSProfile is
        consumed in a Firewall rule, it won't get deleted. In such situations,
        pass \"force=true\" as query param to force delete the NSProfile.

        :type  ns_profile_id: :class:`str`
        :param ns_profile_id: NSProfile Id (required)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
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
                            'ns_profile_id': ns_profile_id,
                            'force': force,
                            })

    def get(self,
            ns_profile_id,
            ):
        """
        Returns information about the specified NSProfile.

        :type  ns_profile_id: :class:`str`
        :param ns_profile_id: NSProfile Id (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSProfile`
        :return: com.vmware.nsx.model.NSProfile
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
                            'ns_profile_id': ns_profile_id,
                            })

    def list(self,
             attribute_type=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List the NSProfiles created in a paginated format.The page size is
        restricted to 50 NSProfiles, so that the size of the response remains
        small even when there are high number of NSProfiles with multiple
        attributes and multiple attribute values for each attribute.

        :type  attribute_type: :class:`str` or ``None``
        :param attribute_type: Fetch NSProfiles for the given attribute type (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.NSProfileListResult`
        :return: com.vmware.nsx.model.NSProfileListResult
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
                            'attribute_type': attribute_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               ns_profile_id,
               ns_profile,
               ):
        """
        Updates the specified NSProfile. Rules for using attributes and
        sub-attributes in single NSProfile 1. One type of attribute can't have
        multiple occurrences. ( Example - Attribute type APP_ID can be used
        only once per NSProfile.) 2. Values for an attribute are mentioned as
        array of strings. ( Example - For type APP_ID , values can be mentioned
        as [\"SSL\",\"FTP\"].) 3. If sub-attribtes are mentioned for an
        attribute, then only single value is allowed for that attribute. 4. To
        get a list of supported attributes and sub-attributes fire the
        following REST API GET https://<nsx-mgr>/api/v1/ns-profiles/attributes

        :type  ns_profile_id: :class:`str`
        :param ns_profile_id: NSProfile Id (required)
        :type  ns_profile: :class:`com.vmware.nsx.model_client.NSProfile`
        :param ns_profile: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSProfile`
        :return: com.vmware.nsx.model.NSProfile
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
                            'ns_profile_id': ns_profile_id,
                            'ns_profile': ns_profile,
                            })
class NsServiceGroups(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ns_service_groups'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NsServiceGroupsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               ns_service_group,
               ):
        """
        Creates a new NSServiceGroup which can contain NSServices. A given
        NSServiceGroup can contain either only ether type of NSServices or only
        non-ether type of NSServices, i.e. an NSServiceGroup cannot contain a
        mix of both ether and non-ether types of NSServices.

        :type  ns_service_group: :class:`com.vmware.nsx.model_client.NSServiceGroup`
        :param ns_service_group: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSServiceGroup`
        :return: com.vmware.nsx.model.NSServiceGroup
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
                            'ns_service_group': ns_service_group,
                            })

    def delete(self,
               ns_service_group_id,
               force=None,
               ):
        """
        Deletes the specified NSServiceGroup. By default, if the NSServiceGroup
        is consumed in a Firewall rule, it won't get deleted. In such
        situations, pass \"force=true\" as query param to force delete the
        NSServiceGroup.

        :type  ns_service_group_id: :class:`str`
        :param ns_service_group_id: NSServiceGroup Id (required)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
            (optional, default to false)
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
        return self._invoke('delete',
                            {
                            'ns_service_group_id': ns_service_group_id,
                            'force': force,
                            })

    def get(self,
            ns_service_group_id,
            ):
        """
        Returns information about the specified NSServiceGroup

        :type  ns_service_group_id: :class:`str`
        :param ns_service_group_id: NSServiceGroup Id (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSServiceGroup`
        :return: com.vmware.nsx.model.NSServiceGroup
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
                            'ns_service_group_id': ns_service_group_id,
                            })

    def list(self,
             cursor=None,
             default_service=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns paginated list of NSServiceGroups

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  default_service: :class:`bool` or ``None``
        :param default_service: Fetch all default NSServiceGroups (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.NSServiceGroupListResult`
        :return: com.vmware.nsx.model.NSServiceGroupListResult
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
                            'default_service': default_service,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               ns_service_group_id,
               ns_service_group,
               ):
        """
        Updates the specified NSService. Modifiable parameters include the
        description, display_name and members.

        :type  ns_service_group_id: :class:`str`
        :param ns_service_group_id: NSServiceGroup Id (required)
        :type  ns_service_group: :class:`com.vmware.nsx.model_client.NSServiceGroup`
        :param ns_service_group: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSServiceGroup`
        :return: com.vmware.nsx.model.NSServiceGroup
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
        return self._invoke('update',
                            {
                            'ns_service_group_id': ns_service_group_id,
                            'ns_service_group': ns_service_group,
                            })
class NsServices(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ns_services'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NsServicesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               ns_service,
               ):
        """
        Creates a new NSService which allows users to specify characteristics
        to use for matching network traffic.

        :type  ns_service: :class:`com.vmware.nsx.model_client.NSService`
        :param ns_service: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSService`
        :return: com.vmware.nsx.model.NSService
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
                            'ns_service': ns_service,
                            })

    def delete(self,
               ns_service_id,
               force=None,
               ):
        """
        Deletes the specified NSService. By default, if the NSService is being
        referred in an NSServiceGroup, it can't be deleted. In such situations,
        pass \"force=true\" as a parameter to force delete the NSService.
        System defined NSServices can't be deleted using \"force\" flag.

        :type  ns_service_id: :class:`str`
        :param ns_service_id: NSService Id (required)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
            (optional, default to false)
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
        return self._invoke('delete',
                            {
                            'ns_service_id': ns_service_id,
                            'force': force,
                            })

    def get(self,
            ns_service_id,
            ):
        """
        Returns information about the specified NSService

        :type  ns_service_id: :class:`str`
        :param ns_service_id: NSService Id (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSService`
        :return: com.vmware.nsx.model.NSService
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
                            'ns_service_id': ns_service_id,
                            })

    def list(self,
             cursor=None,
             default_service=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns paginated list of NSServices

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  default_service: :class:`bool` or ``None``
        :param default_service: Fetch all default NSServices (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.NSServiceListResult`
        :return: com.vmware.nsx.model.NSServiceListResult
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
                            'default_service': default_service,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               ns_service_id,
               ns_service,
               ):
        """
        Updates the specified NSService. Modifiable parameters include the
        description, display_name and the NSService element. The system defined
        NSServices can't be modified

        :type  ns_service_id: :class:`str`
        :param ns_service_id: NSService Id (required)
        :type  ns_service: :class:`com.vmware.nsx.model_client.NSService`
        :param ns_service: (required)
        :rtype: :class:`com.vmware.nsx.model_client.NSService`
        :return: com.vmware.nsx.model.NSService
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
        return self._invoke('update',
                            {
                            'ns_service_id': ns_service_id,
                            'ns_service': ns_service,
                            })
class ServiceConfigs(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.service_configs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceConfigsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               service_config,
               ):
        """
        Creates a new service config that can group profiles and configs

        :type  service_config: :class:`com.vmware.nsx.model_client.ServiceConfig`
        :param service_config: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceConfig`
        :return: com.vmware.nsx.model.ServiceConfig
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
                            'service_config': service_config,
                            })

    def delete(self,
               config_set_id,
               ):
        """
        Deletes the specified service config

        :type  config_set_id: :class:`str`
        :param config_set_id: service Ccnfig Id (required)
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
                            'config_set_id': config_set_id,
                            })

    def get(self,
            config_set_id,
            ):
        """
        Returns information about the specified Service Config.

        :type  config_set_id: :class:`str`
        :param config_set_id: Service Config Id (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceConfig`
        :return: com.vmware.nsx.model.ServiceConfig
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
                            'config_set_id': config_set_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             profile_type=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List of all service configs.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  profile_type: :class:`str` or ``None``
        :param profile_type: Fetch ServiceConfig for the given attribute profile_type (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceConfigListResult`
        :return: com.vmware.nsx.model.ServiceConfigListResult
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
                            'profile_type': profile_type,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               config_set_id,
               service_config,
               ):
        """
        Updates the specified ServiceConfig.

        :type  config_set_id: :class:`str`
        :param config_set_id: service config Id (required)
        :type  service_config: :class:`com.vmware.nsx.model_client.ServiceConfig`
        :param service_config: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceConfig`
        :return: com.vmware.nsx.model.ServiceConfig
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
                            'config_set_id': config_set_id,
                            'service_config': service_config,
                            })
class SwitchingProfiles(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.switching_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SwitchingProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               base_switching_profile,
               ):
        """
        Creates a new, custom qos, port-mirroring, spoof-guard or port-security
        switching profile. You can override their default switching profile
        assignments by creating a new switching profile and assigning it to one
        or more logical switches. You cannot override the default ipfix or
        ip_discovery switching profiles.

        :type  base_switching_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param base_switching_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseSwitchingProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.BaseSwitchingProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseSwitchingProfile`.
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
                            'base_switching_profile': base_switching_profile,
                            })

    def delete(self,
               switching_profile_id,
               unbind=None,
               ):
        """
        Deletes the specified switching profile.

        :type  switching_profile_id: :class:`str`
        :param switching_profile_id: (required)
        :type  unbind: :class:`bool` or ``None``
        :param unbind: force unbinding of logical switches and ports from a switching
            profile (optional, default to false)
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
                            'switching_profile_id': switching_profile_id,
                            'unbind': unbind,
                            })

    def get(self,
            switching_profile_id,
            ):
        """
        Returns information about a specified switching profile.

        :type  switching_profile_id: :class:`str`
        :param switching_profile_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.BaseSwitchingProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseSwitchingProfile`.
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
                            'switching_profile_id': switching_profile_id,
                            })

    def list(self,
             cursor=None,
             include_system_owned=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             switching_profile_type=None,
             ):
        """
        Returns information about the system-default and user-configured
        switching profiles. Each switching profile has a unique ID, a display
        name, and various other read-only and configurable properties. The
        default switching profiles are assigned automatically to each switch.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_system_owned: :class:`bool` or ``None``
        :param include_system_owned: Whether the list result contains system resources (optional,
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
        :type  switching_profile_type: :class:`str` or ``None``
        :param switching_profile_type: comma-separated list of switching profile types, e.g.
            ?switching_profile_type=QosSwitchingProfile,IpDiscoverySwitchingProfile
            (optional)
        :rtype: :class:`com.vmware.nsx.model_client.SwitchingProfilesListResult`
        :return: com.vmware.nsx.model.SwitchingProfilesListResult
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
                            'include_system_owned': include_system_owned,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'switching_profile_type': switching_profile_type,
                            })

    def update(self,
               switching_profile_id,
               base_switching_profile,
               ):
        """
        Updates the user-configurable parameters of a switching profile. Only
        the qos, port-mirroring, spoof-guard and port-security switching
        profiles can be modified. You cannot modify the ipfix or ip-discovery
        switching profiles.

        :type  switching_profile_id: :class:`str`
        :param switching_profile_id: (required)
        :type  base_switching_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param base_switching_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseSwitchingProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.BaseSwitchingProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.BaseSwitchingProfile`.
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
                            'switching_profile_id': switching_profile_id,
                            'base_switching_profile': base_switching_profile,
                            })
class Tasks(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.tasks'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TasksStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            task_id,
            ):
        """
        Get information about the specified task

        :type  task_id: :class:`str`
        :param task_id: ID of task to read (required)
        :rtype: :class:`com.vmware.nsx.model_client.TaskProperties`
        :return: com.vmware.nsx.model.TaskProperties
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
                            'task_id': task_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             request_uri=None,
             sort_ascending=None,
             sort_by=None,
             status=None,
             user=None,
             ):
        """
        Get information about all tasks

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  request_uri: :class:`str` or ``None``
        :param request_uri: Request URI(s) to include in query result (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  status: :class:`str` or ``None``
        :param status: Status(es) to include in query result (optional)
        :type  user: :class:`str` or ``None``
        :param user: Names of users to include in query result (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TaskListResult`
        :return: com.vmware.nsx.model.TaskListResult
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
                            'request_uri': request_uri,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'status': status,
                            'user': user,
                            })
class Traceflows(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.traceflows'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TraceflowsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               traceflow_request,
               ):
        """
        Initiate a Traceflow Operation on the Specified Port

        :type  traceflow_request: :class:`com.vmware.nsx.model_client.TraceflowRequest`
        :param traceflow_request: (required)
        :rtype: :class:`com.vmware.nsx.model_client.Traceflow`
        :return: com.vmware.nsx.model.Traceflow
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
                            'traceflow_request': traceflow_request,
                            })

    def delete(self,
               traceflow_id,
               ):
        """
        Delete the Traceflow round

        :type  traceflow_id: :class:`str`
        :param traceflow_id: (required)
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
                            'traceflow_id': traceflow_id,
                            })

    def get(self,
            traceflow_id,
            ):
        """
        Get the Traceflow round status and result summary

        :type  traceflow_id: :class:`str`
        :param traceflow_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.Traceflow`
        :return: com.vmware.nsx.model.Traceflow
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
                            'traceflow_id': traceflow_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             lport_id=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List all Traceflow rounds; if a logical port id is given as a query
        parameter, only those originated from the logical port are returned.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  lport_id: :class:`str` or ``None``
        :param lport_id: id of the source logical port where the trace flows originated
            (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TraceflowListResult`
        :return: com.vmware.nsx.model.TraceflowListResult
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
                            'lport_id': lport_id,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class TransportNodeCollections(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_node_collections'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TransportNodeCollectionsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               transport_node_collection,
               ):
        """
        When transport node collection is created the hosts which are part of
        compute collection will be prepared automatically i.e. NSX Manager
        attempts to install the NSX components on hosts. Transport nodes for
        these hosts are created using the configuration specified in transport
        node profile.

        :type  transport_node_collection: :class:`com.vmware.nsx.model_client.TransportNodeCollection`
        :param transport_node_collection: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeCollection`
        :return: com.vmware.nsx.model.TransportNodeCollection
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
                            'transport_node_collection': transport_node_collection,
                            })

    def delete(self,
               transport_node_collection_id,
               ):
        """
        By deleting transport node collection, we are detaching the transport
        node profile(TNP) from the compute collection. It has no effect on
        existing transport nodes. However, new hosts added to the compute
        collection will no longer be automatically converted to NSX transport
        node. Detaching TNP from compute collection does not delete TNP.

        :type  transport_node_collection_id: :class:`str`
        :param transport_node_collection_id: (required)
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
                            'transport_node_collection_id': transport_node_collection_id,
                            })

    def get(self,
            transport_node_collection_id,
            ):
        """
        Returns transport node collection by id

        :type  transport_node_collection_id: :class:`str`
        :param transport_node_collection_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeCollection`
        :return: com.vmware.nsx.model.TransportNodeCollection
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
                            'transport_node_collection_id': transport_node_collection_id,
                            })

    def list(self):
        """
        Returns all Transport Node collections


        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeCollectionListResult`
        :return: com.vmware.nsx.model.TransportNodeCollectionListResult
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
               transport_node_collection_id,
               transport_node_collection,
               ):
        """
        Attach different transport node profile to compute collection by
        updating transport node collection.

        :type  transport_node_collection_id: :class:`str`
        :param transport_node_collection_id: (required)
        :type  transport_node_collection: :class:`com.vmware.nsx.model_client.TransportNodeCollection`
        :param transport_node_collection: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeCollection`
        :return: com.vmware.nsx.model.TransportNodeCollection
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
                            'transport_node_collection_id': transport_node_collection_id,
                            'transport_node_collection': transport_node_collection,
                            })
class TransportNodeProfiles(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_node_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TransportNodeProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               transport_node_profile,
               ):
        """
        Transport node profile captures the configuration needed to create a
        transport node. A transport node profile can be attached to compute
        collections for automatic TN creation of member hosts.

        :type  transport_node_profile: :class:`com.vmware.nsx.model_client.TransportNodeProfile`
        :param transport_node_profile: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeProfile`
        :return: com.vmware.nsx.model.TransportNodeProfile
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
                            'transport_node_profile': transport_node_profile,
                            })

    def delete(self,
               transport_node_profile_id,
               ):
        """
        Deletes the specified transport node profile. A transport node profile
        can be deleted only when it is not attached to any compute collection.

        :type  transport_node_profile_id: :class:`str`
        :param transport_node_profile_id: (required)
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
                            'transport_node_profile_id': transport_node_profile_id,
                            })

    def get(self,
            transport_node_profile_id,
            ):
        """
        Returns information about a specified transport node profile.

        :type  transport_node_profile_id: :class:`str`
        :param transport_node_profile_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeProfile`
        :return: com.vmware.nsx.model.TransportNodeProfile
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
                            'transport_node_profile_id': transport_node_profile_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all transport node profiles.

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
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeProfileListResult`
        :return: com.vmware.nsx.model.TransportNodeProfileListResult
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
                            })

    def update(self,
               transport_node_profile_id,
               transport_node_profile,
               esx_mgmt_if_migration_dest=None,
               if_id=None,
               ping_ip=None,
               vnic=None,
               vnic_migration_dest=None,
               ):
        """
        When configurations of a transport node profile(TNP) is updated, all
        the transport nodes in all the compute collections to which this TNP is
        attached are updated to reflect the updated configuration.

        :type  transport_node_profile_id: :class:`str`
        :param transport_node_profile_id: (required)
        :type  transport_node_profile: :class:`com.vmware.nsx.model_client.TransportNodeProfile`
        :param transport_node_profile: (required)
        :type  esx_mgmt_if_migration_dest: :class:`str` or ``None``
        :param esx_mgmt_if_migration_dest: The network ids to which the ESX vmk interfaces will be migrated
            (optional)
        :type  if_id: :class:`str` or ``None``
        :param if_id: The ESX vmk interfaces to migrate (optional)
        :type  ping_ip: :class:`str` or ``None``
        :param ping_ip: IP Addresses to ping right after ESX vmk interfaces were migrated.
            (optional)
        :type  vnic: :class:`str` or ``None``
        :param vnic: The ESX vmk interfaces and/or VM NIC to migrate (optional)
        :type  vnic_migration_dest: :class:`str` or ``None``
        :param vnic_migration_dest: The migration destinations of ESX vmk interfaces and/or VM NIC
            (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeProfile`
        :return: com.vmware.nsx.model.TransportNodeProfile
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
                            'transport_node_profile_id': transport_node_profile_id,
                            'transport_node_profile': transport_node_profile,
                            'esx_mgmt_if_migration_dest': esx_mgmt_if_migration_dest,
                            'if_id': if_id,
                            'ping_ip': ping_ip,
                            'vnic': vnic,
                            'vnic_migration_dest': vnic_migration_dest,
                            })
class TransportNodes(VapiInterface):
    """
    
    """
    UPDATEMAINTENANCEMODE_ACTION_ENTER_MAINTENANCE_MODE = "enter_maintenance_mode"
    """
    Possible value for ``action`` of method
    :func:`TransportNodes.updatemaintenancemode`.

    """
    UPDATEMAINTENANCEMODE_ACTION_FORCED_ENTER_MAINTENANCE_MODE = "forced_enter_maintenance_mode"
    """
    Possible value for ``action`` of method
    :func:`TransportNodes.updatemaintenancemode`.

    """
    UPDATEMAINTENANCEMODE_ACTION_EXIT_MAINTENANCE_MODE = "exit_maintenance_mode"
    """
    Possible value for ``action`` of method
    :func:`TransportNodes.updatemaintenancemode`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_nodes'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TransportNodesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               transport_node,
               ):
        """
        Transport nodes are hypervisor hosts and NSX Edges that will
        participate in an NSX-T overlay. For a hypervisor host, this means that
        it hosts VMs that will communicate over NSX-T logical switches. For NSX
        Edges, this means that it will have logical router uplinks and
        downlinks. This API creates transport node for a host node (hypervisor)
        or edge node (router) in the transport network. When you run this
        command for a host, NSX Manager attempts to install the NSX kernel
        modules, which are packaged as VIB, RPM, or DEB files. For the
        installation to succeed, you must provide the host login credentials
        and the host thumbprint. To get the ESXi host thumbprint, SSH to the
        host and run the **openssl x509 -in /etc/vmware/ssl/rui.crt
        -fingerprint -sha256 -noout** command. To generate host key thumbprint
        using SHA-256 algorithm please follow the steps below. Log into the
        host, making sure that the connection is not vulnerable to a man in the
        middle attack. Check whether a public key already exists. Host public
        key is generally located at '/etc/ssh/ssh_host_rsa_key.pub'. If the key
        is not present then generate a new key by running the following command
        and follow the instructions. **ssh-keygen -t rsa** Now generate a
        SHA256 hash of the key using the following command. Please make sure to
        pass the appropriate file name if the public key is stored with a
        different file name other than the default 'id_rsa.pub'. **awk '{print
        $2}' id_rsa.pub | base64 -d | sha256sum -b | sed 's/ .\*$//' | xxd -r
        -p | base64** This api is deprecated as part of FN+TN unification.
        Please use Transport Node API to install NSX components on a node.
        Additional documentation on creating a transport node can be found in
        the NSX-T Installation Guide. In order for the transport node to
        forward packets, the host_switch_spec property must be specified. Host
        switches (called bridges in OVS on KVM hypervisors) are the individual
        switches within the host virtual switch. Virtual machines are connected
        to the host switches. When creating a transport node, you need to
        specify if the host switches are already manually preconfigured on the
        node, or if NSX should create and manage the host switches. You specify
        this choice by the type of host switches you pass in the
        host_switch_spec property of the TransportNode request payload. For a
        KVM host, you can preconfigure the host switch, or you can have NSX
        Manager perform the configuration. For an ESXi host or NSX Edge node,
        NSX Manager always configures the host switch. To preconfigure the host
        switches on a KVM host, pass an array of PreconfiguredHostSwitchSpec
        objects that describes those host switches. In the current NSX-T
        release, only one prefonfigured host switch can be specified. See the
        PreconfiguredHostSwitchSpec schema definition for documentation on the
        properties that must be provided. Preconfigured host switches are only
        supported on KVM hosts, not on ESXi hosts or NSX Edge nodes. To allow
        NSX to manage the host switch configuration on KVM hosts, ESXi hosts,
        or NSX Edge nodes, pass an array of StandardHostSwitchSpec objects in
        the host_switch_spec property, and NSX will automatically create host
        switches with the properties you provide. In the current NSX-T release,
        up to 5 host switches can be automatically managed. See the
        StandardHostSwitchSpec schema definition for documentation on the
        properties that must be provided. Note: previous versions of NSX-T used
        a property named host_switches to specify the host switch configuration
        on the transport node. That property is deprecated, but still
        functions. You should configure new host switches using the
        host_switch_spec property. The request should either provide
        node_deployement_info or node_id. If the host node (hypervisor) or edge
        node (router) is already added in system then it can be converted to
        transport node by providing node_id in request. If host node
        (hypervisor) or edge node (router) is not already present in system
        then information should be provided under node_deployment_info.

        :type  transport_node: :class:`com.vmware.nsx.model_client.TransportNode`
        :param transport_node: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNode`
        :return: com.vmware.nsx.model.TransportNode
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
                            'transport_node': transport_node,
                            })

    def delete(self,
               transport_node_id,
               force=None,
               unprepare_host=None,
               ):
        """
        Deletes the specified transport node. Query param force can be used to
        force delete the host nodes. Force deletion of edge and public cloud
        gateway nodes is not supported. It also removes the specified node
        (host or edge) from system. If unprepare_host option is set to false,
        then host will be deleted without uninstalling the NSX components from
        the host.

        :type  transport_node_id: :class:`str`
        :param transport_node_id: (required)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
            (optional, default to false)
        :type  unprepare_host: :class:`bool` or ``None``
        :param unprepare_host: Uninstall NSX components from host while deleting (optional,
            default to true)
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
                            'transport_node_id': transport_node_id,
                            'force': force,
                            'unprepare_host': unprepare_host,
                            })

    def deleteontransportnode(self,
                              target_node_id,
                              target_uri,
                              ):
        """
        Invoke DELETE request on target transport node

        :type  target_node_id: :class:`str`
        :param target_node_id: Target node UUID (required)
        :type  target_uri: :class:`str`
        :param target_uri: URI of API to invoke on target node (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
             Gateway Timeout
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
        return self._invoke('deleteontransportnode',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def disableflowcache(self,
                         transport_node_id,
                         ):
        """
        Disable flow cache for edge transport node. Caution: This involves
        restart of the edge dataplane and hence may lead to network disruption.

        :type  transport_node_id: :class:`str`
        :param transport_node_id: (required)
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
        return self._invoke('disableflowcache',
                            {
                            'transport_node_id': transport_node_id,
                            })

    def enableflowcache(self,
                        transport_node_id,
                        ):
        """
        Enable flow cache for edge transport node. Caution: This involves
        restart of the edge dataplane and hence may lead to network disruption.

        :type  transport_node_id: :class:`str`
        :param transport_node_id: (required)
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
        return self._invoke('enableflowcache',
                            {
                            'transport_node_id': transport_node_id,
                            })

    def get(self,
            transport_node_id,
            ):
        """
        Returns information about a specified transport node.

        :type  transport_node_id: :class:`str`
        :param transport_node_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNode`
        :return: com.vmware.nsx.model.TransportNode
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
                            'transport_node_id': transport_node_id,
                            })

    def getontransportnode(self,
                           target_node_id,
                           target_uri,
                           ):
        """
        Invoke GET request on target transport node

        :type  target_node_id: :class:`str`
        :param target_node_id: Target node UUID (required)
        :type  target_uri: :class:`str`
        :param target_uri: URI of API to invoke on target node (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
             Gateway Timeout
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
        return self._invoke('getontransportnode',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def list(self,
             cursor=None,
             in_maintenance_mode=None,
             included_fields=None,
             node_id=None,
             node_ip=None,
             node_types=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             transport_zone_id=None,
             ):
        """
        Returns information about all transport nodes along with underlying
        host or edge details. A transport node is a host or edge that contains
        hostswitches. A hostswitch can have virtual machines connected to them.
        Because each transport node has hostswitches, transport nodes can also
        have virtual tunnel endpoints, which means that they can be part of the
        overlay.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  in_maintenance_mode: :class:`bool` or ``None``
        :param in_maintenance_mode: maintenance mode flag (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  node_id: :class:`str` or ``None``
        :param node_id: node identifier (optional)
        :type  node_ip: :class:`str` or ``None``
        :param node_ip: Fabric node IP address (optional)
        :type  node_types: :class:`str` or ``None``
        :param node_types: a list of fabric node types separated by comma or a single type
            (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  transport_zone_id: :class:`str` or ``None``
        :param transport_zone_id: Transport zone identifier (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeListResult`
        :return: com.vmware.nsx.model.TransportNodeListResult
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
                            'in_maintenance_mode': in_maintenance_mode,
                            'included_fields': included_fields,
                            'node_id': node_id,
                            'node_ip': node_ip,
                            'node_types': node_types,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'transport_zone_id': transport_zone_id,
                            })

    def postontransportnode(self,
                            target_node_id,
                            target_uri,
                            ):
        """
        Invoke POST request on target transport node

        :type  target_node_id: :class:`str`
        :param target_node_id: Target node UUID (required)
        :type  target_uri: :class:`str`
        :param target_uri: URI of API to invoke on target node (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
             Gateway Timeout
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
        return self._invoke('postontransportnode',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def putontransportnode(self,
                           target_node_id,
                           target_uri,
                           ):
        """
        Invoke PUT request on target transport node

        :type  target_node_id: :class:`str`
        :param target_node_id: Target node UUID (required)
        :type  target_uri: :class:`str`
        :param target_uri: URI of API to invoke on target node (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
             Gateway Timeout
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
        return self._invoke('putontransportnode',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def refreshnodeconfiguration(self,
                                 transport_node_id,
                                 ):
        """
        The API is applicable for Edge transport nodes. If you update the VM
        configuration and find a discrepancy in VM configuration at NSX
        Manager, then use this API to refresh configuration at NSX Manager. It
        refreshes the VM configuration from sources external to MP. Sources
        include vSphere Server and the edge node. After this action, the API
        GET api/v1/transport-nodes will show refreshed data.

        :type  transport_node_id: :class:`str`
        :param transport_node_id: (required)
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
        return self._invoke('refreshnodeconfiguration',
                            {
                            'transport_node_id': transport_node_id,
                            })

    def restartinventorysync(self,
                             transport_node_id,
                             ):
        """
        Restart the inventory sync for the node if it is currently internally
        paused. After this action the next inventory sync coming from the node
        is processed.

        :type  transport_node_id: :class:`str`
        :param transport_node_id: (required)
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
        return self._invoke('restartinventorysync',
                            {
                            'transport_node_id': transport_node_id,
                            })

    def restoreclusterconfig(self,
                             transport_node_id,
                             ):
        """
        A host can be overridden to have different configuration than Transport
        Node Profile(TNP) on cluster. This action will restore such overridden
        host back to cluster level TNP. This API can be used in other case.
        When TNP is applied to a cluster, if any validation fails (e.g. VMs
        running on host) then existing transport node (TN) is not updated. In
        that case after the issue is resolved manually (e.g. VMs powered off),
        you can call this API to update TN as per cluster level TNP.

        :type  transport_node_id: :class:`str`
        :param transport_node_id: (required)
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
        return self._invoke('restoreclusterconfig',
                            {
                            'transport_node_id': transport_node_id,
                            })

    def resynchostconfig(self,
                         transportnode_id,
                         ):
        """
        Resync the TransportNode configuration on a host. It is similar to
        updating the TransportNode with existing configuration, but force synce
        these configurations to the host (no backend optimizations).

        :type  transportnode_id: :class:`str`
        :param transportnode_id: (required)
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
        return self._invoke('resynchostconfig',
                            {
                            'transportnode_id': transportnode_id,
                            })

    def update(self,
               transport_node_id,
               transport_node,
               esx_mgmt_if_migration_dest=None,
               if_id=None,
               ping_ip=None,
               vnic=None,
               vnic_migration_dest=None,
               ):
        """
        Modifies the transport node information. The host_switch_name field
        must match the host_switch_name value specified in the transport zone
        (API: transport-zones). You must create the associated uplink profile
        (API: host-switch-profiles) before you can specify an uplink_name here.
        If the host is an ESX and has only one physical NIC being used by a
        vSphere standard switch, TransportNodeUpdateParameters should be used
        to migrate the management interface and the physical NIC into a logical
        switch that is in a transport zone this transport node will join or has
        already joined. If the migration is already done,
        TransportNodeUpdateParameters can also be used to migrate the
        management interface and the physical NIC back to a vSphere standard
        switch. In other cases, the TransportNodeUpdateParameters should NOT be
        used. When updating transport node you should follow pattern where you
        should fetch the existing transport node and then only modify the
        required properties keeping other properties as is. For API backward
        compatibility, property host_switches will be still returned in
        response and will contain the configuration matching the one in
        host_switch_spec. In update call you should only modify configuration
        in either host_switch_spec or host_switches, but not both. Property
        host_switch_spec should be preferred over deprecated host_switches
        property when creating or updating transport nodes. It also modifies
        attributes of node (host or edge).

        :type  transport_node_id: :class:`str`
        :param transport_node_id: (required)
        :type  transport_node: :class:`com.vmware.nsx.model_client.TransportNode`
        :param transport_node: (required)
        :type  esx_mgmt_if_migration_dest: :class:`str` or ``None``
        :param esx_mgmt_if_migration_dest: The network ids to which the ESX vmk interfaces will be migrated
            (optional)
        :type  if_id: :class:`str` or ``None``
        :param if_id: The ESX vmk interfaces to migrate (optional)
        :type  ping_ip: :class:`str` or ``None``
        :param ping_ip: IP Addresses to ping right after ESX vmk interfaces were migrated.
            (optional)
        :type  vnic: :class:`str` or ``None``
        :param vnic: The ESX vmk interfaces and/or VM NIC to migrate (optional)
        :type  vnic_migration_dest: :class:`str` or ``None``
        :param vnic_migration_dest: The migration destinations of ESX vmk interfaces and/or VM NIC
            (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNode`
        :return: com.vmware.nsx.model.TransportNode
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
                            'transport_node_id': transport_node_id,
                            'transport_node': transport_node,
                            'esx_mgmt_if_migration_dest': esx_mgmt_if_migration_dest,
                            'if_id': if_id,
                            'ping_ip': ping_ip,
                            'vnic': vnic,
                            'vnic_migration_dest': vnic_migration_dest,
                            })

    def updatemaintenancemode(self,
                              transportnode_id,
                              action=None,
                              ):
        """
        Put transport node into maintenance mode or exit from maintenance mode.

        :type  transportnode_id: :class:`str`
        :param transportnode_id: (required)
        :type  action: :class:`str` or ``None``
        :param action: (optional)
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
        return self._invoke('updatemaintenancemode',
                            {
                            'transportnode_id': transportnode_id,
                            'action': action,
                            })
class TransportZones(VapiInterface):
    """
    
    """
    LIST_TRANSPORT_TYPE_OVERLAY = "OVERLAY"
    """
    Possible value for ``transportType`` of method :func:`TransportZones.list`.

    """
    LIST_TRANSPORT_TYPE_VLAN = "VLAN"
    """
    Possible value for ``transportType`` of method :func:`TransportZones.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_zones'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TransportZonesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               transport_zone,
               ):
        """
        Creates a new transport zone. The required parameters are
        host_switch_name and transport_type (OVERLAY or VLAN). The optional
        parameters are description and display_name.

        :type  transport_zone: :class:`com.vmware.nsx.model_client.TransportZone`
        :param transport_zone: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportZone`
        :return: com.vmware.nsx.model.TransportZone
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
                            'transport_zone': transport_zone,
                            })

    def delete(self,
               zone_id,
               ):
        """
        Deletes an existing transport zone.

        :type  zone_id: :class:`str`
        :param zone_id: (required)
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
                            'zone_id': zone_id,
                            })

    def get(self,
            zone_id,
            ):
        """
        Returns information about a single transport zone.

        :type  zone_id: :class:`str`
        :param zone_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportZone`
        :return: com.vmware.nsx.model.TransportZone
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
                            'zone_id': zone_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             is_default=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             transport_type=None,
             uplink_teaming_policy_name=None,
             ):
        """
        Returns information about configured transport zones. NSX requires at
        least one transport zone. NSX uses transport zones to provide
        connectivity based on the topology of the underlying network, trust
        zones, or organizational separations. For example, you might have
        hypervisors that use one network for management traffic and a different
        network for VM traffic. This architecture would require two transport
        zones. The combination of transport zones plus transport connectors
        enables NSX to form tunnels between hypervisors. Transport zones define
        which interfaces on the hypervisors can communicate with which other
        interfaces on other hypervisors to establish overlay tunnels or provide
        connectivity to a VLAN. A logical switch can be in one (and only one)
        transport zone. This means that all of a switch's interfaces must be in
        the same transport zone. However, each hypervisor virtual switch (OVS
        or VDS) has multiple interfaces (connectors), and each connector can be
        attached to a different logical switch. For example, on a single
        hypervisor with two connectors, connector A can be attached to logical
        switch 1 in transport zone A, while connector B is attached to logical
        switch 2 in transport zone B. In this way, a single hypervisor can
        participate in multiple transport zones. The API for creating a
        transport zone requires that a single host switch be specified for each
        transport zone, and multiple transport zones can share the same host
        switch.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  is_default: :class:`bool` or ``None``
        :param is_default: Filter to choose if default transport zones will be returned
            (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  transport_type: :class:`str` or ``None``
        :param transport_type: Filter to choose the type of transport zones to return (optional)
        :type  uplink_teaming_policy_name: :class:`str` or ``None``
        :param uplink_teaming_policy_name: The transport zone's uplink teaming policy name (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportZoneListResult`
        :return: com.vmware.nsx.model.TransportZoneListResult
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
                            'is_default': is_default,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'transport_type': transport_type,
                            'uplink_teaming_policy_name': uplink_teaming_policy_name,
                            })

    def update(self,
               zone_id,
               transport_zone,
               ):
        """
        Updates an existing transport zone. Modifiable parameters are
        transport_type (VLAN or OVERLAY), description, and display_name. The
        request must include the existing host_switch_name.

        :type  zone_id: :class:`str`
        :param zone_id: (required)
        :type  transport_zone: :class:`com.vmware.nsx.model_client.TransportZone`
        :param transport_zone: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportZone`
        :return: com.vmware.nsx.model.TransportZone
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
                            'zone_id': zone_id,
                            'transport_zone': transport_zone,
                            })
class TransportzoneProfiles(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transportzone_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TransportzoneProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               transport_zone_profile,
               ):
        """
        Creates a transport zone profile. The resource_type is required.

        :type  transport_zone_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param transport_zone_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.TransportZoneProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.TransportZoneProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.TransportZoneProfile`.
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
                            'transport_zone_profile': transport_zone_profile,
                            })

    def delete(self,
               transportzone_profile_id,
               ):
        """
        Deletes a specified transport zone profile.

        :type  transportzone_profile_id: :class:`str`
        :param transportzone_profile_id: (required)
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
                            'transportzone_profile_id': transportzone_profile_id,
                            })

    def get(self,
            transportzone_profile_id,
            ):
        """
        Returns information about a specified transport zone profile.

        :type  transportzone_profile_id: :class:`str`
        :param transportzone_profile_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.TransportZoneProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.TransportZoneProfile`.
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
                            'transportzone_profile_id': transportzone_profile_id,
                            })

    def list(self,
             cursor=None,
             include_system_owned=None,
             included_fields=None,
             page_size=None,
             resource_type=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about the configured transport zone profiles.
        Transport zone profiles define networking policies for transport zones
        and transport zone endpoints.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_system_owned: :class:`bool` or ``None``
        :param include_system_owned: Whether the list result contains system resources (optional,
            default to false)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: comma-separated list of transport zone profile types, e.g.
            ?resource_type=BfdHealthMonitoringProfile (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportZoneProfileListResult`
        :return: com.vmware.nsx.model.TransportZoneProfileListResult
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
                            'include_system_owned': include_system_owned,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'resource_type': resource_type,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               transportzone_profile_id,
               transport_zone_profile,
               ):
        """
        Modifies a specified transport zone profile. The body of the PUT
        request must include the resource_type.

        :type  transportzone_profile_id: :class:`str`
        :param transportzone_profile_id: (required)
        :type  transport_zone_profile: :class:`vmware.vapi.struct.VapiStruct`
        :param transport_zone_profile: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.TransportZoneProfile`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.TransportZoneProfile
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.TransportZoneProfile`.
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
                            'transportzone_profile_id': transportzone_profile_id,
                            'transport_zone_profile': transport_zone_profile,
                            })
class TrustManagement(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.trust_management'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TrustManagementStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Returns information about the supported algorithms and key sizes.


        :rtype: :class:`com.vmware.nsx.model_client.TrustManagementData`
        :return: com.vmware.nsx.model.TrustManagementData
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
class UiViews(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ui_views'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UiViewsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               view,
               ):
        """
        Creates a new View.

        :type  view: :class:`com.vmware.nsx.model_client.View`
        :param view: (required)
        :rtype: :class:`com.vmware.nsx.model_client.View`
        :return: com.vmware.nsx.model.View
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
                            'view': view,
                            })

    def delete(self,
               view_id,
               ):
        """
        Delete View

        :type  view_id: :class:`str`
        :param view_id: (required)
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
                            'view_id': view_id,
                            })

    def get(self,
            tag=None,
            view_ids=None,
            widget_id=None,
            ):
        """
        If no query params are specified then all the views entitled for the
        user are returned. The views to which a user is entitled to include the
        views created by the user and the shared views.

        :type  tag: :class:`str` or ``None``
        :param tag: The tag for which associated views to be queried. (optional)
        :type  view_ids: :class:`str` or ``None``
        :param view_ids: Ids of the Views (optional)
        :type  widget_id: :class:`str` or ``None``
        :param widget_id: Id of widget configuration (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ViewList`
        :return: com.vmware.nsx.model.ViewList
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
                            'tag': tag,
                            'view_ids': view_ids,
                            'widget_id': widget_id,
                            })

    def get_0(self,
              view_id,
              ):
        """
        Returns Information about a specific View.

        :type  view_id: :class:`str`
        :param view_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.View`
        :return: com.vmware.nsx.model.View
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
        return self._invoke('get_0',
                            {
                            'view_id': view_id,
                            })

    def update(self,
               view_id,
               view,
               ):
        """
        Update View

        :type  view_id: :class:`str`
        :param view_id: (required)
        :type  view: :class:`com.vmware.nsx.model_client.View`
        :param view: (required)
        :rtype: :class:`com.vmware.nsx.model_client.View`
        :return: com.vmware.nsx.model.View
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
                            'view_id': view_id,
                            'view': view,
                            })
class Upgrade(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.upgrade'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpgradeStub)
        self._VAPI_OPERATION_IDS = {}


    def abortpreupgradechecks(self):
        """
        Aborts execution of pre-upgrade checks if already in progress. Halts
        the execution of checks awaiting execution at this point and makes
        best-effort attempts to stop checks already in execution. Returns
        without action if execution of pre-upgrade checks is not in progress.


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
        return self._invoke('abortpreupgradechecks', None)

    def executepostupgradechecks(self,
                                 component_type,
                                 ):
        """
        Run pre-defined checks to identify issues after upgrade of a component.
        The results of the checks are added to the respective upgrade units
        aggregate-info. The progress and status of post-upgrade checks is part
        of aggregate-info of individual upgrade unit groups. Returns HTTP
        status 500 with error code 30953 if execution of post-upgrade checks is
        already in progress.

        :type  component_type: :class:`str`
        :param component_type: (required)
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
        return self._invoke('executepostupgradechecks',
                            {
                            'component_type': component_type,
                            })

    def executepreupgradechecks(self,
                                component_type=None,
                                cursor=None,
                                included_fields=None,
                                page_size=None,
                                sort_ascending=None,
                                sort_by=None,
                                ):
        """
        Run pre-defined checks to identify potential issues which can be
        encountered during an upgrade or can cause an upgrade to fail. The
        results of the checks are added to the respective upgrade units
        aggregate-info. The progress and status of operation is part of upgrade
        status summary of individual components. Returns HTTP status 500 with
        error code 30953 if execution of pre-upgrade checks is already in
        progress.

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
        return self._invoke('executepreupgradechecks',
                            {
                            'component_type': component_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def upgradeuc(self):
        """
        Upgrade the upgrade coordinator module itself. This call is invoked
        after user uploads an upgrade bundle. Once this call is invoked,
        upgrade coordinator stops and gets restarted and target version upgrade
        coordinator module comes up after restart.


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
        return self._invoke('upgradeuc', None)
class _AssociationsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'associated_resource_type': type.StringType(),
            'resource_id': type.StringType(),
            'resource_type': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'fetch_ancestors': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/associations',
            path_variables={
            },
            query_parameters={
                'associated_resource_type': 'associated_resource_type',
                'resource_id': 'resource_id',
                'resource_type': 'resource_type',
                'cursor': 'cursor',
                'fetch_ancestors': 'fetch_ancestors',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'AssociationListResult'),
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
            self, iface_name='com.vmware.nsx.associations',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _BatchStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'batch_request': type.ReferenceType('com.vmware.nsx.model_client', 'BatchRequest'),
            'atomic': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/batch',
            request_body_parameter='batch_request',
            path_variables={
            },
            query_parameters={
                'atomic': 'atomic',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BatchResponse'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.batch',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _BridgeClustersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'bridge_cluster': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeCluster'),
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
            url_template='/api/v1/bridge-clusters',
            request_body_parameter='bridge_cluster',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'bridgecluster_id': type.StringType(),
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
            url_template='/api/v1/bridge-clusters/{bridgecluster-id}',
            path_variables={
                'bridgecluster_id': 'bridgecluster-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'bridgecluster_id': type.StringType(),
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
            url_template='/api/v1/bridge-clusters/{bridgecluster-id}',
            path_variables={
                'bridgecluster_id': 'bridgecluster-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            url_template='/api/v1/bridge-clusters',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'bridgecluster_id': type.StringType(),
            'bridge_cluster': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeCluster'),
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
            url_template='/api/v1/bridge-clusters/{bridgecluster-id}',
            request_body_parameter='bridge_cluster',
            path_variables={
                'bridgecluster_id': 'bridgecluster-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeCluster'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeCluster'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeClusterListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeCluster'),
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
            self, iface_name='com.vmware.nsx.bridge_clusters',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _BridgeEndpointProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'bridge_endpoint_profile': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpointProfile'),
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
            url_template='/api/v1/bridge-endpoint-profiles',
            request_body_parameter='bridge_endpoint_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'bridgeendpointprofile_id': type.StringType(),
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
            url_template='/api/v1/bridge-endpoint-profiles/{bridgeendpointprofile-id}',
            path_variables={
                'bridgeendpointprofile_id': 'bridgeendpointprofile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'bridgeendpointprofile_id': type.StringType(),
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
            url_template='/api/v1/bridge-endpoint-profiles/{bridgeendpointprofile-id}',
            path_variables={
                'bridgeendpointprofile_id': 'bridgeendpointprofile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'edge_cluster_id': type.OptionalType(type.StringType()),
            'failover_mode': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/bridge-endpoint-profiles',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'edge_cluster_id': 'edge_cluster_id',
                'failover_mode': 'failover_mode',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'bridgeendpointprofile_id': type.StringType(),
            'bridge_endpoint_profile': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpointProfile'),
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
            url_template='/api/v1/bridge-endpoint-profiles/{bridgeendpointprofile-id}',
            request_body_parameter='bridge_endpoint_profile',
            path_variables={
                'bridgeendpointprofile_id': 'bridgeendpointprofile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpointProfile'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpointProfile'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpointProfileListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpointProfile'),
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
            self, iface_name='com.vmware.nsx.bridge_endpoint_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _BridgeEndpointsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'bridge_endpoint': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpoint'),
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
            url_template='/api/v1/bridge-endpoints',
            request_body_parameter='bridge_endpoint',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'bridgeendpoint_id': type.StringType(),
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
            url_template='/api/v1/bridge-endpoints/{bridgeendpoint-id}',
            path_variables={
                'bridgeendpoint_id': 'bridgeendpoint-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'bridgeendpoint_id': type.StringType(),
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
            url_template='/api/v1/bridge-endpoints/{bridgeendpoint-id}',
            path_variables={
                'bridgeendpoint_id': 'bridgeendpoint-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'bridge_cluster_id': type.OptionalType(type.StringType()),
            'bridge_endpoint_profile_id': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'logical_switch_id': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'vlan_transport_zone_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/bridge-endpoints',
            path_variables={
            },
            query_parameters={
                'bridge_cluster_id': 'bridge_cluster_id',
                'bridge_endpoint_profile_id': 'bridge_endpoint_profile_id',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'logical_switch_id': 'logical_switch_id',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'vlan_transport_zone_id': 'vlan_transport_zone_id',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'bridgeendpoint_id': type.StringType(),
            'bridge_endpoint': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpoint'),
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
            url_template='/api/v1/bridge-endpoints/{bridgeendpoint-id}',
            request_body_parameter='bridge_endpoint',
            path_variables={
                'bridgeendpoint_id': 'bridgeendpoint-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpoint'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpoint'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpointListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'BridgeEndpoint'),
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
            self, iface_name='com.vmware.nsx.bridge_endpoints',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ClusterStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for backuptoremote operation
        backuptoremote_input_type = type.StructType('operation-input', {})
        backuptoremote_error_dict = {
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
        backuptoremote_input_value_validator_list = [
        ]
        backuptoremote_output_validator_list = [
        ]
        backuptoremote_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/cluster?action=backup_to_remote',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
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
            url_template='/api/v1/cluster/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
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
            url_template='/api/v1/cluster/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
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
            url_template='/api/v1/cluster',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
        })
        get_0_error_dict = {
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
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/cluster/{node-id}',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get_1 operation
        get_1_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        get_1_error_dict = {
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
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
        get_1_input_value_validator_list = [
        ]
        get_1_output_validator_list = [
        ]
        get_1_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/cluster/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for joincluster operation
        joincluster_input_type = type.StructType('operation-input', {
            'join_cluster_parameters': type.ReferenceType('com.vmware.nsx.model_client', 'JoinClusterParameters'),
        })
        joincluster_error_dict = {
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
        joincluster_input_value_validator_list = [
        ]
        joincluster_output_validator_list = [
        ]
        joincluster_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/cluster?action=join_cluster',
            request_body_parameter='join_cluster_parameters',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for removenode operation
        removenode_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'force': type.OptionalType(type.StringType()),
            'graceful_shutdown': type.OptionalType(type.StringType()),
            'ignore_repository_ip_check': type.OptionalType(type.StringType()),
        })
        removenode_error_dict = {
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
        removenode_input_value_validator_list = [
        ]
        removenode_output_validator_list = [
        ]
        removenode_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/cluster/{node-id}?action=remove_node',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
                'force': 'force',
                'graceful_shutdown': 'graceful-shutdown',
                'ignore_repository_ip_check': 'ignore-repository-ip-check',
            },
            content_type='application/json'
        )

        # properties for summarizeinventorytoremote operation
        summarizeinventorytoremote_input_type = type.StructType('operation-input', {})
        summarizeinventorytoremote_error_dict = {
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
        summarizeinventorytoremote_input_value_validator_list = [
        ]
        summarizeinventorytoremote_output_validator_list = [
        ]
        summarizeinventorytoremote_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/cluster?action=summarize_inventory_to_remote',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
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
            url_template='/api/v1/cluster/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'backuptoremote': {
                'input_type': backuptoremote_input_type,
                'output_type': type.VoidType(),
                'errors': backuptoremote_error_dict,
                'input_value_validator_list': backuptoremote_input_value_validator_list,
                'output_validator_list': backuptoremote_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.VoidType(),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ClusterConfig'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ClusterNodeInfo'),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_1': {
                'input_type': get_1_input_type,
                'output_type': type.VoidType(),
                'errors': get_1_error_dict,
                'input_value_validator_list': get_1_input_value_validator_list,
                'output_validator_list': get_1_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'joincluster': {
                'input_type': joincluster_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ClusterConfiguration'),
                'errors': joincluster_error_dict,
                'input_value_validator_list': joincluster_input_value_validator_list,
                'output_validator_list': joincluster_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'removenode': {
                'input_type': removenode_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ClusterConfiguration'),
                'errors': removenode_error_dict,
                'input_value_validator_list': removenode_input_value_validator_list,
                'output_validator_list': removenode_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'summarizeinventorytoremote': {
                'input_type': summarizeinventorytoremote_input_type,
                'output_type': type.VoidType(),
                'errors': summarizeinventorytoremote_error_dict,
                'input_value_validator_list': summarizeinventorytoremote_input_value_validator_list,
                'output_validator_list': summarizeinventorytoremote_output_validator_list,
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
            'backuptoremote': backuptoremote_rest_metadata,
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
            'get_1': get_1_rest_metadata,
            'joincluster': joincluster_rest_metadata,
            'removenode': removenode_rest_metadata,
            'summarizeinventorytoremote': summarizeinventorytoremote_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.cluster',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ClusterProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'cluster_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'ClusterProfile')]),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/cluster-profiles',
            request_body_parameter='cluster_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'cluster_profile_id': type.StringType(),
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
            url_template='/api/v1/cluster-profiles/{cluster-profile-id}',
            path_variables={
                'cluster_profile_id': 'cluster-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster_profile_id': type.StringType(),
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
            url_template='/api/v1/cluster-profiles/{cluster-profile-id}',
            path_variables={
                'cluster_profile_id': 'cluster-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'include_system_owned': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'resource_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/cluster-profiles',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'include_system_owned': 'include_system_owned',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'resource_type': 'resource_type',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'cluster_profile_id': type.StringType(),
            'cluster_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'ClusterProfile')]),
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
            url_template='/api/v1/cluster-profiles/{cluster-profile-id}',
            request_body_parameter='cluster_profile',
            path_variables={
                'cluster_profile_id': 'cluster-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'ClusterProfile')]),
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
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'ClusterProfile')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ClusterProfileListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'ClusterProfile')]),
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
            self, iface_name='com.vmware.nsx.cluster_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ComputeCollectionTransportNodeTemplatesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'compute_collection_transport_node_template': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionTransportNodeTemplate'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/compute-collection-transport-node-templates',
            request_body_parameter='compute_collection_transport_node_template',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'template_id': type.StringType(),
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
            url_template='/api/v1/compute-collection-transport-node-templates/{template-id}',
            path_variables={
                'template_id': 'template-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'template_id': type.StringType(),
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
            url_template='/api/v1/compute-collection-transport-node-templates/{template-id}',
            path_variables={
                'template_id': 'template-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'compute_collection_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/compute-collection-transport-node-templates',
            path_variables={
            },
            query_parameters={
                'compute_collection_id': 'compute_collection_id',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'template_id': type.StringType(),
            'compute_collection_transport_node_template': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionTransportNodeTemplate'),
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
            url_template='/api/v1/compute-collection-transport-node-templates/{template-id}',
            request_body_parameter='compute_collection_transport_node_template',
            path_variables={
                'template_id': 'template-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionTransportNodeTemplate'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionTransportNodeTemplate'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeTemplateListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionTransportNodeTemplate'),
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
            self, iface_name='com.vmware.nsx.compute_collection_transport_node_templates',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _EdgeClustersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'edge_cluster': type.ReferenceType('com.vmware.nsx.model_client', 'EdgeCluster'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/edge-clusters',
            request_body_parameter='edge_cluster',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'edge_cluster_id': type.StringType(),
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
            url_template='/api/v1/edge-clusters/{edge-cluster-id}',
            path_variables={
                'edge_cluster_id': 'edge-cluster-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'edge_cluster_id': type.StringType(),
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
            url_template='/api/v1/edge-clusters/{edge-cluster-id}',
            path_variables={
                'edge_cluster_id': 'edge-cluster-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/edge-clusters',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for replacetransportnode operation
        replacetransportnode_input_type = type.StructType('operation-input', {
            'edge_cluster_id': type.StringType(),
            'edge_cluster_member_transport_node': type.ReferenceType('com.vmware.nsx.model_client', 'EdgeClusterMemberTransportNode'),
        })
        replacetransportnode_error_dict = {
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
        replacetransportnode_input_value_validator_list = [
        ]
        replacetransportnode_output_validator_list = [
            HasFieldsOfValidator()
        ]
        replacetransportnode_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/edge-clusters/{edge-cluster-id}?action=replace_transport_node',
            request_body_parameter='edge_cluster_member_transport_node',
            path_variables={
                'edge_cluster_id': 'edge-cluster-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'edge_cluster_id': type.StringType(),
            'edge_cluster': type.ReferenceType('com.vmware.nsx.model_client', 'EdgeCluster'),
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
            url_template='/api/v1/edge-clusters/{edge-cluster-id}',
            request_body_parameter='edge_cluster',
            path_variables={
                'edge_cluster_id': 'edge-cluster-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'EdgeCluster'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'EdgeCluster'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'EdgeClusterListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'replacetransportnode': {
                'input_type': replacetransportnode_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'EdgeCluster'),
                'errors': replacetransportnode_error_dict,
                'input_value_validator_list': replacetransportnode_input_value_validator_list,
                'output_validator_list': replacetransportnode_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'EdgeCluster'),
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
            'replacetransportnode': replacetransportnode_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.edge_clusters',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ErrorResolverStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'error_id': type.StringType(),
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
            url_template='/api/v1/error-resolver/{error_id}',
            path_variables={
                'error_id': 'error_id',
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
            url_template='/api/v1/error-resolver',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for resolveerror operation
        resolveerror_input_type = type.StructType('operation-input', {
            'error_resolver_metadata_list': type.ReferenceType('com.vmware.nsx.model_client', 'ErrorResolverMetadataList'),
        })
        resolveerror_error_dict = {
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
        resolveerror_input_value_validator_list = [
        ]
        resolveerror_output_validator_list = [
        ]
        resolveerror_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/error-resolver?action=resolve_error',
            request_body_parameter='error_resolver_metadata_list',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ErrorResolverInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ErrorResolverInfoList'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'resolveerror': {
                'input_type': resolveerror_input_type,
                'output_type': type.VoidType(),
                'errors': resolveerror_error_dict,
                'input_value_validator_list': resolveerror_input_value_validator_list,
                'output_validator_list': resolveerror_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'resolveerror': resolveerror_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.error_resolver',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _FailureDomainsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'failure_domain': type.ReferenceType('com.vmware.nsx.model_client', 'FailureDomain'),
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
            url_template='/api/v1/failure-domains',
            request_body_parameter='failure_domain',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'failure_domain_id': type.StringType(),
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
            url_template='/api/v1/failure-domains/{failure-domain-id}',
            path_variables={
                'failure_domain_id': 'failure-domain-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'failure_domain_id': type.StringType(),
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
            url_template='/api/v1/failure-domains/{failure-domain-id}',
            path_variables={
                'failure_domain_id': 'failure-domain-id',
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
            url_template='/api/v1/failure-domains',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'failure_domain_id': type.StringType(),
            'failure_domain': type.ReferenceType('com.vmware.nsx.model_client', 'FailureDomain'),
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
            url_template='/api/v1/failure-domains/{failure-domain-id}',
            request_body_parameter='failure_domain',
            path_variables={
                'failure_domain_id': 'failure-domain-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FailureDomain'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FailureDomain'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FailureDomainListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FailureDomain'),
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
            self, iface_name='com.vmware.nsx.failure_domains',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _GlobalConfigsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'config_type': type.StringType(),
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
            url_template='/api/v1/global-configs/{config-type}',
            path_variables={
                'config_type': 'config-type',
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/global-configs',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for resyncconfig operation
        resyncconfig_input_type = type.StructType('operation-input', {
            'config_type': type.StringType(),
            'global_configs': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'GlobalConfigs')]),
        })
        resyncconfig_error_dict = {
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
        resyncconfig_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        resyncconfig_output_validator_list = [
            HasFieldsOfValidator()
        ]
        resyncconfig_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/global-configs/{config-type}?action=resync_config',
            request_body_parameter='global_configs',
            path_variables={
                'config_type': 'config-type',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'config_type': type.StringType(),
            'global_configs': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'GlobalConfigs')]),
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
            url_template='/api/v1/global-configs/{config-type}',
            request_body_parameter='global_configs',
            path_variables={
                'config_type': 'config-type',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'GlobalConfigs')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'GlobalConfigsListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'resyncconfig': {
                'input_type': resyncconfig_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'GlobalConfigs')]),
                'errors': resyncconfig_error_dict,
                'input_value_validator_list': resyncconfig_input_value_validator_list,
                'output_validator_list': resyncconfig_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'GlobalConfigs')]),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'resyncconfig': resyncconfig_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.global_configs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _HostSwitchProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'base_host_switch_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseHostSwitchProfile')]),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/host-switch-profiles',
            request_body_parameter='base_host_switch_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'host_switch_profile_id': type.StringType(),
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
            url_template='/api/v1/host-switch-profiles/{host-switch-profile-id}',
            path_variables={
                'host_switch_profile_id': 'host-switch-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'host_switch_profile_id': type.StringType(),
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
            url_template='/api/v1/host-switch-profiles/{host-switch-profile-id}',
            path_variables={
                'host_switch_profile_id': 'host-switch-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'hostswitch_profile_type': type.OptionalType(type.StringType()),
            'include_system_owned': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'uplink_teaming_policy_name': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/host-switch-profiles',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'hostswitch_profile_type': 'hostswitch_profile_type',
                'include_system_owned': 'include_system_owned',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'uplink_teaming_policy_name': 'uplink_teaming_policy_name',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'host_switch_profile_id': type.StringType(),
            'base_host_switch_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseHostSwitchProfile')]),
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
            url_template='/api/v1/host-switch-profiles/{host-switch-profile-id}',
            request_body_parameter='base_host_switch_profile',
            path_variables={
                'host_switch_profile_id': 'host-switch-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseHostSwitchProfile')]),
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
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseHostSwitchProfile')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'HostSwitchProfilesListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseHostSwitchProfile')]),
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
            self, iface_name='com.vmware.nsx.host_switch_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _IpSetsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ip_set': type.ReferenceType('com.vmware.nsx.model_client', 'IPSet'),
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
            url_template='/api/v1/ip-sets',
            request_body_parameter='ip_set',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for create_0 operation
        create_0_input_type = type.StructType('operation-input', {
            'ip_set_id': type.StringType(),
            'ip_address_element': type.ReferenceType('com.vmware.nsx.model_client', 'IPAddressElement'),
            'action': type.StringType(),
        })
        create_0_error_dict = {
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
        create_0_input_value_validator_list = [
        ]
        create_0_output_validator_list = [
        ]
        create_0_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/ip-sets/{ip-set-id}',
            request_body_parameter='ip_address_element',
            path_variables={
                'ip_set_id': 'ip-set-id',
            },
            query_parameters={
                'action': 'action',
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'ip_set_id': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/ip-sets/{ip-set-id}',
            path_variables={
                'ip_set_id': 'ip-set-id',
            },
            query_parameters={
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'ip_set_id': type.StringType(),
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
            url_template='/api/v1/ip-sets/{ip-set-id}',
            path_variables={
                'ip_set_id': 'ip-set-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            url_template='/api/v1/ip-sets',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'ip_set_id': type.StringType(),
            'ip_set': type.ReferenceType('com.vmware.nsx.model_client', 'IPSet'),
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
            url_template='/api/v1/ip-sets/{ip-set-id}',
            request_body_parameter='ip_set',
            path_variables={
                'ip_set_id': 'ip-set-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IPSet'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create_0': {
                'input_type': create_0_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IPAddressElement'),
                'errors': create_0_error_dict,
                'input_value_validator_list': create_0_input_value_validator_list,
                'output_validator_list': create_0_output_validator_list,
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IPSet'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IPSetListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IPSet'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'create_0': create_0_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.ip_sets',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _IpfixCollectorProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ipfix_collector_upm_profile': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorUpmProfile'),
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
            url_template='/api/v1/ipfix-collector-profiles',
            request_body_parameter='ipfix_collector_upm_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'ipfix_collector_profile_id': type.StringType(),
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
            url_template='/api/v1/ipfix-collector-profiles/{ipfix-collector-profile-id}',
            path_variables={
                'ipfix_collector_profile_id': 'ipfix-collector-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'ipfix_collector_profile_id': type.StringType(),
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
            url_template='/api/v1/ipfix-collector-profiles/{ipfix-collector-profile-id}',
            path_variables={
                'ipfix_collector_profile_id': 'ipfix-collector-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'profile_types': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/ipfix-collector-profiles',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'profile_types': 'profile_types',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'ipfix_collector_profile_id': type.StringType(),
            'ipfix_collector_upm_profile': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorUpmProfile'),
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
            url_template='/api/v1/ipfix-collector-profiles/{ipfix-collector-profile-id}',
            request_body_parameter='ipfix_collector_upm_profile',
            path_variables={
                'ipfix_collector_profile_id': 'ipfix-collector-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorUpmProfile'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorUpmProfile'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorUpmProfileListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixCollectorUpmProfile'),
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
            self, iface_name='com.vmware.nsx.ipfix_collector_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _IpfixObsPointsStub(ApiInterfaceStub):
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
            url_template='/api/v1/ipfix-obs-points',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixObsPointsListResult'),
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
            self, iface_name='com.vmware.nsx.ipfix_obs_points',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _IpfixProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ipfix_upm_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixUpmProfile')]),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/ipfix-profiles',
            request_body_parameter='ipfix_upm_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'ipfix_profile_id': type.StringType(),
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
            url_template='/api/v1/ipfix-profiles/{ipfix-profile-id}',
            path_variables={
                'ipfix_profile_id': 'ipfix-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'ipfix_profile_id': type.StringType(),
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
            url_template='/api/v1/ipfix-profiles/{ipfix-profile-id}',
            path_variables={
                'ipfix_profile_id': 'ipfix-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'applied_to_entity_id': type.OptionalType(type.StringType()),
            'applied_to_entity_type': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'profile_types': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/ipfix-profiles',
            path_variables={
            },
            query_parameters={
                'applied_to_entity_id': 'applied_to_entity_id',
                'applied_to_entity_type': 'applied_to_entity_type',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'profile_types': 'profile_types',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'ipfix_profile_id': type.StringType(),
            'ipfix_upm_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixUpmProfile')]),
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
            url_template='/api/v1/ipfix-profiles/{ipfix-profile-id}',
            request_body_parameter='ipfix_upm_profile',
            path_variables={
                'ipfix_profile_id': 'ipfix-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixUpmProfile')]),
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
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixUpmProfile')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'IpfixUpmProfileListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'IpfixUpmProfile')]),
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
            self, iface_name='com.vmware.nsx.ipfix_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _LicensesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'license': type.ReferenceType('com.vmware.nsx.model_client', 'License'),
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
            url_template='/api/v1/licenses',
            request_body_parameter='license',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'license_key': type.StringType(),
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
            url_template='/api/v1/licenses/{license-key}',
            path_variables={
                'license_key': 'license-key',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete_0 operation
        delete_0_input_type = type.StructType('operation-input', {
            'license': type.ReferenceType('com.vmware.nsx.model_client', 'License'),
        })
        delete_0_error_dict = {
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
        delete_0_input_value_validator_list = [
        ]
        delete_0_output_validator_list = [
        ]
        delete_0_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/licenses?action=delete',
            request_body_parameter='license',
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
            url_template='/api/v1/license',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for getlicensebykey operation
        getlicensebykey_input_type = type.StructType('operation-input', {
            'license_key': type.StringType(),
        })
        getlicensebykey_error_dict = {
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
        getlicensebykey_input_value_validator_list = [
        ]
        getlicensebykey_output_validator_list = [
        ]
        getlicensebykey_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/licenses/{license-key}',
            path_variables={
                'license_key': 'license-key',
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
            url_template='/api/v1/licenses',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'license': type.ReferenceType('com.vmware.nsx.model_client', 'License'),
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
            url_template='/api/v1/license',
            request_body_parameter='license',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'License'),
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
            'delete_0': {
                'input_type': delete_0_input_type,
                'output_type': type.VoidType(),
                'errors': delete_0_error_dict,
                'input_value_validator_list': delete_0_input_value_validator_list,
                'output_validator_list': delete_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'License'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'getlicensebykey': {
                'input_type': getlicensebykey_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'License'),
                'errors': getlicensebykey_error_dict,
                'input_value_validator_list': getlicensebykey_input_value_validator_list,
                'output_validator_list': getlicensebykey_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LicensesListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'License'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'delete_0': delete_0_rest_metadata,
            'get': get_rest_metadata,
            'getlicensebykey': getlicensebykey_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.licenses',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _LogicalPortsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'logical_port': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPort'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/logical-ports',
            request_body_parameter='logical_port',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'lport_id': type.StringType(),
            'detach': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/logical-ports/{lport-id}',
            path_variables={
                'lport_id': 'lport-id',
            },
            query_parameters={
                'detach': 'detach',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'lport_id': type.StringType(),
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
            url_template='/api/v1/logical-ports/{lport-id}',
            path_variables={
                'lport_id': 'lport-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'attachment_id': type.OptionalType(type.StringType()),
            'attachment_type': type.OptionalType(type.StringType()),
            'bridge_cluster_id': type.OptionalType(type.StringType()),
            'container_ports_only': type.OptionalType(type.BooleanType()),
            'cursor': type.OptionalType(type.StringType()),
            'diagnostic': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'logical_switch_id': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'parent_vif_id': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'switching_profile_id': type.OptionalType(type.StringType()),
            'transport_node_id': type.OptionalType(type.StringType()),
            'transport_zone_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/logical-ports',
            path_variables={
            },
            query_parameters={
                'attachment_id': 'attachment_id',
                'attachment_type': 'attachment_type',
                'bridge_cluster_id': 'bridge_cluster_id',
                'container_ports_only': 'container_ports_only',
                'cursor': 'cursor',
                'diagnostic': 'diagnostic',
                'included_fields': 'included_fields',
                'logical_switch_id': 'logical_switch_id',
                'page_size': 'page_size',
                'parent_vif_id': 'parent_vif_id',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'switching_profile_id': 'switching_profile_id',
                'transport_node_id': 'transport_node_id',
                'transport_zone_id': 'transport_zone_id',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'lport_id': type.StringType(),
            'logical_port': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPort'),
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
            url_template='/api/v1/logical-ports/{lport-id}',
            request_body_parameter='logical_port',
            path_variables={
                'lport_id': 'lport-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPort'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPort'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPortListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPort'),
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
            self, iface_name='com.vmware.nsx.logical_ports',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _LogicalRouterPortsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'logical_router_port': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouterPort')]),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/logical-router-ports',
            request_body_parameter='logical_router_port',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'logical_router_port_id': type.StringType(),
            'cascade_delete_linked_ports': type.OptionalType(type.BooleanType()),
            'force': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/logical-router-ports/{logical-router-port-id}',
            path_variables={
                'logical_router_port_id': 'logical-router-port-id',
            },
            query_parameters={
                'cascade_delete_linked_ports': 'cascade_delete_linked_ports',
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'logical_router_port_id': type.StringType(),
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
            url_template='/api/v1/logical-router-ports/{logical-router-port-id}',
            path_variables={
                'logical_router_port_id': 'logical-router-port-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'logical_router_id': type.OptionalType(type.StringType()),
            'logical_switch_id': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'resource_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/logical-router-ports',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'logical_router_id': 'logical_router_id',
                'logical_switch_id': 'logical_switch_id',
                'page_size': 'page_size',
                'resource_type': 'resource_type',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'logical_router_port_id': type.StringType(),
            'logical_router_port': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouterPort')]),
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
            url_template='/api/v1/logical-router-ports/{logical-router-port-id}',
            request_body_parameter='logical_router_port',
            path_variables={
                'logical_router_port_id': 'logical-router-port-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouterPort')]),
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
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouterPort')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouterPortListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouterPort')]),
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
            self, iface_name='com.vmware.nsx.logical_router_ports',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _LogicalRoutersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'logical_router': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouter'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/logical-routers',
            request_body_parameter='logical_router',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'cascade_delete_linked_ports': type.OptionalType(type.BooleanType()),
            'force': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/logical-routers/{logical-router-id}',
            path_variables={
                'logical_router_id': 'logical-router-id',
            },
            query_parameters={
                'cascade_delete_linked_ports': 'cascade_delete_linked_ports',
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
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
            url_template='/api/v1/logical-routers/{logical-router-id}',
            path_variables={
                'logical_router_id': 'logical-router-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'router_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/logical-routers',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'router_type': 'router_type',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for reallocate operation
        reallocate_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'service_router_allocation_config': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceRouterAllocationConfig'),
        })
        reallocate_error_dict = {
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
        reallocate_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        reallocate_output_validator_list = [
            HasFieldsOfValidator()
        ]
        reallocate_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/logical-routers/{logical-router-id}?action=reallocate',
            request_body_parameter='service_router_allocation_config',
            path_variables={
                'logical_router_id': 'logical-router-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for reprocess operation
        reprocess_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
        })
        reprocess_error_dict = {
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
        reprocess_input_value_validator_list = [
        ]
        reprocess_output_validator_list = [
        ]
        reprocess_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/logical-routers/{logical-router-id}?action=reprocess',
            path_variables={
                'logical_router_id': 'logical-router-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'logical_router': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouter'),
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
            url_template='/api/v1/logical-routers/{logical-router-id}',
            request_body_parameter='logical_router',
            path_variables={
                'logical_router_id': 'logical-router-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouter'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouter'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouterListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reallocate': {
                'input_type': reallocate_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouter'),
                'errors': reallocate_error_dict,
                'input_value_validator_list': reallocate_input_value_validator_list,
                'output_validator_list': reallocate_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reprocess': {
                'input_type': reprocess_input_type,
                'output_type': type.VoidType(),
                'errors': reprocess_error_dict,
                'input_value_validator_list': reprocess_input_value_validator_list,
                'output_validator_list': reprocess_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalRouter'),
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
            'reallocate': reallocate_rest_metadata,
            'reprocess': reprocess_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.logical_routers',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _LogicalSwitchesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'logical_switch': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalSwitch'),
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
            url_template='/api/v1/logical-switches',
            request_body_parameter='logical_switch',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'lswitch_id': type.StringType(),
            'cascade': type.OptionalType(type.BooleanType()),
            'detach': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/logical-switches/{lswitch-id}',
            path_variables={
                'lswitch_id': 'lswitch-id',
            },
            query_parameters={
                'cascade': 'cascade',
                'detach': 'detach',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'lswitch_id': type.StringType(),
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
            url_template='/api/v1/logical-switches/{lswitch-id}',
            path_variables={
                'lswitch_id': 'lswitch-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'diagnostic': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'switching_profile_id': type.OptionalType(type.StringType()),
            'transport_type': type.OptionalType(type.StringType()),
            'transport_zone_id': type.OptionalType(type.StringType()),
            'uplink_teaming_policy_name': type.OptionalType(type.StringType()),
            'vlan': type.OptionalType(type.IntegerType()),
            'vni': type.OptionalType(type.IntegerType()),
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
            url_template='/api/v1/logical-switches',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'diagnostic': 'diagnostic',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'switching_profile_id': 'switching_profile_id',
                'transport_type': 'transport_type',
                'transport_zone_id': 'transport_zone_id',
                'uplink_teaming_policy_name': 'uplink_teaming_policy_name',
                'vlan': 'vlan',
                'vni': 'vni',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'lswitch_id': type.StringType(),
            'logical_switch': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalSwitch'),
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
            url_template='/api/v1/logical-switches/{lswitch-id}',
            request_body_parameter='logical_switch',
            path_variables={
                'lswitch_id': 'lswitch-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalSwitch'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalSwitch'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalSwitchListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalSwitch'),
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
            self, iface_name='com.vmware.nsx.logical_switches',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _MacSetsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'm_AC_set': type.ReferenceType('com.vmware.nsx.model_client', 'MACSet'),
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
            url_template='/api/v1/mac-sets',
            request_body_parameter='m_AC_set',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'mac_set_id': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/mac-sets/{mac-set-id}',
            path_variables={
                'mac_set_id': 'mac-set-id',
            },
            query_parameters={
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'mac_set_id': type.StringType(),
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
            url_template='/api/v1/mac-sets/{mac-set-id}',
            path_variables={
                'mac_set_id': 'mac-set-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            url_template='/api/v1/mac-sets',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'mac_set_id': type.StringType(),
            'm_AC_set': type.ReferenceType('com.vmware.nsx.model_client', 'MACSet'),
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
            url_template='/api/v1/mac-sets/{mac-set-id}',
            request_body_parameter='m_AC_set',
            path_variables={
                'mac_set_id': 'mac-set-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MACSet'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MACSet'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MACSetListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MACSet'),
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
            self, iface_name='com.vmware.nsx.mac_sets',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ManualHealthChecksStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'manual_health_check': type.ReferenceType('com.vmware.nsx.model_client', 'ManualHealthCheck'),
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
            url_template='/api/v1/manual-health-checks',
            request_body_parameter='manual_health_check',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'manual_health_check_id': type.StringType(),
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
            url_template='/api/v1/manual-health-checks/{manual-health-check-id}',
            path_variables={
                'manual_health_check_id': 'manual-health-check-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'manual_health_check_id': type.StringType(),
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
            url_template='/api/v1/manual-health-checks/{manual-health-check-id}',
            path_variables={
                'manual_health_check_id': 'manual-health-check-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            url_template='/api/v1/manual-health-checks',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ManualHealthCheck'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ManualHealthCheck'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ManualHealthCheckListResult'),
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
            self, iface_name='com.vmware.nsx.manual_health_checks',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _MdProxiesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'metadata_proxy': type.ReferenceType('com.vmware.nsx.model_client', 'MetadataProxy'),
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
            url_template='/api/v1/md-proxies',
            request_body_parameter='metadata_proxy',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'proxy_id': type.StringType(),
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
            url_template='/api/v1/md-proxies/{proxy-id}',
            path_variables={
                'proxy_id': 'proxy-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'proxy_id': type.StringType(),
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
            url_template='/api/v1/md-proxies/{proxy-id}',
            path_variables={
                'proxy_id': 'proxy-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            url_template='/api/v1/md-proxies',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'proxy_id': type.StringType(),
            'metadata_proxy': type.ReferenceType('com.vmware.nsx.model_client', 'MetadataProxy'),
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
            url_template='/api/v1/md-proxies/{proxy-id}',
            request_body_parameter='metadata_proxy',
            path_variables={
                'proxy_id': 'proxy-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MetadataProxy'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MetadataProxy'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MetadataProxyListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MetadataProxy'),
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
            self, iface_name='com.vmware.nsx.md_proxies',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _MirrorSessionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'port_mirroring_session': type.ReferenceType('com.vmware.nsx.model_client', 'PortMirroringSession'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/mirror-sessions',
            request_body_parameter='port_mirroring_session',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'mirror_session_id': type.StringType(),
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
            url_template='/api/v1/mirror-sessions/{mirror-session-id}',
            path_variables={
                'mirror_session_id': 'mirror-session-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'mirror_session_id': type.StringType(),
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
            url_template='/api/v1/mirror-sessions/{mirror-session-id}',
            path_variables={
                'mirror_session_id': 'mirror-session-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/mirror-sessions',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'mirror_session_id': type.StringType(),
            'port_mirroring_session': type.ReferenceType('com.vmware.nsx.model_client', 'PortMirroringSession'),
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
            url_template='/api/v1/mirror-sessions/{mirror-session-id}',
            request_body_parameter='port_mirroring_session',
            path_variables={
                'mirror_session_id': 'mirror-session-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for verify operation
        verify_input_type = type.StructType('operation-input', {
            'mirror_session_id': type.StringType(),
        })
        verify_error_dict = {
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
        verify_input_value_validator_list = [
        ]
        verify_output_validator_list = [
        ]
        verify_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/mirror-sessions/{mirror-session-id}?action=verify',
            path_variables={
                'mirror_session_id': 'mirror-session-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PortMirroringSession'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PortMirroringSession'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PortMirroringSessionListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PortMirroringSession'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'verify': {
                'input_type': verify_input_type,
                'output_type': type.VoidType(),
                'errors': verify_error_dict,
                'input_value_validator_list': verify_input_value_validator_list,
                'output_validator_list': verify_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
            'verify': verify_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.mirror_sessions',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NetworkMigrationSpecsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'network_migration_spec': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'NetworkMigrationSpec')]),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/network-migration-specs',
            request_body_parameter='network_migration_spec',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'template_id': type.StringType(),
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
            url_template='/api/v1/network-migration-specs/{template-id}',
            path_variables={
                'template_id': 'template-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'template_id': type.StringType(),
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
            url_template='/api/v1/network-migration-specs/{template-id}',
            path_variables={
                'template_id': 'template-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'include_system_owned': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/network-migration-specs',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'include_system_owned': 'include_system_owned',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'type': 'type',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'template_id': type.StringType(),
            'network_migration_spec': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'NetworkMigrationSpec')]),
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
            url_template='/api/v1/network-migration-specs/{template-id}',
            request_body_parameter='network_migration_spec',
            path_variables={
                'template_id': 'template-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'NetworkMigrationSpec')]),
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
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'NetworkMigrationSpec')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NetworkMigrationSpecListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'NetworkMigrationSpec')]),
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
            self, iface_name='com.vmware.nsx.network_migration_specs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NodeStub(ApiInterfaceStub):
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
            url_template='/api/v1/node',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for restart operation
        restart_input_type = type.StructType('operation-input', {})
        restart_error_dict = {
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
        restart_input_value_validator_list = [
        ]
        restart_output_validator_list = [
        ]
        restart_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/node?action=restart',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for setsystemtime operation
        setsystemtime_input_type = type.StructType('operation-input', {
            'node_time': type.ReferenceType('com.vmware.nsx.model_client', 'NodeTime'),
        })
        setsystemtime_error_dict = {
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
        setsystemtime_input_value_validator_list = [
        ]
        setsystemtime_output_validator_list = [
        ]
        setsystemtime_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/node?action=set_system_time',
            request_body_parameter='node_time',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for shutdown operation
        shutdown_input_type = type.StructType('operation-input', {})
        shutdown_error_dict = {
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
        shutdown_input_value_validator_list = [
        ]
        shutdown_output_validator_list = [
        ]
        shutdown_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/node?action=shutdown',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'node_properties': type.ReferenceType('com.vmware.nsx.model_client', 'NodeProperties'),
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
            url_template='/api/v1/node',
            request_body_parameter='node_properties',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NodeProperties'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'restart': {
                'input_type': restart_input_type,
                'output_type': type.VoidType(),
                'errors': restart_error_dict,
                'input_value_validator_list': restart_input_value_validator_list,
                'output_validator_list': restart_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'setsystemtime': {
                'input_type': setsystemtime_input_type,
                'output_type': type.VoidType(),
                'errors': setsystemtime_error_dict,
                'input_value_validator_list': setsystemtime_input_value_validator_list,
                'output_validator_list': setsystemtime_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'shutdown': {
                'input_type': shutdown_input_type,
                'output_type': type.VoidType(),
                'errors': shutdown_error_dict,
                'input_value_validator_list': shutdown_input_value_validator_list,
                'output_validator_list': shutdown_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NodeProperties'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'restart': restart_rest_metadata,
            'setsystemtime': setsystemtime_rest_metadata,
            'shutdown': shutdown_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.node',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NormalizationsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'preferred_normalization_type': type.StringType(),
            'resource_id': type.StringType(),
            'resource_type': type.StringType(),
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
            url_template='/api/v1/normalizations',
            path_variables={
            },
            query_parameters={
                'preferred_normalization_type': 'preferred_normalization_type',
                'resource_id': 'resource_id',
                'resource_type': 'resource_type',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NormalizedResourceListResult'),
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
            self, iface_name='com.vmware.nsx.normalizations',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NotificationWatchersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'notification_watcher': type.ReferenceType('com.vmware.nsx.model_client', 'NotificationWatcher'),
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
            url_template='/api/v1/notification-watchers',
            request_body_parameter='notification_watcher',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'watcher_id': type.StringType(),
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
            url_template='/api/v1/notification-watchers/{watcher-id}',
            path_variables={
                'watcher_id': 'watcher-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'watcher_id': type.StringType(),
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
            url_template='/api/v1/notification-watchers/{watcher-id}',
            path_variables={
                'watcher_id': 'watcher-id',
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
            url_template='/api/v1/notification-watchers',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'watcher_id': type.StringType(),
            'notification_watcher': type.ReferenceType('com.vmware.nsx.model_client', 'NotificationWatcher'),
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
            url_template='/api/v1/notification-watchers/{watcher-id}',
            request_body_parameter='notification_watcher',
            path_variables={
                'watcher_id': 'watcher-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NotificationWatcher'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NotificationWatcher'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NotificationWatcherListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NotificationWatcher'),
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
            self, iface_name='com.vmware.nsx.notification_watchers',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NsGroupsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for addorremoveexpression operation
        addorremoveexpression_input_type = type.StructType('operation-input', {
            'ns_group_id': type.StringType(),
            'ns_group_expression_list': type.ReferenceType('com.vmware.nsx.model_client', 'NSGroupExpressionList'),
            'action': type.StringType(),
        })
        addorremoveexpression_error_dict = {
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
        addorremoveexpression_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        addorremoveexpression_output_validator_list = [
            HasFieldsOfValidator()
        ]
        addorremoveexpression_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/ns-groups/{ns-group-id}',
            request_body_parameter='ns_group_expression_list',
            path_variables={
                'ns_group_id': 'ns-group-id',
            },
            query_parameters={
                'action': 'action',
            },
            content_type='application/json'
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ns_group': type.ReferenceType('com.vmware.nsx.model_client', 'NSGroup'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/ns-groups',
            request_body_parameter='ns_group',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'ns_group_id': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/ns-groups/{ns-group-id}',
            path_variables={
                'ns_group_id': 'ns-group-id',
            },
            query_parameters={
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'ns_group_id': type.StringType(),
            'populate_references': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/ns-groups/{ns-group-id}',
            path_variables={
                'ns_group_id': 'ns-group-id',
            },
            query_parameters={
                'populate_references': 'populate_references',
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'member_types': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'populate_references': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/ns-groups',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'member_types': 'member_types',
                'page_size': 'page_size',
                'populate_references': 'populate_references',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'ns_group_id': type.StringType(),
            'ns_group': type.ReferenceType('com.vmware.nsx.model_client', 'NSGroup'),
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
            url_template='/api/v1/ns-groups/{ns-group-id}',
            request_body_parameter='ns_group',
            path_variables={
                'ns_group_id': 'ns-group-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'addorremoveexpression': {
                'input_type': addorremoveexpression_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSGroup'),
                'errors': addorremoveexpression_error_dict,
                'input_value_validator_list': addorremoveexpression_input_value_validator_list,
                'output_validator_list': addorremoveexpression_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSGroup'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSGroup'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSGroupListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSGroup'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'addorremoveexpression': addorremoveexpression_rest_metadata,
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.ns_groups',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NsProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ns_profile': type.ReferenceType('com.vmware.nsx.model_client', 'NSProfile'),
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
            url_template='/api/v1/ns-profiles',
            request_body_parameter='ns_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'ns_profile_id': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/ns-profiles/{ns-profile-id}',
            path_variables={
                'ns_profile_id': 'ns-profile-id',
            },
            query_parameters={
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'ns_profile_id': type.StringType(),
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
            url_template='/api/v1/ns-profiles/{ns-profile-id}',
            path_variables={
                'ns_profile_id': 'ns-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'attribute_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/ns-profiles',
            path_variables={
            },
            query_parameters={
                'attribute_type': 'attribute_type',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'ns_profile_id': type.StringType(),
            'ns_profile': type.ReferenceType('com.vmware.nsx.model_client', 'NSProfile'),
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
            url_template='/api/v1/ns-profiles/{ns-profile-id}',
            request_body_parameter='ns_profile',
            path_variables={
                'ns_profile_id': 'ns-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSProfile'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSProfile'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSProfileListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSProfile'),
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
            self, iface_name='com.vmware.nsx.ns_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NsServiceGroupsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ns_service_group': type.ReferenceType('com.vmware.nsx.model_client', 'NSServiceGroup'),
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
            url_template='/api/v1/ns-service-groups',
            request_body_parameter='ns_service_group',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'ns_service_group_id': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/ns-service-groups/{ns-service-group-id}',
            path_variables={
                'ns_service_group_id': 'ns-service-group-id',
            },
            query_parameters={
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'ns_service_group_id': type.StringType(),
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
            url_template='/api/v1/ns-service-groups/{ns-service-group-id}',
            path_variables={
                'ns_service_group_id': 'ns-service-group-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'default_service': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/ns-service-groups',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'default_service': 'default_service',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'ns_service_group_id': type.StringType(),
            'ns_service_group': type.ReferenceType('com.vmware.nsx.model_client', 'NSServiceGroup'),
        })
        update_error_dict = {
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
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/ns-service-groups/{ns-service-group-id}',
            request_body_parameter='ns_service_group',
            path_variables={
                'ns_service_group_id': 'ns-service-group-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSServiceGroup'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSServiceGroup'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSServiceGroupListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSServiceGroup'),
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
            self, iface_name='com.vmware.nsx.ns_service_groups',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NsServicesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'ns_service': type.ReferenceType('com.vmware.nsx.model_client', 'NSService'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/ns-services',
            request_body_parameter='ns_service',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'ns_service_id': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/ns-services/{ns-service-id}',
            path_variables={
                'ns_service_id': 'ns-service-id',
            },
            query_parameters={
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'ns_service_id': type.StringType(),
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
            url_template='/api/v1/ns-services/{ns-service-id}',
            path_variables={
                'ns_service_id': 'ns-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'default_service': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/ns-services',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'default_service': 'default_service',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'ns_service_id': type.StringType(),
            'ns_service': type.ReferenceType('com.vmware.nsx.model_client', 'NSService'),
        })
        update_error_dict = {
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
        update_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/ns-services/{ns-service-id}',
            request_body_parameter='ns_service',
            path_variables={
                'ns_service_id': 'ns-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSService'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSService'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSServiceListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NSService'),
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
            self, iface_name='com.vmware.nsx.ns_services',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ServiceConfigsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'service_config': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceConfig'),
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
            url_template='/api/v1/service-configs',
            request_body_parameter='service_config',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'config_set_id': type.StringType(),
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
            url_template='/api/v1/service-configs/{config-set-id}',
            path_variables={
                'config_set_id': 'config-set-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'config_set_id': type.StringType(),
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
            url_template='/api/v1/service-configs/{config-set-id}',
            path_variables={
                'config_set_id': 'config-set-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'profile_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/service-configs',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'profile_type': 'profile_type',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'config_set_id': type.StringType(),
            'service_config': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceConfig'),
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
            url_template='/api/v1/service-configs/{config-set-id}',
            request_body_parameter='service_config',
            path_variables={
                'config_set_id': 'config-set-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceConfig'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceConfig'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceConfigListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceConfig'),
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
            self, iface_name='com.vmware.nsx.service_configs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SwitchingProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'base_switching_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseSwitchingProfile')]),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/switching-profiles',
            request_body_parameter='base_switching_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'switching_profile_id': type.StringType(),
            'unbind': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/switching-profiles/{switching-profile-id}',
            path_variables={
                'switching_profile_id': 'switching-profile-id',
            },
            query_parameters={
                'unbind': 'unbind',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'switching_profile_id': type.StringType(),
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
            url_template='/api/v1/switching-profiles/{switching-profile-id}',
            path_variables={
                'switching_profile_id': 'switching-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'include_system_owned': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'switching_profile_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/switching-profiles',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'include_system_owned': 'include_system_owned',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'switching_profile_type': 'switching_profile_type',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'switching_profile_id': type.StringType(),
            'base_switching_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseSwitchingProfile')]),
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
            url_template='/api/v1/switching-profiles/{switching-profile-id}',
            request_body_parameter='base_switching_profile',
            path_variables={
                'switching_profile_id': 'switching-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseSwitchingProfile')]),
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
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseSwitchingProfile')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'SwitchingProfilesListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'BaseSwitchingProfile')]),
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
            self, iface_name='com.vmware.nsx.switching_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TasksStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'task_id': type.StringType(),
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
            url_template='/api/v1/tasks/{task-id}',
            path_variables={
                'task_id': 'task-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'request_uri': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'status': type.OptionalType(type.StringType()),
            'user': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/tasks',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'request_uri': 'request_uri',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'status': 'status',
                'user': 'user',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TaskProperties'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TaskListResult'),
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
            self, iface_name='com.vmware.nsx.tasks',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TraceflowsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'traceflow_request': type.ReferenceType('com.vmware.nsx.model_client', 'TraceflowRequest'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/traceflows',
            request_body_parameter='traceflow_request',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'traceflow_id': type.StringType(),
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
            url_template='/api/v1/traceflows/{traceflow-id}',
            path_variables={
                'traceflow_id': 'traceflow-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'traceflow_id': type.StringType(),
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
            url_template='/api/v1/traceflows/{traceflow-id}',
            path_variables={
                'traceflow_id': 'traceflow-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'lport_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/traceflows',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'lport_id': 'lport_id',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'Traceflow'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'Traceflow'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TraceflowListResult'),
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
            self, iface_name='com.vmware.nsx.traceflows',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TransportNodeCollectionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'transport_node_collection': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeCollection'),
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
            url_template='/api/v1/transport-node-collections',
            request_body_parameter='transport_node_collection',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'transport_node_collection_id': type.StringType(),
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
            url_template='/api/v1/transport-node-collections/{transport-node-collection-id}',
            path_variables={
                'transport_node_collection_id': 'transport-node-collection-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'transport_node_collection_id': type.StringType(),
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
            url_template='/api/v1/transport-node-collections/{transport-node-collection-id}',
            path_variables={
                'transport_node_collection_id': 'transport-node-collection-id',
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
            url_template='/api/v1/transport-node-collections',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'transport_node_collection_id': type.StringType(),
            'transport_node_collection': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeCollection'),
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
            url_template='/api/v1/transport-node-collections/{transport-node-collection-id}',
            request_body_parameter='transport_node_collection',
            path_variables={
                'transport_node_collection_id': 'transport-node-collection-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeCollection'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeCollection'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeCollectionListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeCollection'),
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
            self, iface_name='com.vmware.nsx.transport_node_collections',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TransportNodeProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'transport_node_profile': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeProfile'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-node-profiles',
            request_body_parameter='transport_node_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'transport_node_profile_id': type.StringType(),
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
            url_template='/api/v1/transport-node-profiles/{transport-node-profile-id}',
            path_variables={
                'transport_node_profile_id': 'transport-node-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'transport_node_profile_id': type.StringType(),
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
            url_template='/api/v1/transport-node-profiles/{transport-node-profile-id}',
            path_variables={
                'transport_node_profile_id': 'transport-node-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/transport-node-profiles',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'transport_node_profile_id': type.StringType(),
            'transport_node_profile': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeProfile'),
            'esx_mgmt_if_migration_dest': type.OptionalType(type.StringType()),
            'if_id': type.OptionalType(type.StringType()),
            'ping_ip': type.OptionalType(type.StringType()),
            'vnic': type.OptionalType(type.StringType()),
            'vnic_migration_dest': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/transport-node-profiles/{transport-node-profile-id}',
            request_body_parameter='transport_node_profile',
            path_variables={
                'transport_node_profile_id': 'transport-node-profile-id',
            },
            query_parameters={
                'esx_mgmt_if_migration_dest': 'esx_mgmt_if_migration_dest',
                'if_id': 'if_id',
                'ping_ip': 'ping_ip',
                'vnic': 'vnic',
                'vnic_migration_dest': 'vnic_migration_dest',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeProfile'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeProfile'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeProfileListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeProfile'),
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
            self, iface_name='com.vmware.nsx.transport_node_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TransportNodesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'transport_node': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNode'),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes',
            request_body_parameter='transport_node',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'transport_node_id': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
            'unprepare_host': type.OptionalType(type.BooleanType()),
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
            url_template='/api/v1/transport-nodes/{transport-node-id}',
            path_variables={
                'transport_node_id': 'transport-node-id',
            },
            query_parameters={
                'force': 'force',
                'unprepare_host': 'unprepare_host',
            },
            content_type='application/json'
        )

        # properties for deleteontransportnode operation
        deleteontransportnode_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        deleteontransportnode_error_dict = {
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
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
        deleteontransportnode_input_value_validator_list = [
        ]
        deleteontransportnode_output_validator_list = [
        ]
        deleteontransportnode_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/transport-nodes/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for disableflowcache operation
        disableflowcache_input_type = type.StructType('operation-input', {
            'transport_node_id': type.StringType(),
        })
        disableflowcache_error_dict = {
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
        disableflowcache_input_value_validator_list = [
        ]
        disableflowcache_output_validator_list = [
        ]
        disableflowcache_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes/{transport-node-id}?action=disable_flow_cache',
            path_variables={
                'transport_node_id': 'transport-node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for enableflowcache operation
        enableflowcache_input_type = type.StructType('operation-input', {
            'transport_node_id': type.StringType(),
        })
        enableflowcache_error_dict = {
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
        enableflowcache_input_value_validator_list = [
        ]
        enableflowcache_output_validator_list = [
        ]
        enableflowcache_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes/{transport-node-id}?action=enable_flow_cache',
            path_variables={
                'transport_node_id': 'transport-node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'transport_node_id': type.StringType(),
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
            url_template='/api/v1/transport-nodes/{transport-node-id}',
            path_variables={
                'transport_node_id': 'transport-node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for getontransportnode operation
        getontransportnode_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        getontransportnode_error_dict = {
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
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
        getontransportnode_input_value_validator_list = [
        ]
        getontransportnode_output_validator_list = [
        ]
        getontransportnode_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/transport-nodes/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'in_maintenance_mode': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'node_id': type.OptionalType(type.StringType()),
            'node_ip': type.OptionalType(type.StringType()),
            'node_types': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'transport_zone_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/transport-nodes',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'in_maintenance_mode': 'in_maintenance_mode',
                'included_fields': 'included_fields',
                'node_id': 'node_id',
                'node_ip': 'node_ip',
                'node_types': 'node_types',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'transport_zone_id': 'transport_zone_id',
            },
            content_type='application/json'
        )

        # properties for postontransportnode operation
        postontransportnode_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        postontransportnode_error_dict = {
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
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
        postontransportnode_input_value_validator_list = [
        ]
        postontransportnode_output_validator_list = [
        ]
        postontransportnode_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for putontransportnode operation
        putontransportnode_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        putontransportnode_error_dict = {
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
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
        putontransportnode_input_value_validator_list = [
        ]
        putontransportnode_output_validator_list = [
        ]
        putontransportnode_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/transport-nodes/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for refreshnodeconfiguration operation
        refreshnodeconfiguration_input_type = type.StructType('operation-input', {
            'transport_node_id': type.StringType(),
        })
        refreshnodeconfiguration_error_dict = {
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
        refreshnodeconfiguration_input_value_validator_list = [
        ]
        refreshnodeconfiguration_output_validator_list = [
        ]
        refreshnodeconfiguration_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes/{transport-node-id}?action=refresh_node_configuration&resource_type=EdgeNode',
            path_variables={
                'transport_node_id': 'transport-node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for restartinventorysync operation
        restartinventorysync_input_type = type.StructType('operation-input', {
            'transport_node_id': type.StringType(),
        })
        restartinventorysync_error_dict = {
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
        restartinventorysync_input_value_validator_list = [
        ]
        restartinventorysync_output_validator_list = [
        ]
        restartinventorysync_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes/{transport-node-id}?action=restart_inventory_sync',
            path_variables={
                'transport_node_id': 'transport-node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for restoreclusterconfig operation
        restoreclusterconfig_input_type = type.StructType('operation-input', {
            'transport_node_id': type.StringType(),
        })
        restoreclusterconfig_error_dict = {
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
        restoreclusterconfig_input_value_validator_list = [
        ]
        restoreclusterconfig_output_validator_list = [
        ]
        restoreclusterconfig_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes/{transport-node-id}?action=restore_cluster_config',
            path_variables={
                'transport_node_id': 'transport-node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for resynchostconfig operation
        resynchostconfig_input_type = type.StructType('operation-input', {
            'transportnode_id': type.StringType(),
        })
        resynchostconfig_error_dict = {
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
        resynchostconfig_input_value_validator_list = [
        ]
        resynchostconfig_output_validator_list = [
        ]
        resynchostconfig_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes/{transportnode-id}?action=resync_host_config',
            path_variables={
                'transportnode_id': 'transportnode-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'transport_node_id': type.StringType(),
            'transport_node': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNode'),
            'esx_mgmt_if_migration_dest': type.OptionalType(type.StringType()),
            'if_id': type.OptionalType(type.StringType()),
            'ping_ip': type.OptionalType(type.StringType()),
            'vnic': type.OptionalType(type.StringType()),
            'vnic_migration_dest': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/transport-nodes/{transport-node-id}',
            request_body_parameter='transport_node',
            path_variables={
                'transport_node_id': 'transport-node-id',
            },
            query_parameters={
                'esx_mgmt_if_migration_dest': 'esx_mgmt_if_migration_dest',
                'if_id': 'if_id',
                'ping_ip': 'ping_ip',
                'vnic': 'vnic',
                'vnic_migration_dest': 'vnic_migration_dest',
            },
            content_type='application/json'
        )

        # properties for updatemaintenancemode operation
        updatemaintenancemode_input_type = type.StructType('operation-input', {
            'transportnode_id': type.StringType(),
            'action': type.OptionalType(type.StringType()),
        })
        updatemaintenancemode_error_dict = {
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
        updatemaintenancemode_input_value_validator_list = [
        ]
        updatemaintenancemode_output_validator_list = [
        ]
        updatemaintenancemode_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transport-nodes/{transportnode-id}',
            path_variables={
                'transportnode_id': 'transportnode-id',
            },
            query_parameters={
                'action': 'action',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNode'),
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
            'deleteontransportnode': {
                'input_type': deleteontransportnode_input_type,
                'output_type': type.VoidType(),
                'errors': deleteontransportnode_error_dict,
                'input_value_validator_list': deleteontransportnode_input_value_validator_list,
                'output_validator_list': deleteontransportnode_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'disableflowcache': {
                'input_type': disableflowcache_input_type,
                'output_type': type.VoidType(),
                'errors': disableflowcache_error_dict,
                'input_value_validator_list': disableflowcache_input_value_validator_list,
                'output_validator_list': disableflowcache_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'enableflowcache': {
                'input_type': enableflowcache_input_type,
                'output_type': type.VoidType(),
                'errors': enableflowcache_error_dict,
                'input_value_validator_list': enableflowcache_input_value_validator_list,
                'output_validator_list': enableflowcache_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNode'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'getontransportnode': {
                'input_type': getontransportnode_input_type,
                'output_type': type.VoidType(),
                'errors': getontransportnode_error_dict,
                'input_value_validator_list': getontransportnode_input_value_validator_list,
                'output_validator_list': getontransportnode_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'postontransportnode': {
                'input_type': postontransportnode_input_type,
                'output_type': type.VoidType(),
                'errors': postontransportnode_error_dict,
                'input_value_validator_list': postontransportnode_input_value_validator_list,
                'output_validator_list': postontransportnode_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'putontransportnode': {
                'input_type': putontransportnode_input_type,
                'output_type': type.VoidType(),
                'errors': putontransportnode_error_dict,
                'input_value_validator_list': putontransportnode_input_value_validator_list,
                'output_validator_list': putontransportnode_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'refreshnodeconfiguration': {
                'input_type': refreshnodeconfiguration_input_type,
                'output_type': type.VoidType(),
                'errors': refreshnodeconfiguration_error_dict,
                'input_value_validator_list': refreshnodeconfiguration_input_value_validator_list,
                'output_validator_list': refreshnodeconfiguration_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'restartinventorysync': {
                'input_type': restartinventorysync_input_type,
                'output_type': type.VoidType(),
                'errors': restartinventorysync_error_dict,
                'input_value_validator_list': restartinventorysync_input_value_validator_list,
                'output_validator_list': restartinventorysync_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'restoreclusterconfig': {
                'input_type': restoreclusterconfig_input_type,
                'output_type': type.VoidType(),
                'errors': restoreclusterconfig_error_dict,
                'input_value_validator_list': restoreclusterconfig_input_value_validator_list,
                'output_validator_list': restoreclusterconfig_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'resynchostconfig': {
                'input_type': resynchostconfig_input_type,
                'output_type': type.VoidType(),
                'errors': resynchostconfig_error_dict,
                'input_value_validator_list': resynchostconfig_input_value_validator_list,
                'output_validator_list': resynchostconfig_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNode'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'updatemaintenancemode': {
                'input_type': updatemaintenancemode_input_type,
                'output_type': type.VoidType(),
                'errors': updatemaintenancemode_error_dict,
                'input_value_validator_list': updatemaintenancemode_input_value_validator_list,
                'output_validator_list': updatemaintenancemode_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'deleteontransportnode': deleteontransportnode_rest_metadata,
            'disableflowcache': disableflowcache_rest_metadata,
            'enableflowcache': enableflowcache_rest_metadata,
            'get': get_rest_metadata,
            'getontransportnode': getontransportnode_rest_metadata,
            'list': list_rest_metadata,
            'postontransportnode': postontransportnode_rest_metadata,
            'putontransportnode': putontransportnode_rest_metadata,
            'refreshnodeconfiguration': refreshnodeconfiguration_rest_metadata,
            'restartinventorysync': restartinventorysync_rest_metadata,
            'restoreclusterconfig': restoreclusterconfig_rest_metadata,
            'resynchostconfig': resynchostconfig_rest_metadata,
            'update': update_rest_metadata,
            'updatemaintenancemode': updatemaintenancemode_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.transport_nodes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TransportZonesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'transport_zone': type.ReferenceType('com.vmware.nsx.model_client', 'TransportZone'),
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
            url_template='/api/v1/transport-zones',
            request_body_parameter='transport_zone',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'zone_id': type.StringType(),
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
            url_template='/api/v1/transport-zones/{zone-id}',
            path_variables={
                'zone_id': 'zone-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'zone_id': type.StringType(),
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
            url_template='/api/v1/transport-zones/{zone-id}',
            path_variables={
                'zone_id': 'zone-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'is_default': type.OptionalType(type.BooleanType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'transport_type': type.OptionalType(type.StringType()),
            'uplink_teaming_policy_name': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/transport-zones',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'is_default': 'is_default',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'transport_type': 'transport_type',
                'uplink_teaming_policy_name': 'uplink_teaming_policy_name',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'zone_id': type.StringType(),
            'transport_zone': type.ReferenceType('com.vmware.nsx.model_client', 'TransportZone'),
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
            url_template='/api/v1/transport-zones/{zone-id}',
            request_body_parameter='transport_zone',
            path_variables={
                'zone_id': 'zone-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportZone'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportZone'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportZoneListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportZone'),
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
            self, iface_name='com.vmware.nsx.transport_zones',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TransportzoneProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'transport_zone_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'TransportZoneProfile')]),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/transportzone-profiles',
            request_body_parameter='transport_zone_profile',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'transportzone_profile_id': type.StringType(),
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
            url_template='/api/v1/transportzone-profiles/{transportzone-profile-id}',
            path_variables={
                'transportzone_profile_id': 'transportzone-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'transportzone_profile_id': type.StringType(),
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
            url_template='/api/v1/transportzone-profiles/{transportzone-profile-id}',
            path_variables={
                'transportzone_profile_id': 'transportzone-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'include_system_owned': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'resource_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/transportzone-profiles',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'include_system_owned': 'include_system_owned',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'resource_type': 'resource_type',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'transportzone_profile_id': type.StringType(),
            'transport_zone_profile': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'TransportZoneProfile')]),
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
            url_template='/api/v1/transportzone-profiles/{transportzone-profile-id}',
            request_body_parameter='transport_zone_profile',
            path_variables={
                'transportzone_profile_id': 'transportzone-profile-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'TransportZoneProfile')]),
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
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'TransportZoneProfile')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportZoneProfileListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'TransportZoneProfile')]),
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
            self, iface_name='com.vmware.nsx.transportzone_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TrustManagementStub(ApiInterfaceStub):
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
            url_template='/api/v1/trust-management',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TrustManagementData'),
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
            self, iface_name='com.vmware.nsx.trust_management',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _UiViewsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'view': type.ReferenceType('com.vmware.nsx.model_client', 'View'),
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
            url_template='/api/v1/ui-views',
            request_body_parameter='view',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'view_id': type.StringType(),
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
            url_template='/api/v1/ui-views/{view-id}',
            path_variables={
                'view_id': 'view-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tag': type.OptionalType(type.StringType()),
            'view_ids': type.OptionalType(type.StringType()),
            'widget_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/ui-views',
            path_variables={
            },
            query_parameters={
                'tag': 'tag',
                'view_ids': 'view_ids',
                'widget_id': 'widget_id',
            },
            content_type='application/json'
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'view_id': type.StringType(),
        })
        get_0_error_dict = {
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
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/ui-views/{view-id}',
            path_variables={
                'view_id': 'view-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'view_id': type.StringType(),
            'view': type.ReferenceType('com.vmware.nsx.model_client', 'View'),
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
            url_template='/api/v1/ui-views/{view-id}',
            request_body_parameter='view',
            path_variables={
                'view_id': 'view-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'View'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ViewList'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'View'),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'View'),
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
            'get_0': get_0_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.ui_views',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _UpgradeStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for abortpreupgradechecks operation
        abortpreupgradechecks_input_type = type.StructType('operation-input', {})
        abortpreupgradechecks_error_dict = {
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
        abortpreupgradechecks_input_value_validator_list = [
        ]
        abortpreupgradechecks_output_validator_list = [
        ]
        abortpreupgradechecks_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade?action=abort_pre_upgrade_checks',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for executepostupgradechecks operation
        executepostupgradechecks_input_type = type.StructType('operation-input', {
            'component_type': type.StringType(),
        })
        executepostupgradechecks_error_dict = {
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
        executepostupgradechecks_input_value_validator_list = [
        ]
        executepostupgradechecks_output_validator_list = [
        ]
        executepostupgradechecks_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade/{component-type}?action=execute_post_upgrade_checks',
            path_variables={
                'component_type': 'component-type',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for executepreupgradechecks operation
        executepreupgradechecks_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
        })
        executepreupgradechecks_error_dict = {
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
        executepreupgradechecks_input_value_validator_list = [
        ]
        executepreupgradechecks_output_validator_list = [
        ]
        executepreupgradechecks_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade?action=execute_pre_upgrade_checks',
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

        # properties for upgradeuc operation
        upgradeuc_input_type = type.StructType('operation-input', {})
        upgradeuc_error_dict = {
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
        upgradeuc_input_value_validator_list = [
        ]
        upgradeuc_output_validator_list = [
        ]
        upgradeuc_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/upgrade?action=upgrade_uc',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'abortpreupgradechecks': {
                'input_type': abortpreupgradechecks_input_type,
                'output_type': type.VoidType(),
                'errors': abortpreupgradechecks_error_dict,
                'input_value_validator_list': abortpreupgradechecks_input_value_validator_list,
                'output_validator_list': abortpreupgradechecks_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'executepostupgradechecks': {
                'input_type': executepostupgradechecks_input_type,
                'output_type': type.VoidType(),
                'errors': executepostupgradechecks_error_dict,
                'input_value_validator_list': executepostupgradechecks_input_value_validator_list,
                'output_validator_list': executepostupgradechecks_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'executepreupgradechecks': {
                'input_type': executepreupgradechecks_input_type,
                'output_type': type.VoidType(),
                'errors': executepreupgradechecks_error_dict,
                'input_value_validator_list': executepreupgradechecks_input_value_validator_list,
                'output_validator_list': executepreupgradechecks_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'upgradeuc': {
                'input_type': upgradeuc_input_type,
                'output_type': type.VoidType(),
                'errors': upgradeuc_error_dict,
                'input_value_validator_list': upgradeuc_input_value_validator_list,
                'output_validator_list': upgradeuc_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'abortpreupgradechecks': abortpreupgradechecks_rest_metadata,
            'executepostupgradechecks': executepostupgradechecks_rest_metadata,
            'executepreupgradechecks': executepreupgradechecks_rest_metadata,
            'upgradeuc': upgradeuc_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.upgrade',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Associations': Associations,
        'Batch': Batch,
        'BridgeClusters': BridgeClusters,
        'BridgeEndpointProfiles': BridgeEndpointProfiles,
        'BridgeEndpoints': BridgeEndpoints,
        'Cluster': Cluster,
        'ClusterProfiles': ClusterProfiles,
        'ComputeCollectionTransportNodeTemplates': ComputeCollectionTransportNodeTemplates,
        'EdgeClusters': EdgeClusters,
        'ErrorResolver': ErrorResolver,
        'FailureDomains': FailureDomains,
        'GlobalConfigs': GlobalConfigs,
        'HostSwitchProfiles': HostSwitchProfiles,
        'IpSets': IpSets,
        'IpfixCollectorProfiles': IpfixCollectorProfiles,
        'IpfixObsPoints': IpfixObsPoints,
        'IpfixProfiles': IpfixProfiles,
        'Licenses': Licenses,
        'LogicalPorts': LogicalPorts,
        'LogicalRouterPorts': LogicalRouterPorts,
        'LogicalRouters': LogicalRouters,
        'LogicalSwitches': LogicalSwitches,
        'MacSets': MacSets,
        'ManualHealthChecks': ManualHealthChecks,
        'MdProxies': MdProxies,
        'MirrorSessions': MirrorSessions,
        'NetworkMigrationSpecs': NetworkMigrationSpecs,
        'Node': Node,
        'Normalizations': Normalizations,
        'NotificationWatchers': NotificationWatchers,
        'NsGroups': NsGroups,
        'NsProfiles': NsProfiles,
        'NsServiceGroups': NsServiceGroups,
        'NsServices': NsServices,
        'ServiceConfigs': ServiceConfigs,
        'SwitchingProfiles': SwitchingProfiles,
        'Tasks': Tasks,
        'Traceflows': Traceflows,
        'TransportNodeCollections': TransportNodeCollections,
        'TransportNodeProfiles': TransportNodeProfiles,
        'TransportNodes': TransportNodes,
        'TransportZones': TransportZones,
        'TransportzoneProfiles': TransportzoneProfiles,
        'TrustManagement': TrustManagement,
        'UiViews': UiViews,
        'Upgrade': Upgrade,
        'aaa': 'com.vmware.nsx.aaa_client.StubFactory',
        'administration': 'com.vmware.nsx.administration_client.StubFactory',
        'app_discovery': 'com.vmware.nsx.app_discovery_client.StubFactory',
        'bridge_clusters': 'com.vmware.nsx.bridge_clusters_client.StubFactory',
        'bridge_endpoints': 'com.vmware.nsx.bridge_endpoints_client.StubFactory',
        'capacity': 'com.vmware.nsx.capacity_client.StubFactory',
        'cluster': 'com.vmware.nsx.cluster_client.StubFactory',
        'compute_collection_transport_node_templates': 'com.vmware.nsx.compute_collection_transport_node_templates_client.StubFactory',
        'configs': 'com.vmware.nsx.configs_client.StubFactory',
        'dhcp': 'com.vmware.nsx.dhcp_client.StubFactory',
        'directory': 'com.vmware.nsx.directory_client.StubFactory',
        'dns': 'com.vmware.nsx.dns_client.StubFactory',
        'edge_clusters': 'com.vmware.nsx.edge_clusters_client.StubFactory',
        'eula': 'com.vmware.nsx.eula_client.StubFactory',
        'fabric': 'com.vmware.nsx.fabric_client.StubFactory',
        'firewall': 'com.vmware.nsx.firewall_client.StubFactory',
        'hpm': 'com.vmware.nsx.hpm_client.StubFactory',
        'idfw': 'com.vmware.nsx.idfw_client.StubFactory',
        'intelligence': 'com.vmware.nsx.intelligence_client.StubFactory',
        'ip_sets': 'com.vmware.nsx.ip_sets_client.StubFactory',
        'ipfix': 'com.vmware.nsx.ipfix_client.StubFactory',
        'ipfix_obs_points': 'com.vmware.nsx.ipfix_obs_points_client.StubFactory',
        'ipv6': 'com.vmware.nsx.ipv6_client.StubFactory',
        'licenses': 'com.vmware.nsx.licenses_client.StubFactory',
        'loadbalancer': 'com.vmware.nsx.loadbalancer_client.StubFactory',
        'logical_ports': 'com.vmware.nsx.logical_ports_client.StubFactory',
        'logical_router_ports': 'com.vmware.nsx.logical_router_ports_client.StubFactory',
        'logical_routers': 'com.vmware.nsx.logical_routers_client.StubFactory',
        'logical_switches': 'com.vmware.nsx.logical_switches_client.StubFactory',
        'mac_sets': 'com.vmware.nsx.mac_sets_client.StubFactory',
        'md_proxies': 'com.vmware.nsx.md_proxies_client.StubFactory',
        'migration': 'com.vmware.nsx.migration_client.StubFactory',
        'model': 'com.vmware.nsx.model_client.StubFactory',
        'node': 'com.vmware.nsx.node_client.StubFactory',
        'notification_watchers': 'com.vmware.nsx.notification_watchers_client.StubFactory',
        'ns_groups': 'com.vmware.nsx.ns_groups_client.StubFactory',
        'ns_profiles': 'com.vmware.nsx.ns_profiles_client.StubFactory',
        'pbr': 'com.vmware.nsx.pbr_client.StubFactory',
        'pktcap': 'com.vmware.nsx.pktcap_client.StubFactory',
        'pools': 'com.vmware.nsx.pools_client.StubFactory',
        'proxy': 'com.vmware.nsx.proxy_client.StubFactory',
        'realization_state_barrier': 'com.vmware.nsx.realization_state_barrier_client.StubFactory',
        'service_configs': 'com.vmware.nsx.service_configs_client.StubFactory',
        'serviceinsertion': 'com.vmware.nsx.serviceinsertion_client.StubFactory',
        'switching_profiles': 'com.vmware.nsx.switching_profiles_client.StubFactory',
        'tasks': 'com.vmware.nsx.tasks_client.StubFactory',
        'telemetry': 'com.vmware.nsx.telemetry_client.StubFactory',
        'traceflows': 'com.vmware.nsx.traceflows_client.StubFactory',
        'transport_node_collections': 'com.vmware.nsx.transport_node_collections_client.StubFactory',
        'transport_nodes': 'com.vmware.nsx.transport_nodes_client.StubFactory',
        'transport_zones': 'com.vmware.nsx.transport_zones_client.StubFactory',
        'trust_management': 'com.vmware.nsx.trust_management_client.StubFactory',
        'ui_views': 'com.vmware.nsx.ui_views_client.StubFactory',
        'upgrade': 'com.vmware.nsx.upgrade_client.StubFactory',
    }

