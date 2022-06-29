[![Test deployment](https://github.com/GeekOops/geekoops-collectd/actions/workflows/CI.yml/badge.svg)](https://github.com/GeekOops/geekoops-collectd/actions/workflows/CI.yml)

# geekoops-collectd

Easy ansible role to setup system metrics transmission to `collectd`. This ansible role works with

- openSUSE Leap 15.3
- openSUSE Leap 15.4


## Role Variables

| Value | Description | Default |
|-------|-------------|---------|
|`nodename`| Name of the node that will be shown in grafana | `{{ ansible_hostname }}` |
|`interval`| Report interval in seconds | `10` |
|`overwrite`| Overwrite existing `collectd.conf` file | `true` |
|`influx_host`| If set, collectd will push its metrics to this InfluxDB host | "" |
|`influx_port`| InfluxDB post | `25826` |
|`prometheus_port`| If set, collectd will open a webserver of this port to accept scrape requests from Prometheus on this port | `""` |
|`enable_disk`| Enable the disk plugin | `true` |
|`disk_disks`| Disks added to the `disk` plugin | [] |
|`enable_cpu`| Enable the CPU plugin | `true` |
|`enable_uptime`| Enable the uptime plugin | `true` |
|`enable_cpufreq`| Enable the cpufreq plugin | `true` |
|`enable_load`| Enable the load plugin | `true` |
|`enable_memory`| Enable the memory plugin | `true` |
|`enable_swap`| Enable the swap plugin | `true` |
|`enable_smart`| Enable the smart plugin | `false` |
|`smart_disk` | Select disk(s) to be monitored by the smart plugin | `""` |
|`smart_use_serial` | Use the disk serial number instead of the kernel name to store data | `true` |
|`enable_df`| Enable the df plugin | `false` |
|`df_disks`| Disks added to the `df` plugin | `[]` |
|`enable_apcups`| Enable the apcups plugin | `false` |
|`apcups_host` | Hostname of the running `acpupsd` to query | `localhost` |
|`apcups_port` | Port to query | `3551` |
|`apcups_report_seconds` | Convert the lifetime to seconds | `true` |
|`apcups_persistent_connection` | Keep the connection between reads open | `true` |
|`enable_vmem`| Enable the vmem plugin | `false` |
|`vmem_verbose`| Report vmem stats verbosely | `false` |
|`enable_connectivity`| Enable the connectivity plugin to report if interfaces are up or down | `false` |
|`connectivity_interfaces`| Set the list of interfaces for the connectivity plugin to monitor | `[]` |
|`enable_battery` | Enable the battery plugin | `false` |
|`battery_percentage` | Report the battery stats as percentages | `true` |
|`battery_report_degraded` | Report the degraded stats instead the corrected-for-degraded stats | `false` |
|`enable_hddtemp` | Enable the hddtemp plugin | `false` |
|`hdd_temp_host` | Host to query by the plugin. This is where the hddtemp daemon is running | `127.0.0.1` |
|`hdd_temp_port` | Port of the hddtemp host to query | `7634` |
|`enable_md` | Enable the md plugin (RAID monitoring) | `false` |
|`md_device` | Device the md plugin should monitor | `/dev/md0` |



If `overwrite` is true, any existing `collectd.conf` file will be overwritten by ansible. Use this with caution! The existing configuration will only be written, if `collectd` is installed.

## Example Playbook

    - hosts: jellyfish
      roles:
         - { role: geekoops-collectd }

Extended example

    - hosts: jellyfish
      roles:
         - role: geekoops-collectd
           vars:
             nodename: "jellyfish"
             influx_host: "192.168.122.3"
             enable_df: true

## License

MIT
