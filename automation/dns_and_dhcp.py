from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
dns_dhcp_config = [
    'ip dhcp pool LAN',
    'network 192.168.1.0 255.255.255.0',
    'default-router 192.168.1.1',
    'dns-server 8.8.8.8 8.8.4.4',
]
net_connect.send_config_set(dns_dhcp_config)
net_connect.disconnect()

