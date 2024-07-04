#!/bin/sh
# Example script to show basic OpenWRT configuration
uci set network.lan.ipaddr='192.168.1.1'
uci commit network
/etc/init.d/network restart

