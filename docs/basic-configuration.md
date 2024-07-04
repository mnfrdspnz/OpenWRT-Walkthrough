# Basic Configuration

## 3.1 Network Settings

**Configuring LAN and WAN Interfaces:**
1. **Access the Interface Configuration**:
   - Navigate to "Network" -> "Interfaces".
   - Click "Edit" on the LAN or WAN interface you want to configure.

2. **LAN Interface Configuration**:
   - Set the IPv4 address and netmask.
   - Configure DHCP options if needed.

3. **WAN Interface Configuration**:
   - Select the protocol (e.g., DHCP, Static IP, PPPoE).
   - Enter the necessary details based on the selected protocol.

**DHCP and Static IP Setup:**
1. **DHCP Setup**:
   - Go to "Network" -> "Interfaces".
   - Click "Edit" on the LAN interface.
   - Under "DHCP Server", configure the DHCP settings such as start and limit.

2. **Static IP Setup**:
   - Go to "Network" -> "Interfaces".
   - Click "Edit" on the LAN or WAN interface.
   - Set the IPv4 address, netmask, gateway, and DNS.

## 3.2 Wireless Configuration

**Setting Up Wi-Fi Networks (SSID, Security, Channels):**
1. **Access Wireless Settings**:
   - Navigate to "Network" -> "Wireless".
   - Click "Edit" on the wireless interface (e.g., `radio0`).

2. **Configure SSID and Security**:
   - Set the SSID (network name).
   - Choose the wireless security mode (e.g., WPA2-PSK).
   - Enter the passphrase.

3. **Set Channels**:
   - Select the channel or leave it to auto.
   - Configure advanced settings if necessary.

**Guest Wi-Fi Network Configuration:**
1. **Create a New Wireless Network**:
   - Go to "Network" -> "Wireless".
   - Click "Add" to create a new Wi-Fi network.
   - Set a different SSID for the guest network.

2. **Set Up Firewall Rules**:
   - Navigate to "Network" -> "Firewall".
   - Create a new zone for the guest network.
   - Configure the firewall rules to isolate the guest network from the main network.

## 3.3 Firewall Configuration

**Basic Firewall Rules:**
1. **Access Firewall Settings**:
   - Go to "Network" -> "Firewall".
   - Configure the default input, output, and forward rules.

2. **Add Custom Rules**:
   - Click "Add" under "Traffic Rules".
   - Define the custom rules for specific traffic needs.

**Port Forwarding and NAT:**
1. **Set Up Port Forwarding**:
   - Go to "Network" -> "Firewall".
   - Click "Add" under "Port Forwards".
   - Enter the source and destination information.

2. **Configure NAT**:
   - Ensure NAT is enabled for the WAN zone.
   - Configure any specific NAT rules if necessary.

## 3.4 System Management

**Firmware Updates:**
1. **Check for Updates**:
   - Navigate to "System" -> "Software".
   - Click "Update lists" to refresh the package lists.

2. **Perform the Update**:
   - Go to "System" -> "Backup / Flash Firmware".
   - Upload the new firmware file and follow the prompts.

**Backup and Restore Settings:**
1. **Backup Settings**:
   - Navigate to "System" -> "Backup / Flash Firmware".
   - Click "Generate Archive" to download the current settings.

2. **Restore Settings**:
   - Go to "System" -> "Backup / Flash Firmware".
   - Upload the backup file and click "Restore".

