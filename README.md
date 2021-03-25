# geekoops-collectd

Easy ansible role to setup `collectd`. Currently only `influxdb` is supported by this role. This ansible role works with

- openSUSE Leap 15.2


## Role Variables

| Value | Description | Default |
|-------|-------------|---------|
|`nodename`| Name of the node that will be shown in grafana | "localhost" |
|`interval`| Report interval in seconds | 10 |
|`overwrite`| Overwrite existing `collectd.conf` file | false |
|`enable_influx`| Enable InfluxDB | false |
|`influx_host`| InfluxDB host | "127.0.0.1" |
|`influx_port`| InfluxDB post | 25826 |
|`enable_disk`| Enable disk plugin | true |
|`enable_cpu`| Enable CPU plugin | true |
|`enable_load`| Enable load plugin | true |
|`enable_memory`| Enable memory plugin | true |
|`enable_swap`| Enable swap plugin | true |
|`enable_df`| Enable df plugin | false |
|`disk_disks`| Disks added to the `disk` plugin | [] |
|`df_disks`| Disks added to the `df` plugin | [] |

If `overwrite` is true, any existing `collectd.conf` file will be overwritten by ansible. Use this with caution! The existing configuration will only be written, if `collectd` is installed.

## Example Playbook

    - hosts: jellyfish
      roles:
         - { role: geekoops-collectd }

## License

MIT

## Author Information

phoenix

Have a lot of fun!
