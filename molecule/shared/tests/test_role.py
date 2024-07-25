import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("docker-ce"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/etc/docker/daemon.json"),
        ("root", "root", "/etc/systemd/system/docker.service.d/options.conf"),
        ("root", "root", "/etc/containerd/config.toml"),
    ],
)
def test_logstash_config_file(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname
