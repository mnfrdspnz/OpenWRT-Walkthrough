import paramiko

def monitor_network(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('vnstat --json')
    output = stdout.read().decode()
    print(output)
    ssh.close()

monitor_network('192.168.1.1', 'root', 'password')

