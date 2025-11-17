# Network Scanner Tool (Scapy)

This project is a simple **local network scanner** built using the Python **Scapy** library. It sends ARP requests to identify all active devices (IP + MAC) on your network.

---

## 📌 Features
- Scan your local network for active devices
- Displays IP and MAC address of each device
- Works on Linux (Kali, Ubuntu, etc.)
- Useful for cybersecurity learning and home network monitoring

---

## 🛠️ Installation

### 1. Install Python3 (if not installed)
```bash
sudo apt install python3 python3-pip -y
```

### 2. Install Scapy
```bash
sudo pip3 install scapy
```

### 3. Clone your GitHub repository
```bash
git clone https://github.com/yourusername/network-scanner
cd network-scanner
```

---

## ▶️ How to Use

### 1. Run the script with sudo
```bash
sudo python3 network_scan.py
```

### 2. Example Output
```
[+] Scanning network: 192.168.56.0/22

Active Devices Found:
IP                   MAC
------------------------------------------
192.168.56.1         00:14:22:01:23:45
192.168.56.22        5e:4c:b2:df:3e:0e
192.168.56.31        d6:54:b3:1f:36:c7

Scan complete.
```

---

## 🧠 How It Works
This tool uses **ARP (Address Resolution Protocol)** to discover devices.

1. Sends ARP broadcast packets (`ff:ff:ff:ff:ff:ff`)
2. Devices on the LAN respond with their IP + MAC
3. Scapy collects responses and prints the device list

ARP works only within your local network (Layer-2), so this tool cannot scan the internet.

---

## 🔐 Cybersecurity Use Cases
This scanner is helpful for:

- Learning network discovery techniques
- Understanding ARP behavior
- Detecting unknown devices on your Wi-Fi
- Building your own security tools
- Checking if someone else is connected to your hotspot

⚠️ **Use only on networks you own or have permission to test.**

---

## 👤 Normal People Use Cases
- See all devices connected to your Wi-Fi
- Identify strangers using your network
- Check if your smart home devices are online

---

## 📸 Sample Screenshot
*(You can add your screenshot here)*

Example placeholder:
```
![Network Scan Result](images/sample_output.png)
```

---

## 📂 File Structure
```
network-scanner/
│
├── network_scan.py
└── README.md
```

---

## 📜 License
This project is open‑source. You may modify and share it.

---

## 💬 Support
If you need help improving this tool or adding features like:
- Vendor lookup (Samsung, Apple, etc.)
- Retry scanning
- Saving results to file
- Better UI

Feel free to ask!

