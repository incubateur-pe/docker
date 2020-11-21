docker-bare-metal
=========

Install and configure docker on a server
If you plan to use anything on your server that needs the forward policy to be set to ACCEPT, this role can configure the DOCKER-USER rule needed

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
| docker_allow_forward | false | Configure iptables rules to allow forward, as docker set it to DROP |
| docker_repo_valid_ssl | true | Set to false to use a repository with for example a self signed certifcate |

Example Playbook
----------------

Simple docker install:

```yaml
- hosts: all
  roles:
  - role: 'docker-bare-metal'
```

Install docker and configure some insecure registries and mirrors:

```yaml
- hosts: all
  roles:
  - role: 'docker-bare-metal'
  vars:
    docker_data_root: /repertoire/docker
    docker_insecure_registries:
      - adresse_1
      - adresse_2
    docker_registry_mirrors:
      - https://adresse_3
```



Tests
-----

The tests use molecule + libvirt + kvm distant + testinfra, allowing on the fly multi-nodes clusters creation and system configuration checks

__Tests execution with docker:__
```
# interactive :
docker run --env-file molecule/common/env_local_tests.sh -v $(pwd):/sources/docker -w /sources/docker   -v ~/.vagrant.d/boxes/:/root/.vagrant.d/boxes/   -v /var/run/libvirt/libvirt-sock:/var/run/libvirt/libvirt-sock -it --entrypoint bash ulrichg/molecule-vagrant-libvirt:latest

# lint:
docker run --env-file molecule/common/env_local_tests.sh -v $(pwd):/sources/docker -w /sources/docker   -v ~/.vagrant.d/boxes/:/root/.vagrant.d/boxes/   -v /var/run/libvirt/libvirt-sock:/var/run/libvirt/libvirt-sock ulrichg/molecule-vagrant-libvirt:latest lint

# default scenario:
docker run --env-file molecule/common/env_local_tests.sh -v $(pwd):/sources/docker -w /sources/docker   -v ~/.vagrant.d/boxes/:/root/.vagrant.d/boxes/   -v /var/run/libvirt/libvirt-sock:/var/run/libvirt/libvirt-sock ulrichg/molecule-vagrant-libvirt:latest

# other scenario:
docker run --env-file molecule/common/env_local_tests.sh -v $(pwd):/sources/docker -w /sources/docker   -v ~/.vagrant.d/boxes/:/root/.vagrant.d/boxes/   -v /var/run/libvirt/libvirt-sock:/var/run/libvirt/libvirt-sock ulrichg/molecule-vagrant-libvirt:latest test -s cluster1master
```

License
-------

BSD 3-Clause
