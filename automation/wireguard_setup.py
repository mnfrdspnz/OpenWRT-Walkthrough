import paramiko

def setup_wireguard(host, username, password, wg_config_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(wg_config_path, '/etc/wireguard/wg0.conf')
    sftp.close()
    ssh.exec_command('wg-quick up wg0')
    ssh.exec_command('systemctl enable wg-quick@wg0')
    ssh.close()

setup_wireguard('192.168.1.1', 'root', 'password', 'path/to/wg0.conf')

