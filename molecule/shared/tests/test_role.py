import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("ca-certificates"),
        ("cron"),
        ("gnupg2"),
        ("python3-docker"),
    ],
)
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "name",
    [
        ("containerd.io"),
        ("docker-buildx-plugin"),
        ("docker-ce"),
        ("docker-ce-cli"),
        ("docker-ce-rootless-extras"),
        ("docker-compose-plugin"),
    ],
)
def test_docker_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_docker_service_is_running(host):
    service = host.service("docker")
    assert service.is_running
    assert service.is_enabled


def test_docker_group_exists(host):
    group = host.group("docker")
    assert group.exists


def test_docker_command_works(host):
    cmd = host.run("docker --version")
    assert cmd.rc == 0
    assert "Docker version" in cmd.stdout


def test_docker_compose_command_works(host):
    cmd = host.run("docker compose version")
    assert cmd.rc == 0


@pytest.mark.parametrize(
    "path,user,group,mode",
    [
        ("/etc/docker", "root", "root", 0o755),
        ("/etc/systemd/system/docker.service.d", "root", "root", 0o755),
    ],
)
def test_docker_directories_exist(host, path, user, group, mode):
    directory = host.file(path)
    assert directory.exists
    assert directory.is_directory
    assert directory.user == user
    assert directory.group == group
    assert directory.mode == mode


@pytest.mark.parametrize(
    "path,user,group,mode",
    [
        ("/etc/docker/daemon.json", "root", "root", 0o644),
        ("/etc/systemd/system/docker.service.d/options.conf", "root", "root", 0o644),
        ("/etc/containerd/config.toml", "root", "root", 0o644),
    ],
)
def test_docker_config_files_exist(host, path, user, group, mode):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode


def test_docker_cron_job_exists(host):
    cron_file = host.file("/etc/cron.d/docker-disk-clean-up")
    assert cron_file.exists
    assert cron_file.is_file
    assert cron_file.contains("docker system prune")
