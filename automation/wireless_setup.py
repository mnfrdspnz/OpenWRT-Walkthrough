from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
wifi_config = [
    'interface Dot11Radio0',
    'ssid MyWiFi',
    'authentication open',
    'authentication key-management wpa version 2',
    'wpa-psk ascii 0 MyPassword',
    'exit',
    'interface Dot11Radio0',
    'channel 6',
    'no shutdown',
]
net_connect.send_config_set(wifi_config)
net_connect.disconnect()

