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
module: apimanagementproductsubscription_info
version_added: '2.9'
short_description: Get ProductSubscription info.
description:
  - Get info of ProductSubscription.
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
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
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
          - Resource type for API Management resource.
        type: str
      owner_id:
        description:
          - >-
            The user resource identifier of the subscription owner. The value is
            a valid relative URL in the format of /users/{userId} where {userId}
            is a user identifier.
        type: str
      scope:
        description:
          - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
        required: true
        type: str
      display_name:
        description:
          - >-
            The name of the subscription, or null if the subscription has no
            name.
        type: str
      state:
        description:
          - >-
            Subscription state. Possible states are * active – the subscription
            is active, * suspended – the subscription is blocked, and the
            subscriber cannot call any APIs of the product, * submitted – the
            subscription request has been made by the developer, but has not yet
            been approved or rejected, * rejected – the subscription request has
            been denied by an administrator, * cancelled – the subscription has
            been cancelled by the developer or administrator, * expired – the
            subscription reached its expiration date and was deactivated.
        required: true
        type: str
      created_date:
        description:
          - >-
            Subscription creation date. The date conforms to the following
            format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
            standard.<br>
        type: datetime
      start_date:
        description:
          - >-
            Subscription activation date. The setting is for audit purposes only
            and the subscription is not automatically activated. The
            subscription lifecycle can be managed by using the `state` property.
            The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.<br>
        type: datetime
      expiration_date:
        description:
          - >-
            Subscription expiration date. The setting is for audit purposes only
            and the subscription is not automatically expired. The subscription
            lifecycle can be managed by using the `state` property. The date
            conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.<br>
        type: datetime
      end_date:
        description:
          - >-
            Date when subscription was cancelled or expired. The setting is for
            audit purposes only and the subscription is not automatically
            cancelled. The subscription lifecycle can be managed by using the
            `state` property. The date conforms to the following format:
            `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
        type: datetime
      notification_date:
        description:
          - >-
            Upcoming subscription expiration notification date. The date
            conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.<br>
        type: datetime
      primary_key:
        description:
          - Subscription primary key.
        required: true
        type: str
      secondary_key:
        description:
          - Subscription secondary key.
        required: true
        type: str
      state_comment:
        description:
          - Optional subscription comment added by an administrator.
        type: str
      allow_tracing:
        description:
          - Determines whether tracing is enabled
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
- name: ApiManagementListProductSubscriptions
  azure.rm.apimanagementproductsubscription.info:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct

'''

RETURN = '''
product_subscriptions:
  description: >-
    A list of dict results where the key is the name of the ProductSubscription
    and the values are the facts for that ProductSubscription.
  returned: always
  type: complex
  contains:
    productsubscription_name:
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
                - Resource type for API Management resource.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Subscription contract properties.
              returned: always
              type: dict
              sample: null
            owner_id:
              description:
                - >-
                  The user resource identifier of the subscription owner. The
                  value is a valid relative URL in the format of /users/{userId}
                  where {userId} is a user identifier.
              returned: always
              type: str
              sample: null
            scope:
              description:
                - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - >-
                  The name of the subscription, or null if the subscription has
                  no name.
              returned: always
              type: str
              sample: null
            state:
              description:
                - >-
                  Subscription state. Possible states are * active – the
                  subscription is active, * suspended – the subscription is
                  blocked, and the subscriber cannot call any APIs of the
                  product, * submitted – the subscription request has been made
                  by the developer, but has not yet been approved or rejected, *
                  rejected – the subscription request has been denied by an
                  administrator, * cancelled – the subscription has been
                  cancelled by the developer or administrator, * expired – the
                  subscription reached its expiration date and was deactivated.
              returned: always
              type: str
              sample: null
            created_date:
              description:
                - >-
                  Subscription creation date. The date conforms to the following
                  format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
                  standard.<br>
              returned: always
              type: datetime
              sample: null
            start_date:
              description:
                - >-
                  Subscription activation date. The setting is for audit
                  purposes only and the subscription is not automatically
                  activated. The subscription lifecycle can be managed by using
                  the `state` property. The date conforms to the following
                  format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
                  standard.<br>
              returned: always
              type: datetime
              sample: null
            expiration_date:
              description:
                - >-
                  Subscription expiration date. The setting is for audit
                  purposes only and the subscription is not automatically
                  expired. The subscription lifecycle can be managed by using
                  the `state` property. The date conforms to the following
                  format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
                  standard.<br>
              returned: always
              type: datetime
              sample: null
            end_date:
              description:
                - >-
                  Date when subscription was cancelled or expired. The setting
                  is for audit purposes only and the subscription is not
                  automatically cancelled. The subscription lifecycle can be
                  managed by using the `state` property. The date conforms to
                  the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by
                  the ISO 8601 standard.<br>
              returned: always
              type: datetime
              sample: null
            notification_date:
              description:
                - >-
                  Upcoming subscription expiration notification date. The date
                  conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
                  specified by the ISO 8601 standard.<br>
              returned: always
              type: datetime
              sample: null
            primary_key:
              description:
                - Subscription primary key.
              returned: always
              type: str
              sample: null
            secondary_key:
              description:
                - Subscription secondary key.
              returned: always
              type: str
              sample: null
            state_comment:
              description:
                - Optional subscription comment added by an administrator.
              returned: always
              type: str
              sample: null
            allow_tracing:
              description:
                - Determines whether tracing is enabled
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


class AzureRMProductSubscriptionsInfo(AzureRMModuleBase):
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
            product_id=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.service_name = None
        self.product_id = None
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
        super(AzureRMProductSubscriptionsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.product_id is not None):
            self.results['product_subscriptions'] = self.format_item(self.list())
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
                    '/products' +
                    '/{{ product_name }}' +
                    '/subscriptions' +
                    '/{{ subscription_id }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ product_name }}', self.product_name)
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)

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
    AzureRMProductSubscriptionsInfo()


if __name__ == '__main__':
    main()
