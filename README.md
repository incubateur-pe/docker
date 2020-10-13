docker-bare-metal
=========

Installe docker sur un serveur ou une vm

Pré-requis
------------

La machine doit disposer des AC de la PKI interne, voir role galaxy configuration-bare-metal

Role Variables
--------------

| Nom | valeur par defaut | description |
|-----|-------------------|-------------|
| centos.docker_proxy | https://repository.pole-emploi.intra/artifactory/rpm-docker-centos-proxy | Adresse d'un mirroir du repository docker yum |
| docker.data_root | /data/docker | Répertoire des données de docker : containers, images, volumes etc... |
| docker.insecure_registries | ["docker-snapshots-virtual.artefact-repo.pole-emploi.intra"] | liste des insecure-registries a configurer |
| docker.registry_mirrors | ["https://docker-dev-virtual.repository.pole-emploi.intra"] | Liste des registry mirror a configurer |
| docker.log_driver | json-file | Driver de logs docker |
| docker.log_max_size | 100m | Taille maximale de la log docker |
| docker.storage_driver | overlay2 | Driver de stockage docker |
| docker.native.cgroupdriver | systemd | Driver cgroup (sytemd ou docker) |

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

  - hosts: all
    roles:
    - role: 'docker-bare-metal'
      tags: docker
    vars:
      centos:
        docker_proxy: https://repository.pole-emploi.intra/artifactory/rpm-docker-centos-proxy
      docker:
        data_root: /repertoire/docker
        insecure_registries:
          - adresse_1
          - adresse_2
        registry_mirrors:
          - https://adresse_3

