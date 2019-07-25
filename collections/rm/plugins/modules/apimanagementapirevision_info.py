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
module: apimanagementapirevision_info
version_added: '2.9'
short_description: Get ApiRevision info.
description:
  - Get info of ApiRevision.
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
  api_id:
    description:
      - >-
        API identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  value:
    description:
      - Page values.
    type: list
    suboptions:
      api_id:
        description:
          - Identifier of the API Revision.
        type: str
      api_revision:
        description:
          - Revision number of API.
        type: str
      created_date_time:
        description:
          - >-
            The time the API Revision was created. The date conforms to the
            following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601
            standard.
        type: datetime
      updated_date_time:
        description:
          - >-
            The time the API Revision were updated. The date conforms to the
            following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601
            standard.
        type: datetime
      description:
        description:
          - Description of the API Revision.
        type: str
      private_url:
        description:
          - Gateway URL for accessing the non-current API Revision.
        type: str
      is_online:
        description:
          - Indicates if API revision is the current api revision.
        type: boolean
      is_current:
        description:
          - Indicates if API revision is accessible via the gateway.
        type: boolean
  next_link:
    description:
      - Next page link if any.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiRevisions
  azure.rm.apimanagementapirevision.info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi

'''

RETURN = '''
api_revision:
  description: >-
    A list of dict results where the key is the name of the ApiRevision and the
    values are the facts for that ApiRevision.
  returned: always
  type: complex
  contains:
    apirevision_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - Page values.
          returned: always
          type: dict
          sample: null
          contains:
            api_id:
              description:
                - Identifier of the API Revision.
              returned: always
              type: str
              sample: null
            api_revision:
              description:
                - Revision number of API.
              returned: always
              type: str
              sample: null
            created_date_time:
              description:
                - >-
                  The time the API Revision was created. The date conforms to
                  the following format: yyyy-MM-ddTHH:mm:ssZ as specified by the
                  ISO 8601 standard.
              returned: always
              type: datetime
              sample: null
            updated_date_time:
              description:
                - >-
                  The time the API Revision were updated. The date conforms to
                  the following format: yyyy-MM-ddTHH:mm:ssZ as specified by the
                  ISO 8601 standard.
              returned: always
              type: datetime
              sample: null
            description:
              description:
                - Description of the API Revision.
              returned: always
              type: str
              sample: null
            private_url:
              description:
                - Gateway URL for accessing the non-current API Revision.
              returned: always
              type: str
              sample: null
            is_online:
              description:
                - Indicates if API revision is the current api revision.
              returned: always
              type: boolean
              sample: null
            is_current:
              description:
                - Indicates if API revision is accessible via the gateway.
              returned: always
              type: boolean
              sample: null
        next_link:
          description:
            - Next page link if any.
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


class AzureRMApiRevisionInfo(AzureRMModuleBase):
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
            api_id=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
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
        super(AzureRMApiRevisionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.api_id is not None):
            self.results['api_revision'] = self.format_item(self.listbyservice())
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
                    '/apis' +
                    '/{{ api_name }}' +
                    '/revisions')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ api_name }}', self.name)

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
    AzureRMApiRevisionInfo()


if __name__ == '__main__':
    main()
