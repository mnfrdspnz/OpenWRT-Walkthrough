import paramiko

def backup_config(host, username, password, backup_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.get('/etc/config', backup_path)
    sftp.close()
    ssh.close()

def restore_config(host, username, password, backup_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(backup_path, '/etc/config')
    sftp.close()
    ssh.exec_command('reboot')
    ssh.close()

# Example usage:
backup_config('192.168.1.1', 'root', 'password', 'path/to/backup/config')
restore_config('192.168.1.1', 'root', 'password', 'path/to/backup/config')

