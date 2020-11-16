"""Role testing files using testinfra."""


def test_docker_packages(host):
    docker = host.package("docker-ce")
    assert docker.is_installed


def test_docker_service(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled


def test_docker_config(host):
    config = host.file("/etc/docker/daemon.json")
    assert config.exists
    assert config.user == "root"
    assert config.group == "root"
    assert config.mode == 0o644
