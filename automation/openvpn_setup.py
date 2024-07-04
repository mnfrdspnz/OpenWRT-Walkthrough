import paramiko

def setup_openvpn(host, username, password, ovpn_config_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(ovpn_config_path, '/etc/openvpn/client.conf')
    sftp.close()
    ssh.exec_command('systemctl start openvpn@client')
    ssh.exec_command('systemctl enable openvpn@client')
    ssh.close()

setup_openvpn('192.168.1.1', 'root', 'password', 'path/to/client.conf')

