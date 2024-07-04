# Home Network Setup

## Comprehensive Guide for a Typical Home Network

1. **Network Topology**:
   - **Devices**: Router, multiple wireless devices (laptops, smartphones, tablets), wired devices (desktop PCs, smart TV), smart home devices (lights, thermostats, cameras).
   - **IP Address Range**: 192.168.1.0/24
   - **Wi-Fi Networks**: Primary SSID for family, guest SSID for visitors, IoT SSID for smart devices.

2. **Initial Router Configuration**:
   - **Static IP for Router**: 192.168.1.1
   - **Configure DNS and Gateway**: Use reliable DNS servers such as Google (8.8.8.8, 8.8.4.4) or Cloudflare (1.1.1.1).

3. **LAN Configuration**:
   - **Static IP for Router**:
     ```bash
     uci set network.lan.ipaddr='192.168.1.1'
     uci set network.lan.netmask='255.255.255.0'
     uci set network.lan.gateway='192.168.1.1'
     uci set network.lan.dns='8.8.8.8 8.8.4.4'
     uci commit network
     ```

4. **DHCP Configuration**:
   - **DHCP Range**:
     ```bash
     uci set dhcp.lan.start='100'
     uci set dhcp.lan.limit='150'
     uci set dhcp.lan.leasetime='12h'
     uci commit dhcp
     ```

5. **Wi-Fi Configuration**:
   - **Primary Wi-Fi Network**:
     ```bash
     uci set wireless.@wifi-iface[0].ssid='HomeNetwork'
     uci set wireless.@wifi-iface[0].encryption='psk2+ccmp'
     uci set wireless.@wifi-iface[0].key='YourSecurePassword'
     uci commit wireless
     ```
   - **Guest Wi-Fi Network**:
     ```bash
     uci add wireless wifi-iface
     uci set wireless.@wifi-iface[-1].device='radio0'
     uci set wireless.@wifi-iface[-1].mode='ap'
     uci set wireless.@wifi-iface[-1].network='guest'
     uci set wireless.@wifi-iface[-1].ssid='GuestNetwork'
     uci set wireless.@wifi-iface[-1].encryption='psk2+ccmp'
     uci set wireless.@wifi-iface[-1].key='GuestPassword'
     uci set wireless.@wifi-iface[-1].isolate='1'
     uci commit wireless
     ```
   - **IoT Wi-Fi Network**:
     ```bash
     uci add wireless wifi-iface
     uci set wireless.@wifi-iface[-1].device='radio0'
     uci set wireless.@wifi-iface[-1].mode='ap'
     uci set wireless.@wifi-iface[-1].network='iot'
     uci set wireless.@wifi-iface[-1].ssid='IoTNetwork'
     uci set wireless.@wifi-iface[-1].encryption='psk2+ccmp'
     uci set wireless.@wifi-iface[-1].key='IoTPassword'
     uci commit wireless
     ```

6. **Network Segmentation**:
   - **Create VLANs for Guest and IoT Networks**:
     ```bash
     uci set network.guest='interface'
     uci set network.guest.proto='static'
     uci set network.guest.ipaddr='192.168.2.1'
     uci set network.guest.netmask='255.255.255.0'
     uci commit network

     uci set network.iot='interface'
     uci set network.iot.proto='static'
     uci set network.iot.ipaddr='192.168.3.1'
     uci set network.iot.netmask='255.255.255.0'
     uci commit network
     ```

   - **Configure DHCP for VLANs**:
     ```bash
     uci add dhcp
     uci set dhcp.@dhcp[-1].interface='guest'
     uci set dhcp.@dhcp[-1].start='100'
     uci set dhcp.@dhcp[-1].limit='50'
     uci set dhcp.@dhcp[-1].leasetime='12h'
     uci commit dhcp

     uci add dhcp
     uci set dhcp.@dhcp[-1].interface='iot'
     uci set dhcp.@dhcp[-1].start='100'
     uci set dhcp.@dhcp[-1].limit='50'
     uci set dhcp.@dhcp[-1].leasetime='12h'
     uci commit dhcp
     ```

7. **Firewall Configuration**:
   - **Basic Firewall Rules**:
     ```bash
     uci set firewall.@defaults[0].input='ACCEPT'
     uci set firewall.@defaults[0].output='ACCEPT'
     uci set firewall.@defaults[0].forward='REJECT'
     uci commit firewall
     ```
   - **Guest Network Isolation**:
     ```bash
     uci add firewall zone
     uci set firewall.@zone[-1].name='guest'
     uci set firewall.@zone[-1].network='guest'
     uci set firewall.@zone[-1].input='REJECT'
     uci set firewall.@zone[-1].forward='REJECT'
     uci set firewall.@zone[-1].output='ACCEPT'
     uci add firewall forwarding
     uci set firewall.@forwarding[-1].src='guest'
     uci set firewall.@forwarding[-1].dest='wan'
     uci commit firewall
     ```
   - **IoT Network Isolation**:
     ```bash
     uci add firewall zone
     uci set firewall.@zone[-1].name='iot'
     uci set firewall.@zone[-1].network='iot'
     uci set firewall.@zone[-1].input='REJECT'
     uci set firewall.@zone[-1].forward='REJECT'
     uci set firewall.@zone[-1].output='ACCEPT'
     uci add firewall forwarding
     uci set firewall.@forwarding[-1].src='iot'
     uci set firewall.@forwarding[-1].dest='wan'
     uci commit firewall
     ```
   - **Allow Internet Access for Guest and IoT Networks**:
     ```bash
     uci add firewall rule
     uci set firewall.@rule[-1].name='Allow-DHCP-Guest'
     uci set firewall.@rule[-1].src='guest'
     uci set firewall.@rule[-1].proto='udp'
     uci set firewall.@rule[-1].dest_port='67-68'
     uci set firewall.@rule[-1].target='ACCEPT'
     uci add firewall rule
     uci set firewall.@rule[-1].name='Allow-DNS-Guest'
     uci set firewall.@rule[-1].src='guest'
     uci set firewall.@rule[-1].proto='tcp udp'
     uci set firewall.@rule[-1].dest_port='53'
     uci set firewall.@rule[-1].target='ACCEPT'
     uci commit firewall

     uci add firewall rule
     uci set firewall.@rule[-1].name='Allow-DHCP-IoT'
     uci set firewall.@rule[-1].src='iot'
     uci set firewall.@rule[-1].proto='udp'
     uci set firewall.@rule[-1].dest_port='67-68'
     uci set firewall.@rule[-1].target='ACCEPT'
     uci add firewall rule
     uci set firewall.@rule[-1].name='Allow-DNS-IoT'
     uci set firewall.@rule[-1].src='iot'
     uci set firewall.@rule[-1].proto='tcp udp'
     uci set firewall.@rule[-1].dest_port='53'
     uci set firewall.@rule[-1].target='ACCEPT'
     uci commit firewall
     ```

8. **Advanced Security Measures**:
   - **Change Default Passwords**:
     ```bash
     passwd
     ```
   - **Enable HTTPS for Web Interface**:
     ```bash
     uci set uhttpd.main.redirect_https='1'
     uci commit uhttpd
     /etc/init.d/uhttpd restart
     ```
   - **Disable Remote Access to Web Interface**:
     ```bash
     uci set uhttpd.main.listen_http='127.0.0.1:80'
     uci set uhttpd.main.listen_https='127.0.0.1:443'
     uci commit uhttpd
     /etc/init.d/uhttpd restart
     ```
   - **Configure SSH Access**:
     ```bash
     uci set dropbear.@dropbear[0].Port='2222'
     uci set dropbear.@dropbear[0].PasswordAuth='off'
     uci set dropbear.@dropbear[0].RootPasswordAuth='off'
     uci commit dropbear
     /etc/init.d/dropbear restart
     ```
   - **Set Up SSH Keys**:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
     ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.1.1
     ```

9. **Network Monitoring and Management**:
   - **Install Monitoring Tools**:
     ```bash
     opkg update
     opkg install htop iftop vnstat
     ```
   - **Configure vnStat**:
     ```bash
     /etc/init.d/vnstat start
     /etc/init.d/vnstat enable
     ```

10. **Backup and Restore Configuration**:
    - **Backup Settings**:
      ```bash
      sysupgrade -b /tmp/backup-$(date +%F).tar.gz
      ```
    - **Restore Settings**:
      ```bash
      sysupgrade -r /path/to/backup.tar.gz
      ```

11. **Regular Maintenance**:
    - **Update Firmware Regularly**:
      ```bash
      opkg update
      opkg list-upgradable | cut -f 1 -d ' ' | xargs opkg upgrade
      ```
