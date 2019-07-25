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
module: apimanagementservicesku_info
version_added: '2.9'
short_description: Get ApiManagementServiceSku info.
description:
  - Get info of ApiManagementServiceSku.
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
  value:
    description:
      - The list of skus available for the service.
    type: list
    suboptions:
      resource_type:
        description:
          - The type of resource the SKU applies to.
        type: str
      sku:
        description:
          - Specifies API Management SKU.
        type: dict
        suboptions:
          name:
            description:
              - Name of the Sku.
            type: str
      capacity:
        description:
          - Specifies the number of API Management units.
        type: dict
        suboptions:
          minimum:
            description:
              - The minimum capacity.
            type: number
          maximum:
            description:
              - The maximum capacity that can be set.
            type: number
          default:
            description:
              - The default capacity.
            type: number
          scale_type:
            description:
              - The scale type applicable to the sku.
            type: str
  next_link:
    description:
      - The uri to fetch the next page of API Management service Skus.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListSKUs-Dedicated
  azure.rm.apimanagementservicesku.info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementListSKUs-Consumption
  azure.rm.apimanagementservicesku.info:
    resource_group: myResourceGroup
    name: myService

'''

RETURN = '''
api_management_service_skus:
  description: >-
    A list of dict results where the key is the name of the
    ApiManagementServiceSku and the values are the facts for that
    ApiManagementServiceSku.
  returned: always
  type: complex
  contains:
    apimanagementservicesku_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - The list of skus available for the service.
          returned: always
          type: dict
          sample: null
          contains:
            resource_type:
              description:
                - The type of resource the SKU applies to.
              returned: always
              type: str
              sample: null
            sku:
              description:
                - Specifies API Management SKU.
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the Sku.
                  returned: always
                  type: str
                  sample: null
            capacity:
              description:
                - Specifies the number of API Management units.
              returned: always
              type: dict
              sample: null
              contains:
                minimum:
                  description:
                    - The minimum capacity.
                  returned: always
                  type: number
                  sample: null
                maximum:
                  description:
                    - The maximum capacity that can be set.
                  returned: always
                  type: number
                  sample: null
                default:
                  description:
                    - The default capacity.
                  returned: always
                  type: number
                  sample: null
                scale_type:
                  description:
                    - The scale type applicable to the sku.
                  returned: always
                  type: str
                  sample: null
        next_link:
          description:
            - The uri to fetch the next page of API Management service Skus.
          returned: always
          type: str
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMApiManagementServiceSkusInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.name = None
        self.value = None
        self.next_link = None

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
        super(AzureRMApiManagementServiceSkusInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['api_management_service_skus'] = self.format_item(self.listavailableserviceskus())
        return self.results

    def listavailableserviceskus(self):
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
                    '/skus')
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
    AzureRMApiManagementServiceSkusInfo()


if __name__ == '__main__':
    main()
