# Monitoring and Troubleshooting

## 6.1 Network Monitoring Tools

**Using LuCI (Web Interface) for Monitoring:**
1. **Access LuCI Interface**:
   - Open a web browser and navigate to `http://192.168.1.1`.
   - Log in with your root password.

2. **Real-Time Graphs**:
   - Go to "Status" -> "Realtime Graphs".
   - View real-time graphs for CPU usage, memory usage, network traffic, and more.

3. **Network Status**:
   - Navigate to "Status" -> "Overview".
   - Check the status of network interfaces, active connections, and device uptime.

**CLI Monitoring Tools:**
1. **top**:
   - SSH into your OpenWRT device.
   - Run the `top` command to display real-time system performance information, including CPU and memory usage.
     ```bash
     top
     ```

2. **iftop**:
   - Install `iftop` if it’s not already installed:
     ```bash
     opkg update
     opkg install iftop
     ```
   - Run `iftop` to monitor real-time network bandwidth usage by each connection.
     ```bash
     iftop
     ```

3. **vnstat**:
   - Install `vnstat` if it’s not already installed:
     ```bash
     opkg update
     opkg install vnstat
     ```
   - Start the `vnstat` service:
     ```bash
     /etc/init.d/vnstat start
     ```
   - Run `vnstat` to view network traffic statistics.
     ```bash
     vnstat
     ```

## 6.2 Logs and Diagnostics

**Accessing System Logs:**
1. **Using LuCI**:
   - Navigate to "Status" -> "System Log" to view the system log.
   - Navigate to "Status" -> "Kernel Log" to view the kernel log.

2. **Using CLI**:
   - SSH into your OpenWRT device.
   - View the system log with the following command:
     ```bash
     logread
     ```
   - View the kernel log with the following command:
     ```bash
     dmesg
     ```

**Common Troubleshooting Commands and Techniques:**
1. **Check Network Interfaces**:
   - Use the `ifconfig` or `ip a` command to check the status of network interfaces.
     ```bash
     ifconfig
     ```
     or
     ```bash
     ip a
     ```

2. **Check Network Connectivity**:
   - Use the `ping` command to check connectivity to other devices or the internet.
     ```bash
     ping 8.8.8.8
     ```

3. **DNS Resolution**:
   - Use the `nslookup` or `dig` command to check DNS resolution.
     ```bash
     nslookup google.com
     ```
     or
     ```bash
     dig google.com
     ```

4. **Check Active Connections**:
   - Use the `netstat` or `ss` command to check active network connections.
     ```bash
     netstat -tuln
     ```
     or
     ```bash
     ss -tuln
     ```

5. **Restart Services**:
   - Restart network services if there are connectivity issues.
     ```bash
     /etc/init.d/network restart
     ```

