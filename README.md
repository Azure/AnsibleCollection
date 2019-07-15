
# Documentation

## 1.Create the collection
    Collection Metadata
```
collection/
├── README.md
├── galaxy.yml
├── plugins/
│   ├── modules/
│       |── managementgroup.py
|       |── managementgroupsubscription.py
|       └── subscriptionfactory.py
└── roles/
    └── my_role
```
    Collections require a galaxy.yml at the root level of the collection. This file contains all of the metadata that Galaxy and Mazer need in order to package and import a collection.
```
namespace: "smile37773"
name: "rm"
version: "0.0.4"
readme: "README.md"
authors:
    - "Liu Qingyi"
license:
    - "MIT"
tags:
    - demo
    - collection
repository: "https://github.com/Azure/AnsibleCollection"
```
    Create the role by command - “ansible-galaxy init my_role”

## 2.Build the collection 
    mazer build
    This will create a releases/ directory inside the collection with the build artifacts, which can be uploaded to Galaxy.

## 3.Upload the collection
    Open the website: https://galaxy.ansible.com/my-content/namespaces. Click the buttom "Add Content" and upload the file in the releases/ directory.

## 4.Install the collection
    mazer install smile37773.rm

## 5.Using the collection
    playbook: test.yml
```
- hosts: localhost
  collections:
    - smile37773.rm
  tasks:
    - name: PutManagementGroup
      managementgroup:
        group_id: ChildGroup
        id: /providers/Microsoft.Management/managementGroups/ChildGroup
        type: /providers/Microsoft.Management/managementGroups/
        name: ChildGroup
        properties:
          tenant_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
          display_name: ChildGroup
          details:
            parent:
              id: /providers/Microsoft.Management/managementGroups/RootGroup
    - name: AddSubscriptionToManagementGroup
      managementgroupsubscription:
        group_id: myManagementGroup
    - name: Create Subscription
      subscriptionfactory:
        enrollment_account_name: myEnrollmentAccount
        body:
          offerType: MS-AZR-0017P
          displayName: Test Ea Azure Sub
          owners:
            - objectId: 973034ff-acb7-409c-b731-e789672c7b31
            - objectId: 67439a9e-8519-4016-a630-f5f805eba567
          additionalParameters:
            customData:
              key1: value1
              key2: true
```
