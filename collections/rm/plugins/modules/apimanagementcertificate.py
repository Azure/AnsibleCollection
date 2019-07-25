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
module: apimanagementcertificate
version_added: '2.9'
short_description: Manage Azure Certificate instance.
description:
  - 'Create, update and delete instance of Azure Certificate.'
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
  certificate_id:
    description:
      - >-
        Identifier of the certificate entity. Must be unique in the current API
        Management service instance.
    required: true
    type: str
  data:
    description:
      - >-
        Base 64 encoded certificate using the application/x-pkcs12
        representation.
    required: true
    type: str
  password:
    description:
      - Password for the Certificate
    required: true
    type: str
  subject:
    description:
      - Subject attribute of the certificate.
    required: true
    type: str
  thumbprint:
    description:
      - Thumbprint of the certificate.
    required: true
    type: str
  expiration_date:
    description:
      - >-
        Expiration date of the certificate. The date conforms to the following
        format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
        standard.<br>
    required: true
    type: datetime
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
      - Resource type for API Management resource.
    type: str
  state:
    description:
      - Assert the state of the Certificate.
      - >-
        Use C(present) to create or update an Certificate and C(absent) to
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
- name: ApiManagementCreateCertificate
  azure.rm.apimanagementcertificate:
    resource_group: myResourceGroup
    service_name: myService
    certificate_id: myCertificate
    data: >-
      ****************Base 64 Encoded Certificate
      *******************************
    password: '****Certificate Password******'
- name: ApiManagementDeleteCertificate
  azure.rm.apimanagementcertificate:
    resource_group: myResourceGroup
    service_name: myService
    certificate_id: myCertificate
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
    - Certificate properties details.
  returned: always
  type: dict
  sample: null
  contains:
    subject:
      description:
        - Subject attribute of the certificate.
      returned: always
      type: str
      sample: null
    thumbprint:
      description:
        - Thumbprint of the certificate.
      returned: always
      type: str
      sample: null
    expiration_date:
      description:
        - >-
          Expiration date of the certificate. The date conforms to the following
          format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
          standard.<br>
      returned: always
      type: datetime
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCertificate(AzureRMModuleBaseExt):
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
            certificate_id=dict(
                type='str',
                updatable=False,
                disposition='certificateId',
                required=true
            ),
            data=dict(
                type='str',
                disposition='/properties/*',
                required=true
            ),
            password=dict(
                type='str',
                no_log=True,
                disposition='/properties/*',
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.certificate_id = None
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

        super(AzureRMCertificate, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/certificates' +
                    '/{{ certificate_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ certificate_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("Certificate instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Certificate instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the Certificate instance')

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
            self.log('Certificate instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Certificate instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Certificate instance {0}'.format(self.))

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
            self.log('Error attempting to create the Certificate instance.')
            self.fail('Error creating the Certificate instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Certificate instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Certificate instance.')
            self.fail('Error deleting the Certificate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Certificate instance {0} is present'.format(self.))
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
            # self.log("Certificate instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Certificate instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMCertificate()


if __name__ == '__main__':
    main()
