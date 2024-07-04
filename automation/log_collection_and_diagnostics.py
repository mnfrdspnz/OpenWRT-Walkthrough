import paramiko

def collect_logs(host, username, password, log_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.get('/var/log/syslog', log_path)
    sftp.close()
    ssh.close()

collect_logs('192.168.1.1', 'root', 'password', 'path/to/syslog')

