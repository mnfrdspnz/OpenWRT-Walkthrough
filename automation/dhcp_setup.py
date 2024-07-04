from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
dhcp_config = [
    'ip dhcp pool LAN',
    'network 192.168.1.0 255.255.255.0',
    'default-router 192.168.1.1',
    'dns-server 8.8.8.8 8.8.4.4',
]
static_ip_config = [
    'interface GigabitEthernet0/3',
    'ip address 192.168.2.1 255.255.255.0',
    'no shutdown',
]
net_connect.send_config_set(dhcp_config)
net_connect.send_config_set(static_ip_config)
net_connect.disconnect()

