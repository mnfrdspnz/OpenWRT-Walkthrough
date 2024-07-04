from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
qos_config = [
    'policy-map QOS_POLICY',
    'class class-default',
    'fair-queue',
    'exit',
    'interface GigabitEthernet0/1',
    'service-policy output QOS_POLICY',
]
net_connect.send_config_set(qos_config)
net_connect.disconnect()

