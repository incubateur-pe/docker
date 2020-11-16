docker-bare-metal
=========

Install docker on a server

Role Variables
--------------

| Nom | valeur par defaut | description |
|-----|-------------------|-------------|
| docker_repo | https://download.docker.com/linux/ | Docker repository (or mirror to) containing packages |
| docker_data_root | /var/lib/docker | Docker data directory  |
| docker_insecure_registries | [] | Insecure registries to add to docker configuration |
| docker_registry_mirrors | [] | Registries to configure as mirrors |
| docker_log_driver | json-file | Docker log driver |
| docker_log_max_size | 100m | Docker log maximum size |
| docker_storage_driver | overlay2 | Docker storage driver |
| docker_native_cgroupdriver | systemd | cgroup driver |
| docker_edition | ce | Docker edition to install |
| docker_enable_edge | false | Enables edge packages |
| docker_enable_test | false | Enables test packages |
| docker_apt_ignore_key_error | true | Ignore errors on gpg key import |
| docker_users | [] | List of users to add to docker group |


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

  - hosts: all
    roles:
    - role: 'docker-bare-metal'
      tags: docker
    vars:
      docker_data_root: /repertoire/docker
      docker_insecure_registries:
        - adresse_1
        - adresse_2
      docker_registry_mirrors:
        - https://adresse_3
