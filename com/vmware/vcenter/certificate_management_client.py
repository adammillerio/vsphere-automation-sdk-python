# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.certificate_management.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.certificate_management_client`` module provides
classes to manage certificates.

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


class X509CertChain(VapiStruct):
    """
    The ``X509CertChain`` class contains x509 certificate chain. This class was
    added in vSphere API 6.7.2.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 cert_chain=None,
                ):
        """
        :type  cert_chain: :class:`list` of :class:`str`
        :param cert_chain: Certificate chain in base64 format. This attribute was added in
            vSphere API 6.7.2.
        """
        self.cert_chain = cert_chain
        VapiStruct.__init__(self)


X509CertChain._set_binding_type(type.StructType(
    'com.vmware.vcenter.certificate_management.x509_cert_chain', {
        'cert_chain': type.ListType(type.StringType()),
    },
    X509CertChain,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
        'vcenter': 'com.vmware.vcenter.certificate_management.vcenter_client.StubFactory',
    }

