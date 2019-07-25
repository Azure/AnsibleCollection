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
module: apimanagementreport_info
version_added: '2.9'
short_description: Get Report info.
description:
  - Get info of Report.
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
  interval:
    description:
      - >-
        By time interval. Interval must be multiple of 15 minutes and may not be
        zero. The value should be in ISO  8601 format
        (http://en.wikipedia.org/wiki/ISO_8601#Durations).This code can be used
        to convert TimeSpan to a valid interval string: XmlConvert.ToString(new
        TimeSpan(hours, minutes, seconds)).
    type: 'unknown-primary[timeSpan]'
  value:
    description:
      - Page values.
    type: list
    suboptions:
      name:
        description:
          - >-
            Name depending on report endpoint specifies product, API, operation
            or developer name.
        type: str
      timestamp:
        description:
          - >-
            Start of aggregation period. The date conforms to the following
            format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
            standard.<br>
        type: datetime
      interval:
        description:
          - >-
            Length of aggregation period.  Interval must be multiple of 15
            minutes and may not be zero. The value should be in ISO 8601 format
            (http://en.wikipedia.org/wiki/ISO_8601#Durations).
        type: str
      country:
        description:
          - Country to which this record data is related.
        type: str
      region:
        description:
          - Country region to which this record data is related.
        type: str
      zip:
        description:
          - Zip code to which this record data is related.
        type: str
      user_id:
        description:
          - 'User identifier path. /users/{userId}'
        type: str
      product_id:
        description:
          - 'Product identifier path. /products/{productId}'
        type: str
      api_id:
        description:
          - 'API identifier path. /apis/{apiId}'
        type: str
      operation_id:
        description:
          - 'Operation identifier path. /apis/{apiId}/operations/{operationId}'
        type: str
      api_region:
        description:
          - API region identifier.
        type: str
      subscription_id:
        description:
          - 'Subscription identifier path. /subscriptions/{subscriptionId}'
        type: str
      call_count_success:
        description:
          - >-
            Number of successful calls. This includes calls returning
            HttpStatusCode <= 301 and HttpStatusCode.NotModified and
            HttpStatusCode.TemporaryRedirect
        type: number
      call_count_blocked:
        description:
          - >-
            Number of calls blocked due to invalid credentials. This includes
            calls returning HttpStatusCode.Unauthorized and
            HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests
        type: number
      call_count_failed:
        description:
          - >-
            Number of calls failed due to proxy or backend errors. This includes
            calls returning HttpStatusCode.BadRequest(400) and any Code between
            HttpStatusCode.InternalServerError (500) and 600
        type: number
      call_count_other:
        description:
          - Number of other calls.
        type: number
      call_count_total:
        description:
          - Total number of calls.
        type: number
      bandwidth:
        description:
          - Bandwidth consumed.
        type: number
      cache_hit_count:
        description:
          - Number of times when content was served from cache policy.
        type: number
      cache_miss_count:
        description:
          - Number of times content was fetched from backend.
        type: number
      api_time_avg:
        description:
          - Average time it took to process request.
        type: number
      api_time_min:
        description:
          - Minimum time it took to process request.
        type: number
      api_time_max:
        description:
          - Maximum time it took to process request.
        type: number
      service_time_avg:
        description:
          - Average time it took to process request on backend.
        type: number
      service_time_min:
        description:
          - Minimum time it took to process request on backend.
        type: number
      service_time_max:
        description:
          - Maximum time it took to process request on backend.
        type: number
  count:
    description:
      - Total record count number across all pages.
    type: number
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
- name: ApiManagementGetReportsByApi
  azure.rm.apimanagementreport.info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetReportsByGeo
  azure.rm.apimanagementreport.info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetReportsByUser
  azure.rm.apimanagementreport.info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetReportsByTime
  azure.rm.apimanagementreport.info:
    resource_group: myResourceGroup
    name: myService
    interval: PT15M
- name: ApiManagementGetReportsByProduct
  azure.rm.apimanagementreport.info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetReportsByRequest
  azure.rm.apimanagementreport.info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetReportsByOperation
  azure.rm.apimanagementreport.info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetReportsBySubscription
  azure.rm.apimanagementreport.info:
    resource_group: myResourceGroup
    name: myService

'''

RETURN = '''
reports:
  description: >-
    A list of dict results where the key is the name of the Report and the
    values are the facts for that Report.
  returned: always
  type: complex
  contains:
    report_name:
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
            name:
              description:
                - >-
                  Name depending on report endpoint specifies product, API,
                  operation or developer name.
              returned: always
              type: str
              sample: null
            timestamp:
              description:
                - >-
                  Start of aggregation period. The date conforms to the
                  following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the
                  ISO 8601 standard.<br>
              returned: always
              type: datetime
              sample: null
            interval:
              description:
                - >-
                  Length of aggregation period.  Interval must be multiple of 15
                  minutes and may not be zero. The value should be in ISO 8601
                  format (http://en.wikipedia.org/wiki/ISO_8601#Durations).
              returned: always
              type: str
              sample: null
            country:
              description:
                - Country to which this record data is related.
              returned: always
              type: str
              sample: null
            region:
              description:
                - Country region to which this record data is related.
              returned: always
              type: str
              sample: null
            zip:
              description:
                - Zip code to which this record data is related.
              returned: always
              type: str
              sample: null
            user_id:
              description:
                - 'User identifier path. /users/{userId}'
              returned: always
              type: str
              sample: null
            product_id:
              description:
                - 'Product identifier path. /products/{productId}'
              returned: always
              type: str
              sample: null
            api_id:
              description:
                - 'API identifier path. /apis/{apiId}'
              returned: always
              type: str
              sample: null
            operation_id:
              description:
                - >-
                  Operation identifier path.
                  /apis/{apiId}/operations/{operationId}
              returned: always
              type: str
              sample: null
            api_region:
              description:
                - API region identifier.
              returned: always
              type: str
              sample: null
            subscription_id:
              description:
                - 'Subscription identifier path. /subscriptions/{subscriptionId}'
              returned: always
              type: str
              sample: null
            call_count_success:
              description:
                - >-
                  Number of successful calls. This includes calls returning
                  HttpStatusCode <= 301 and HttpStatusCode.NotModified and
                  HttpStatusCode.TemporaryRedirect
              returned: always
              type: number
              sample: null
            call_count_blocked:
              description:
                - >-
                  Number of calls blocked due to invalid credentials. This
                  includes calls returning HttpStatusCode.Unauthorized and
                  HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests
              returned: always
              type: number
              sample: null
            call_count_failed:
              description:
                - >-
                  Number of calls failed due to proxy or backend errors. This
                  includes calls returning HttpStatusCode.BadRequest(400) and
                  any Code between HttpStatusCode.InternalServerError (500) and
                  600
              returned: always
              type: number
              sample: null
            call_count_other:
              description:
                - Number of other calls.
              returned: always
              type: number
              sample: null
            call_count_total:
              description:
                - Total number of calls.
              returned: always
              type: number
              sample: null
            bandwidth:
              description:
                - Bandwidth consumed.
              returned: always
              type: number
              sample: null
            cache_hit_count:
              description:
                - Number of times when content was served from cache policy.
              returned: always
              type: number
              sample: null
            cache_miss_count:
              description:
                - Number of times content was fetched from backend.
              returned: always
              type: number
              sample: null
            api_time_avg:
              description:
                - Average time it took to process request.
              returned: always
              type: number
              sample: null
            api_time_min:
              description:
                - Minimum time it took to process request.
              returned: always
              type: number
              sample: null
            api_time_max:
              description:
                - Maximum time it took to process request.
              returned: always
              type: number
              sample: null
            service_time_avg:
              description:
                - Average time it took to process request on backend.
              returned: always
              type: number
              sample: null
            service_time_min:
              description:
                - Minimum time it took to process request on backend.
              returned: always
              type: number
              sample: null
            service_time_max:
              description:
                - Maximum time it took to process request on backend.
              returned: always
              type: number
              sample: null
        count:
          description:
            - Total record count number across all pages.
          returned: always
          type: number
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


class AzureRMReportsInfo(AzureRMModuleBase):
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
            interval=dict(
                type='unknown-primary[timeSpan]'
            )
        )

        self.resource_group = None
        self.name = None
        self.interval = None
        self.value = None
        self.count = None
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
        super(AzureRMReportsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['reports'] = self.format_item(self.listbysubscription())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['reports'] = self.format_item(self.listbyoperation())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['reports'] = self.format_item(self.listbyrequest())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['reports'] = self.format_item(self.listbyproduct())
        elif (self.resource_group is not None and
              self.name is not None and
              self.interval is not None):
            self.results['reports'] = self.format_item(self.listbytime())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['reports'] = self.format_item(self.listbyuser())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['reports'] = self.format_item(self.listbygeo())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['reports'] = self.format_item(self.listbyapi())
        return self.results

    def listbysubscription(self):
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
                    '/reports' +
                    '/{{ report_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ report_name }}', self.name)

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

    def listbyoperation(self):
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
                    '/reports' +
                    '/{{ report_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ report_name }}', self.name)

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

    def listbyrequest(self):
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
                    '/reports' +
                    '/{{ report_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ report_name }}', self.name)

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

    def listbyproduct(self):
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
                    '/reports' +
                    '/{{ report_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ report_name }}', self.name)

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

    def listbytime(self):
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
                    '/reports' +
                    '/{{ report_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ report_name }}', self.name)

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

    def listbyuser(self):
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
                    '/reports' +
                    '/{{ report_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ report_name }}', self.name)

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

    def listbygeo(self):
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
                    '/reports' +
                    '/{{ report_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ report_name }}', self.name)

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

    def listbyapi(self):
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
                    '/reports' +
                    '/{{ report_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ report_name }}', self.name)

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
    AzureRMReportsInfo()


if __name__ == '__main__':
    main()
