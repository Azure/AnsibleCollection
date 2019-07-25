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
module: apimanagementpolicysnippet_info
version_added: '2.9'
short_description: Get PolicySnippet info.
description:
  - Get info of PolicySnippet.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  scope:
    description:
      - Policy scope.
    required: true
    type: str
  value:
    description:
      - Policy snippet value.
    type: list
    suboptions:
      name:
        description:
          - Snippet name.
        type: str
      content:
        description:
          - Snippet content.
        type: str
      tool_tip:
        description:
          - Snippet toolTip.
        type: str
      scope:
        description:
          - Binary OR value of the Snippet scope.
        type: number
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListPolicySnippets
  azure.rm.apimanagementpolicysnippet.info:
    resource_group: myResourceGroup
    name: myService
    scope: Api

'''

RETURN = '''
policy_snippet:
  description: >-
    A list of dict results where the key is the name of the PolicySnippet and
    the values are the facts for that PolicySnippet.
  returned: always
  type: complex
  contains:
    policysnippet_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - Policy snippet value.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Snippet name.
              returned: always
              type: str
              sample: null
            content:
              description:
                - Snippet content.
              returned: always
              type: str
              sample: null
            tool_tip:
              description:
                - Snippet toolTip.
              returned: always
              type: str
              sample: null
            scope:
              description:
                - Binary OR value of the Snippet scope.
              returned: always
              type: number
              sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMPolicySnippetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            ),
            scope=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.name = None
        self.scope = None
        self.value = None

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
        super(AzureRMPolicySnippetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['policy_snippet'] = self.format_item(self.listbyservice())
        return self.results

    def listbyservice(self):
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
                    '/policySnippets')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.name)

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
    AzureRMPolicySnippetInfo()


if __name__ == '__main__':
    main()
