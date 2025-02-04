# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2020 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.certificate_management.vcenter.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.certificate_management.vcenter_client`` module
provides classes to manage certificates.

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


class TrustedRootChains(VapiInterface):
    """
    The ``TrustedRootChains`` interface provides methods to create, modify,
    delete and read trusted root certificate chains. This class was added in
    vSphere API 6.7.2.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.certificate_management.vcenter.trusted_root_chains'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TrustedRootChainsStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``TrustedRootChains.Info`` class contains information for a trusted
        root certificate chain. This class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     cert_chain=None,
                    ):
            """
            :type  cert_chain: :class:`com.vmware.vcenter.certificate_management_client.X509CertChain`
            :param cert_chain: A certificate chain in base64 encoding. This attribute was added in
                vSphere API 6.7.2.
            """
            self.cert_chain = cert_chain
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.trusted_root_chains.info', {
            'cert_chain': type.ReferenceType('com.vmware.vcenter.certificate_management_client', 'X509CertChain'),
        },
        Info,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``TrustedRootChains.Summary`` class contains a trusted root certificate
        chain summary suitable for UI presentation. This class was added in vSphere
        API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     chain=None,
                    ):
            """
            :type  chain: :class:`str`
            :param chain: Unique identifier for chain. This attribute was added in vSphere
                API 6.7.2.
            """
            self.chain = chain
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.trusted_root_chains.summary', {
            'chain': type.StringType(),
        },
        Summary,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``TrustedRootChains.CreateSpec`` class contains information to create a
        trusted root certificate chain. This class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     cert_chain=None,
                     chain=None,
                    ):
            """
            :type  cert_chain: :class:`com.vmware.vcenter.certificate_management_client.X509CertChain`
            :param cert_chain: Certificate chain in base64 encoding. This attribute was added in
                vSphere API 6.7.2.
            :type  chain: :class:`str` or ``None``
            :param chain: Unique identifier for this trusted root. Client can specify at
                creation as long as it is unique, otherwise one will be generated.
                An example of a client providing the identifier would be if this
                trusted root is associated with a VC trust. In this case the
                identifier would be the domain id. This attribute was added in
                vSphere API 6.7.2.
                A unique id will be generated if not given.
            """
            self.cert_chain = cert_chain
            self.chain = chain
            VapiStruct.__init__(self)


    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.trusted_root_chains.create_spec', {
            'cert_chain': type.ReferenceType('com.vmware.vcenter.certificate_management_client', 'X509CertChain'),
            'chain': type.OptionalType(type.StringType()),
        },
        CreateSpec,
        False,
        None))



    def list(self):
        """
        Returns summary information for each trusted root certificate chain.
        This method was added in vSphere API 6.7.2.


        :rtype: :class:`list` of :class:`TrustedRootChains.Summary`
        :return: List of trusted root certificate chains summaries.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if authorization is not given to caller.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('list', None)

    def create(self,
               spec,
               ):
        """
        Creates a new trusted root certificate chain from the CreateSpec. This
        method was added in vSphere API 6.7.2.

        :type  spec: :class:`TrustedRootChains.CreateSpec`
        :param spec: The information needed to create a trusted root certificate chain.
        :rtype: :class:`str`
        :return: The unique identifier for the new trusted root chain.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if authorization is not given to caller.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if a trusted root certificate chain exists with id in given spec.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``CertificateManagement.Manage`` and
              ``CertificateManagement.Administer``.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })

    def get(self,
            chain,
            ):
        """
        Retrieve a trusted root certificate chain for a given identifier. This
        method was added in vSphere API 6.7.2.

        :type  chain: :class:`str`
        :param chain: Unique identifier for a trusted root cert chain.
        :rtype: :class:`TrustedRootChains.Info`
        :return: TrustedRootChain.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if authorization is not given to caller.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a trusted root certificate chain does not exist for given id.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'chain': chain,
                            })

    def delete(self,
               chain,
               ):
        """
        Deletes trusted root certificate chain for a given identifier. This
        method was added in vSphere API 6.7.2.

        :type  chain: :class:`str`
        :param chain: Unique identifier for a trusted root cert chain.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if authorization is not given to caller.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a trusted root certificate chain does not exist for given id.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``CertificateManagement.Manage`` and
              ``CertificateManagement.Administer``.
        """
        return self._invoke('delete',
                            {
                            'chain': chain,
                            })
class Tls(VapiInterface):
    """
    The ``Tls`` interface provides methods to replace Tls certificate. This
    class was added in vSphere API 6.7.2.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.certificate_management.vcenter.tls'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TlsStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``Tls.Info`` class contains information from a TLS certificate. This
        class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'is_CA': 'is_ca',
                                }

        def __init__(self,
                     version=None,
                     serial_number=None,
                     signature_algorithm=None,
                     issuer_dn=None,
                     valid_from=None,
                     valid_to=None,
                     subject_dn=None,
                     thumbprint=None,
                     is_ca=None,
                     path_length_constraint=None,
                     key_usage=None,
                     extended_key_usage=None,
                     subject_alternative_name=None,
                     authority_information_access_uri=None,
                     cert=None,
                    ):
            """
            :type  version: :class:`long`
            :param version: Version (version number) value from the certificate. This attribute
                was added in vSphere API 6.7.2.
            :type  serial_number: :class:`str`
            :param serial_number: SerialNumber value from the certificate. This attribute was added
                in vSphere API 6.7.2.
            :type  signature_algorithm: :class:`str`
            :param signature_algorithm: Signature algorithm name from the certificate. This attribute was
                added in vSphere API 6.7.2.
            :type  issuer_dn: :class:`str`
            :param issuer_dn: Issuer (issuer distinguished name) value from the certificate. This
                attribute was added in vSphere API 6.7.2.
            :type  valid_from: :class:`datetime.datetime`
            :param valid_from: validFrom specify the start date of the certificate. This attribute
                was added in vSphere API 6.7.2.
            :type  valid_to: :class:`datetime.datetime`
            :param valid_to: validTo specify the end date of the certificate. This attribute was
                added in vSphere API 6.7.2.
            :type  subject_dn: :class:`str`
            :param subject_dn: Subject (subject distinguished name) value from the certificate.
                This attribute was added in vSphere API 6.7.2.
            :type  thumbprint: :class:`str`
            :param thumbprint: Thumbprint value from the certificate. This attribute was added in
                vSphere API 6.7.2.
            :type  is_ca: :class:`bool`
            :param is_ca: Certificate constraints isCA from the critical BasicConstraints
                extension, (OID = 2.5.29.19). This attribute was added in vSphere
                API 6.7.2.
            :type  path_length_constraint: :class:`long`
            :param path_length_constraint: Certificate constraints path length from the critical
                BasicConstraints extension, (OID = 2.5.29.19). This attribute was
                added in vSphere API 6.7.2.
            :type  key_usage: :class:`list` of :class:`str`
            :param key_usage: Collection of keyusage contained in the certificate. This attribute
                was added in vSphere API 6.7.2.
            :type  extended_key_usage: :class:`list` of :class:`str`
            :param extended_key_usage: Collection of extended keyusage that contains details for which the
                certificate can be used for. This attribute was added in vSphere
                API 6.7.2.
            :type  subject_alternative_name: :class:`list` of :class:`str`
            :param subject_alternative_name: Collection of subject alternative names. This attribute was added
                in vSphere API 6.7.2.
            :type  authority_information_access_uri: :class:`list` of :class:`str`
            :param authority_information_access_uri: Collection of authority information access URI. This attribute was
                added in vSphere API 6.7.2.
            :type  cert: :class:`str`
            :param cert: TLS certificate in PEM format. This attribute was added in vSphere
                API 6.7.2.
            """
            self.version = version
            self.serial_number = serial_number
            self.signature_algorithm = signature_algorithm
            self.issuer_dn = issuer_dn
            self.valid_from = valid_from
            self.valid_to = valid_to
            self.subject_dn = subject_dn
            self.thumbprint = thumbprint
            self.is_ca = is_ca
            self.path_length_constraint = path_length_constraint
            self.key_usage = key_usage
            self.extended_key_usage = extended_key_usage
            self.subject_alternative_name = subject_alternative_name
            self.authority_information_access_uri = authority_information_access_uri
            self.cert = cert
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.tls.info', {
            'version': type.IntegerType(),
            'serial_number': type.StringType(),
            'signature_algorithm': type.StringType(),
            'issuer_dn': type.StringType(),
            'valid_from': type.DateTimeType(),
            'valid_to': type.DateTimeType(),
            'subject_dn': type.StringType(),
            'thumbprint': type.StringType(),
            'is_CA': type.BooleanType(),
            'path_length_constraint': type.IntegerType(),
            'key_usage': type.ListType(type.StringType()),
            'extended_key_usage': type.ListType(type.StringType()),
            'subject_alternative_name': type.ListType(type.StringType()),
            'authority_information_access_uri': type.ListType(type.StringType()),
            'cert': type.StringType(),
        },
        Info,
        False,
        None))


    class Spec(VapiStruct):
        """
        The ``Tls.Spec`` class contains information for a Certificate and Private
        Key. This class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     cert=None,
                     key=None,
                     root_cert=None,
                    ):
            """
            :type  cert: :class:`str`
            :param cert: Certificate string in PEM format. This attribute was added in
                vSphere API 6.7.2.
            :type  key: :class:`str` or ``None``
            :param key: Private key string in PEM format. This attribute was added in
                vSphere API 6.7.2.
                If None the private key from the certificate store will be used. It
                is required when replacing the certificate with a third party
                signed certificate.
            :type  root_cert: :class:`str` or ``None``
            :param root_cert: Third party Root CA certificate in PEM format. This attribute was
                added in vSphere API 6.9.1.
                If None the new third party root CA certificate will not be added
                to the trust store. It is required when replacing the certificate
                with a third party signed certificate if the root certificate of
                the third party is not already a trusted root.
            """
            self.cert = cert
            self.key = key
            self.root_cert = root_cert
            VapiStruct.__init__(self)


    Spec._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.tls.spec', {
            'cert': type.StringType(),
            'key': type.OptionalType(type.SecretType()),
            'root_cert': type.OptionalType(type.StringType()),
        },
        Spec,
        False,
        None))


    class ReplaceSpec(VapiStruct):
        """
        The ``Tls.ReplaceSpec`` class contains information to generate a Private
        Key , CSR and hence VMCA signed machine SSL. This class was added in
        vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     key_size=None,
                     common_name=None,
                     organization=None,
                     organization_unit=None,
                     locality=None,
                     state_or_province=None,
                     country=None,
                     email_address=None,
                     subject_alt_name=None,
                    ):
            """
            :type  key_size: :class:`long` or ``None``
            :param key_size: The size of the key to be used for public and private key
                generation. This attribute was added in vSphere API 6.7.2.
                If None the key size will be '2048'.
            :type  common_name: :class:`str` or ``None``
            :param common_name: The common name of the host for which certificate is generated.
                This attribute was added in vSphere API 6.7.2.
                If None will default to PNID of host.
            :type  organization: :class:`str`
            :param organization: Organization field in certificate subject. This attribute was added
                in vSphere API 6.7.2.
            :type  organization_unit: :class:`str`
            :param organization_unit: Organization unit field in certificate subject. This attribute was
                added in vSphere API 6.7.2.
            :type  locality: :class:`str`
            :param locality: Locality field in certificate subject. This attribute was added in
                vSphere API 6.7.2.
            :type  state_or_province: :class:`str`
            :param state_or_province: State field in certificate subject. This attribute was added in
                vSphere API 6.7.2.
            :type  country: :class:`str`
            :param country: Country field in certificate subject. This attribute was added in
                vSphere API 6.7.2.
            :type  email_address: :class:`str`
            :param email_address: Email field in Certificate extensions. This attribute was added in
                vSphere API 6.7.2.
            :type  subject_alt_name: :class:`list` of :class:`str` or ``None``
            :param subject_alt_name: SubjectAltName is list of Dns Names and Ip addresses. This
                attribute was added in vSphere API 6.7.2.
                If None PNID of host will be used as IPAddress or Hostname for
                certificate generation .
            """
            self.key_size = key_size
            self.common_name = common_name
            self.organization = organization
            self.organization_unit = organization_unit
            self.locality = locality
            self.state_or_province = state_or_province
            self.country = country
            self.email_address = email_address
            self.subject_alt_name = subject_alt_name
            VapiStruct.__init__(self)


    ReplaceSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.tls.replace_spec', {
            'key_size': type.OptionalType(type.IntegerType()),
            'common_name': type.OptionalType(type.StringType()),
            'organization': type.StringType(),
            'organization_unit': type.StringType(),
            'locality': type.StringType(),
            'state_or_province': type.StringType(),
            'country': type.StringType(),
            'email_address': type.StringType(),
            'subject_alt_name': type.OptionalType(type.ListType(type.StringType())),
        },
        ReplaceSpec,
        False,
        None))



    def set(self,
            spec,
            ):
        """
        Replaces the rhttpproxy TLS certificate with the specified certificate.
        This method can be used in three scenarios : 
        
        #. When the CSR is created and the private key is already stored, this
           method can replace the certificate. The certificate but not the private
           key and root certificate must be provided as input.
        #. When the certificate is signed by a third party certificate
           authority/VMCA and the root certificate of the third party certificate
           authority/VMCA is already one of the trusted roots in the trust store,
           this method can replace the certificate and private key. The
           certificate and the private key but not the root certificate must be
           provided as input.
        #. When the certificate is signed by a third party certificate
           authority and the root certificate of the third party certificate
           authority is not one of the trusted roots in the trust store, this
           method can replace the certificate, private key and root CA
           certificate. The certificate, private key and root certificate must be
           provided as input.
        
        After this method completes, the services using the certificate will be
        restarted for the new certificate to take effect. 
        
        The above three scenarios are only supported from vsphere 7.0 onwards..
        This method was added in vSphere API 6.7.2.

        :type  spec: :class:`Tls.Spec`
        :param spec: The information needed to replace the TLS certificate.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the private key is not present in the VECS store.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            If the specified certificate thumbprint is the same as the existing
            TLS certificate thumbprint.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If the system failed to replace the TLS certificate.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``CertificateManagement.Administer``.
        """
        return self._invoke('set',
                            {
                            'spec': spec,
                            })

    def get(self):
        """
        Returns the rhttpproxy TLS certificate. This method was added in
        vSphere API 6.7.2.


        :rtype: :class:`Tls.Info`
        :return: TLS certificate.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the rhttpproxy certificate is not present in VECS store.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if failed due to generic exception.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('get', None)

    def renew(self,
              duration=None,
              ):
        """
        Renews the TLS certificate for the given duration period. 
        
        After this method completes, the services using the certificate will be
        restarted for the new certificate to take effect.. This method was
        added in vSphere API 6.7.2.

        :type  duration: :class:`long` or ``None``
        :param duration: The duration (in days) of the new TLS certificate. The duration
            should be less than or equal to 730 days.
            If None, the duration will be 730 days (two years).
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            If the TLS certificate is not VMCA generated.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the duration period specified is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If the system failed to renew the TLS certificate.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``CertificateManagement.Administer``.
        """
        return self._invoke('renew',
                            {
                            'duration': duration,
                            })

    def replace_vmca_signed(self,
                            spec,
                            ):
        """
        Replace MACHINE SSL with VMCA signed one with the given Spec.The system
        will go for restart. 
        
        After this method completes, the services using the certificate will be
        restarted for the new certificate to take effect.. This method was
        added in vSphere API 6.9.1.

        :type  spec: :class:`Tls.ReplaceSpec`
        :param spec: The information needed to generate VMCA signed Machine SSL
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the Spec given is not complete or invalid
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If the system failed to replace the machine ssl certificate
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``CertificateManagement.Administer``.
        """
        return self._invoke('replace_vmca_signed',
                            {
                            'spec': spec,
                            })
class TlsCsr(VapiInterface):
    """
    The ``TlsCsr`` interface provides methods to generate certificate signing
    request. This class was added in vSphere API 6.7.2.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.certificate_management.vcenter.tls_csr'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TlsCsrStub)
        self._VAPI_OPERATION_IDS = {}

    class Info(VapiStruct):
        """
        The ``TlsCsr.Info`` class contains information for a Certificate signing
        request. This class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     csr=None,
                    ):
            """
            :type  csr: :class:`str`
            :param csr: Certificate Signing Request in PEM format. This attribute was added
                in vSphere API 6.7.2.
            """
            self.csr = csr
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.tls_csr.info', {
            'csr': type.StringType(),
        },
        Info,
        False,
        None))


    class Spec(VapiStruct):
        """
        The ``TlsCsr.Spec`` class contains information to generate a Private Key
        and CSR. This class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     key_size=None,
                     common_name=None,
                     organization=None,
                     organization_unit=None,
                     locality=None,
                     state_or_province=None,
                     country=None,
                     email_address=None,
                     subject_alt_name=None,
                    ):
            """
            :type  key_size: :class:`long` or ``None``
            :param key_size: This attribute was added in vSphere API 6.7.2.
                keySize will take 2048 bits if not modified.
            :type  common_name: :class:`str` or ``None``
            :param common_name: This attribute was added in vSphere API 6.7.2.
                commonName will take PNID if not modified.
            :type  organization: :class:`str`
            :param organization: Organization field in certificate subject. This attribute was added
                in vSphere API 6.7.2.
            :type  organization_unit: :class:`str`
            :param organization_unit: Organization unit field in certificate subject. This attribute was
                added in vSphere API 6.7.2.
            :type  locality: :class:`str`
            :param locality: Locality field in certificate subject. This attribute was added in
                vSphere API 6.7.2.
            :type  state_or_province: :class:`str`
            :param state_or_province: State field in certificate subject. This attribute was added in
                vSphere API 6.7.2.
            :type  country: :class:`str`
            :param country: Country field in certificate subject. This attribute was added in
                vSphere API 6.7.2.
            :type  email_address: :class:`str`
            :param email_address: Email field in Certificate extensions. This attribute was added in
                vSphere API 6.7.2.
            :type  subject_alt_name: :class:`list` of :class:`str` or ``None``
            :param subject_alt_name: This attribute was added in vSphere API 6.7.2.
                subjectAltName is list of Dns Names and Ip addresses
            """
            self.key_size = key_size
            self.common_name = common_name
            self.organization = organization
            self.organization_unit = organization_unit
            self.locality = locality
            self.state_or_province = state_or_province
            self.country = country
            self.email_address = email_address
            self.subject_alt_name = subject_alt_name
            VapiStruct.__init__(self)


    Spec._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.tls_csr.spec', {
            'key_size': type.OptionalType(type.IntegerType()),
            'common_name': type.OptionalType(type.StringType()),
            'organization': type.StringType(),
            'organization_unit': type.StringType(),
            'locality': type.StringType(),
            'state_or_province': type.StringType(),
            'country': type.StringType(),
            'email_address': type.StringType(),
            'subject_alt_name': type.OptionalType(type.ListType(type.StringType())),
        },
        Spec,
        False,
        None))



    def create(self,
               spec,
               ):
        """
        Generates a CSR with the given Spec. This method was added in vSphere
        API 6.7.2.

        :type  spec: :class:`TlsCsr.Spec`
        :param spec: The information needed to create a CSR.
        :rtype: :class:`TlsCsr.Info`
        :return: A Certificate Signing Request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If CSR could not be created for given spec for a generic error.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``CertificateManagement.Manage`` and
              ``CertificateManagement.Administer``.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })
class VmcaRoot(VapiInterface):
    """
    The ``VmcaRoot`` interface provides methods to replace VMware Certificate
    Authority (VMCA) root certificate. This class was added in vSphere API
    6.9.1.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.certificate_management.vcenter.vmca_root'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VmcaRootStub)
        self._VAPI_OPERATION_IDS = {}

    class CreateSpec(VapiStruct):
        """
        The ``VmcaRoot.CreateSpec`` contains information. to generate a Private Key
        and CSR. This class was added in vSphere API 6.9.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     key_size=None,
                     common_name=None,
                     organization=None,
                     organization_unit=None,
                     locality=None,
                     state_or_province=None,
                     country=None,
                     email_address=None,
                     subject_alt_name=None,
                    ):
            """
            :type  key_size: :class:`long` or ``None``
            :param key_size: The size of the key to be used for public and private key
                generation. This attribute was added in vSphere API 6.9.1.
                If None the key size will be 2048.
            :type  common_name: :class:`str` or ``None``
            :param common_name: The common name of the host for which certificate is generated.
                This attribute was added in vSphere API 6.9.1.
                If None the common name will be the primary network identifier
                (PNID) of the vCenter Virtual Server Appliance (VCSA).
            :type  organization: :class:`str` or ``None``
            :param organization: Organization field in certificate subject. This attribute was added
                in vSphere API 6.9.1.
                If None the organization will be 'VMware'.
            :type  organization_unit: :class:`str` or ``None``
            :param organization_unit: Organization unit field in certificate subject. This attribute was
                added in vSphere API 6.9.1.
                If None the organization unit will be 'VMware Engineering'.
            :type  locality: :class:`str` or ``None``
            :param locality: Locality field in certificate subject. This attribute was added in
                vSphere API 6.9.1.
                If None the locality will be 'Palo Alto'.
            :type  state_or_province: :class:`str` or ``None``
            :param state_or_province: State field in certificate subject. This attribute was added in
                vSphere API 6.9.1.
                If None the state will be 'California'.
            :type  country: :class:`str` or ``None``
            :param country: Country field in certificate subject. This attribute was added in
                vSphere API 6.9.1.
                If None the country will be 'US'.
            :type  email_address: :class:`str` or ``None``
            :param email_address: Email field in Certificate extensions. This attribute was added in
                vSphere API 6.9.1.
                If None the emailAddress will be 'email\\\\@acme.com'.
            :type  subject_alt_name: :class:`list` of :class:`str` or ``None``
            :param subject_alt_name: SubjectAltName is list of Dns Names and Ip addresses. This
                attribute was added in vSphere API 6.9.1.
                If None PNID of host will be used as IPAddress or Hostname for
                certificate generation.
            """
            self.key_size = key_size
            self.common_name = common_name
            self.organization = organization
            self.organization_unit = organization_unit
            self.locality = locality
            self.state_or_province = state_or_province
            self.country = country
            self.email_address = email_address
            self.subject_alt_name = subject_alt_name
            VapiStruct.__init__(self)


    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.certificate_management.vcenter.vmca_root.create_spec', {
            'key_size': type.OptionalType(type.IntegerType()),
            'common_name': type.OptionalType(type.StringType()),
            'organization': type.OptionalType(type.StringType()),
            'organization_unit': type.OptionalType(type.StringType()),
            'locality': type.OptionalType(type.StringType()),
            'state_or_province': type.OptionalType(type.StringType()),
            'country': type.OptionalType(type.StringType()),
            'email_address': type.OptionalType(type.StringType()),
            'subject_alt_name': type.OptionalType(type.ListType(type.StringType())),
        },
        CreateSpec,
        False,
        None))



    def create(self,
               spec=None,
               ):
        """
        Replace Root Certificate with VMCA signed one using the given Spec. 
        
        After this method completes, the services using the certificate will be
        restarted for the new certificate to take effect.. This method was
        added in vSphere API 6.9.1.

        :type  spec: :class:`VmcaRoot.CreateSpec` or ``None``
        :param spec: The information needed to generate VMCA signed Root Certificate.
            Default values will be set for all null parameters.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If the system failed to renew the TLS certificate.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``CertificateManagement.Administer``.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })
class _TrustedRootChainsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/certificate-management/vcenter/trusted-root-chains',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'TrustedRootChains.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/certificate-management/vcenter/trusted-root-chains',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'chain': type.StringType(),
        })
        get_error_dict = {
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
            url_template='/vcenter/certificate-management/vcenter/trusted-root-chains/{chain}',
            path_variables={
                'chain': 'chain',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'chain': type.StringType(),
        })
        delete_error_dict = {
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
            url_template='/vcenter/certificate-management/vcenter/trusted-root-chains/{chain}',
            path_variables={
                'chain': 'chain',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'TrustedRootChains.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.StringType(),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'TrustedRootChains.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.certificate_management.vcenter.trusted_root_chains',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _TlsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Tls.Spec'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/vcenter/certificate-management/vcenter/tls',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/certificate-management/vcenter/tls',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for renew operation
        renew_input_type = type.StructType('operation-input', {
            'duration': type.OptionalType(type.IntegerType()),
        })
        renew_error_dict = {
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        renew_input_value_validator_list = [
        ]
        renew_output_validator_list = [
        ]
        renew_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/certificate-management/vcenter/tls',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for replace_vmca_signed operation
        replace_vmca_signed_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Tls.ReplaceSpec'),
        })
        replace_vmca_signed_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        replace_vmca_signed_input_value_validator_list = [
        ]
        replace_vmca_signed_output_validator_list = [
        ]
        replace_vmca_signed_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/certificate-management/vcenter/tls?action=replace-vmca-signed',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_value_validator_list': set_input_value_validator_list,
                'output_validator_list': set_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Tls.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'renew': {
                'input_type': renew_input_type,
                'output_type': type.VoidType(),
                'errors': renew_error_dict,
                'input_value_validator_list': renew_input_value_validator_list,
                'output_validator_list': renew_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'replace_vmca_signed': {
                'input_type': replace_vmca_signed_input_type,
                'output_type': type.VoidType(),
                'errors': replace_vmca_signed_error_dict,
                'input_value_validator_list': replace_vmca_signed_input_value_validator_list,
                'output_validator_list': replace_vmca_signed_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'set': set_rest_metadata,
            'get': get_rest_metadata,
            'renew': renew_rest_metadata,
            'replace_vmca_signed': replace_vmca_signed_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.certificate_management.vcenter.tls',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _TlsCsrStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'TlsCsr.Spec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/certificate-management/vcenter/tls-csr',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType(__name__, 'TlsCsr.Info'),
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
            self, iface_name='com.vmware.vcenter.certificate_management.vcenter.tls_csr',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _VmcaRootStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.OptionalType(type.ReferenceType(__name__, 'VmcaRoot.CreateSpec')),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/certificate-management/vcenter/vmca-root',
            path_variables={
            },
            query_parameters={
            }
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
        }
        rest_metadata = {
            'create': create_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.certificate_management.vcenter.vmca_root',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'TrustedRootChains': TrustedRootChains,
        'Tls': Tls,
        'TlsCsr': TlsCsr,
        'VmcaRoot': VmcaRoot,
    }

