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
module: apimanagementemailtemplate
version_added: '2.9'
short_description: Manage Azure EmailTemplate instance.
description:
  - 'Create, update and delete instance of Azure EmailTemplate.'
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
      - Resource name.
    type: str
  subject:
    description:
      - Subject of the Template.
    type: str
  title:
    description:
      - Title of the Template.
    type: str
  description:
    description:
      - Description of the Email Template.
    type: str
  body:
    description:
      - Email Template Body. This should be a valid XDocument
    type: str
  parameters:
    description:
      - Email Template Parameter values.
    type: list
    suboptions:
      name:
        description:
          - Template parameter name.
        type: str
      title:
        description:
          - Template parameter title.
        type: str
      description:
        description:
          - Template parameter description.
        type: str
  is_default:
    description:
      - >-
        Whether the template is the default template provided by Api Management
        or has been edited.
    type: boolean
  id:
    description:
      - Resource ID.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  state:
    description:
      - Assert the state of the EmailTemplate.
      - >-
        Use C(present) to create or update an EmailTemplate and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementCreateEmailTemplate
  azure.rm.apimanagementemailtemplate:
    resource_group: myResourceGroup
    service_name: myService
    name: myTemplate
    subject: Your request for $IssueName was successfully received.
- name: ApiManagementUpdateEmailTemplate
  azure.rm.apimanagementemailtemplate:
    resource_group: myResourceGroup
    service_name: myService
    name: myTemplate
    subject: Your application $AppName is published in the gallery
    body: "<!DOCTYPE html >\r\n<html>\r\n  <head />\r\n  <body>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Dear $DevFirstName $DevLastName,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">\r\n          We are happy to let you know that your request to publish the $AppName application in the gallery has been approved. Your application has been published and can be viewed <a href=\"http://$DevPortalUrl/Applications/Details/$AppId\">here</a>.\r\n        </p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Best,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">The $OrganizationName API Team</p>\r\n  </body>\r\n</html>"
- name: ApiManagementDeleteEmailTemplate
  azure.rm.apimanagementemailtemplate:
    resource_group: myResourceGroup
    service_name: myService
    name: myTemplate
    state: absent

'''

RETURN = '''
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
    - Resource type for API Management resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Email Template entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    subject:
      description:
        - Subject of the Template.
      returned: always
      type: str
      sample: null
    body:
      description:
        - Email Template Body. This should be a valid XDocument
      returned: always
      type: str
      sample: null
    title:
      description:
        - Title of the Template.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Description of the Email Template.
      returned: always
      type: str
      sample: null
    is_default:
      description:
        - >-
          Whether the template is the default template provided by Api
          Management or has been edited.
      returned: always
      type: boolean
      sample: null
    parameters:
      description:
        - Email Template Parameter values.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Template parameter name.
          returned: always
          type: str
          sample: null
        title:
          description:
            - Template parameter title.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Template parameter description.
          returned: always
          type: str
          sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMEmailTemplate(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                disposition='serviceName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='templateName',
                required=true
            ),
            subject=dict(
                type='str',
                disposition='/properties/*'
            ),
            title=dict(
                type='str',
                disposition='/properties/*'
            ),
            description=dict(
                type='str',
                disposition='/properties/*'
            ),
            body=dict(
                type='str',
                disposition='/properties/*'
            ),
            parameters=dict(
                type='list',
                disposition='/properties/*',
                options=dict(
                    name=dict(
                        type='str'
                    ),
                    title=dict(
                        type='str'
                    ),
                    description=dict(
                        type='str'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMEmailTemplate, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                   supports_check_mode=True,
                                                   supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/templates' +
                    '/{{ template_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ template_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("EmailTemplate instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('EmailTemplate instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the EmailTemplate instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('EmailTemplate instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('EmailTemplate instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the EmailTemplate instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the EmailTemplate instance.')
            self.fail('Error creating the EmailTemplate instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the EmailTemplate instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the EmailTemplate instance.')
            self.fail('Error deleting the EmailTemplate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the EmailTemplate instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("EmailTemplate instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the EmailTemplate instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMEmailTemplate()


if __name__ == '__main__':
    main()
