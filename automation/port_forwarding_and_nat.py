from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
nat_config = [
    'ip nat inside source static tcp 192.168.1.100 80 interface GigabitEthernet0/2 8080',
    'interface GigabitEthernet0/1',
    'ip nat inside',
    'interface GigabitEthernet0/2',
    'ip nat outside',
]
net_connect.send_config_set(nat_config)
net_connect.disconnect()

