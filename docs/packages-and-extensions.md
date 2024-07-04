# Packages and Extensions

## 5.1 Package Management

**Installing and Removing Packages:**
1. **Access Software Management**:
   - Navigate to "System" -> "Software".

2. **Update Package Lists**:
   - Click "Update lists" to refresh the available packages.

3. **Install a Package**:
   - Use the search bar to find the desired package.
   - Click "Install" next to the package name.
   - Confirm the installation when prompted.

4. **Remove a Package**:
   - Find the installed package in the list.
   - Click "Remove" next to the package name.
   - Confirm the removal when prompted.

**Commonly Used Packages:**
1. **luci**: Web interface for OpenWRT.
2. **luci-app-sqm**: Smart Queue Management for QoS.
3. **openvpn-openssl**: OpenVPN server and client.
4. **wireguard**: WireGuard VPN.
5. **luci-app-ddns**: Dynamic DNS client.
6. **nano**: Text editor.
7. **htop**: Interactive process viewer.

## 5.2 Custom Scripts

**Writing and Deploying Custom Scripts:**
1. **Create a Script**:
   - Use SSH or the web interface to access the router.
   - Navigate to `/etc/` or `/usr/bin/` directory.
   - Create a new script file. For example, using `nano`:
     ```bash
     nano /etc/custom_script.sh
     ```

2. **Write the Script**:
   - Add your script content. For example, a simple backup script:
     ```bash
     #!/bin/sh
     # Custom backup script
     tar -czf /tmp/backup.tgz /etc/config
     ```

3. **Make the Script Executable**:
   - Change the permissions to make the script executable:
     ```bash
     chmod +x /etc/custom_script.sh
     ```

4. **Deploy the Script**:
   - Run the script manually:
     ```bash
     /etc/custom_script.sh
     ```
   - Schedule the script to run automatically using cron jobs:
     ```bash
     crontab -e
     ```
     Add a cron job entry. For example, to run the script daily at midnight:
     ```bash
     0 0 * * * /etc/custom_script.sh
     ```

**Automation Tasks Using Scripts:**
1. **Automate Configuration Backups**:
   - Create a script to back up the configuration files and store them on a remote server.
   - Schedule the script to run at regular intervals using cron jobs.

2. **Automate Firmware Updates**:
   - Create a script to check for firmware updates, download, and install them.
   - Schedule the script to run at regular intervals.

3. **Automate Network Monitoring**:
   - Create a script to monitor network usage and generate reports.
   - Schedule the script to run at regular intervals.

