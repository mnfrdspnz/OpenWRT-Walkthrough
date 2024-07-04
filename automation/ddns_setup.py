import paramiko

def setup_ddns(host, username, password, ddns_config_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(ddns_config_path, '/etc/config/ddns')
    sftp.close()
    ssh.exec_command('/etc/init.d/ddns start')
    ssh.exec_command('/etc/init.d/ddns enable')
    ssh.close()

setup_ddns('192.168.1.1', 'root', 'password', 'path/to/ddns_config')

