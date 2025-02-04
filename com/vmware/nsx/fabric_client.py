# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.fabric.
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


class ComputeCollectionFabricTemplates(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.compute_collection_fabric_templates'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComputeCollectionFabricTemplatesStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               compute_collection_fabric_template,
               ):
        """
        Fabric templates are fabric configurations applied at the compute
        collection level. This configurations is used to decide what automated
        operations should be a run when a host membership changes.

        :type  compute_collection_fabric_template: :class:`com.vmware.nsx.model_client.ComputeCollectionFabricTemplate`
        :param compute_collection_fabric_template: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollectionFabricTemplate`
        :return: com.vmware.nsx.model.ComputeCollectionFabricTemplate
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'compute_collection_fabric_template': compute_collection_fabric_template,
                            })

    def delete(self,
               fabric_template_id,
               ):
        """
        Deletes compute collection fabric template for the given id

        :type  fabric_template_id: :class:`str`
        :param fabric_template_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'fabric_template_id': fabric_template_id,
                            })

    def get(self,
            fabric_template_id,
            ):
        """
        Get compute collection fabric template for the given id

        :type  fabric_template_id: :class:`str`
        :param fabric_template_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollectionFabricTemplate`
        :return: com.vmware.nsx.model.ComputeCollectionFabricTemplate
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'fabric_template_id': fabric_template_id,
                            })

    def list(self,
             compute_collection_id=None,
             ):
        """
        Returns compute collection fabric templates

        :type  compute_collection_id: :class:`str` or ``None``
        :param compute_collection_id: Compute collection id (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollectionFabricTemplateListResult`
        :return: com.vmware.nsx.model.ComputeCollectionFabricTemplateListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
               fabric_template_id,
               compute_collection_fabric_template,
               ):
        """
        Updates compute collection fabric template for the given id

        :type  fabric_template_id: :class:`str`
        :param fabric_template_id: (required)
        :type  compute_collection_fabric_template: :class:`com.vmware.nsx.model_client.ComputeCollectionFabricTemplate`
        :param compute_collection_fabric_template: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollectionFabricTemplate`
        :return: com.vmware.nsx.model.ComputeCollectionFabricTemplate
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'fabric_template_id': fabric_template_id,
                            'compute_collection_fabric_template': compute_collection_fabric_template,
                            })
class ComputeCollections(VapiInterface):
    """
    
    """
    CREATE_ACTION_NSX = "remove_nsx"
    """
    Possible value for ``action`` of method :func:`ComputeCollections.create`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.compute_collections'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComputeCollectionsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               cc_ext_id,
               action=None,
               ):
        """
        Perform action specific to NSX on the compute-collection. cc-ext-id
        should be of type VC_Cluster.

        :type  cc_ext_id: :class:`str`
        :param cc_ext_id: (required)
        :type  action: :class:`str` or ``None``
        :param action: Supported actions on compute-collection (optional)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'cc_ext_id': cc_ext_id,
                            'action': action,
                            })

    def get(self,
            cc_ext_id,
            ):
        """
        Returns information about a specific compute collection.

        :type  cc_ext_id: :class:`str`
        :param cc_ext_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollection`
        :return: com.vmware.nsx.model.ComputeCollection
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'cc_ext_id': cc_ext_id,
                            })

    def list(self,
             cm_local_id=None,
             cursor=None,
             discovered_node_id=None,
             display_name=None,
             external_id=None,
             included_fields=None,
             node_id=None,
             origin_id=None,
             origin_type=None,
             owner_id=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all compute collections.

        :type  cm_local_id: :class:`str` or ``None``
        :param cm_local_id: Local Id of the compute collection in the Compute Manager
            (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  discovered_node_id: :class:`str` or ``None``
        :param discovered_node_id: Id of the discovered node which belongs to this Compute Collection
            (optional)
        :type  display_name: :class:`str` or ``None``
        :param display_name: Name of the ComputeCollection in source compute manager (optional)
        :type  external_id: :class:`str` or ``None``
        :param external_id: External ID of the ComputeCollection in the source Compute manager,
            e.g. mo-ref in VC (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  node_id: :class:`str` or ``None``
        :param node_id: Id of the fabric node created from a discovered node belonging to
            this Compute Collection (optional)
        :type  origin_id: :class:`str` or ``None``
        :param origin_id: Id of the compute manager from where this Compute Collection was
            discovered (optional)
        :type  origin_type: :class:`str` or ``None``
        :param origin_type: ComputeCollection type like VC_Cluster. Here the Compute Manager
            type prefix would help in differentiating similar named Compute
            Collection types from different Compute Managers (optional)
        :type  owner_id: :class:`str` or ``None``
        :param owner_id: Id of the owner of compute collection in the Compute Manager
            (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeCollectionListResult`
        :return: com.vmware.nsx.model.ComputeCollectionListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'cm_local_id': cm_local_id,
                            'cursor': cursor,
                            'discovered_node_id': discovered_node_id,
                            'display_name': display_name,
                            'external_id': external_id,
                            'included_fields': included_fields,
                            'node_id': node_id,
                            'origin_id': origin_id,
                            'origin_type': origin_type,
                            'owner_id': owner_id,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class ComputeManagers(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.compute_managers'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComputeManagersStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               compute_manager,
               ):
        """
        Registers compute manager with NSX. Inventory service will collect data
        from the registered compute manager

        :type  compute_manager: :class:`com.vmware.nsx.model_client.ComputeManager`
        :param compute_manager: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeManager`
        :return: com.vmware.nsx.model.ComputeManager
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'compute_manager': compute_manager,
                            })

    def delete(self,
               compute_manager_id,
               ):
        """
        Unregisters a specified compute manager

        :type  compute_manager_id: :class:`str`
        :param compute_manager_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'compute_manager_id': compute_manager_id,
                            })

    def get(self,
            compute_manager_id,
            ):
        """
        Returns information about a specific compute manager

        :type  compute_manager_id: :class:`str`
        :param compute_manager_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeManager`
        :return: com.vmware.nsx.model.ComputeManager
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'compute_manager_id': compute_manager_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             origin_type=None,
             page_size=None,
             server=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all compute managers.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  origin_type: :class:`str` or ``None``
        :param origin_type: Compute manager type like vCenter (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  server: :class:`str` or ``None``
        :param server: IP address or hostname of compute manager (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeManagerListResult`
        :return: com.vmware.nsx.model.ComputeManagerListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'origin_type': origin_type,
                            'page_size': page_size,
                            'server': server,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def update(self,
               compute_manager_id,
               compute_manager,
               ):
        """
        Updates a specified compute manager

        :type  compute_manager_id: :class:`str`
        :param compute_manager_id: (required)
        :type  compute_manager: :class:`com.vmware.nsx.model_client.ComputeManager`
        :param compute_manager: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ComputeManager`
        :return: com.vmware.nsx.model.ComputeManager
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'compute_manager_id': compute_manager_id,
                            'compute_manager': compute_manager,
                            })
class ContainerApplicationInstances(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.container_application_instances'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ContainerApplicationInstancesStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            container_application_instance_id,
            ):
        """
        Returns information about a specific container application instance.

        :type  container_application_instance_id: :class:`str`
        :param container_application_instance_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ContainerApplicationInstance`
        :return: com.vmware.nsx.model.ContainerApplicationInstance
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_application_instance_id': container_application_instance_id,
                            })

    def list(self,
             container_application_id=None,
             container_cluster_id=None,
             container_project_id=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all container application instance.

        :type  container_application_id: :class:`str` or ``None``
        :param container_application_id: Identifier of the container application (optional)
        :type  container_cluster_id: :class:`str` or ``None``
        :param container_cluster_id: Identifier of the container cluster (optional)
        :type  container_project_id: :class:`str` or ``None``
        :param container_project_id: Identifier of the container project (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.ContainerApplicationInstanceListResult`
        :return: com.vmware.nsx.model.ContainerApplicationInstanceListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_application_id': container_application_id,
                            'container_cluster_id': container_cluster_id,
                            'container_project_id': container_project_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class ContainerApplications(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.container_applications'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ContainerApplicationsStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            container_application_id,
            ):
        """
        Returns information about a specific Container Application within a
        project.

        :type  container_application_id: :class:`str`
        :param container_application_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ContainerApplication`
        :return: com.vmware.nsx.model.ContainerApplication
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_application_id': container_application_id,
                            })

    def list(self,
             container_cluster_id=None,
             container_project_id=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all Container Applications.

        :type  container_cluster_id: :class:`str` or ``None``
        :param container_cluster_id: Identifier of the container cluster (optional)
        :type  container_project_id: :class:`str` or ``None``
        :param container_project_id: Identifier of the container project (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.ContainerApplicationListResult`
        :return: com.vmware.nsx.model.ContainerApplicationListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_cluster_id': container_cluster_id,
                            'container_project_id': container_project_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class ContainerClusterNodes(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.container_cluster_nodes'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ContainerClusterNodesStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            container_cluster_node_id,
            ):
        """
        Returns information about a specific container cluster node.

        :type  container_cluster_node_id: :class:`str`
        :param container_cluster_node_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ContainerClusterNode`
        :return: com.vmware.nsx.model.ContainerClusterNode
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_cluster_node_id': container_cluster_node_id,
                            })

    def list(self,
             container_cluster_id=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all container cluster nodes.

        :type  container_cluster_id: :class:`str` or ``None``
        :param container_cluster_id: Identifier of the container cluster (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.ContainerClusterNodeListResult`
        :return: com.vmware.nsx.model.ContainerClusterNodeListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_cluster_id': container_cluster_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class ContainerClusters(VapiInterface):
    """
    
    """
    LIST_CLUSTER_TYPE_PAS = "PAS"
    """
    Possible value for ``clusterType`` of method :func:`ContainerClusters.list`.

    """
    LIST_CLUSTER_TYPE_PKS = "PKS"
    """
    Possible value for ``clusterType`` of method :func:`ContainerClusters.list`.

    """
    LIST_CLUSTER_TYPE_KUBERNETES = "Kubernetes"
    """
    Possible value for ``clusterType`` of method :func:`ContainerClusters.list`.

    """
    LIST_CLUSTER_TYPE_OPENSHIFT = "Openshift"
    """
    Possible value for ``clusterType`` of method :func:`ContainerClusters.list`.

    """
    LIST_CLUSTER_TYPE_WCP = "WCP"
    """
    Possible value for ``clusterType`` of method :func:`ContainerClusters.list`.

    """
    LIST_CLUSTER_TYPE_OTHER = "Other"
    """
    Possible value for ``clusterType`` of method :func:`ContainerClusters.list`.

    """
    LIST_INFRA_TYPE_VSPHERE = "vSphere"
    """
    Possible value for ``infraType`` of method :func:`ContainerClusters.list`.

    """
    LIST_INFRA_TYPE_AWS = "AWS"
    """
    Possible value for ``infraType`` of method :func:`ContainerClusters.list`.

    """
    LIST_INFRA_TYPE_AZURE = "Azure"
    """
    Possible value for ``infraType`` of method :func:`ContainerClusters.list`.

    """
    LIST_INFRA_TYPE_VMC = "VMC"
    """
    Possible value for ``infraType`` of method :func:`ContainerClusters.list`.

    """
    LIST_INFRA_TYPE_KVM = "KVM"
    """
    Possible value for ``infraType`` of method :func:`ContainerClusters.list`.

    """
    LIST_INFRA_TYPE_BAREMETAL = "Baremetal"
    """
    Possible value for ``infraType`` of method :func:`ContainerClusters.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.container_clusters'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ContainerClustersStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            container_cluster_id,
            ):
        """
        Returns information about a specific container cluster

        :type  container_cluster_id: :class:`str`
        :param container_cluster_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ContainerCluster`
        :return: com.vmware.nsx.model.ContainerCluster
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_cluster_id': container_cluster_id,
                            })

    def list(self,
             cluster_type=None,
             cursor=None,
             included_fields=None,
             infra_type=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all Container Clusters.

        :type  cluster_type: :class:`str` or ``None``
        :param cluster_type: Type of container cluster (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  infra_type: :class:`str` or ``None``
        :param infra_type: Type of infrastructure (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ContainerClusterListResult`
        :return: com.vmware.nsx.model.ContainerClusterListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'cluster_type': cluster_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'infra_type': infra_type,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class ContainerIngressPolicies(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.container_ingress_policies'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ContainerIngressPoliciesStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            ingress_policy_id,
            ):
        """
        Returns information about a specific ingress policy.

        :type  ingress_policy_id: :class:`str`
        :param ingress_policy_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ContainerIngressPolicy`
        :return: com.vmware.nsx.model.ContainerIngressPolicy
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'ingress_policy_id': ingress_policy_id,
                            })

    def list(self,
             container_cluster_id=None,
             container_project_id=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all ingress policies.

        :type  container_cluster_id: :class:`str` or ``None``
        :param container_cluster_id: Identifier of the container cluster (optional)
        :type  container_project_id: :class:`str` or ``None``
        :param container_project_id: Identifier of the container project (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.ContainerIngressPolicyListResult`
        :return: com.vmware.nsx.model.ContainerIngressPolicyListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_cluster_id': container_cluster_id,
                            'container_project_id': container_project_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class ContainerNetworkPolicies(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.container_network_policies'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ContainerNetworkPoliciesStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            network_policy_id,
            ):
        """
        Returns information about a specific network policy.

        :type  network_policy_id: :class:`str`
        :param network_policy_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ContainerNetworkPolicy`
        :return: com.vmware.nsx.model.ContainerNetworkPolicy
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'network_policy_id': network_policy_id,
                            })

    def list(self,
             container_cluster_id=None,
             container_project_id=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all network policies.

        :type  container_cluster_id: :class:`str` or ``None``
        :param container_cluster_id: Identifier of the container cluster (optional)
        :type  container_project_id: :class:`str` or ``None``
        :param container_project_id: Identifier of the container project (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.ContainerNetworkPolicyListResult`
        :return: com.vmware.nsx.model.ContainerNetworkPolicyListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_cluster_id': container_cluster_id,
                            'container_project_id': container_project_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class ContainerProjects(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.container_projects'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ContainerProjectsStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self,
            container_project_id,
            ):
        """
        Returns information about a specific project

        :type  container_project_id: :class:`str`
        :param container_project_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ContainerProject`
        :return: com.vmware.nsx.model.ContainerProject
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_project_id': container_project_id,
                            })

    def list(self,
             container_cluster_id=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all container projects

        :type  container_cluster_id: :class:`str` or ``None``
        :param container_cluster_id: Identifier of the container cluster (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.ContainerProjectListResult`
        :return: com.vmware.nsx.model.ContainerProjectListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'container_cluster_id': container_cluster_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class DiscoveredNodes(VapiInterface):
    """
    
    """
    LIST_HAS_PARENT_TRUE = "true"
    """
    Possible value for ``hasParent`` of method :func:`DiscoveredNodes.list`.

    """
    LIST_HAS_PARENT_FALSE = "false"
    """
    Possible value for ``hasParent`` of method :func:`DiscoveredNodes.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.discovered_nodes'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DiscoveredNodesStub)
        self._VAPI_OPERATION_IDS = {}


    def createtransportnode(self,
                            node_ext_id,
                            transport_node,
                            ):
        """
        NSX components are installaed on host and transport node is created
        with given configurations.

        :type  node_ext_id: :class:`str`
        :param node_ext_id: (required)
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
        return self._invoke('createtransportnode',
                            {
                            'node_ext_id': node_ext_id,
                            'transport_node': transport_node,
                            })

    def get(self,
            node_ext_id,
            ):
        """
        Returns information about a specific discovered node.

        :type  node_ext_id: :class:`str`
        :param node_ext_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.DiscoveredNode`
        :return: com.vmware.nsx.model.DiscoveredNode
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'node_ext_id': node_ext_id,
                            })

    def hostprep(self,
                 node_ext_id,
                 ):
        """
        

        :type  node_ext_id: :class:`str`
        :param node_ext_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.Node
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.Node`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('hostprep',
                            {
                            'node_ext_id': node_ext_id,
                            })

    def list(self,
             cm_local_id=None,
             cursor=None,
             display_name=None,
             external_id=None,
             has_parent=None,
             included_fields=None,
             ip_address=None,
             node_id=None,
             node_type=None,
             origin_id=None,
             page_size=None,
             parent_compute_collection=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all discovered nodes.

        :type  cm_local_id: :class:`str` or ``None``
        :param cm_local_id: Local Id of the discovered node in the Compute Manager (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  display_name: :class:`str` or ``None``
        :param display_name: Display name of discovered node (optional)
        :type  external_id: :class:`str` or ``None``
        :param external_id: External id of the discovered node, ex. a mo-ref from VC (optional)
        :type  has_parent: :class:`str` or ``None``
        :param has_parent: Discovered node has a parent compute collection or is a standalone
            host (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  ip_address: :class:`str` or ``None``
        :param ip_address: IP address of the discovered node (optional)
        :type  node_id: :class:`str` or ``None``
        :param node_id: Id of the fabric node created from the discovered node (optional)
        :type  node_type: :class:`str` or ``None``
        :param node_type: Discovered Node type like HostNode (optional)
        :type  origin_id: :class:`str` or ``None``
        :param origin_id: Id of the compute manager from where this node was discovered
            (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  parent_compute_collection: :class:`str` or ``None``
        :param parent_compute_collection: External id of the compute collection to which this node belongs
            (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.DiscoveredNodeListResult`
        :return: com.vmware.nsx.model.DiscoveredNodeListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'cm_local_id': cm_local_id,
                            'cursor': cursor,
                            'display_name': display_name,
                            'external_id': external_id,
                            'has_parent': has_parent,
                            'included_fields': included_fields,
                            'ip_address': ip_address,
                            'node_id': node_id,
                            'node_type': node_type,
                            'origin_id': origin_id,
                            'page_size': page_size,
                            'parent_compute_collection': parent_compute_collection,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def reapplyclusterconfig(self,
                             node_ext_id,
                             ):
        """
        

        :type  node_ext_id: :class:`str`
        :param node_ext_id: (required)
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
        return self._invoke('reapplyclusterconfig',
                            {
                            'node_ext_id': node_ext_id,
                            })
class Nodes(VapiInterface):
    """
    
    """
    LIST_HYPERVISOR_OS_TYPE_ESXI = "ESXI"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_RHELKVM = "RHELKVM"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_UBUNTUKVM = "UBUNTUKVM"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_HYPERV = "HYPERV"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_RHELCONTAINER = "RHELCONTAINER"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_CENTOSCONTAINER = "CENTOSCONTAINER"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_RHELSERVER = "RHELSERVER"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_UBUNTUSERVER = "UBUNTUSERVER"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_CENTOSSERVER = "CENTOSSERVER"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_CENTOSKVM = "CENTOSKVM"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_SLESKVM = "SLESKVM"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_HYPERVISOR_OS_TYPE_SLESSERVER = "SLESSERVER"
    """
    Possible value for ``hypervisorOsType`` of method :func:`Nodes.list`.

    """
    LIST_RESOURCE_TYPE_HOSTNODE = "HostNode"
    """
    Possible value for ``resourceType`` of method :func:`Nodes.list`.

    """
    LIST_RESOURCE_TYPE_EDGENODE = "EdgeNode"
    """
    Possible value for ``resourceType`` of method :func:`Nodes.list`.

    """
    LIST_RESOURCE_TYPE_PUBLICCLOUDGATEWAYNODE = "PublicCloudGatewayNode"
    """
    Possible value for ``resourceType`` of method :func:`Nodes.list`.

    """
    PERFORMACTION_ACTION_ENTER_MAINTENANCE_MODE = "enter_maintenance_mode"
    """
    Possible value for ``action`` of method :func:`Nodes.performaction`.

    """
    PERFORMACTION_ACTION_EXIT_MAINTENANCE_MODE = "exit_maintenance_mode"
    """
    Possible value for ``action`` of method :func:`Nodes.performaction`.

    """
    PERFORMACTION_ACTION_GET_MAINTENANCE_MODE_STATE = "get_maintenance_mode_state"
    """
    Possible value for ``action`` of method :func:`Nodes.performaction`.

    """
    PERFORMACTION_VSAN_MODE_EVACUATE_ALL_DATA = "evacuate_all_data"
    """
    Possible value for ``vsanMode`` of method :func:`Nodes.performaction`.

    """
    PERFORMACTION_VSAN_MODE_ENSURE_OBJECT_ACCESSIBILITY = "ensure_object_accessibility"
    """
    Possible value for ``vsanMode`` of method :func:`Nodes.performaction`.

    """
    PERFORMACTION_VSAN_MODE_NO_ACTION = "no_action"
    """
    Possible value for ``vsanMode`` of method :func:`Nodes.performaction`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.nodes'
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


    def create(self,
               node,
               ):
        """
        Creates a host node (hypervisor) or edge node (router) in the transport
        network. When you run this command for a host, NSX Manager attempts to
        install the NSX kernel modules, which are packaged as VIB, RPM, or DEB
        files. For the installation to succeed, you must provide the host login
        credentials and the host thumbprint. To get the ESXi host thumbprint,
        SSH to the host and run the **openssl x509 -in /etc/vmware/ssl/rui.crt
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
        Please use Transport Node API POST /transport-nodes to install NSX
        components on a node.

        :type  node: :class:`vmware.vapi.struct.VapiStruct`
        :param node: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.Node`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.Node
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.Node`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'node': node,
                            })

    def create_0(self,
                 target_node_id,
                 target_uri,
                 ):
        """
        Invoke POST request on target fabric node. This api is deprecated as
        part of FN+TN unification. Please use Transport Node API POST
        /transport-nodes/<transport-node-id>/<target-node-id>/<target-uri>

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
        return self._invoke('create_0',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def delete(self,
               node_id,
               unprepare_host=None,
               ):
        """
        

        :type  node_id: :class:`str`
        :param node_id: (required)
        :type  unprepare_host: :class:`bool` or ``None``
        :param unprepare_host: Delete a host and uninstall NSX components (optional, default to
            true)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'node_id': node_id,
                            'unprepare_host': unprepare_host,
                            })

    def delete_0(self,
                 target_node_id,
                 target_uri,
                 ):
        """
        Invoke DELETE request on target fabric node. This api is deprecated as
        part of FN+TN unification. Please use Transport Node API DELETE
        /transport-nodes/<transport-node-id>/<target-node-id>/<target-uri>

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
        return self._invoke('delete_0',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def get(self,
            node_id,
            ):
        """
        Returns information about a specific fabric node (host or edge). This
        api is deprecated, use Transport Node API GET
        /transport-nodes/<transport-node-id> to get fabric node information.

        :type  node_id: :class:`str`
        :param node_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.Node
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.Node`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'node_id': node_id,
                            })

    def get_0(self,
              target_node_id,
              target_uri,
              ):
        """
        Invoke GET request on target fabric node. This api is deprecated as
        part of FN+TN unification. Please use Transport Node API GET
        /transport-nodes/<transport-node-id>/<target-node-id>/<target-uri>

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
        return self._invoke('get_0',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def list(self,
             cursor=None,
             discovered_node_id=None,
             display_name=None,
             external_id=None,
             hardware_id=None,
             hypervisor_os_type=None,
             included_fields=None,
             ip_address=None,
             page_size=None,
             resource_type=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all fabric nodes (hosts and edges). This api
        is deprecated as part of FN+TN unification. Please use Transport Node
        API GET /transport-nodes to list all fabric nodes.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  discovered_node_id: :class:`str` or ``None``
        :param discovered_node_id: Id of the discovered node which was converted to create this node
            (optional)
        :type  display_name: :class:`str` or ``None``
        :param display_name: HostNode display name (optional)
        :type  external_id: :class:`str` or ``None``
        :param external_id: HostNode external id (optional)
        :type  hardware_id: :class:`str` or ``None``
        :param hardware_id: Hardware Id of the host (optional)
        :type  hypervisor_os_type: :class:`str` or ``None``
        :param hypervisor_os_type: HostNode's Hypervisor type, for example ESXi, RHEL KVM or UBUNTU
            KVM. (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  ip_address: :class:`str` or ``None``
        :param ip_address: Management IP address of the node (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: Node type from 'HostNode', 'EdgeNode', 'PublicCloudGatewayNode'
            (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.NodeListResult`
        :return: com.vmware.nsx.model.NodeListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'discovered_node_id': discovered_node_id,
                            'display_name': display_name,
                            'external_id': external_id,
                            'hardware_id': hardware_id,
                            'hypervisor_os_type': hypervisor_os_type,
                            'included_fields': included_fields,
                            'ip_address': ip_address,
                            'page_size': page_size,
                            'resource_type': resource_type,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def performaction(self,
                      node_id,
                      action=None,
                      evacuate_powered_off_vms=None,
                      vsan_mode=None,
                      ):
        """
        The supported fabric node actions are enter_maintenance_mode,
        exit_maintenance_mode for EdgeNode. This API is deprecated, please call
        TransportNode maintenance mode API to update maintenance mode, refer to
        \"Update transport node maintenance mode\".

        :type  node_id: :class:`str`
        :param node_id: (required)
        :type  action: :class:`str` or ``None``
        :param action: Supported fabric node actions (optional)
        :type  evacuate_powered_off_vms: :class:`bool` or ``None``
        :param evacuate_powered_off_vms: Evacuate powered-off vms (optional, default to false)
        :type  vsan_mode: :class:`str` or ``None``
        :param vsan_mode: Vsan decommission mode (optional, default to
            ensure_object_accessibility)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.Node
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.Node`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('performaction',
                            {
                            'node_id': node_id,
                            'action': action,
                            'evacuate_powered_off_vms': evacuate_powered_off_vms,
                            'vsan_mode': vsan_mode,
                            })

    def restartinventorysync(self,
                             node_id,
                             ):
        """
        Restart the inventory sync for the node if it is currently internally
        paused. After this action the next inventory sync coming from the node
        is processed. This api is deprecated as part of FN+TN unification.
        Please use Transport Node API POST
        /transport-nodes/<transport-node-id>?action=restart_inventory_sync to
        restart inventory sync of node.

        :type  node_id: :class:`str`
        :param node_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'node_id': node_id,
                            })

    def update(self,
               node_id,
               node,
               ):
        """
        

        :type  node_id: :class:`str`
        :param node_id: (required)
        :type  node: :class:`vmware.vapi.struct.VapiStruct`
        :param node: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.Node`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.Node
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.Node`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'node_id': node_id,
                            'node': node,
                            })

    def update_0(self,
                 target_node_id,
                 target_uri,
                 ):
        """
        Invoke PUT request on target fabric node. This api is deprecated as
        part of FN+TN unification. Please use Transport Node API PUT
        /transport-nodes/<transport-node-id>/<target-node-id>/<target-uri>

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
        return self._invoke('update_0',
                            {
                            'target_node_id': target_node_id,
                            'target_uri': target_uri,
                            })

    def upgradeinfra(self,
                     node_id,
                     disable_vm_migration=None,
                     ):
        """
        Perform a service deployment upgrade on a host node

        :type  node_id: :class:`str`
        :param node_id: (required)
        :type  disable_vm_migration: :class:`bool` or ``None``
        :param disable_vm_migration: Should VM migration be disabled during upgrade (optional, default
            to false)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.Node
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.Node`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('upgradeinfra',
                            {
                            'node_id': node_id,
                            'disable_vm_migration': disable_vm_migration,
                            })
class Ostypes(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.ostypes'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OstypesStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Returns names of all supported host OS.


        :rtype: :class:`com.vmware.nsx.model_client.SupportedHostOSListResult`
        :return: com.vmware.nsx.model.SupportedHostOSListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
class Vifs(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.vifs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VifsStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             cursor=None,
             host_id=None,
             included_fields=None,
             lport_attachment_id=None,
             owner_vm_id=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             vm_id=None,
             ):
        """
        Returns information about all VIFs. A virtual network interface
        aggregates network interfaces into a logical interface unit that is
        indistinuishable from a physical network interface.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  host_id: :class:`str` or ``None``
        :param host_id: Id of the host where this vif is located. (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  lport_attachment_id: :class:`str` or ``None``
        :param lport_attachment_id: LPort Attachment Id of the virtual network interface. (optional)
        :type  owner_vm_id: :class:`str` or ``None``
        :param owner_vm_id: External id of the virtual machine. (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  vm_id: :class:`str` or ``None``
        :param vm_id: External id of the virtual machine. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.VirtualNetworkInterfaceListResult`
        :return: com.vmware.nsx.model.VirtualNetworkInterfaceListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'host_id': host_id,
                            'included_fields': included_fields,
                            'lport_attachment_id': lport_attachment_id,
                            'owner_vm_id': owner_vm_id,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'vm_id': vm_id,
                            })
class VirtualMachines(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.fabric.virtual_machines'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VirtualMachinesStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             cursor=None,
             display_name=None,
             external_id=None,
             host_id=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all virtual machines.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  display_name: :class:`str` or ``None``
        :param display_name: Display Name of the virtual machine (optional)
        :type  external_id: :class:`str` or ``None``
        :param external_id: External id of the virtual machine (optional)
        :type  host_id: :class:`str` or ``None``
        :param host_id: Id of the host where this vif is located (optional)
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
        :rtype: :class:`com.vmware.nsx.model_client.VirtualMachineListResult`
        :return: com.vmware.nsx.model.VirtualMachineListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
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
                            'display_name': display_name,
                            'external_id': external_id,
                            'host_id': host_id,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def updatetags(self,
                   virtual_machine_tag_update,
                   ):
        """
        Update tags applied to the virtual machine. External id of the virtual
        machine will be specified in the request body. Request body should
        contain all the tags to be applied. To clear all tags, provide an empty
        list. User can apply maximum 25 tags on a virtual machine. The
        remaining 5 are reserved for system defined tags.

        :type  virtual_machine_tag_update: :class:`com.vmware.nsx.model_client.VirtualMachineTagUpdate`
        :param virtual_machine_tag_update: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('updatetags',
                            {
                            'virtual_machine_tag_update': virtual_machine_tag_update,
                            })
class _ComputeCollectionFabricTemplatesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'compute_collection_fabric_template': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionFabricTemplate'),
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
            url_template='/api/v1/fabric/compute-collection-fabric-templates',
            request_body_parameter='compute_collection_fabric_template',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'fabric_template_id': type.StringType(),
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
            url_template='/api/v1/fabric/compute-collection-fabric-templates/{fabric-template-id}',
            path_variables={
                'fabric_template_id': 'fabric-template-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'fabric_template_id': type.StringType(),
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
            url_template='/api/v1/fabric/compute-collection-fabric-templates/{fabric-template-id}',
            path_variables={
                'fabric_template_id': 'fabric-template-id',
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
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/fabric/compute-collection-fabric-templates',
            path_variables={
            },
            query_parameters={
                'compute_collection_id': 'compute_collection_id',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'fabric_template_id': type.StringType(),
            'compute_collection_fabric_template': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionFabricTemplate'),
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
            url_template='/api/v1/fabric/compute-collection-fabric-templates/{fabric-template-id}',
            request_body_parameter='compute_collection_fabric_template',
            path_variables={
                'fabric_template_id': 'fabric-template-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionFabricTemplate'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionFabricTemplate'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionFabricTemplateListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionFabricTemplate'),
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
            self, iface_name='com.vmware.nsx.fabric.compute_collection_fabric_templates',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ComputeCollectionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'cc_ext_id': type.StringType(),
            'action': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/compute-collections/{cc-ext-id}',
            path_variables={
                'cc_ext_id': 'cc-ext-id',
            },
            query_parameters={
                'action': 'action',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cc_ext_id': type.StringType(),
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
            url_template='/api/v1/fabric/compute-collections/{cc-ext-id}',
            path_variables={
                'cc_ext_id': 'cc-ext-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cm_local_id': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'discovered_node_id': type.OptionalType(type.StringType()),
            'display_name': type.OptionalType(type.StringType()),
            'external_id': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'node_id': type.OptionalType(type.StringType()),
            'origin_id': type.OptionalType(type.StringType()),
            'origin_type': type.OptionalType(type.StringType()),
            'owner_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/compute-collections',
            path_variables={
            },
            query_parameters={
                'cm_local_id': 'cm_local_id',
                'cursor': 'cursor',
                'discovered_node_id': 'discovered_node_id',
                'display_name': 'display_name',
                'external_id': 'external_id',
                'included_fields': 'included_fields',
                'node_id': 'node_id',
                'origin_id': 'origin_id',
                'origin_type': 'origin_type',
                'owner_id': 'owner_id',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.VoidType(),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollection'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeCollectionListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.fabric.compute_collections',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ComputeManagersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'compute_manager': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeManager'),
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
            url_template='/api/v1/fabric/compute-managers',
            request_body_parameter='compute_manager',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'compute_manager_id': type.StringType(),
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
            url_template='/api/v1/fabric/compute-managers/{compute-manager-id}',
            path_variables={
                'compute_manager_id': 'compute-manager-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'compute_manager_id': type.StringType(),
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
            url_template='/api/v1/fabric/compute-managers/{compute-manager-id}',
            path_variables={
                'compute_manager_id': 'compute-manager-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'origin_type': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'server': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/compute-managers',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'origin_type': 'origin_type',
                'page_size': 'page_size',
                'server': 'server',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'compute_manager_id': type.StringType(),
            'compute_manager': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeManager'),
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
            url_template='/api/v1/fabric/compute-managers/{compute-manager-id}',
            request_body_parameter='compute_manager',
            path_variables={
                'compute_manager_id': 'compute-manager-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeManager'),
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeManager'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeManagerListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ComputeManager'),
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
            self, iface_name='com.vmware.nsx.fabric.compute_managers',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ContainerApplicationInstancesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'container_application_instance_id': type.StringType(),
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
            url_template='/api/v1/fabric/container-application-instances/{container-application-instance-id}',
            path_variables={
                'container_application_instance_id': 'container-application-instance-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'container_application_id': type.OptionalType(type.StringType()),
            'container_cluster_id': type.OptionalType(type.StringType()),
            'container_project_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/container-application-instances',
            path_variables={
            },
            query_parameters={
                'container_application_id': 'container_application_id',
                'container_cluster_id': 'container_cluster_id',
                'container_project_id': 'container_project_id',
                'cursor': 'cursor',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerApplicationInstance'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerApplicationInstanceListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.container_application_instances',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ContainerApplicationsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'container_application_id': type.StringType(),
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
            url_template='/api/v1/fabric/container-applications/{container-application-id}',
            path_variables={
                'container_application_id': 'container-application-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'container_cluster_id': type.OptionalType(type.StringType()),
            'container_project_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/container-applications',
            path_variables={
            },
            query_parameters={
                'container_cluster_id': 'container_cluster_id',
                'container_project_id': 'container_project_id',
                'cursor': 'cursor',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerApplication'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerApplicationListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.container_applications',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ContainerClusterNodesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'container_cluster_node_id': type.StringType(),
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
            url_template='/api/v1/fabric/container-cluster-nodes/{container-cluster-node-id}',
            path_variables={
                'container_cluster_node_id': 'container-cluster-node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'container_cluster_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/container-cluster-nodes',
            path_variables={
            },
            query_parameters={
                'container_cluster_id': 'container_cluster_id',
                'cursor': 'cursor',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerClusterNode'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerClusterNodeListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.container_cluster_nodes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ContainerClustersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'container_cluster_id': type.StringType(),
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
            url_template='/api/v1/fabric/container-clusters/{container-cluster-id}',
            path_variables={
                'container_cluster_id': 'container-cluster-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cluster_type': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'infra_type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/container-clusters',
            path_variables={
            },
            query_parameters={
                'cluster_type': 'cluster_type',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'infra_type': 'infra_type',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerCluster'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerClusterListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.container_clusters',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ContainerIngressPoliciesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'ingress_policy_id': type.StringType(),
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
            url_template='/api/v1/fabric/container-ingress-policies/{ingress-policy-id}',
            path_variables={
                'ingress_policy_id': 'ingress-policy-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'container_cluster_id': type.OptionalType(type.StringType()),
            'container_project_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/container-ingress-policies',
            path_variables={
            },
            query_parameters={
                'container_cluster_id': 'container_cluster_id',
                'container_project_id': 'container_project_id',
                'cursor': 'cursor',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerIngressPolicy'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerIngressPolicyListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.container_ingress_policies',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ContainerNetworkPoliciesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'network_policy_id': type.StringType(),
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
            url_template='/api/v1/fabric/container-network-policies/{network-policy-id}',
            path_variables={
                'network_policy_id': 'network-policy-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'container_cluster_id': type.OptionalType(type.StringType()),
            'container_project_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/container-network-policies',
            path_variables={
            },
            query_parameters={
                'container_cluster_id': 'container_cluster_id',
                'container_project_id': 'container_project_id',
                'cursor': 'cursor',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerNetworkPolicy'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerNetworkPolicyListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.container_network_policies',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ContainerProjectsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'container_project_id': type.StringType(),
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
            url_template='/api/v1/fabric/container-projects/{container-project-id}',
            path_variables={
                'container_project_id': 'container-project-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'container_cluster_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/container-projects',
            path_variables={
            },
            query_parameters={
                'container_cluster_id': 'container_cluster_id',
                'cursor': 'cursor',
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerProject'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ContainerProjectListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.container_projects',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _DiscoveredNodesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for createtransportnode operation
        createtransportnode_input_type = type.StructType('operation-input', {
            'node_ext_id': type.StringType(),
            'transport_node': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNode'),
        })
        createtransportnode_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        createtransportnode_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        createtransportnode_output_validator_list = [
            HasFieldsOfValidator()
        ]
        createtransportnode_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/fabric/discovered-nodes/{node-ext-id}?action=create_transport_node',
            request_body_parameter='transport_node',
            path_variables={
                'node_ext_id': 'node-ext-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'node_ext_id': type.StringType(),
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
            url_template='/api/v1/fabric/discovered-nodes/{node-ext-id}',
            path_variables={
                'node_ext_id': 'node-ext-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for hostprep operation
        hostprep_input_type = type.StructType('operation-input', {
            'node_ext_id': type.StringType(),
        })
        hostprep_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        hostprep_input_value_validator_list = [
        ]
        hostprep_output_validator_list = [
            HasFieldsOfValidator()
        ]
        hostprep_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/fabric/discovered-nodes/{node-ext-id}?action=hostprep',
            path_variables={
                'node_ext_id': 'node-ext-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cm_local_id': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'display_name': type.OptionalType(type.StringType()),
            'external_id': type.OptionalType(type.StringType()),
            'has_parent': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'ip_address': type.OptionalType(type.StringType()),
            'node_id': type.OptionalType(type.StringType()),
            'node_type': type.OptionalType(type.StringType()),
            'origin_id': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'parent_compute_collection': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/discovered-nodes',
            path_variables={
            },
            query_parameters={
                'cm_local_id': 'cm_local_id',
                'cursor': 'cursor',
                'display_name': 'display_name',
                'external_id': 'external_id',
                'has_parent': 'has_parent',
                'included_fields': 'included_fields',
                'ip_address': 'ip_address',
                'node_id': 'node_id',
                'node_type': 'node_type',
                'origin_id': 'origin_id',
                'page_size': 'page_size',
                'parent_compute_collection': 'parent_compute_collection',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for reapplyclusterconfig operation
        reapplyclusterconfig_input_type = type.StructType('operation-input', {
            'node_ext_id': type.StringType(),
        })
        reapplyclusterconfig_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        reapplyclusterconfig_input_value_validator_list = [
        ]
        reapplyclusterconfig_output_validator_list = [
            HasFieldsOfValidator()
        ]
        reapplyclusterconfig_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/fabric/discovered-nodes/{node-ext-id}?action=reapply_cluster_config',
            path_variables={
                'node_ext_id': 'node-ext-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'createtransportnode': {
                'input_type': createtransportnode_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNode'),
                'errors': createtransportnode_error_dict,
                'input_value_validator_list': createtransportnode_input_value_validator_list,
                'output_validator_list': createtransportnode_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'DiscoveredNode'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'hostprep': {
                'input_type': hostprep_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'Node')]),
                'errors': hostprep_error_dict,
                'input_value_validator_list': hostprep_input_value_validator_list,
                'output_validator_list': hostprep_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'DiscoveredNodeListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reapplyclusterconfig': {
                'input_type': reapplyclusterconfig_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNode'),
                'errors': reapplyclusterconfig_error_dict,
                'input_value_validator_list': reapplyclusterconfig_input_value_validator_list,
                'output_validator_list': reapplyclusterconfig_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'createtransportnode': createtransportnode_rest_metadata,
            'get': get_rest_metadata,
            'hostprep': hostprep_rest_metadata,
            'list': list_rest_metadata,
            'reapplyclusterconfig': reapplyclusterconfig_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.fabric.discovered_nodes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NodesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'node': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'Node')]),
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
            url_template='/api/v1/fabric/nodes',
            request_body_parameter='node',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for create_0 operation
        create_0_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        create_0_error_dict = {
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
        create_0_input_value_validator_list = [
        ]
        create_0_output_validator_list = [
        ]
        create_0_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/fabric/nodes/{target-node-id}/{target-uri}',
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
            'node_id': type.StringType(),
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
            url_template='/api/v1/fabric/nodes/{node-id}',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
                'unprepare_host': 'unprepare_host',
            },
            content_type='application/json'
        )

        # properties for delete_0 operation
        delete_0_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        delete_0_error_dict = {
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
        delete_0_input_value_validator_list = [
        ]
        delete_0_output_validator_list = [
        ]
        delete_0_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/fabric/nodes/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
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
            url_template='/api/v1/fabric/nodes/{node-id}',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        get_0_error_dict = {
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
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/fabric/nodes/{target-node-id}/{target-uri}',
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
            'discovered_node_id': type.OptionalType(type.StringType()),
            'display_name': type.OptionalType(type.StringType()),
            'external_id': type.OptionalType(type.StringType()),
            'hardware_id': type.OptionalType(type.StringType()),
            'hypervisor_os_type': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'ip_address': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/nodes',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'discovered_node_id': 'discovered_node_id',
                'display_name': 'display_name',
                'external_id': 'external_id',
                'hardware_id': 'hardware_id',
                'hypervisor_os_type': 'hypervisor_os_type',
                'included_fields': 'included_fields',
                'ip_address': 'ip_address',
                'page_size': 'page_size',
                'resource_type': 'resource_type',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for performaction operation
        performaction_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'action': type.OptionalType(type.StringType()),
            'evacuate_powered_off_vms': type.OptionalType(type.BooleanType()),
            'vsan_mode': type.OptionalType(type.StringType()),
        })
        performaction_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        performaction_input_value_validator_list = [
        ]
        performaction_output_validator_list = [
            HasFieldsOfValidator()
        ]
        performaction_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/fabric/nodes/{node-id}',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
                'action': 'action',
                'evacuate_powered_off_vms': 'evacuate_powered_off_vms',
                'vsan_mode': 'vsan_mode',
            },
            content_type='application/json'
        )

        # properties for restartinventorysync operation
        restartinventorysync_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
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
            url_template='/api/v1/fabric/nodes/{node-id}?action=restart_inventory_sync',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'node': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'Node')]),
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
            url_template='/api/v1/fabric/nodes/{node-id}',
            request_body_parameter='node',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update_0 operation
        update_0_input_type = type.StructType('operation-input', {
            'target_node_id': type.StringType(),
            'target_uri': type.StringType(),
        })
        update_0_error_dict = {
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
        update_0_input_value_validator_list = [
        ]
        update_0_output_validator_list = [
        ]
        update_0_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/fabric/nodes/{target-node-id}/{target-uri}',
            path_variables={
                'target_node_id': 'target-node-id',
                'target_uri': 'target-uri',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for upgradeinfra operation
        upgradeinfra_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'disable_vm_migration': type.OptionalType(type.BooleanType()),
        })
        upgradeinfra_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        upgradeinfra_input_value_validator_list = [
        ]
        upgradeinfra_output_validator_list = [
            HasFieldsOfValidator()
        ]
        upgradeinfra_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/fabric/nodes/{node-id}?action=upgrade_infra',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
                'disable_vm_migration': 'disable_vm_migration',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'Node')]),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create_0': {
                'input_type': create_0_input_type,
                'output_type': type.VoidType(),
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
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'Node')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.VoidType(),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NodeListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'performaction': {
                'input_type': performaction_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'Node')]),
                'errors': performaction_error_dict,
                'input_value_validator_list': performaction_input_value_validator_list,
                'output_validator_list': performaction_output_validator_list,
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
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'Node')]),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update_0': {
                'input_type': update_0_input_type,
                'output_type': type.VoidType(),
                'errors': update_0_error_dict,
                'input_value_validator_list': update_0_input_value_validator_list,
                'output_validator_list': update_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'upgradeinfra': {
                'input_type': upgradeinfra_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'Node')]),
                'errors': upgradeinfra_error_dict,
                'input_value_validator_list': upgradeinfra_input_value_validator_list,
                'output_validator_list': upgradeinfra_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'create_0': create_0_rest_metadata,
            'delete': delete_rest_metadata,
            'delete_0': delete_0_rest_metadata,
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
            'list': list_rest_metadata,
            'performaction': performaction_rest_metadata,
            'restartinventorysync': restartinventorysync_rest_metadata,
            'update': update_rest_metadata,
            'update_0': update_0_rest_metadata,
            'upgradeinfra': upgradeinfra_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.fabric.nodes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _OstypesStub(ApiInterfaceStub):
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
            url_template='/api/v1/fabric/ostypes',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'SupportedHostOSListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.ostypes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _VifsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'host_id': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'lport_attachment_id': type.OptionalType(type.StringType()),
            'owner_vm_id': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'vm_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/vifs',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'host_id': 'host_id',
                'included_fields': 'included_fields',
                'lport_attachment_id': 'lport_attachment_id',
                'owner_vm_id': 'owner_vm_id',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'vm_id': 'vm_id',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'VirtualNetworkInterfaceListResult'),
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
            self, iface_name='com.vmware.nsx.fabric.vifs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _VirtualMachinesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'display_name': type.OptionalType(type.StringType()),
            'external_id': type.OptionalType(type.StringType()),
            'host_id': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/fabric/virtual-machines',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'display_name': 'display_name',
                'external_id': 'external_id',
                'host_id': 'host_id',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for updatetags operation
        updatetags_input_type = type.StructType('operation-input', {
            'virtual_machine_tag_update': type.ReferenceType('com.vmware.nsx.model_client', 'VirtualMachineTagUpdate'),
        })
        updatetags_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        updatetags_input_value_validator_list = [
        ]
        updatetags_output_validator_list = [
        ]
        updatetags_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/fabric/virtual-machines?action=update_tags',
            request_body_parameter='virtual_machine_tag_update',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'VirtualMachineListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'updatetags': {
                'input_type': updatetags_input_type,
                'output_type': type.VoidType(),
                'errors': updatetags_error_dict,
                'input_value_validator_list': updatetags_input_value_validator_list,
                'output_validator_list': updatetags_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'updatetags': updatetags_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.fabric.virtual_machines',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ComputeCollectionFabricTemplates': ComputeCollectionFabricTemplates,
        'ComputeCollections': ComputeCollections,
        'ComputeManagers': ComputeManagers,
        'ContainerApplicationInstances': ContainerApplicationInstances,
        'ContainerApplications': ContainerApplications,
        'ContainerClusterNodes': ContainerClusterNodes,
        'ContainerClusters': ContainerClusters,
        'ContainerIngressPolicies': ContainerIngressPolicies,
        'ContainerNetworkPolicies': ContainerNetworkPolicies,
        'ContainerProjects': ContainerProjects,
        'DiscoveredNodes': DiscoveredNodes,
        'Nodes': Nodes,
        'Ostypes': Ostypes,
        'Vifs': Vifs,
        'VirtualMachines': VirtualMachines,
        'compute_collections': 'com.vmware.nsx.fabric.compute_collections_client.StubFactory',
        'compute_managers': 'com.vmware.nsx.fabric.compute_managers_client.StubFactory',
        'nodes': 'com.vmware.nsx.fabric.nodes_client.StubFactory',
        'virtual_machines': 'com.vmware.nsx.fabric.virtual_machines_client.StubFactory',
    }

