
# Using the collection

## 1.Install the collection
    Use the command - "mazer install azure.rm"

## 2.Using the collection in playooks
    playbook: test.yml
```
- hosts: localhost
  tasks:
    - name: PutManagementGroup
      azure.rm.managementgroup:
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
      azure.rm.managementgroupsubscription:
        group_id: myManagementGroup
    - name: Create Subscription
      azure.rm.subscriptionfactory:
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
    To avoid a lot of typing, you can also use the collections keyword added in Ansbile 2.8:
```
- hosts: localhost
  collections:
    - azure.rm
  tasks:
    - name: PutManagementGroup
      managementgroup:
        ...
    - name: AddSubscriptionToManagementGroup
      managementgroupsubscription:
        ...
    - name: Create Subscription
      subscriptionfactory:
        ...

```

# Contributing to the Collection 

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
namespace: "azure"
name: "rm"
version: "0.0.5"
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
    Use the command - "mazer build"
    This will create a releases/ directory inside the collection with the build artifacts, which can be uploaded to Galaxy.

## 3.Upload the collection
    Way one:
    Open the website: https://galaxy.ansible.com/my-content/namespaces. Click the buttom "Add Content" and upload the file in the releases/ directory.
    Way two:
    Use the command - “mazer publish --api-key=SECRET path/to/azure-rm-0.0.1.tar.gz”. The api-key can be found in https://galaxy.ansible.com/me/preferences.
