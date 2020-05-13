Ansible role for terraform-plugins
==================================

An Ansible role to download Terraform plugins

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-terraform-plugins/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-terraform-plugins/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-terraform-plugins/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-terraform-plugins/actions?query=workflow%3A%22Release%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| terraform_plugins | A list of GitHub release URLs | `list(string)` | `[]` | no |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-terraform-plugins
      vars:
        terraform_plugins:
          - https://github.com/gavinbunney/terraform-provider-kubectl/releases/download/v1.4.2/terraform-provider-kubectl-linux-amd64
```

License
-------

[Apache License](LICENSE)
