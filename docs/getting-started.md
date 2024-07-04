# Getting Started

## 2.1 Installation

**Supported Devices:**
OpenWRT supports a wide range of devices, including many popular routers from brands like TP-Link, Linksys, Netgear, and Asus. To check if your device is supported:
- Visit the [OpenWRT Table of Hardware](https://openwrt.org/toh/start).
- Search for your device model to see if there is a compatible OpenWRT firmware available.

**Downloading OpenWRT Firmware:**
1. Go to the [OpenWRT Firmware Selector](https://firmware-selector.openwrt.org/).
2. Enter your device model in the search bar.
3. Select the appropriate firmware version for your device.
4. Click on the download link to download the firmware file.

**Flashing OpenWRT on Your Device:**
1. **Backup Current Settings**: Before flashing, make sure to back up your current router settings.
2. **Access Router Interface**: Connect to your router and access its web interface (usually at `192.168.1.1` or `192.168.0.1`).
3. **Upload Firmware**:
   - Navigate to the firmware upgrade section of your router's interface.
   - Select the downloaded OpenWRT firmware file.
   - Follow the prompts to upload and install the firmware.
4. **Wait for Reboot**: The router will reboot with the new OpenWRT firmware installed. This may take a few minutes.

## 2.2 Initial Setup

**Accessing the OpenWRT Interface:**
1. Connect your computer to the router via an Ethernet cable or Wi-Fi.
2. Open a web browser and navigate to `http://192.168.1.1`.
3. You will be prompted to set a root password. Enter a strong password and save it.

**Basic Configuration:**

1. **Setting Up Wi-Fi**:
   - Go to the "Network" tab and select "Wireless".
   - Click "Edit" on the default wireless network (usually labeled `radio0`).
   - Set the SSID (network name) and configure the wireless security (WPA2-PSK is recommended).
   - Save and apply the changes.

2. **Configuring LAN and WAN**:
   - Navigate to "Network" -> "Interfaces".
   - Click "Edit" on the LAN interface to set a static IP address if needed.
   - Configure the WAN interface for your internet connection (e.g., DHCP, PPPoE).

3. **Setting Passwords**:
   - Go to "System" -> "Administration".
   - Set a strong password for the root user if you haven’t already.
   - Configure SSH access if needed, and set SSH keys for secure access.

