from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
firewall_rules = [
    'ip access-list extended ALLOW_HTTP',
    'permit tcp any any eq 80',
    'permit tcp any any eq 443',
    'exit',
    'interface GigabitEthernet0/1',
    'ip access-group ALLOW_HTTP in',
]
net_connect.send_config_set(firewall_rules)
net_connect.disconnect()

