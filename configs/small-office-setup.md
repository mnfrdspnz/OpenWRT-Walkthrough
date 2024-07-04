# Small Office Network Setup

## Comprehensive Guide for a Small Office Network

1. **Network Topology**:
   - **Devices**: Router, multiple wired devices (computers, printers, IP phones), wireless devices (laptops, smartphones), and smart devices (cameras, IoT devices).
   - **IP Address Range**: 192.168.2.0/24
   - **Separate VLANs**: For different departments or purposes (e.g., Admin, IT, Sales, Guests).

2. **Initial Router Configuration**:
   - **Static IP for Router**: 192.168.2.1
   - **Configure DNS and Gateway**: Use reliable DNS servers such as Google (8.8.8.8, 8.8.4.4) or Cloudflare (1.1.1.1).

3. **LAN Configuration**:
   - **Static IP for Router**:
     ```bash
     uci set network.lan.ipaddr='192.168.2.1'
     uci set network.lan.netmask='255.255.255.0'
     uci set network.lan.gateway='192.168.2.1'
     uci set network.lan.dns='8.8.8.8 8.8.4.4'
     uci commit network
     ```

4. **DHCP Configuration**:
   - **DHCP Range**:
     ```bash
     uci set dhcp.lan.start='100'
     uci set dhcp.lan.limit='100'
     uci set dhcp.lan.leasetime='12h'
     uci commit dhcp
     ```

5. **VLAN Configuration**:
   - **Create VLANs for Different Departments**:
     ```bash
     uci set network.vlan10='interface'
     uci set network.vlan10.ifname='eth0.10'
     uci set network.vlan10.proto='static'
     uci set network.vlan10.ipaddr='192.168.10.1'
     uci set network.vlan10.netmask='255.255.255.0'
     uci commit network

     uci set network.vlan20='interface'
     uci set network.vlan20.ifname='eth0.20'
     uci set network.vlan20.proto='static'
     uci set network.vlan20.ipaddr='192.168.20.1'
     uci set network.vlan20.netmask='255.255.255.0'
     uci commit network

     uci set network.vlan30='interface'
     uci set network.vlan30.ifname='eth0.30'
     uci set network.vlan30.proto='static'
     uci set network.vlan30.ipaddr='192.168.30.1'
     uci set network.vlan30.netmask='255.255.255.0'
     uci commit network
     ```

   - **Configure DHCP for VLANs**:
     ```bash
     uci add dhcp
     uci set dhcp.@dhcp[-1].interface='vlan10'
     uci set dhcp.@dhcp[-1].start='100'
     uci set dhcp.@dhcp[-1].limit='50'
     uci set dhcp.@dhcp[-1].leasetime='12h'
     uci commit dhcp

     uci add dhcp
     uci set dhcp.@dhcp[-1].interface='vlan20'
     uci set dhcp.@dhcp[-1].start='100'
     uci set dhcp.@dhcp[-1].limit='50'
     uci set dhcp.@dhcp[-1].leasetime='12h'
     uci commit dhcp

     uci add dhcp
     uci set dhcp.@dhcp[-1].interface='vlan30'
     uci set dhcp.@dhcp[-1].start='100'
     uci set dhcp.@dhcp[-1].limit='50'
     uci set dhcp.@dhcp[-1].leasetime='12h'
     uci commit dhcp
     ```

6. **Wi-Fi Configuration**:
   - **Primary Wi-Fi Network**:
     ```bash
     uci set wireless.@wifi-iface[0].ssid='OfficeNetwork'
     uci set wireless.@wifi-iface[0].encryption='psk2+ccmp'
     uci set wireless.@wifi-iface[0].key='OfficeSecurePassword'
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

7. **Firewall Configuration**:
   - **Basic Firewall Rules**:
     ```bash
     uci set firewall.@defaults[0].input='ACCEPT'
     uci set firewall.@defaults[0].output='ACCEPT'
     uci set firewall.@defaults[0].forward='REJECT'
     uci commit firewall
     ```
   - **Inter-VLAN Routing**:
     ```bash
     uci add firewall zone
     uci set firewall.@zone[-1].name='vlan10'
     uci set firewall.@zone[-1].network='vlan10'
     uci set firewall.@zone[-1].input='ACCEPT'
     uci set firewall.@zone[-1].forward='ACCEPT'
     uci set firewall.@zone[-1].output='ACCEPT'
     uci commit firewall

     uci add firewall zone
     uci set firewall.@zone[-1].name='vlan20'
     uci set firewall.@zone[-1].network='vlan20'
     uci set firewall.@zone[-1].input='ACCEPT'
     uci set firewall.@zone[-1].forward='ACCEPT'
     uci set firewall.@zone[-1].output='ACCEPT'
     uci commit firewall

     uci add firewall zone
     uci set firewall.@zone[-1].name='vlan30'
     uci set firewall.@zone[-1].network='vlan30'
     uci set firewall.@zone[-1].input='ACCEPT'
     uci set firewall.@zone[-1].forward='ACCEPT'
     uci set firewall.@zone[-1].output='ACCEPT'
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

8. **VPN Configuration**:
   - **Setting Up OpenVPN Server**:
     ```bash
     opkg update
     opkg install openvpn-openssl
     ```

   - **Create OpenVPN Server Configuration**:
     ```bash
     cat <<EOF > /etc/openvpn/server.conf
     port 1194
     proto udp
     dev tun
     ca /etc/openvpn/ca.crt
     cert /etc/openvpn/server.crt
     key /etc/openvpn/server.key
     dh /etc/openvpn/dh.pem
     server 10.8.0.0 255.255.255.0
     ifconfig-pool-persist /var/log/openvpn/ipp.txt
     push "redirect-gateway def1 bypass-dhcp"
     push "dhcp-option DNS 8.8.8.8"
     push "dhcp-option DNS 8.8.4.4"
     keepalive 10 120
     cipher AES-256-CBC
     user nobody
     group nogroup
     persist-key
     persist-tun
     status /var/log/openvpn/openvpn-status.log
     log-append /var/log/openvpn/openvpn.log
     verb 3
     EOF
     ```

   - **Start OpenVPN Service**:
     ```bash
     /etc/init.d/openvpn start
     /etc/init.d/openvpn enable
     ```

   - **Firewall Rules for OpenVPN**:
     ```bash
     uci add firewall rule
     uci set firewall.@rule[-1].name='Allow-OpenVPN'
     uci set firewall.@rule[-1].src='wan'
     uci set firewall.@rule[-1].proto='udp'
     uci set firewall.@rule[-1].dest_port='1194'
     uci set firewall.@rule[-1].target='ACCEPT'
     uci commit firewall
     /etc/init.d/firewall restart
     ```

   - **Setting Up WireGuard VPN**:
     ```bash
     opkg update
     opkg install wireguard-tools
     ```

   - **Create WireGuard Configuration**:
     ```bash
     cat <<EOF > /etc/config/network
     config interface 'wg0'
         option proto 'wireguard'
         option private_key 'your_private_key'
         option listen_port '51820'
         list addresses '10.9.0.1/24'

     config wireguard_wg0
         option public_key 'client_public_key'
         list allowed_ips '10.9.0.2/32'
         option route_allowed_ips '1'
         option persistent_keepalive '25'
     EOF
     ```

   - **Start WireGuard Service**:
     ```bash
     /etc/init.d/network restart
     ```

9. **Accessing Shared SaaS Services**:
   - **Configure DNS Forwarding**:
     ```bash
     uci set dhcp.@dnsmasq[0].server='8.8.8.8'
     uci set dhcp.@dnsmasq[0].server='8.8.4.4'
     uci commit dhcp
     /etc/init.d/dnsmasq restart
     ```

   - **Firewall Rules for SaaS Access**:
     ```bash
     uci add firewall rule
     uci set firewall.@rule[-1].name='Allow-Google-Apps'
     uci set firewall.@rule[-1].src='lan'
     uci set firewall.@rule[-1].dest='wan'
     uci set firewall.@rule[-1].proto='tcp'
     uci set firewall.@rule[-1].dest_port='80 443'
     uci set firewall.@rule[-1].target='ACCEPT'
     uci commit firewall
     /etc/init.d/firewall restart
     ```

10. **Advanced Security Measures**:
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
      ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.2.1
      ```

11. **Network Monitoring and Management**:
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

12. **Backup and Restore Configuration**:
    - **Backup Settings**:
      ```bash
      sysupgrade -b /tmp/backup-$(date +%F).tar.gz
      ```
    - **Restore Settings**:
      ```bash
      sysupgrade -r /path/to/backup.tar.gz
      ```

13. **Regular Maintenance**:
    - **Update Firmware Regularly**:
      ```bash
      opkg update
      opkg list-upgradable | cut -f 1 -d ' ' | xargs opkg upgrade
      ```


