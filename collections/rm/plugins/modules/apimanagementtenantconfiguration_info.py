#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: apimanagementtenantconfiguration_info
version_added: '2.9'
short_description: Get TenantConfiguration info.
description:
  - Get info of TenantConfiguration.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  name:
    description:
      - The identifier of the Git Configuration Operation.
    required: true
    type: str
  branch:
    description:
      - The name of Git branch.
    type: str
  commit_id:
    description:
      - The latest commit Id.
    type: str
  is_export:
    description:
      - >-
        value indicating if last sync was save (true) or deploy (false)
        operation.
    type: boolean
  is_synced:
    description:
      - >-
        value indicating if last synchronization was later than the
        configuration change.
    type: boolean
  is_git_enabled:
    description:
      - value indicating whether Git configuration access is enabled.
    type: boolean
  sync_date:
    description:
      - >-
        The date of the latest synchronization. The date conforms to the
        following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
        standard.<br>
    type: datetime
  configuration_change_date:
    description:
      - >-
        The date of the latest configuration change. The date conforms to the
        following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
        standard.<br>
    type: datetime
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementTenantAccessSyncState
  azure.rm.apimanagementtenantconfiguration.info:
    resource_group: myResourceGroup
    service_name: myService
    name: myTenant

'''

RETURN = '''
tenant_configuration:
  description: >-
    A list of dict results where the key is the name of the TenantConfiguration
    and the values are the facts for that TenantConfiguration.
  returned: always
  type: complex
  contains:
    tenantconfiguration_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        branch:
          description:
            - The name of Git branch.
          returned: always
          type: str
          sample: null
        commit_id:
          description:
            - The latest commit Id.
          returned: always
          type: str
          sample: null
        is_export:
          description:
            - >-
              value indicating if last sync was save (true) or deploy (false)
              operation.
          returned: always
          type: boolean
          sample: null
        is_synced:
          description:
            - >-
              value indicating if last synchronization was later than the
              configuration change.
          returned: always
          type: boolean
          sample: null
        is_git_enabled:
          description:
            - value indicating whether Git configuration access is enabled.
          returned: always
          type: boolean
          sample: null
        sync_date:
          description:
            - >-
              The date of the latest synchronization. The date conforms to the
              following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
              8601 standard.<br>
          returned: always
          type: datetime
          sample: null
        configuration_change_date:
          description:
            - >-
              The date of the latest configuration change. The date conforms to
              the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the
              ISO 8601 standard.<br>
          returned: always
          type: datetime
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMTenantConfigurationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            service_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.service_name = None
        self.name = None
        self.branch = None
        self.commit_id = None
        self.is_export = None
        self.is_synced = None
        self.is_git_enabled = None
        self.sync_date = None
        self.configuration_change_date = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTenantConfigurationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.name is not None):
            self.results['tenant_configuration'] = self.format_item(self.getsyncstate())
        return self.results

    def getsyncstate(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/tenant' +
                    '/{{ tenant_name }}' +
                    '/syncState')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ tenant_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMTenantConfigurationInfo()


if __name__ == '__main__':
    main()
