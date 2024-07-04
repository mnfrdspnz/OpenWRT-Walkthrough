from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
vlan_config = [
    'vlan 10',
    'name VLAN10',
    'exit',
    'vlan 20',
    'name VLAN20',
    'exit',
    'interface GigabitEthernet0/1',
    'switchport mode trunk',
    'switchport trunk allowed vlan 10,20',
]
net_connect.send_config_set(vlan_config)
net_connect.disconnect()

