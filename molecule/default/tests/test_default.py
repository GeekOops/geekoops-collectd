#!/usr/bin/python3
# -*- coding: utf-8 -*-


import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 
def test_collectd(host):
	# Just ensure, the collectd config file is overwritten
	cmd = host.run("cat /etc/collectd.conf | grep Hostname | grep jellyfish")
	assert cmd.succeeded
