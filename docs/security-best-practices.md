# Security Best Practices

## 7.1 Securing OpenWRT

**Best Practices for Securing Your Router:**
1. **Change Default Passwords**:
   - Upon initial setup, change the default root password to a strong, unique password.
   - Navigate to "System" -> "Administration" and set a new password.

2. **Disable Unnecessary Services**:
   - Disable any services that are not in use to reduce potential attack vectors.
   - Navigate to "System" -> "Startup" and disable unnecessary services.

3. **Keep Firmware Updated**:
   - Regularly check for and apply firmware updates to ensure you have the latest security patches.
   - Navigate to "System" -> "Backup / Flash Firmware" to update firmware.

4. **Enable Firewall**:
   - Ensure the firewall is enabled and properly configured.
   - Navigate to "Network" -> "Firewall" and verify the firewall rules.

5. **Use Strong Encryption for Wi-Fi**:
   - Configure your wireless networks to use WPA3 or WPA2 with a strong passphrase.
   - Navigate to "Network" -> "Wireless" and configure the security settings.

6. **Limit Access to the Web Interface**:
   - Restrict access to the LuCI web interface to specific IP addresses or disable remote access if not needed.
   - Navigate to "System" -> "Administration" and configure the access settings.

**Configuring SSH and HTTPS Access:**
1. **Enable HTTPS for Web Interface**:
   - Navigate to "System" -> "Administration".
   - Under the "Router Password" section, enable HTTPS access.
   - Install the necessary packages if prompted.

2. **Configure SSH Access**:
   - Navigate to "System" -> "Administration".
   - Under the "SSH Access" section, configure the following:
     - Change the SSH port from the default (22) to a non-standard port.
     - Restrict SSH access to specific IP addresses.
     - Enable key-based authentication for added security.

3. **Generate SSH Keys**:
   - Generate an SSH key pair on your local machine:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
     ```
   - Copy the public key to your OpenWRT router:
     ```bash
     ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.1.1
     ```

4. **Disable Password Authentication for SSH**:
   - Edit the SSH configuration file on your router:
     ```bash
     nano /etc/ssh/sshd_config
     ```
   - Set `PasswordAuthentication` to `no` and restart the SSH service:
     ```bash
     /etc/init.d/sshd restart
     ```

## 7.2 User Management

**Creating and Managing User Accounts:**
1. **Create a New User**:
   - SSH into your OpenWRT router.
   - Use the following command to add a new user:
     ```bash
     adduser newusername
     ```
   - Follow the prompts to set the user's password and other details.

2. **Add User to Sudoers**:
   - Edit the sudoers file to grant the new user administrative privileges:
     ```bash
     visudo
     ```
   - Add the following line:
     ```bash
     newusername ALL=(ALL) NOPASSWD:ALL
     ```

3. **Manage User Accounts**:
   - List all user accounts:
     ```bash
     cat /etc/passwd
     ```
   - Delete a user account:
     ```bash
     userdel -r username
     ```

**Setting Permissions:**
1. **Set File and Directory Permissions**:
   - Use `chmod` to change file and directory permissions. For example:
     ```bash
     chmod 700 /home/username
     ```
   - Use `chown` to change file and directory ownership. For example:
     ```bash
     chown username:groupname /home/username
     ```

2. **Limit Access to Configuration Files**:
   - Ensure sensitive configuration files are only accessible by root or authorized users.
   - For example, set permissions for the `/etc/config` directory:
     ```bash
     chmod 700 /etc/config
     ```

