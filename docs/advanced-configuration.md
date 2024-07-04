# Advanced Configuration

## 4.1 VLANs and Subnetting

**Configuring VLANs:**
1. **Access Switch Configuration**:
   - Navigate to "Network" -> "Switch".
   - Add VLANs by specifying VLAN IDs and assigning them to specific ports.

2. **Assign VLANs to Interfaces**:
   - Navigate to "Network" -> "Interfaces".
   - Click "Add new interface" and create a new interface for each VLAN.
   - Assign each interface to the corresponding VLAN.

**Setting Up Multiple Subnets:**
1. **Create New Interfaces**:
   - Go to "Network" -> "Interfaces".
   - Click "Add new interface" for each subnet you want to create.
   - Set the IP address and netmask for each subnet.

2. **Configure DHCP for Subnets**:
   - For each new interface, configure the DHCP settings under the "DHCP Server" tab.

## 4.2 Quality of Service (QoS)

**Traffic Shaping and Prioritization:**
1. **Access QoS Settings**:
   - Navigate to "Network" -> "QoS".
   - Enable QoS and configure basic settings such as upload and download limits.

2. **Define QoS Rules**:
   - Add custom QoS rules to prioritize specific traffic types or devices.

**Configuring SQM (Smart Queue Management):**
1. **Install SQM**:
   - Navigate to "System" -> "Software".
   - Install the `luci-app-sqm` package.

2. **Configure SQM**:
   - Go to "Network" -> "SQM QoS".
   - Enable SQM on the desired interface and configure the upload/download speeds.
   - Select the appropriate queue discipline (e.g., Cake, fq_codel).

## 4.3 VPN Setup

**Setting Up OpenVPN Server/Client:**
1. **Install OpenVPN**:
   - Navigate to "System" -> "Software".
   - Install the `openvpn-openssl` and `luci-app-openvpn` packages.

2. **Configure OpenVPN**:
   - Go to "Services" -> "OpenVPN".
   - Create and configure the server/client instances using the configuration templates provided by OpenVPN.

**Configuring WireGuard VPN:**
1. **Install WireGuard**:
   - Navigate to "System" -> "Software".
   - Install the `wireguard` and `luci-app-wireguard` packages.

2. **Configure WireGuard**:
   - Go to "Network" -> "Interfaces".
   - Click "Add new interface" and select "WireGuard VPN".
   - Configure the interface with the private and public keys, peers, and allowed IPs.

## 4.4 Network Services

**Configuring DNS and DHCP Options:**
1. **Access DHCP and DNS Settings**:
   - Navigate to "Network" -> "DHCP and DNS".
   - Configure the DNS forwardings, local domain, and other DNS settings.

2. **Configure DHCP Options**:
   - Define specific DHCP options such as DNS servers, lease time, and static leases.

**Setting Up Dynamic DNS (DDNS):**
1. **Install DDNS**:
   - Navigate to "System" -> "Software".
   - Install the `luci-app-ddns` package.

2. **Configure DDNS**:
   - Go to "Services" -> "Dynamic DNS".
   - Add a new DDNS configuration with the service provider's details and your account information.

