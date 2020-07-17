# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_vmc_app.model.
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


class AdvertisedRoute(VapiStruct):
    """
    Advertised BGP route

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    ADVERTISEMENT_STATE_SUCCESS = "SUCCESS"
    """


    """
    ADVERTISEMENT_STATE_FAILED = "FAILED"
    """


    """



    _canonical_to_pep_names = {
                            'advertisement_state': 'advertisement_state',
                            'ipv4_cidr': 'ipv4_cidr',
                            }

    def __init__(self,
                 advertisement_state=None,
                 ipv4_cidr=None,
                ):
        """
        :type  advertisement_state: :class:`str`
        :param advertisement_state: Possible values are: 
            
            * :attr:`AdvertisedRoute.ADVERTISEMENT_STATE_SUCCESS`
            * :attr:`AdvertisedRoute.ADVERTISEMENT_STATE_FAILED`
            
             State of advertisement
        :type  ipv4_cidr: :class:`str`
        :param ipv4_cidr: The route that is advertised to on-premise datacenter via Direct
            Connect format: ipv4-cidr-block
        """
        self.advertisement_state = advertisement_state
        self.ipv4_cidr = ipv4_cidr
        VapiStruct.__init__(self)


AdvertisedRoute._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.advertised_route', {
        'advertisement_state': type.StringType(),
        'ipv4_cidr': type.StringType(),
    },
    AdvertisedRoute,
    False,
    None))



class ApiError(VapiStruct):
    """
    Detailed information about an API Error

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'details': 'details',
                            'error_code': 'error_code',
                            'error_data': 'error_data',
                            'error_message': 'error_message',
                            'module_name': 'module_name',
                            'related_errors': 'related_errors',
                            }

    def __init__(self,
                 details=None,
                 error_code=None,
                 error_data=None,
                 error_message=None,
                 module_name=None,
                 related_errors=None,
                ):
        """
        :type  details: :class:`str` or ``None``
        :param details: Further details about the error
        :type  error_code: :class:`long` or ``None``
        :param error_code: A numeric error code format: int64
        :type  error_data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param error_data: Additional data about the error
        :type  error_message: :class:`str` or ``None``
        :param error_message: A description of the error
        :type  module_name: :class:`str` or ``None``
        :param module_name: The module name where the error occurred
        :type  related_errors: :class:`list` of :class:`RelatedApiError` or ``None``
        :param related_errors: Other errors related to this error
        """
        self.details = details
        self.error_code = error_code
        self.error_data = error_data
        self.error_message = error_message
        self.module_name = module_name
        self.related_errors = related_errors
        VapiStruct.__init__(self)


ApiError._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.api_error', {
        'details': type.OptionalType(type.StringType()),
        'error_code': type.OptionalType(type.IntegerType()),
        'error_data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'error_message': type.OptionalType(type.StringType()),
        'module_name': type.OptionalType(type.StringType()),
        'related_errors': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'RelatedApiError'))),
    },
    ApiError,
    False,
    None))



class AssociatedBaseGroupConnectionInfo(VapiStruct):
    """
    Base abstract associated Group connection infomation for the local SDDC.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AssociatedBaseGroupConnectionInfo"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    RESOURCE_TYPE_ASSOCIATEDTGWGROUPCONNECTIONINFO = "AssociatedTgwGroupConnectionInfo"
    """


    """



    _canonical_to_pep_names = {
                            'description': 'description',
                            'id': 'id',
                            'name': 'name',
                            'resource_type': 'resource_type',
                            }

    def __init__(self,
                 description=None,
                 id=None,
                 name=None,
                 resource_type='AssociatedBaseGroupConnectionInfo',
                ):
        """
        :type  description: :class:`str` or ``None``
        :param description: SDDC Group description
        :type  id: :class:`str`
        :param id: SDDC Group ID
        :type  name: :class:`str` or ``None``
        :param name: SDDC Group name
        :type  resource_type: :class:`str`
        :param resource_type: Possible values are: 
            
            *
              :attr:`AssociatedBaseGroupConnectionInfo.RESOURCE_TYPE_ASSOCIATEDTGWGROUPCONNECTIONINFO`
            
             Group connection type
        """
        self.description = description
        self.id = id
        self.name = name
        self._resource_type = resource_type
        VapiStruct.__init__(self)

    @property
    def resource_type(self):
        """
        Return the discriminator value
        """
        return self._resource_type

AssociatedBaseGroupConnectionInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.associated_base_group_connection_info', {
        'description': type.OptionalType(type.StringType()),
        'id': type.StringType(),
        'name': type.OptionalType(type.StringType()),
        'resource_type': type.StringType(),
    },
    AssociatedBaseGroupConnectionInfo,
    False,
    None))



class AssociatedGroupConnectionInfosListResult(VapiStruct):
    """
    Associated Group connection list result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param results: 
            When clients pass a value of this class as a parameter, the
            attribute must contain all the attributes defined in
            :class:`AssociatedBaseGroupConnectionInfo`. When methods return a
            value of this class as a return value, the attribute will contain
            all the attributes defined in
            :class:`AssociatedBaseGroupConnectionInfo`.
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


AssociatedGroupConnectionInfosListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.associated_group_connection_infos_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType(__name__, 'AssociatedBaseGroupConnectionInfo')]))),
    },
    AssociatedGroupConnectionInfosListResult,
    False,
    None))



class AssociatedTgwGroupConnectionInfo(VapiStruct):
    """
    Associated Group connection infomation for the local SDDC by using AWS TGW
    as a connector.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AssociatedTgwGroupConnectionInfo"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    STATE_CONNECTED = "CONNECTED"
    """


    """
    STATE_DISCONNECTED = "DISCONNECTED"
    """


    """



    _canonical_to_pep_names = {
                            'external_route_table_id': 'external_route_table_id',
                            'sddcs_route_table_id': 'sddcs_route_table_id',
                            'state': 'state',
                            'tgw_attachment_id': 'tgw_attachment_id',
                            'tgw_id': 'tgw_id',
                            'description': 'description',
                            'id': 'id',
                            'name': 'name',
                            'resource_type': 'resource_type',
                            }

    def __init__(self,
                 external_route_table_id=None,
                 sddcs_route_table_id=None,
                 state=None,
                 tgw_attachment_id=None,
                 tgw_id=None,
                 description=None,
                 id=None,
                 name=None,
                 resource_type='AssociatedTgwGroupConnectionInfo',
                ):
        """
        :type  external_route_table_id: :class:`str`
        :param external_route_table_id: TGW external route table ID used for external customers VPCs
            association
        :type  sddcs_route_table_id: :class:`str`
        :param sddcs_route_table_id: TGW SDDCs route table ID used for SDDCs association
        :type  state: :class:`str` or ``None``
        :param state: Possible values are: 
            
            * :attr:`AssociatedTgwGroupConnectionInfo.STATE_CONNECTED`
            * :attr:`AssociatedTgwGroupConnectionInfo.STATE_DISCONNECTED`
            
             The TGW attachment state of the SDDC in the Group
        :type  tgw_attachment_id: :class:`str`
        :param tgw_attachment_id: TGW attachment ID for the local SDDC in the Group
        :type  tgw_id: :class:`str`
        :param tgw_id: TGW ID for the local SDDC in the Group
        :type  description: :class:`str` or ``None``
        :param description: SDDC Group description
        :type  id: :class:`str`
        :param id: SDDC Group ID
        :type  name: :class:`str` or ``None``
        :param name: SDDC Group name
        :type  resource_type: :class:`str`
        :param resource_type: Possible values are: 
            
            *
              :attr:`AssociatedBaseGroupConnectionInfo.RESOURCE_TYPE_ASSOCIATEDTGWGROUPCONNECTIONINFO`
            
             Group connection type
        """
        self.external_route_table_id = external_route_table_id
        self.sddcs_route_table_id = sddcs_route_table_id
        self.state = state
        self.tgw_attachment_id = tgw_attachment_id
        self.tgw_id = tgw_id
        self.description = description
        self.id = id
        self.name = name
        self._resource_type = resource_type
        VapiStruct.__init__(self)

    @property
    def resource_type(self):
        """
        Return the discriminator value
        """
        return self._resource_type

AssociatedTgwGroupConnectionInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.associated_tgw_group_connection_info', {
        'external_route_table_id': type.StringType(),
        'sddcs_route_table_id': type.StringType(),
        'state': type.OptionalType(type.StringType()),
        'tgw_attachment_id': type.StringType(),
        'tgw_id': type.StringType(),
        'description': type.OptionalType(type.StringType()),
        'id': type.StringType(),
        'name': type.OptionalType(type.StringType()),
        'resource_type': type.StringType(),
    },
    AssociatedTgwGroupConnectionInfo,
    False,
    None))



class BGPAdvertisedRoutes(VapiStruct):
    """
    Advertised bgp routes

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'advertised_routes': 'advertised_routes',
                            'failed_advertised_routes': 'failed_advertised_routes',
                            }

    def __init__(self,
                 advertised_routes=None,
                 failed_advertised_routes=None,
                ):
        """
        :type  advertised_routes: :class:`list` of :class:`AdvertisedRoute` or ``None``
        :param advertised_routes: Routes advertised to on-premise datacenter via Direct Connect
        :type  failed_advertised_routes: :class:`long` or ``None``
        :param failed_advertised_routes: Number of routes failed to advertise format: int32
        """
        self.advertised_routes = advertised_routes
        self.failed_advertised_routes = failed_advertised_routes
        VapiStruct.__init__(self)


BGPAdvertisedRoutes._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.BGP_advertised_routes', {
        'advertised_routes': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AdvertisedRoute'))),
        'failed_advertised_routes': type.OptionalType(type.IntegerType()),
    },
    BGPAdvertisedRoutes,
    False,
    None))



class BGPLearnedRoutes(VapiStruct):
    """
    Learned bgp routes

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ipv4_cidr': 'ipv4_cidr',
                            }

    def __init__(self,
                 ipv4_cidr=None,
                ):
        """
        :type  ipv4_cidr: :class:`list` of :class:`str` or ``None``
        :param ipv4_cidr: The route that is learned from BGP via Direct Connect format:
            ipv4-cidr-block
        """
        self.ipv4_cidr = ipv4_cidr
        VapiStruct.__init__(self)


BGPLearnedRoutes._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.BGP_learned_routes', {
        'ipv4_cidr': type.OptionalType(type.ListType(type.StringType())),
    },
    BGPLearnedRoutes,
    False,
    None))



class ConnectedServiceListResult(VapiStruct):
    """
    A list of status of 'Enabled/Disabled' for a service connected to a linked
    vpc

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`ConnectedServiceStatus`
        :param results: Connected service status list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


ConnectedServiceListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.connected_service_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.ListType(type.ReferenceType(__name__, 'ConnectedServiceStatus')),
    },
    ConnectedServiceListResult,
    False,
    None))



class ConnectedServiceStatus(VapiStruct):
    """
    Status of 'Enabled/Disabled' for a service connected to a linked vpc

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'enabled': 'enabled',
                            'name': 'name',
                            }

    def __init__(self,
                 enabled=None,
                 name=None,
                ):
        """
        :type  enabled: :class:`bool` or ``None``
        :param enabled: status of service
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  name: :class:`str` or ``None``
        :param name: service name
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.enabled = enabled
        self.name = name
        VapiStruct.__init__(self)


ConnectedServiceStatus._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.connected_service_status', {
        'enabled': type.OptionalType(type.BooleanType()),
        'name': type.OptionalType(type.StringType()),
    },
    ConnectedServiceStatus,
    False,
    None))



class CsvListResult(VapiStruct):
    """
    Base type for CSV result.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'file_name': 'file_name',
                            }

    def __init__(self,
                 file_name=None,
                ):
        """
        :type  file_name: :class:`str` or ``None``
        :param file_name: File name set by HTTP server if API returns CSV result as a file.
        """
        self.file_name = file_name
        VapiStruct.__init__(self)


CsvListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.csv_list_result', {
        'file_name': type.OptionalType(type.StringType()),
    },
    CsvListResult,
    False,
    None))



class CsvRecord(VapiStruct):
    """
    Base type for CSV records.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                ):
        """
        """
        VapiStruct.__init__(self)


CsvRecord._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.csv_record', {
    },
    CsvRecord,
    False,
    None))



class DirectConnectBgpInfo(VapiStruct):
    """
    Direct Connect BGP related information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    ROUTE_PREFERENCE_DIRECT_CONNECT_PREFERRED_OVER_VPN = "DIRECT_CONNECT_PREFERRED_OVER_VPN"
    """


    """
    ROUTE_PREFERENCE_VPN_PREFERRED_OVER_DIRECT_CONNECT = "VPN_PREFERRED_OVER_DIRECT_CONNECT"
    """


    """



    _canonical_to_pep_names = {
                            'local_as_num': 'local_as_num',
                            'mtu': 'mtu',
                            'route_preference': 'route_preference',
                            }

    def __init__(self,
                 local_as_num=None,
                 mtu=None,
                 route_preference=None,
                ):
        """
        :type  local_as_num: :class:`str` or ``None``
        :param local_as_num: The ASN paired with the VGW attached to the VPC. AWS allowed
            private BGP ASN range - [64512, 65534] and [4200000000,
            4294967294]. If omitted in the payload, BGP ASN will not be
            modified.
        :type  mtu: :class:`long` or ``None``
        :param mtu: Maximum transmission unit allowed by the VIF format: int32
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  route_preference: :class:`str` or ``None``
        :param route_preference: Possible values are: 
            
            *
              :attr:`DirectConnectBgpInfo.ROUTE_PREFERENCE_DIRECT_CONNECT_PREFERRED_OVER_VPN`
            *
              :attr:`DirectConnectBgpInfo.ROUTE_PREFERENCE_VPN_PREFERRED_OVER_DIRECT_CONNECT`
            
            Direct connect route preference over VPN routes. If omitted in the
            payload, route preference will not be modified.
        """
        self.local_as_num = local_as_num
        self.mtu = mtu
        self.route_preference = route_preference
        VapiStruct.__init__(self)


DirectConnectBgpInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.direct_connect_bgp_info', {
        'local_as_num': type.OptionalType(type.StringType()),
        'mtu': type.OptionalType(type.IntegerType()),
        'route_preference': type.OptionalType(type.StringType()),
    },
    DirectConnectBgpInfo,
    False,
    None))



class DirectConnectConfig(VapiStruct):
    """
    Direct Connect configuration

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'connected_vpc_mtu': 'connected_vpc_mtu',
                            'internet_mtu': 'internet_mtu',
                            'intranet_mtu': 'intranet_mtu',
                            }

    def __init__(self,
                 connected_vpc_mtu=None,
                 internet_mtu=None,
                 intranet_mtu=None,
                ):
        """
        :type  connected_vpc_mtu: :class:`long` or ``None``
        :param connected_vpc_mtu: Uplink MTU of connected VPC traffic in edge tier-0 router port.
            format: int32
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  internet_mtu: :class:`long` or ``None``
        :param internet_mtu: Uplink MTU of internet traffic in edge tier-0 router port. format:
            int32
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  intranet_mtu: :class:`long`
        :param intranet_mtu: Uplink MTU of direct connect, sddc-grouping and outposts traffic in
            edge tier-0 router port. format: int32
        """
        self.connected_vpc_mtu = connected_vpc_mtu
        self.internet_mtu = internet_mtu
        self.intranet_mtu = intranet_mtu
        VapiStruct.__init__(self)


DirectConnectConfig._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.direct_connect_config', {
        'connected_vpc_mtu': type.OptionalType(type.IntegerType()),
        'internet_mtu': type.OptionalType(type.IntegerType()),
        'intranet_mtu': type.IntegerType(),
    },
    DirectConnectConfig,
    False,
    None))



class ExternalSddcConnectivity(VapiStruct):
    """
    External SDDC connectivity

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    CONNECTIVITY_TYPE_DIRECT_CONNECT = "DIRECT_CONNECT"
    """


    """
    CONNECTIVITY_TYPE_DEPLOYMENT_CONNECTIVITY_GROUP = "DEPLOYMENT_CONNECTIVITY_GROUP"
    """


    """
    ROUTE_TYPE_PROPAGATED = "PROPAGATED"
    """


    """
    ROUTE_TYPE_STATIC = "STATIC"
    """


    """
    STATUS_SUCCEEDED = "SUCCEEDED"
    """


    """
    STATUS_FAILED = "FAILED"
    """


    """



    _canonical_to_pep_names = {
                            'connectivity_type': 'connectivity_type',
                            'route_type': 'route_type',
                            'source': 'source',
                            'status': 'status',
                            'status_message': 'status_message',
                            }

    def __init__(self,
                 connectivity_type=None,
                 route_type=None,
                 source=None,
                 status=None,
                 status_message=None,
                ):
        """
        :type  connectivity_type: :class:`str`
        :param connectivity_type: Possible values are: 
            
            * :attr:`ExternalSddcConnectivity.CONNECTIVITY_TYPE_DIRECT_CONNECT`
            *
              :attr:`ExternalSddcConnectivity.CONNECTIVITY_TYPE_DEPLOYMENT_CONNECTIVITY_GROUP`
            
            The external SDDC connectivity type is used by the SDDC for the L3
            connectivity. DIRECT_CONNECT means that the external SDDC
            connectivity is through AWS Direct Connect.
            DEPLOYMENT_CONNECTIVITY_GROUP means that the external SDDC
            connectivity is through AWS TGW.
        :type  route_type: :class:`str` or ``None``
        :param route_type: Possible values are: 
            
            * :attr:`ExternalSddcConnectivity.ROUTE_TYPE_PROPAGATED`
            * :attr:`ExternalSddcConnectivity.ROUTE_TYPE_STATIC`
            
             The type of the route for the connectivity
        :type  source: :class:`str` or ``None``
        :param source: The source of the route for the connectivity
        :type  status: :class:`str` or ``None``
        :param status: Possible values are: 
            
            * :attr:`ExternalSddcConnectivity.STATUS_SUCCEEDED`
            * :attr:`ExternalSddcConnectivity.STATUS_FAILED`
            
             The status of the route for the connectivity
        :type  status_message: :class:`str` or ``None``
        :param status_message: The error message if the status is FAILED, the optional warning
            message if the status is SUCCEEDED.
        """
        self.connectivity_type = connectivity_type
        self.route_type = route_type
        self.source = source
        self.status = status
        self.status_message = status_message
        VapiStruct.__init__(self)


ExternalSddcConnectivity._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.external_sddc_connectivity', {
        'connectivity_type': type.StringType(),
        'route_type': type.OptionalType(type.StringType()),
        'source': type.OptionalType(type.StringType()),
        'status': type.OptionalType(type.StringType()),
        'status_message': type.OptionalType(type.StringType()),
    },
    ExternalSddcConnectivity,
    False,
    None))



class ExternalSddcRoute(VapiStruct):
    """
    External SDDC route

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'connectivities': 'connectivities',
                            'destination': 'destination',
                            }

    def __init__(self,
                 connectivities=None,
                 destination=None,
                ):
        """
        :type  connectivities: :class:`list` of :class:`ExternalSddcConnectivity`
        :param connectivities: The route used for what kind of connectivities
        :type  destination: :class:`str`
        :param destination: Destination IP CIDR Block format: ipv4-cidr-block
        """
        self.connectivities = connectivities
        self.destination = destination
        VapiStruct.__init__(self)


ExternalSddcRoute._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.external_sddc_route', {
        'connectivities': type.ListType(type.ReferenceType(__name__, 'ExternalSddcConnectivity')),
        'destination': type.StringType(),
    },
    ExternalSddcRoute,
    False,
    None))



class ExternalSddcRouteCsvRecord(VapiStruct):
    """
    CSV record for External SDDC route

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'connectivity_details': 'connectivity_details',
                            'destination': 'destination',
                            }

    def __init__(self,
                 connectivity_details=None,
                 destination=None,
                ):
        """
        :type  connectivity_details: :class:`str`
        :param connectivity_details: The connectivity datails contains status of route, source of the
            route, connectivity type
        :type  destination: :class:`str`
        :param destination: Destination IP CIDR Block format: ipv4-cidr-block
        """
        self.connectivity_details = connectivity_details
        self.destination = destination
        VapiStruct.__init__(self)


ExternalSddcRouteCsvRecord._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.external_sddc_route_csv_record', {
        'connectivity_details': type.StringType(),
        'destination': type.StringType(),
    },
    ExternalSddcRouteCsvRecord,
    False,
    None))



class ExternalSddcRoutesListResult(VapiStruct):
    """
    External SDDC routes list result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'routes': 'routes',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 routes=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  routes: :class:`list` of :class:`ExternalSddcRoute` or ``None``
        :param routes: 
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.routes = routes
        VapiStruct.__init__(self)


ExternalSddcRoutesListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.external_sddc_routes_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'routes': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ExternalSddcRoute'))),
    },
    ExternalSddcRoutesListResult,
    False,
    None))



class ExternalSddcRoutesListResultInCsvFormat(VapiStruct):
    """
    External SDDC routes list result in CSV format

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'file_name': 'file_name',
                            'results': 'results',
                            }

    def __init__(self,
                 file_name=None,
                 results=None,
                ):
        """
        :type  file_name: :class:`str` or ``None``
        :param file_name: File name set by HTTP server if API returns CSV result as a file.
        :type  results: :class:`list` of :class:`ExternalSddcRouteCsvRecord` or ``None``
        :param results: 
        """
        self.file_name = file_name
        self.results = results
        VapiStruct.__init__(self)


ExternalSddcRoutesListResultInCsvFormat._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.external_sddc_routes_list_result_in_csv_format', {
        'file_name': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ExternalSddcRouteCsvRecord'))),
    },
    ExternalSddcRoutesListResultInCsvFormat,
    False,
    None))



class IncludedFieldsParameters(VapiStruct):
    """
    A list of fields to include in query results

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'included_fields': 'included_fields',
                            }

    def __init__(self,
                 included_fields=None,
                ):
        """
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result
        """
        self.included_fields = included_fields
        VapiStruct.__init__(self)


IncludedFieldsParameters._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.included_fields_parameters', {
        'included_fields': type.OptionalType(type.StringType()),
    },
    IncludedFieldsParameters,
    False,
    None))



class IpAttachmentPair(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'attachment_id': 'attachment_id',
                            'ip': 'ip',
                            }

    def __init__(self,
                 attachment_id=None,
                 ip=None,
                ):
        """
        :type  attachment_id: :class:`str`
        :param attachment_id: Attachment id which maps to management VM IP
        :type  ip: :class:`str`
        :param ip: Management VM IP Address format: ipv4
        """
        self.attachment_id = attachment_id
        self.ip = ip
        VapiStruct.__init__(self)


IpAttachmentPair._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.ip_attachment_pair', {
        'attachment_id': type.StringType(),
        'ip': type.StringType(),
    },
    IpAttachmentPair,
    False,
    None))



class LinkedSubnetInfo(VapiStruct):
    """
    Infromation related to a subnet where linked ENIs were created.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'availability_zone': 'availability_zone',
                            'cidr': 'cidr',
                            'id': 'id',
                            }

    def __init__(self,
                 availability_zone=None,
                 cidr=None,
                 id=None,
                ):
        """
        :type  availability_zone: :class:`str`
        :param availability_zone: Linked subnet availability zone
        :type  cidr: :class:`str`
        :param cidr: Linked subnet CIDR format: ipv4-cidr-block
        :type  id: :class:`str`
        :param id: Linked subnet identifier
        """
        self.availability_zone = availability_zone
        self.cidr = cidr
        self.id = id
        VapiStruct.__init__(self)


LinkedSubnetInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.linked_subnet_info', {
        'availability_zone': type.StringType(),
        'cidr': type.StringType(),
        'id': type.StringType(),
    },
    LinkedSubnetInfo,
    False,
    None))



class LinkedVpcInfo(VapiStruct):
    """
    Linked VPC info

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'active_eni': 'active_eni',
                            'arn_role': 'arn_role',
                            'external_id': 'external_id',
                            'linked_account': 'linked_account',
                            'linked_vpc_addresses': 'linked_vpc_addresses',
                            'linked_vpc_id': 'linked_vpc_id',
                            'linked_vpc_nat_ips': 'linked_vpc_nat_ips',
                            'linked_vpc_subnets': 'linked_vpc_subnets',
                            'route_table_ids': 'route_table_ids',
                            'service_arn_role': 'service_arn_role',
                            }

    def __init__(self,
                 active_eni=None,
                 arn_role=None,
                 external_id=None,
                 linked_account=None,
                 linked_vpc_addresses=None,
                 linked_vpc_id=None,
                 linked_vpc_nat_ips=None,
                 linked_vpc_subnets=None,
                 route_table_ids=None,
                 service_arn_role=None,
                ):
        """
        :type  active_eni: :class:`str` or ``None``
        :param active_eni: Active network interface used for linked vpc traffic
        :type  arn_role: :class:`str`
        :param arn_role: ARN role for linked VPC operations
        :type  external_id: :class:`str`
        :param external_id: External identifier for ARN role
        :type  linked_account: :class:`str`
        :param linked_account: Linked VPC account number
        :type  linked_vpc_addresses: :class:`list` of :class:`str`
        :param linked_vpc_addresses: Linked VPC CIDRs format: ipv4-cidr-block
        :type  linked_vpc_id: :class:`str` or ``None``
        :param linked_vpc_id: Linked VPC identifier
        :type  linked_vpc_nat_ips: :class:`list` of :class:`str`
        :param linked_vpc_nat_ips: The IPs of linked VPC NAT rule for service access. format: ipv4
        :type  linked_vpc_subnets: :class:`list` of :class:`LinkedSubnetInfo`
        :param linked_vpc_subnets: Infromation related to the subnets where linked ENIs were created.
        :type  route_table_ids: :class:`list` of :class:`str`
        :param route_table_ids: The identifiers of route tables to be dynamically updated with SDDC
            networks
        :type  service_arn_role: :class:`str` or ``None``
        :param service_arn_role: service ARN role
        """
        self.active_eni = active_eni
        self.arn_role = arn_role
        self.external_id = external_id
        self.linked_account = linked_account
        self.linked_vpc_addresses = linked_vpc_addresses
        self.linked_vpc_id = linked_vpc_id
        self.linked_vpc_nat_ips = linked_vpc_nat_ips
        self.linked_vpc_subnets = linked_vpc_subnets
        self.route_table_ids = route_table_ids
        self.service_arn_role = service_arn_role
        VapiStruct.__init__(self)


LinkedVpcInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.linked_vpc_info', {
        'active_eni': type.OptionalType(type.StringType()),
        'arn_role': type.StringType(),
        'external_id': type.StringType(),
        'linked_account': type.StringType(),
        'linked_vpc_addresses': type.ListType(type.StringType()),
        'linked_vpc_id': type.OptionalType(type.StringType()),
        'linked_vpc_nat_ips': type.ListType(type.StringType()),
        'linked_vpc_subnets': type.ListType(type.ReferenceType(__name__, 'LinkedSubnetInfo')),
        'route_table_ids': type.ListType(type.StringType()),
        'service_arn_role': type.OptionalType(type.StringType()),
    },
    LinkedVpcInfo,
    False,
    None))



class LinkedVpcsListResult(VapiStruct):
    """
    Linked VPC list query result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`LinkedVpcInfo` or ``None``
        :param results: Linked VPCs list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


LinkedVpcsListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.linked_vpcs_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'LinkedVpcInfo'))),
    },
    LinkedVpcsListResult,
    False,
    None))



class ListResult(VapiStruct):
    """
    Base class for list results from collections

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        VapiStruct.__init__(self)


ListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
    },
    ListResult,
    False,
    None))



class MgmtServiceEntry(VapiStruct):
    """
    A service entry describes the detail of a network service.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'display_name': 'display_name',
                            'path': 'path',
                            }

    def __init__(self,
                 display_name=None,
                 path=None,
                ):
        """
        :type  display_name: :class:`str` or ``None``
        :param display_name: Display name for this service
        :type  path: :class:`str` or ``None``
        :param path: Service path should refer to a valid service in the system. Service
            can be system defined or user defined.
        """
        self.display_name = display_name
        self.path = path
        VapiStruct.__init__(self)


MgmtServiceEntry._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.mgmt_service_entry', {
        'display_name': type.OptionalType(type.StringType()),
        'path': type.OptionalType(type.StringType()),
    },
    MgmtServiceEntry,
    False,
    None))



class MgmtVmInfo(VapiStruct):
    """
    Management VM access information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'display_name': 'display_name',
                            'group_path': 'group_path',
                            'id': 'id',
                            'ip_attachment_pairs': 'ip_attachment_pairs',
                            'ips': 'ips',
                            'services': 'services',
                            }

    def __init__(self,
                 display_name=None,
                 group_path=None,
                 id=None,
                 ip_attachment_pairs=None,
                 ips=None,
                 services=None,
                ):
        """
        :type  display_name: :class:`str` or ``None``
        :param display_name: Management VM name
        :type  group_path: :class:`str` or ``None``
        :param group_path: For each management VM, a dedicated policy group will be created.
            This property will reflect its group path.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  id: :class:`str` or ``None``
        :param id: Management VM identifier
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  ip_attachment_pairs: :class:`list` of :class:`IpAttachmentPair` or ``None``
        :param ip_attachment_pairs: IP address and attachment id pairs for tagging managment VM
        :type  ips: :class:`list` of :class:`str` or ``None``
        :param ips: Local IPs of a management VM format: address-or-block-or-range
        :type  services: :class:`list` of :class:`MgmtServiceEntry` or ``None``
        :param services: Details services path and display name.
        """
        self.display_name = display_name
        self.group_path = group_path
        self.id = id
        self.ip_attachment_pairs = ip_attachment_pairs
        self.ips = ips
        self.services = services
        VapiStruct.__init__(self)


MgmtVmInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.mgmt_vm_info', {
        'display_name': type.OptionalType(type.StringType()),
        'group_path': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'ip_attachment_pairs': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'IpAttachmentPair'))),
        'ips': type.OptionalType(type.ListType(type.StringType())),
        'services': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'MgmtServiceEntry'))),
    },
    MgmtVmInfo,
    False,
    None))



class MgmtVmsListResult(VapiStruct):
    """
    Management VM list query result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`MgmtVmInfo` or ``None``
        :param results: Management VMs list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


MgmtVmsListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.mgmt_vms_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'MgmtVmInfo'))),
    },
    MgmtVmsListResult,
    False,
    None))



class ModelInterface(VapiStruct):
    """
    Interface information (Label)

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'id': 'id',
                            'name': 'name',
                            }

    def __init__(self,
                 id=None,
                 name=None,
                ):
        """
        :type  id: :class:`str`
        :param id: Identifier of the Interface label
        :type  name: :class:`str`
        :param name: Name of the Interface label
        """
        self.id = id
        self.name = name
        VapiStruct.__init__(self)


ModelInterface._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.model_interface', {
        'id': type.StringType(),
        'name': type.StringType(),
    },
    ModelInterface,
    False,
    None))



class PublicIp(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'display_name': 'display_name',
                            'id': 'id',
                            'ip': 'ip',
                            }

    def __init__(self,
                 display_name=None,
                 id=None,
                 ip=None,
                ):
        """
        :type  display_name: :class:`str` or ``None``
        :param display_name: 
        :type  id: :class:`str` or ``None``
        :param id: Public IP identifier
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  ip: :class:`str` or ``None``
        :param ip: IPv4 address format: ipv4
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.display_name = display_name
        self.id = id
        self.ip = ip
        VapiStruct.__init__(self)


PublicIp._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.public_ip', {
        'display_name': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'ip': type.OptionalType(type.StringType()),
    },
    PublicIp,
    False,
    None))



class PublicIpsListResult(VapiStruct):
    """
    Public IP list

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`PublicIp` or ``None``
        :param results: Public IP list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


PublicIpsListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.public_ips_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'PublicIp'))),
    },
    PublicIpsListResult,
    False,
    None))



class RelatedApiError(VapiStruct):
    """
    Detailed information about a related API error

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'details': 'details',
                            'error_code': 'error_code',
                            'error_data': 'error_data',
                            'error_message': 'error_message',
                            'module_name': 'module_name',
                            }

    def __init__(self,
                 details=None,
                 error_code=None,
                 error_data=None,
                 error_message=None,
                 module_name=None,
                ):
        """
        :type  details: :class:`str` or ``None``
        :param details: Further details about the error
        :type  error_code: :class:`long` or ``None``
        :param error_code: A numeric error code format: int64
        :type  error_data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param error_data: Additional data about the error
        :type  error_message: :class:`str` or ``None``
        :param error_message: A description of the error
        :type  module_name: :class:`str` or ``None``
        :param module_name: The module name where the error occurred
        """
        self.details = details
        self.error_code = error_code
        self.error_data = error_data
        self.error_message = error_message
        self.module_name = module_name
        VapiStruct.__init__(self)


RelatedApiError._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.related_api_error', {
        'details': type.OptionalType(type.StringType()),
        'error_code': type.OptionalType(type.IntegerType()),
        'error_data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'error_message': type.OptionalType(type.StringType()),
        'module_name': type.OptionalType(type.StringType()),
    },
    RelatedApiError,
    False,
    None))



class Resource(VapiStruct):
    """
    Base class for resources

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        VapiStruct.__init__(self)


Resource._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.resource', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
    },
    Resource,
    False,
    None))



class ResourceLink(VapiStruct):
    """
    A link to a related resource

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'action': 'action',
                            'href': 'href',
                            'rel': 'rel',
                            }

    def __init__(self,
                 action=None,
                 href=None,
                 rel=None,
                ):
        """
        :type  action: :class:`str` or ``None``
        :param action: Optional action
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  href: :class:`str` or ``None``
        :param href: Link to resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  rel: :class:`str` or ``None``
        :param rel: Custom relation type (follows RFC 5988 where appropriate
            definitions exist)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.action = action
        self.href = href
        self.rel = rel
        VapiStruct.__init__(self)


ResourceLink._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.resource_link', {
        'action': type.OptionalType(type.StringType()),
        'href': type.OptionalType(type.StringType()),
        'rel': type.OptionalType(type.StringType()),
    },
    ResourceLink,
    False,
    None))



class SddcUserConfiguration(VapiStruct):
    """
    SDDC configuration parameters for users. User-level addresses/CIDRs are
    provided.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'all_uplink_interface_label': 'all_uplink_interface_label',
                            'all_vpn_interface_label': 'all_vpn_interface_label',
                            'cgw_snat_ip': 'cgw_snat_ip',
                            'compute_domain': 'compute_domain',
                            'compute_gateway': 'compute_gateway',
                            'dx_interface_label': 'dx_interface_label',
                            'interfaces': 'interfaces',
                            'linked_vpc_interface_label': 'linked_vpc_interface_label',
                            'management_domain': 'management_domain',
                            'management_gateway': 'management_gateway',
                            'management_gateway_label': 'management_gateway_label',
                            'mgmt_subnet': 'mgmt_subnet',
                            'mgw_snat_ip': 'mgw_snat_ip',
                            'provider_gateways': 'provider_gateways',
                            'provider_name': 'provider_name',
                            'public_interface_label': 'public_interface_label',
                            'sddc_infra_subnet': 'sddc_infra_subnet',
                            'vpn_dx_ips': 'vpn_dx_ips',
                            'vpn_endpoints': 'vpn_endpoints',
                            'vpn_internet_ips': 'vpn_internet_ips',
                            }

    def __init__(self,
                 all_uplink_interface_label=None,
                 all_vpn_interface_label=None,
                 cgw_snat_ip=None,
                 compute_domain=None,
                 compute_gateway=None,
                 dx_interface_label=None,
                 interfaces=None,
                 linked_vpc_interface_label=None,
                 management_domain=None,
                 management_gateway=None,
                 management_gateway_label=None,
                 mgmt_subnet=None,
                 mgw_snat_ip=None,
                 provider_gateways=None,
                 provider_name=None,
                 public_interface_label=None,
                 sddc_infra_subnet=None,
                 vpn_dx_ips=None,
                 vpn_endpoints=None,
                 vpn_internet_ips=None,
                ):
        """
        :type  all_uplink_interface_label: :class:`str` or ``None``
        :param all_uplink_interface_label: All uplink interfaces label name. Deprecated, please use
            interfaces.
        :type  all_vpn_interface_label: :class:`str` or ``None``
        :param all_vpn_interface_label: All VPN interfaces label name. Deprecated, please use interfaces.
        :type  cgw_snat_ip: :class:`str` or ``None``
        :param cgw_snat_ip: Compute gateway SNAT ip address format: ipv4
        :type  compute_domain: :class:`str` or ``None``
        :param compute_domain: Compute domain id
        :type  compute_gateway: :class:`str`
        :param compute_gateway: Compute gateway name
        :type  dx_interface_label: :class:`str` or ``None``
        :param dx_interface_label: DirectConnect interface label name. Deprecated, please use
            interfaces.
        :type  interfaces: :class:`list` of :class:`ModelInterface` or ``None``
        :param interfaces: Interfaces (labels) including public interface, direct connect
            interface, linked vpc interface, etc.
        :type  linked_vpc_interface_label: :class:`str` or ``None``
        :param linked_vpc_interface_label: Linked VPC interface label name. Deprecated, please use interfaces.
        :type  management_domain: :class:`str` or ``None``
        :param management_domain: Management domain id
        :type  management_gateway: :class:`str`
        :param management_gateway: Management gateway name
        :type  management_gateway_label: :class:`str`
        :param management_gateway_label: Management gateway label name.
        :type  mgmt_subnet: :class:`list` of :class:`str`
        :param mgmt_subnet: Management subnet CIDRs format: ipv4-cidr-block
        :type  mgw_snat_ip: :class:`str` or ``None``
        :param mgw_snat_ip: Management gateway SNAT ip address format: ipv4
        :type  provider_gateways: :class:`list` of :class:`VmcKeyValueProviderGatewayListPair` or ``None``
        :param provider_gateways: Provider gateway list. Including both tier-0 gateways and tier-1
            gateways.
        :type  provider_name: :class:`str`
        :param provider_name: Service provider Name
        :type  public_interface_label: :class:`str` or ``None``
        :param public_interface_label: Public interface label name. Deprecated, please use interfaces.
        :type  sddc_infra_subnet: :class:`list` of :class:`str`
        :param sddc_infra_subnet: SDDC infra subnet CIDRs format: ipv4-cidr-block
        :type  vpn_dx_ips: :class:`list` of :class:`str` or ``None``
        :param vpn_dx_ips: Local IPs for VPN tunnel over Direct Connect. Deprecated. Please
            use vpn_endpoints instead of vpn_dx_ips. format: ipv4
        :type  vpn_endpoints: :class:`list` of :class:`VpnEndpoint` or ``None``
        :param vpn_endpoints: VPN tunnel endpoints. Currently containing public IPs for VPN over
            internet and local IPs for VPN over Direct Connect.
        :type  vpn_internet_ips: :class:`list` of :class:`str` or ``None``
        :param vpn_internet_ips: Public IPs for VPN tunnel over internet. Deprecated. Please use
            vpn_endpoints instead of vpn_internet_ips. format: ipv4
        """
        self.all_uplink_interface_label = all_uplink_interface_label
        self.all_vpn_interface_label = all_vpn_interface_label
        self.cgw_snat_ip = cgw_snat_ip
        self.compute_domain = compute_domain
        self.compute_gateway = compute_gateway
        self.dx_interface_label = dx_interface_label
        self.interfaces = interfaces
        self.linked_vpc_interface_label = linked_vpc_interface_label
        self.management_domain = management_domain
        self.management_gateway = management_gateway
        self.management_gateway_label = management_gateway_label
        self.mgmt_subnet = mgmt_subnet
        self.mgw_snat_ip = mgw_snat_ip
        self.provider_gateways = provider_gateways
        self.provider_name = provider_name
        self.public_interface_label = public_interface_label
        self.sddc_infra_subnet = sddc_infra_subnet
        self.vpn_dx_ips = vpn_dx_ips
        self.vpn_endpoints = vpn_endpoints
        self.vpn_internet_ips = vpn_internet_ips
        VapiStruct.__init__(self)


SddcUserConfiguration._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.sddc_user_configuration', {
        'all_uplink_interface_label': type.OptionalType(type.StringType()),
        'all_vpn_interface_label': type.OptionalType(type.StringType()),
        'cgw_snat_ip': type.OptionalType(type.StringType()),
        'compute_domain': type.OptionalType(type.StringType()),
        'compute_gateway': type.StringType(),
        'dx_interface_label': type.OptionalType(type.StringType()),
        'interfaces': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ModelInterface'))),
        'linked_vpc_interface_label': type.OptionalType(type.StringType()),
        'management_domain': type.OptionalType(type.StringType()),
        'management_gateway': type.StringType(),
        'management_gateway_label': type.StringType(),
        'mgmt_subnet': type.ListType(type.StringType()),
        'mgw_snat_ip': type.OptionalType(type.StringType()),
        'provider_gateways': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VmcKeyValueProviderGatewayListPair'))),
        'provider_name': type.StringType(),
        'public_interface_label': type.OptionalType(type.StringType()),
        'sddc_infra_subnet': type.ListType(type.StringType()),
        'vpn_dx_ips': type.OptionalType(type.ListType(type.StringType())),
        'vpn_endpoints': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VpnEndpoint'))),
        'vpn_internet_ips': type.OptionalType(type.ListType(type.StringType())),
    },
    SddcUserConfiguration,
    False,
    None))



class SelfResourceLink(VapiStruct):
    """
    The server will populate this field when returing the resource. Ignored on
    PUT and POST.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'action': 'action',
                            'href': 'href',
                            'rel': 'rel',
                            }

    def __init__(self,
                 action=None,
                 href=None,
                 rel=None,
                ):
        """
        :type  action: :class:`str` or ``None``
        :param action: Optional action
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  href: :class:`str` or ``None``
        :param href: Link to resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  rel: :class:`str` or ``None``
        :param rel: Custom relation type (follows RFC 5988 where appropriate
            definitions exist)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.action = action
        self.href = href
        self.rel = rel
        VapiStruct.__init__(self)


SelfResourceLink._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.self_resource_link', {
        'action': type.OptionalType(type.StringType()),
        'href': type.OptionalType(type.StringType()),
        'rel': type.OptionalType(type.StringType()),
    },
    SelfResourceLink,
    False,
    None))



class VMCAccounts(VapiStruct):
    """
    Shadow account and linked VPC account

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'linked_vpc_account': 'linked_vpc_account',
                            'shadow_account': 'shadow_account',
                            }

    def __init__(self,
                 linked_vpc_account=None,
                 shadow_account=None,
                ):
        """
        :type  linked_vpc_account: :class:`str` or ``None``
        :param linked_vpc_account: linked VPC account number
        :type  shadow_account: :class:`str`
        :param shadow_account: Shadow VPC account number
        """
        self.linked_vpc_account = linked_vpc_account
        self.shadow_account = shadow_account
        VapiStruct.__init__(self)


VMCAccounts._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.VMC_accounts', {
        'linked_vpc_account': type.OptionalType(type.StringType()),
        'shadow_account': type.StringType(),
    },
    VMCAccounts,
    False,
    None))



class VifsListResult(VapiStruct):
    """
    Direct Connect VIFs (Virtual Interface) list query result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`VirtualInterface` or ``None``
        :param results: VIFs list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


VifsListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vifs_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VirtualInterface'))),
    },
    VifsListResult,
    False,
    None))



class VirtualInterface(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    BGP_STATUS_UP = "UP"
    """


    """
    BGP_STATUS_DOWN = "DOWN"
    """


    """
    STATE_CONFIRMING = "CONFIRMING"
    """


    """
    STATE_VERIFYING = "VERIFYING"
    """


    """
    STATE_PENDING = "PENDING"
    """


    """
    STATE_AVAILABLE = "AVAILABLE"
    """


    """
    STATE_DOWN = "DOWN"
    """


    """
    STATE_DELETING = "DELETING"
    """


    """
    STATE_DELETED = "DELETED"
    """


    """
    STATE_REJECTED = "REJECTED"
    """


    """
    STATE_ATTACHED = "ATTACHED"
    """


    """
    STATE_ATTACHING = "ATTACHING"
    """


    """
    STATE_ERROR = "ERROR"
    """


    """



    _canonical_to_pep_names = {
                            'bgp_status': 'bgp_status',
                            'direct_connect_id': 'direct_connect_id',
                            'id': 'id',
                            'local_ip': 'local_ip',
                            'mtu': 'mtu',
                            'name': 'name',
                            'remote_asn': 'remote_asn',
                            'remote_ip': 'remote_ip',
                            'state': 'state',
                            }

    def __init__(self,
                 bgp_status=None,
                 direct_connect_id=None,
                 id=None,
                 local_ip=None,
                 mtu=None,
                 name=None,
                 remote_asn=None,
                 remote_ip=None,
                 state=None,
                ):
        """
        :type  bgp_status: :class:`str`
        :param bgp_status: Possible values are: 
            
            * :attr:`VirtualInterface.BGP_STATUS_UP`
            * :attr:`VirtualInterface.BGP_STATUS_DOWN`
            
             BGP status
        :type  direct_connect_id: :class:`str`
        :param direct_connect_id: Identifier for the Direct Connect
        :type  id: :class:`str`
        :param id: Identifier for the virtual interface
        :type  local_ip: :class:`str` or ``None``
        :param local_ip: amazon side address format: ipv4
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  mtu: :class:`long` or ``None``
        :param mtu: Maximum transmission unit allowed by the VIF format: int32
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  name: :class:`str`
        :param name: VIF name
        :type  remote_asn: :class:`str` or ``None``
        :param remote_asn: Remote autonomous system number of vif
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  remote_ip: :class:`str` or ``None``
        :param remote_ip: customer address format: ipv4
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  state: :class:`str`
        :param state: Possible values are: 
            
            * :attr:`VirtualInterface.STATE_CONFIRMING`
            * :attr:`VirtualInterface.STATE_VERIFYING`
            * :attr:`VirtualInterface.STATE_PENDING`
            * :attr:`VirtualInterface.STATE_AVAILABLE`
            * :attr:`VirtualInterface.STATE_DOWN`
            * :attr:`VirtualInterface.STATE_DELETING`
            * :attr:`VirtualInterface.STATE_DELETED`
            * :attr:`VirtualInterface.STATE_REJECTED`
            * :attr:`VirtualInterface.STATE_ATTACHED`
            * :attr:`VirtualInterface.STATE_ATTACHING`
            * :attr:`VirtualInterface.STATE_ERROR`
            
             VIF State
        """
        self.bgp_status = bgp_status
        self.direct_connect_id = direct_connect_id
        self.id = id
        self.local_ip = local_ip
        self.mtu = mtu
        self.name = name
        self.remote_asn = remote_asn
        self.remote_ip = remote_ip
        self.state = state
        VapiStruct.__init__(self)


VirtualInterface._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.virtual_interface', {
        'bgp_status': type.StringType(),
        'direct_connect_id': type.StringType(),
        'id': type.StringType(),
        'local_ip': type.OptionalType(type.StringType()),
        'mtu': type.OptionalType(type.IntegerType()),
        'name': type.StringType(),
        'remote_asn': type.OptionalType(type.StringType()),
        'remote_ip': type.OptionalType(type.StringType()),
        'state': type.StringType(),
    },
    VirtualInterface,
    False,
    None))



class VmcConsolidatedRealizedStatus(VapiStruct):
    """
    Represents aggregated realized status for intent entity across associated
    realized entities.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'consolidated_status': 'consolidated_status',
                            'consolidated_status_per_object': 'consolidated_status_per_object',
                            'intent_path': 'intent_path',
                            }

    def __init__(self,
                 consolidated_status=None,
                 consolidated_status_per_object=None,
                 intent_path=None,
                ):
        """
        :type  consolidated_status: :class:`VmcConsolidatedStatus` or ``None``
        :param consolidated_status: Consolidated state of objects for a given intent entity.
        :type  consolidated_status_per_object: :class:`list` of :class:`VmcConsolidatedStatusPerObject` or ``None``
        :param consolidated_status_per_object: Aggregated consolidated status by enforcement point.
        :type  intent_path: :class:`str` or ``None``
        :param intent_path: Intent path of the object representing this consolidated state.
        """
        self.consolidated_status = consolidated_status
        self.consolidated_status_per_object = consolidated_status_per_object
        self.intent_path = intent_path
        VapiStruct.__init__(self)


VmcConsolidatedRealizedStatus._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_consolidated_realized_status', {
        'consolidated_status': type.OptionalType(type.ReferenceType(__name__, 'VmcConsolidatedStatus')),
        'consolidated_status_per_object': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VmcConsolidatedStatusPerObject'))),
        'intent_path': type.OptionalType(type.StringType()),
    },
    VmcConsolidatedRealizedStatus,
    False,
    None))



class VmcConsolidatedStatus(VapiStruct):
    """
    Consolidated status of an object.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    CONSOLIDATED_STATUS_IN_PROGRESS = "IN_PROGRESS"
    """


    """
    CONSOLIDATED_STATUS_SUCCESS = "SUCCESS"
    """


    """
    CONSOLIDATED_STATUS_ERROR = "ERROR"
    """


    """
    CONSOLIDATED_STATUS_UNAVAILABLE = "UNAVAILABLE"
    """


    """



    _canonical_to_pep_names = {
                            'consolidated_status': 'consolidated_status',
                            'status_message': 'status_message',
                            }

    def __init__(self,
                 consolidated_status=None,
                 status_message=None,
                ):
        """
        :type  consolidated_status: :class:`str` or ``None``
        :param consolidated_status: Possible values are: 
            
            * :attr:`VmcConsolidatedStatus.CONSOLIDATED_STATUS_IN_PROGRESS`
            * :attr:`VmcConsolidatedStatus.CONSOLIDATED_STATUS_SUCCESS`
            * :attr:`VmcConsolidatedStatus.CONSOLIDATED_STATUS_ERROR`
            * :attr:`VmcConsolidatedStatus.CONSOLIDATED_STATUS_UNAVAILABLE`
            
            Possible values could be IN_PROGRESS, SUCCESS, ERROR, UNAVAILABLE.
            IN_PROGRESS - The object realization is in progress. ERROR - The
            object realization fails or is caught in an error. SUCCESS - The
            realization succeeds. UNAVAILABLE - The object realization status
            is unavailable.
        :type  status_message: :class:`str` or ``None``
        :param status_message: Help message for the current status regarding an object, providing
            information for each state.
        """
        self.consolidated_status = consolidated_status
        self.status_message = status_message
        VapiStruct.__init__(self)


VmcConsolidatedStatus._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_consolidated_status', {
        'consolidated_status': type.OptionalType(type.StringType()),
        'status_message': type.OptionalType(type.StringType()),
    },
    VmcConsolidatedStatus,
    False,
    None))



class VmcConsolidatedStatusPerObject(VapiStruct):
    """
    Realized status consolidated by individual objects.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'consolidated_status': 'consolidated_status',
                            'object_id': 'object_id',
                            }

    def __init__(self,
                 consolidated_status=None,
                 object_id=None,
                ):
        """
        :type  consolidated_status: :class:`VmcConsolidatedStatus` or ``None``
        :param consolidated_status: Detailed consolidated realized status for an intent object.
        :type  object_id: :class:`str`
        :param object_id: Object id used to consolidate state. This can be a particular
            backend task/job, etc.
        """
        self.consolidated_status = consolidated_status
        self.object_id = object_id
        VapiStruct.__init__(self)


VmcConsolidatedStatusPerObject._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_consolidated_status_per_object', {
        'consolidated_status': type.OptionalType(type.ReferenceType(__name__, 'VmcConsolidatedStatus')),
        'object_id': type.StringType(),
    },
    VmcConsolidatedStatusPerObject,
    False,
    None))



class VmcFeatureFlagInfo(VapiStruct):
    """
    VMC Feature Flag

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATE_ENABLED = "enabled"
    """


    """
    STATE_DISABLED = "disabled"
    """


    """
    STATE_INACTIVE = "inactive"
    """


    """



    _canonical_to_pep_names = {
                            'internal_name': 'internal_name',
                            'message': 'message',
                            'name': 'name',
                            'state': 'state',
                            }

    def __init__(self,
                 internal_name=None,
                 message=None,
                 name=None,
                 state=None,
                ):
        """
        :type  internal_name: :class:`str` or ``None``
        :param internal_name: Internal Name
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  message: :class:`str` or ``None``
        :param message: Message
        :type  name: :class:`str`
        :param name: Feature Name
        :type  state: :class:`str`
        :param state: Possible values are: 
            
            * :attr:`VmcFeatureFlagInfo.STATE_ENABLED`
            * :attr:`VmcFeatureFlagInfo.STATE_DISABLED`
            * :attr:`VmcFeatureFlagInfo.STATE_INACTIVE`
            
             state
        """
        self.internal_name = internal_name
        self.message = message
        self.name = name
        self.state = state
        VapiStruct.__init__(self)


VmcFeatureFlagInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_feature_flag_info', {
        'internal_name': type.OptionalType(type.StringType()),
        'message': type.OptionalType(type.StringType()),
        'name': type.StringType(),
        'state': type.StringType(),
    },
    VmcFeatureFlagInfo,
    False,
    None))



class VmcFeatureFlags(VapiStruct):
    """
    VMC Feature flags

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'features': 'features',
                            }

    def __init__(self,
                 features=None,
                ):
        """
        :type  features: :class:`list` of :class:`VmcFeatureFlagInfo`
        :param features: 
        """
        self.features = features
        VapiStruct.__init__(self)


VmcFeatureFlags._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_feature_flags', {
        'features': type.ListType(type.ReferenceType(__name__, 'VmcFeatureFlagInfo')),
    },
    VmcFeatureFlags,
    False,
    None))



class VmcKeyValueProviderGatewayListPair(VapiStruct):
    """
    A list for provider gateways

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'key': 'key',
                            'value': 'value',
                            }

    def __init__(self,
                 key=None,
                 value=None,
                ):
        """
        :type  key: :class:`str`
        :param key: Key
        :type  value: :class:`list` of :class:`VmcProviderGateway`
        :param value: Value
        """
        self.key = key
        self.value = value
        VapiStruct.__init__(self)


VmcKeyValueProviderGatewayListPair._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_key_value_provider_gateway_list_pair', {
        'key': type.StringType(),
        'value': type.ListType(type.ReferenceType(__name__, 'VmcProviderGateway')),
    },
    VmcKeyValueProviderGatewayListPair,
    False,
    None))



class VmcProviderGateway(VapiStruct):
    """
    Provider gateway, including tier-0s & tier-1s

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'display_name': 'display_name',
                            'id': 'id',
                            'path': 'path',
                            }

    def __init__(self,
                 display_name=None,
                 id=None,
                 path=None,
                ):
        """
        :type  display_name: :class:`str` or ``None``
        :param display_name: display_name
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  id: :class:`str` or ``None``
        :param id: id
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  path: :class:`str` or ``None``
        :param path: path
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.display_name = display_name
        self.id = id
        self.path = path
        VapiStruct.__init__(self)


VmcProviderGateway._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_provider_gateway', {
        'display_name': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'path': type.OptionalType(type.StringType()),
    },
    VmcProviderGateway,
    False,
    None))



class VpnEndpoint(VapiStruct):
    """
    VPN endpoint information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ip': 'ip',
                            'name': 'name',
                            }

    def __init__(self,
                 ip=None,
                 name=None,
                ):
        """
        :type  ip: :class:`str`
        :param ip: IP address of VPN endpoint format: ipv4
        :type  name: :class:`str`
        :param name: Name of the VPN endpoint
        """
        self.ip = ip
        self.name = name
        VapiStruct.__init__(self)


VpnEndpoint._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vpn_endpoint', {
        'ip': type.StringType(),
        'name': type.StringType(),
    },
    VpnEndpoint,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

