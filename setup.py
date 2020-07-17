#!/usr/bin/env python

import os

# CHANGED: Added find_packages inport
from setuptools import setup, find_packages

# CHANGED: Renamed to vsphere-automation-sdk
setup(name='vsphere-automation-sdk',
      # CHANGED: Make sure this is the version from github
      version='1.31.0',
      description='VMware vSphere Automation SDK for Python',
      url='https://github.com/vmware/vsphere-automation-sdk-python',
      author='VMware, Inc.',
      license='MIT',
      # CHANGED: Added find_packages statement to include copde
      packages=find_packages(),
      # CHANGED: Added this to read MANIFEST.in
      include_package_data=True,
      # CHANGED: Removed all local wheel dependencies
      install_requires=[
        'lxml >= 4.3.0',
        'suds ; python_version < "3"',
        'suds-jurko ; python_version >= "3.0"',
        'pyVmomi >= 6.7',
        'pyOpenSSL >= 18.0.0',
        'requests >= 2.21.0'
      ]
      )
