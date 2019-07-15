
# Documentation

## 1.Create the collection
    galaxy.yml
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

## 2.Build the collection 
    mazer build
    This will create a releases/ directory inside the collection with the build artifacts, which can be uploaded to Galaxy.

## 3.Upload the collection
    Open the website: https://galaxy.ansible.com/my-content/namespaces. Upload the file in the releases/ directory.

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
```
