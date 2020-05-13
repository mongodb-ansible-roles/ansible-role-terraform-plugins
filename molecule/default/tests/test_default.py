import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_plugin_installed(host):
    filepath = "/root/.terraform.d/plugins"
    assert host.file(filepath).exists
    plugin = "terraform-provider-kubectl"
    assert host.file(f"{filepath}/{plugin}").exists
    assert host.file(f"{filepath}/{plugin}").mode == 0o777
