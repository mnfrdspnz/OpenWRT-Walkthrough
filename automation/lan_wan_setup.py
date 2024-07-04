from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
config_commands = [
    'interface GigabitEthernet0/1',
    'ip address 192.168.1.2 255.255.255.0',
    'no shutdown',
    'exit',
    'interface GigabitEthernet0/2',
    'ip address dhcp',
    'no shutdown',
]
net_connect.send_config_set(config_commands)
net_connect.disconnect()

