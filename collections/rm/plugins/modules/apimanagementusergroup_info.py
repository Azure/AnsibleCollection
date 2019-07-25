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
module: apimanagementusergroup_info
version_added: '2.9'
short_description: Get UserGroup info.
description:
  - Get info of UserGroup.
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
  user_id:
    description:
      - >-
        User identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  value:
    description:
      - Page values.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Group type.
        type: str
      display_name:
        description:
          - Group name.
        required: true
        type: str
      description:
        description:
          - Group description. Can contain HTML formatting tags.
        type: str
      built_in:
        description:
          - >-
            true if the group is one of the three system groups (Administrators,
            Developers, or Guests); otherwise false.
        type: boolean
      external_id:
        description:
          - >-
            For external groups, this property contains the id of the group from
            the external identity provider, e.g. for Azure Active Directory
            `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise
            the value is null.
        type: str
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
- name: ApiManagementListUserGroups
  azure.rm.apimanagementusergroup.info:
    resource_group: myResourceGroup
    service_name: myService
    user_id: myUser

'''

RETURN = '''
user_group:
  description: >-
    A list of dict results where the key is the name of the UserGroup and the
    values are the facts for that UserGroup.
  returned: always
  type: complex
  contains:
    usergroup_name:
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
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
            name:
              description:
                - Resource name.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Group type.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Group entity contract properties.
              returned: always
              type: dict
              sample: null
            display_name:
              description:
                - Group name.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Group description. Can contain HTML formatting tags.
              returned: always
              type: str
              sample: null
            built_in:
              description:
                - >-
                  true if the group is one of the three system groups
                  (Administrators, Developers, or Guests); otherwise false.
              returned: always
              type: boolean
              sample: null
            external_id:
              description:
                - >-
                  For external groups, this property contains the id of the
                  group from the external identity provider, e.g. for Azure
                  Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group
                  object id>`; otherwise the value is null.
              returned: always
              type: str
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


class AzureRMUserGroupInfo(AzureRMModuleBase):
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
            user_id=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.service_name = None
        self.user_id = None
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
        super(AzureRMUserGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.user_id is not None):
            self.results['user_group'] = self.format_item(self.list())
        return self.results

    def list(self):
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
                    '/users' +
                    '/{{ user_name }}' +
                    '/groups')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ user_name }}', self.name)

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
    AzureRMUserGroupInfo()


if __name__ == '__main__':
    main()
