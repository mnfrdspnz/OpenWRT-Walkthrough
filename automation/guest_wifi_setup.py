from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
guest_wifi_config = [
    'interface Dot11Radio0',
    'ssid GuestWiFi',
    'authentication open',
    'authentication key-management wpa version 2',
    'wpa-psk ascii 0 GuestPassword',
    'exit',
    'interface Dot11Radio0',
    'channel 11',
    'no shutdown',
]
net_connect.send_config_set(guest_wifi_config)
net_connect.disconnect()

