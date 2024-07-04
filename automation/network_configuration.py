# network_configuration.py
import os

def configure_lan(ip_address, netmask):
    os.system(f"uci set network.lan.ipaddr='{ip_address}'")
    os.system(f"uci set network.lan.netmask='{netmask}'")
    os.system("uci commit network")
    os.system("/etc/init.d/network restart")

if __name__ == "__main__":
    configure_lan("192.168.1.1", "255.255.255.0")

