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
module: apimanagementtagresource_info
version_added: '2.9'
short_description: Get TagResource info.
description:
  - Get info of TagResource.
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
      - Page values.
    type: list
    suboptions:
      tag:
        description:
          - Tag associated with the resource.
        required: true
        type: dict
        suboptions:
          id:
            description:
              - Tag identifier
            type: str
          name:
            description:
              - Tag Name
            type: str
      api:
        description:
          - Api associated with the tag.
        type: dict
        suboptions:
          description:
            description:
              - Description of the API. May include HTML formatting tags.
            type: str
          authentication_settings:
            description:
              - Collection of authentication settings included into this API.
            type: dict
            suboptions:
              o_auth2:
                description:
                  - OAuth2 Authentication settings
                type: dict
                suboptions:
                  authorization_server_id:
                    description:
                      - OAuth authorization server identifier.
                    type: str
                  scope:
                    description:
                      - operations scope.
                    type: str
              openid:
                description:
                  - OpenID Connect Authentication Settings
                type: dict
                suboptions:
                  openid_provider_id:
                    description:
                      - OAuth authorization server identifier.
                    type: str
                  bearer_token_sending_methods:
                    description:
                      - How to send token to the server.
                    type: list
              subscription_key_required:
                description:
                  - >-
                    Specifies whether subscription key is required during call
                    to this API, true - API is included into closed products
                    only, false - API is included into open products alone, null
                    - there is a mix of products.
                type: boolean
          subscription_key_parameter_names:
            description:
              - Protocols over which API is made available.
            type: dict
            suboptions:
              header:
                description:
                  - Subscription key header name.
                type: str
              query:
                description:
                  - Subscription key query string parameter name.
                type: str
          type:
            description:
              - Type of API.
            type: str
          api_revision:
            description:
              - >-
                Describes the Revision of the Api. If no value is provided,
                default revision 1 is created
            type: str
          api_version:
            description:
              - >-
                Indicates the Version identifier of the API if the API is
                versioned
            type: str
          is_current:
            description:
              - Indicates if API revision is current api revision.
            type: boolean
          is_online:
            description:
              - Indicates if API revision is accessible via the gateway.
            type: boolean
          api_revision_description:
            description:
              - Description of the Api Revision.
            type: str
          api_version_description:
            description:
              - Description of the Api Version.
            type: str
          api_version_set_id:
            description:
              - A resource identifier for the related ApiVersionSet.
            type: str
          subscription_required:
            description:
              - >-
                Specifies whether an API or Product subscription is required for
                accessing the API.
            type: boolean
          id:
            description:
              - 'API identifier in the form /apis/{apiId}.'
            type: str
          name:
            description:
              - API name.
            type: str
          service_url:
            description:
              - Absolute URL of the backend service implementing this API.
            type: str
          path:
            description:
              - >-
                Relative URL uniquely identifying this API and all of its
                resource paths within the API Management service instance. It is
                appended to the API endpoint base URL specified during the
                service instance creation to form a public URL for this API.
            type: str
          protocols:
            description:
              - >-
                Describes on which protocols the operations in this API can be
                invoked.
            type: list
      operation:
        description:
          - Operation associated with the tag.
        type: dict
        suboptions:
          id:
            description:
              - 'Identifier of the operation in form /operations/{operationId}.'
            type: str
          name:
            description:
              - Operation name.
            type: str
          api_name:
            description:
              - Api Name.
            type: str
          api_revision:
            description:
              - Api Revision.
            type: str
          api_version:
            description:
              - Api Version.
            type: str
          description:
            description:
              - Operation Description.
            type: str
          method:
            description:
              - >-
                A Valid HTTP Operation Method. Typical Http Methods like GET,
                PUT, POST but not limited by only them.
            type: str
          url_template:
            description:
              - >-
                Relative URL template identifying the target resource for this
                operation. May include parameters. Example:
                /customers/{cid}/orders/{oid}/?date={date}
            type: str
      product:
        description:
          - Product associated with the tag.
        type: dict
        suboptions:
          description:
            description:
              - Product description. May include HTML formatting tags.
            type: str
          terms:
            description:
              - >-
                Product terms of use. Developers trying to subscribe to the
                product will be presented and required to accept these terms
                before they can complete the subscription process.
            type: str
          subscription_required:
            description:
              - >-
                Whether a product subscription is required for accessing APIs
                included in this product. If true, the product is referred to as
                "protected" and a valid subscription key is required for a
                request to an API included in the product to succeed. If false,
                the product is referred to as "open" and requests to an API
                included in the product can be made without a subscription key.
                If property is omitted when creating a new product it's value is
                assumed to be true.
            type: boolean
          approval_required:
            description:
              - >-
                whether subscription approval is required. If false, new
                subscriptions will be approved automatically enabling developers
                to call the product’s APIs immediately after subscribing. If
                true, administrators must manually approve the subscription
                before the developer can any of the product’s APIs. Can be
                present only if subscriptionRequired property is present and has
                a value of false.
            type: boolean
          subscriptions_limit:
            description:
              - >-
                Whether the number of subscriptions a user can have to this
                product at the same time. Set to null or omit to allow unlimited
                per user subscriptions. Can be present only if
                subscriptionRequired property is present and has a value of
                false.
            type: number
          state:
            description:
              - >-
                whether product is published or not. Published products are
                discoverable by users of developer portal. Non published
                products are visible only to administrators. Default state of
                Product is notPublished.
            type: str
          id:
            description:
              - 'Identifier of the product in the form of /products/{productId}'
            type: str
          name:
            description:
              - Product name.
            required: true
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
- name: ApiManagementListTagResources
  azure.rm.apimanagementtagresource.info:
    resource_group: myResourceGroup
    name: myService

'''

RETURN = '''
tag_resource:
  description: >-
    A list of dict results where the key is the name of the TagResource and the
    values are the facts for that TagResource.
  returned: always
  type: complex
  contains:
    tagresource_name:
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
            tag:
              description:
                - Tag associated with the resource.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Tag identifier
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - Tag Name
                  returned: always
                  type: str
                  sample: null
            api:
              description:
                - Api associated with the tag.
              returned: always
              type: dict
              sample: null
              contains:
                description:
                  description:
                    - Description of the API. May include HTML formatting tags.
                  returned: always
                  type: str
                  sample: null
                authentication_settings:
                  description:
                    - >-
                      Collection of authentication settings included into this
                      API.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    o_auth2:
                      description:
                        - OAuth2 Authentication settings
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        authorization_server_id:
                          description:
                            - OAuth authorization server identifier.
                          returned: always
                          type: str
                          sample: null
                        scope:
                          description:
                            - operations scope.
                          returned: always
                          type: str
                          sample: null
                    openid:
                      description:
                        - OpenID Connect Authentication Settings
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        openid_provider_id:
                          description:
                            - OAuth authorization server identifier.
                          returned: always
                          type: str
                          sample: null
                        bearer_token_sending_methods:
                          description:
                            - How to send token to the server.
                          returned: always
                          type: str
                          sample: null
                    subscription_key_required:
                      description:
                        - >-
                          Specifies whether subscription key is required during
                          call to this API, true - API is included into closed
                          products only, false - API is included into open
                          products alone, null - there is a mix of products.
                      returned: always
                      type: boolean
                      sample: null
                subscription_key_parameter_names:
                  description:
                    - Protocols over which API is made available.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    header:
                      description:
                        - Subscription key header name.
                      returned: always
                      type: str
                      sample: null
                    query:
                      description:
                        - Subscription key query string parameter name.
                      returned: always
                      type: str
                      sample: null
                type:
                  description:
                    - Type of API.
                  returned: always
                  type: str
                  sample: null
                api_revision:
                  description:
                    - >-
                      Describes the Revision of the Api. If no value is
                      provided, default revision 1 is created
                  returned: always
                  type: str
                  sample: null
                api_version:
                  description:
                    - >-
                      Indicates the Version identifier of the API if the API is
                      versioned
                  returned: always
                  type: str
                  sample: null
                is_current:
                  description:
                    - Indicates if API revision is current api revision.
                  returned: always
                  type: boolean
                  sample: null
                is_online:
                  description:
                    - Indicates if API revision is accessible via the gateway.
                  returned: always
                  type: boolean
                  sample: null
                api_revision_description:
                  description:
                    - Description of the Api Revision.
                  returned: always
                  type: str
                  sample: null
                api_version_description:
                  description:
                    - Description of the Api Version.
                  returned: always
                  type: str
                  sample: null
                api_version_set_id:
                  description:
                    - A resource identifier for the related ApiVersionSet.
                  returned: always
                  type: str
                  sample: null
                subscription_required:
                  description:
                    - >-
                      Specifies whether an API or Product subscription is
                      required for accessing the API.
                  returned: always
                  type: boolean
                  sample: null
                id:
                  description:
                    - 'API identifier in the form /apis/{apiId}.'
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - API name.
                  returned: always
                  type: str
                  sample: null
                service_url:
                  description:
                    - Absolute URL of the backend service implementing this API.
                  returned: always
                  type: str
                  sample: null
                path:
                  description:
                    - >-
                      Relative URL uniquely identifying this API and all of its
                      resource paths within the API Management service instance.
                      It is appended to the API endpoint base URL specified
                      during the service instance creation to form a public URL
                      for this API.
                  returned: always
                  type: str
                  sample: null
                protocols:
                  description:
                    - >-
                      Describes on which protocols the operations in this API
                      can be invoked.
                  returned: always
                  type: str
                  sample: null
            operation:
              description:
                - Operation associated with the tag.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - >-
                      Identifier of the operation in form
                      /operations/{operationId}.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - Operation name.
                  returned: always
                  type: str
                  sample: null
                api_name:
                  description:
                    - Api Name.
                  returned: always
                  type: str
                  sample: null
                api_revision:
                  description:
                    - Api Revision.
                  returned: always
                  type: str
                  sample: null
                api_version:
                  description:
                    - Api Version.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Operation Description.
                  returned: always
                  type: str
                  sample: null
                method:
                  description:
                    - >-
                      A Valid HTTP Operation Method. Typical Http Methods like
                      GET, PUT, POST but not limited by only them.
                  returned: always
                  type: str
                  sample: null
                url_template:
                  description:
                    - >-
                      Relative URL template identifying the target resource for
                      this operation. May include parameters. Example:
                      /customers/{cid}/orders/{oid}/?date={date}
                  returned: always
                  type: str
                  sample: null
            product:
              description:
                - Product associated with the tag.
              returned: always
              type: dict
              sample: null
              contains:
                description:
                  description:
                    - Product description. May include HTML formatting tags.
                  returned: always
                  type: str
                  sample: null
                terms:
                  description:
                    - >-
                      Product terms of use. Developers trying to subscribe to
                      the product will be presented and required to accept these
                      terms before they can complete the subscription process.
                  returned: always
                  type: str
                  sample: null
                subscription_required:
                  description:
                    - >-
                      Whether a product subscription is required for accessing
                      APIs included in this product. If true, the product is
                      referred to as "protected" and a valid subscription key is
                      required for a request to an API included in the product
                      to succeed. If false, the product is referred to as "open"
                      and requests to an API included in the product can be made
                      without a subscription key. If property is omitted when
                      creating a new product it's value is assumed to be true.
                  returned: always
                  type: boolean
                  sample: null
                approval_required:
                  description:
                    - >-
                      whether subscription approval is required. If false, new
                      subscriptions will be approved automatically enabling
                      developers to call the product’s APIs immediately after
                      subscribing. If true, administrators must manually approve
                      the subscription before the developer can any of the
                      product’s APIs. Can be present only if
                      subscriptionRequired property is present and has a value
                      of false.
                  returned: always
                  type: boolean
                  sample: null
                subscriptions_limit:
                  description:
                    - >-
                      Whether the number of subscriptions a user can have to
                      this product at the same time. Set to null or omit to
                      allow unlimited per user subscriptions. Can be present
                      only if subscriptionRequired property is present and has a
                      value of false.
                  returned: always
                  type: number
                  sample: null
                state:
                  description:
                    - >-
                      whether product is published or not. Published products
                      are discoverable by users of developer portal. Non
                      published products are visible only to administrators.
                      Default state of Product is notPublished.
                  returned: always
                  type: str
                  sample: null
                id:
                  description:
                    - >-
                      Identifier of the product in the form of
                      /products/{productId}
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - Product name.
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


class AzureRMTagResourceInfo(AzureRMModuleBase):
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
        super(AzureRMTagResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['tag_resource'] = self.format_item(self.listbyservice())
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
                    '/tagResources')
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
    AzureRMTagResourceInfo()


if __name__ == '__main__':
    main()
