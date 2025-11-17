from scapy.all import ARP, Ether, srp

def network_scan(target_ip):
    # Create ARP request packet
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    print(f"\n[+] Scanning network: {target_ip}")
    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("\nActive Devices Found:")
    print("IP" + " " * 18 + "MAC")
    print("------------------------------------------")
    for device in devices:
        print(f"{device['ip']:16}    {device['mac']}")
    print("\nScan complete.\n")

# Example usage:
# Change the subnet based on your network
network_scan("192.168.56.0/22")
