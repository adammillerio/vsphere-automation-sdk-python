# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.tier_0s.locale_services.
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


class Bgp(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.bgp'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BgpStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            tier0_id,
            locale_service_id,
            ):
        """
        Read BGP routing config

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.BgpRoutingConfig`
        :return: com.vmware.nsx_policy.model.BgpRoutingConfig
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            })
class ByodServiceInstances(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.byod_service_instances'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ByodServiceInstancesStub)
        self._VAPI_OPERATION_IDS = {}


    def delete(self,
               tier0_id,
               locale_service_id,
               service_instance_id,
               ):
        """
        Delete BYOD policy service instance

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            })

    def get(self,
            tier0_id,
            locale_service_id,
            service_instance_id,
            ):
        """
        Read byod service instance

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ByodPolicyServiceInstance`
        :return: com.vmware.nsx_policy.model.ByodPolicyServiceInstance
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            })

    def list(self,
             tier0_id,
             locale_service_id,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Read all BYOD service instance objects under a tier-0

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.ByodPolicyServiceInstanceListResult`
        :return: com.vmware.nsx_policy.model.ByodPolicyServiceInstanceListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier0_id,
              locale_service_id,
              service_instance_id,
              byod_policy_service_instance,
              ):
        """
        Create BYOD Service Instance which represent instance of service
        definition created on manager.

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :type  byod_policy_service_instance: :class:`com.vmware.nsx_policy.model_client.ByodPolicyServiceInstance`
        :param byod_policy_service_instance: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            'byod_policy_service_instance': byod_policy_service_instance,
                            })

    def update(self,
               tier0_id,
               locale_service_id,
               service_instance_id,
               byod_policy_service_instance,
               ):
        """
        Create BYOD Service Instance which represent instance of service
        definition created on manager.

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Byod service instance id (required)
        :type  byod_policy_service_instance: :class:`com.vmware.nsx_policy.model_client.ByodPolicyServiceInstance`
        :param byod_policy_service_instance: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ByodPolicyServiceInstance`
        :return: com.vmware.nsx_policy.model.ByodPolicyServiceInstance
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            'byod_policy_service_instance': byod_policy_service_instance,
                            })
class IpsecVpnServices(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.ipsec_vpn_services'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _IpsecVpnServicesStub)
        self._VAPI_OPERATION_IDS = {}


    def delete(self,
               tier0_id,
               locale_service_id,
               service_id,
               ):
        """
        Delete IPSec VPN service for given locale service under Tier-0.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  service_id: :class:`str`
        :param service_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_id': service_id,
                            })

    def get(self,
            tier0_id,
            locale_service_id,
            service_id,
            ):
        """
        Get IPSec VPN service for given locale service under Tier-0.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  service_id: :class:`str`
        :param service_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.IPSecVpnService`
        :return: com.vmware.nsx_policy.model.IPSecVpnService
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_id': service_id,
                            })

    def list(self,
             tier0_id,
             locale_service_id,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Get paginated list of all IPSec VPN services for given locale service
        under Tier-0.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.IPSecVpnServiceListResult`
        :return: com.vmware.nsx_policy.model.IPSecVpnServiceListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier0_id,
              locale_service_id,
              service_id,
              ip_sec_vpn_service,
              ):
        """
        Create or patch IPSec VPN service for given locale service under
        Tier-0.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  ip_sec_vpn_service: :class:`com.vmware.nsx_policy.model_client.IPSecVpnService`
        :param ip_sec_vpn_service: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_id': service_id,
                            'ip_sec_vpn_service': ip_sec_vpn_service,
                            })

    def update(self,
               tier0_id,
               locale_service_id,
               service_id,
               ip_sec_vpn_service,
               ):
        """
        Create or fully replace IPSec VPN service for given locale service
        under Tier-0. Revision is optional for creation and required for
        update.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  ip_sec_vpn_service: :class:`com.vmware.nsx_policy.model_client.IPSecVpnService`
        :param ip_sec_vpn_service: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.IPSecVpnService`
        :return: com.vmware.nsx_policy.model.IPSecVpnService
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_id': service_id,
                            'ip_sec_vpn_service': ip_sec_vpn_service,
                            })
class L2vpnContext(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_context'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _L2vpnContextStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            tier0_id,
            locale_service_id,
            ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L2VpnContext`
        :return: com.vmware.nsx_policy.model.L2VpnContext
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            })
class L2vpnServices(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_services'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _L2vpnServicesStub)
        self._VAPI_OPERATION_IDS = {}


    def delete(self,
               tier0_id,
               locale_service_id,
               service_id,
               ):
        """
        Delete L2VPN service for given locale service.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  service_id: :class:`str`
        :param service_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_id': service_id,
                            })

    def get(self,
            tier0_id,
            locale_service_id,
            service_id,
            ):
        """
        Get L2VPN service for given locale service.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  service_id: :class:`str`
        :param service_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L2VPNService`
        :return: com.vmware.nsx_policy.model.L2VPNService
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_id': service_id,
                            })

    def list(self,
             tier0_id,
             locale_service_id,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Get paginated list of all L2VPN services.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.L2VPNServiceListResult`
        :return: com.vmware.nsx_policy.model.L2VPNServiceListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier0_id,
              locale_service_id,
              service_id,
              l2_vpn_service,
              ):
        """
        Create or patch L2VPN service for given locale service.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  l2_vpn_service: :class:`com.vmware.nsx_policy.model_client.L2VPNService`
        :param l2_vpn_service: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_id': service_id,
                            'l2_vpn_service': l2_vpn_service,
                            })

    def update(self,
               tier0_id,
               locale_service_id,
               service_id,
               l2_vpn_service,
               ):
        """
        Create or fully replace L2VPN service for given locale service.
        Revision is optional for creation and required for update.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  l2_vpn_service: :class:`com.vmware.nsx_policy.model_client.L2VPNService`
        :param l2_vpn_service: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L2VPNService`
        :return: com.vmware.nsx_policy.model.L2VPNService
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_id': service_id,
                            'l2_vpn_service': l2_vpn_service,
                            })
class L3vpnContext(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpn_context'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _L3vpnContextStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            tier0_id,
            locale_service_id,
            ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3VpnContext`
        :return: com.vmware.nsx_policy.model.L3VpnContext
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            })
class L3vpns(VapiInterface):
    """
    
    """
    LIST_L3VPN_SESSION_POLICYBASEDL3VPNSESSION = "PolicyBasedL3VpnSession"
    """
    Possible value for ``l3vpnSession`` of method :func:`L3vpns.list`.

    """
    LIST_L3VPN_SESSION_ROUTEBASEDL3VPNSESSION = "RouteBasedL3VpnSession"
    """
    Possible value for ``l3vpnSession`` of method :func:`L3vpns.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpns'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _L3vpnsStub)
        self._VAPI_OPERATION_IDS = {}


    def delete(self,
               tier0_id,
               locale_service_id,
               l3vpn_id,
               ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            })

    def get(self,
            tier0_id,
            locale_service_id,
            l3vpn_id,
            ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :return: com.vmware.nsx_policy.model.L3Vpn
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            })

    def list(self,
             tier0_id,
             locale_service_id,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             l3vpn_session=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_mark_for_delete_objects: :class:`bool` or ``None``
        :param include_mark_for_delete_objects: Include objects that are marked for deletion in results (optional,
            default to false)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  l3vpn_session: :class:`str` or ``None``
        :param l3vpn_session: Resource type of L3Vpn Session (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3VpnListResult`
        :return: com.vmware.nsx_policy.model.L3VpnListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'l3vpn_session': l3vpn_session,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier0_id,
              locale_service_id,
              l3vpn_id,
              l3_vpn,
              ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :type  l3_vpn: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :param l3_vpn: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            'l3_vpn': l3_vpn,
                            })

    def showsensitivedata(self,
                          tier0_id,
                          locale_service_id,
                          l3vpn_id,
                          ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :return: com.vmware.nsx_policy.model.L3Vpn
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('showsensitivedata',
                            {
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            })

    def update(self,
               tier0_id,
               locale_service_id,
               l3vpn_id,
               l3_vpn,
               ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :type  l3_vpn: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :param l3_vpn: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :return: com.vmware.nsx_policy.model.L3Vpn
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            'l3_vpn': l3_vpn,
                            })
class ServiceInstances(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.service_instances'
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


    def delete(self,
               tier0_id,
               locale_service_id,
               service_instance_id,
               ):
        """
        Delete policy service instance

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            })

    def get(self,
            tier0_id,
            locale_service_id,
            service_instance_id,
            ):
        """
        Read service instance

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyServiceInstance`
        :return: com.vmware.nsx_policy.model.PolicyServiceInstance
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            })

    def list(self,
             tier0_id,
             locale_service_id,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Read all service instance objects under a tier-0

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyServiceInstanceListResult`
        :return: com.vmware.nsx_policy.model.PolicyServiceInstanceListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier0_id,
              locale_service_id,
              service_instance_id,
              policy_service_instance,
              ):
        """
        Create Service Instance. Please note that, only display_name,
        description and deployment_spec_name are allowed to be modified in an
        exisiting entity. If the deployment spec name is changed, it will
        trigger the upgrade operation for the SVMs.

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :type  policy_service_instance: :class:`com.vmware.nsx_policy.model_client.PolicyServiceInstance`
        :param policy_service_instance: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            'policy_service_instance': policy_service_instance,
                            })

    def reauth(self,
               tier0_id,
               locale_service_id,
               service_instance_id,
               ):
        """
        

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('reauth',
                            {
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            })

    def update(self,
               tier0_id,
               locale_service_id,
               service_instance_id,
               policy_service_instance,
               ):
        """
        Create service instance. Please note that, only display_name,
        description and deployment_spec_name are allowed to be modified in an
        exisiting entity. If the deployment spec name is changed, it will
        trigger the upgrade operation for the SVMs.

        :type  tier0_id: :class:`str`
        :param tier0_id: Tier-0 id (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: Locale service id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :type  policy_service_instance: :class:`com.vmware.nsx_policy.model_client.PolicyServiceInstance`
        :param policy_service_instance: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyServiceInstance`
        :return: com.vmware.nsx_policy.model.PolicyServiceInstance
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'service_instance_id': service_instance_id,
                            'policy_service_instance': policy_service_instance,
                            })
class _BgpStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'BgpRoutingConfig'),
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
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.bgp',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ByodServiceInstancesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/byod-service-instances/{service-instance-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/byod-service-instances/{service-instance-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/byod-service-instances',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
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
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'byod_policy_service_instance': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ByodPolicyServiceInstance'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/byod-service-instances/{service-instance-id}',
            request_body_parameter='byod_policy_service_instance',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'byod_policy_service_instance': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ByodPolicyServiceInstance'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/byod-service-instances/{service-instance-id}',
            request_body_parameter='byod_policy_service_instance',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ByodPolicyServiceInstance'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ByodPolicyServiceInstanceListResult'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ByodPolicyServiceInstance'),
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
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.byod_service_instances',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _IpsecVpnServicesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/ipsec-vpn-services/{service-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_id': 'service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/ipsec-vpn-services/{service-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_id': 'service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/ipsec-vpn-services',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
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
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_id': type.StringType(),
            'ip_sec_vpn_service': type.ReferenceType('com.vmware.nsx_policy.model_client', 'IPSecVpnService'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/ipsec-vpn-services/{service-id}',
            request_body_parameter='ip_sec_vpn_service',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_id': 'service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_id': type.StringType(),
            'ip_sec_vpn_service': type.ReferenceType('com.vmware.nsx_policy.model_client', 'IPSecVpnService'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/ipsec-vpn-services/{service-id}',
            request_body_parameter='ip_sec_vpn_service',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_id': 'service-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'IPSecVpnService'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'IPSecVpnServiceListResult'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'IPSecVpnService'),
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
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.ipsec_vpn_services',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _L2vpnContextStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l2vpn-context',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L2VpnContext'),
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
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_context',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _L2vpnServicesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l2vpn-services/{service-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_id': 'service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l2vpn-services/{service-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_id': 'service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l2vpn-services',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
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
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_id': type.StringType(),
            'l2_VPN_service': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L2VPNService'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l2vpn-services/{service-id}',
            request_body_parameter='l2_VPN_service',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_id': 'service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_id': type.StringType(),
            'l2_VPN_service': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L2VPNService'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l2vpn-services/{service-id}',
            request_body_parameter='l2_VPN_service',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_id': 'service-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L2VPNService'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L2VPNServiceListResult'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L2VPNService'),
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
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_services',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _L3vpnContextStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpn-context',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3VpnContext'),
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
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpn_context',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _L3vpnsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'include_mark_for_delete_objects': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'l3vpn_session': type.OptionalType(type.StringType()),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'include_mark_for_delete_objects': 'include_mark_for_delete_objects',
                'included_fields': 'included_fields',
                'l3vpn_session': 'l3vpn_session',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
            'l3_vpn': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}',
            request_body_parameter='l3_vpn',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for showsensitivedata operation
        showsensitivedata_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
        })
        showsensitivedata_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        showsensitivedata_input_value_validator_list = [
        ]
        showsensitivedata_output_validator_list = [
            HasFieldsOfValidator()
        ]
        showsensitivedata_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}?action=show_sensitive_data',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
            'l3_vpn': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}',
            request_body_parameter='l3_vpn',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3VpnListResult'),
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
            'showsensitivedata': {
                'input_type': showsensitivedata_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
                'errors': showsensitivedata_error_dict,
                'input_value_validator_list': showsensitivedata_input_value_validator_list,
                'output_validator_list': showsensitivedata_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
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
            'showsensitivedata': showsensitivedata_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpns',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ServiceInstancesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/service-instances/{service-instance-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/service-instances/{service-instance-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/service-instances',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
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
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'policy_service_instance': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyServiceInstance'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/service-instances/{service-instance-id}',
            request_body_parameter='policy_service_instance',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for reauth operation
        reauth_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
        })
        reauth_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        reauth_input_value_validator_list = [
        ]
        reauth_output_validator_list = [
        ]
        reauth_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/service-instances/{service-instance-id}?action=reauth',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'policy_service_instance': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyServiceInstance'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/service-instances/{service-instance-id}',
            request_body_parameter='policy_service_instance',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'service_instance_id': 'service-instance-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyServiceInstance'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyServiceInstanceListResult'),
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
            'reauth': {
                'input_type': reauth_input_type,
                'output_type': type.VoidType(),
                'errors': reauth_error_dict,
                'input_value_validator_list': reauth_input_value_validator_list,
                'output_validator_list': reauth_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyServiceInstance'),
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
            'reauth': reauth_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.service_instances',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Bgp': Bgp,
        'ByodServiceInstances': ByodServiceInstances,
        'IpsecVpnServices': IpsecVpnServices,
        'L2vpnContext': L2vpnContext,
        'L2vpnServices': L2vpnServices,
        'L3vpnContext': L3vpnContext,
        'L3vpns': L3vpns,
        'ServiceInstances': ServiceInstances,
        'byod_service_instances': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.byod_service_instances_client.StubFactory',
        'endpoints': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.endpoints_client.StubFactory',
        'ipsec_vpn_services': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.ipsec_vpn_services_client.StubFactory',
        'l2vpn_context': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_context_client.StubFactory',
        'l2vpn_services': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_services_client.StubFactory',
        'l3vpns': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpns_client.StubFactory',
        'service_instances': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.service_instances_client.StubFactory',
    }

