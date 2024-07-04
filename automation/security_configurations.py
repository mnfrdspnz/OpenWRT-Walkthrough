from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
security_config = [
    'ip access-list extended ALLOW_SSH',
    'permit tcp any any eq 22',
    'exit',
    'line vty 0 4',
    'access-class ALLOW_SSH in',
]
net_connect.send_config_set(security_config)
net_connect.disconnect()

