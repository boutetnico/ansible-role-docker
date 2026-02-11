[![tests](https://github.com/boutetnico/ansible-role-docker/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-docker/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.docker-blue.svg)](https://galaxy.ansible.com/boutetnico/docker)

ansible-role-docker
===================

This role installs Docker.

Requirements
------------

Ansible 2.15 or newer.

Supported Platforms
-------------------

- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Debian - 13 (Trixie)](https://wiki.debian.org/DebianTrixie)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                        | Required | Default              | Choices | Comments                                           |
|---------------------------------|----------|----------------------|---------|----------------------------------------------------|
| docker_dependencies             | true     |                      | list    | See `defaults/main.yml`.                           |
| docker_packages                 | true     |                      | list    | See `defaults/main.yml`.                           |
| docker_package_state            | true     | `present`            | string  |                                                    |
| docker_users                    | true     | `[root]`             | list    |                                                    |
| docker_daemon_flags             | true     | `[-H unix://]`       | list    |                                                    |
| docker_daemon_json              | true     | `{}`                 | dict    |                                                    |
| docker_cron_jobs                | true     |                      | list    | See `defaults/main.yml`.                           |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-docker

Testing
-------

## Debian

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-12
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-13

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2204
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2404

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
