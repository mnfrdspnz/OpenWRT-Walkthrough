import paramiko

def update_firmware(host, username, password, firmware_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(firmware_path, '/tmp/firmware.bin')
    sftp.close()
    stdin, stdout, stderr = ssh.exec_command('sysupgrade /tmp/firmware.bin')
    stdout.channel.recv_exit_status()
    ssh.close()

update_firmware('192.168.1.1', 'root', 'password', 'path/to/firmware.bin')

