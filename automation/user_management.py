import paramiko

def add_user(host, username, password, new_user, new_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    commands = [
        f'useradd -m {new_user}',
        f'echo "{new_user}:{new_password}" | chpasswd',
        f'usermod -aG sudo {new_user}',
    ]
    for command in commands:
        ssh.exec_command(command)
    ssh.close()

add_user('192.168.1.1', 'root', 'password', 'newuser', 'newpassword')

