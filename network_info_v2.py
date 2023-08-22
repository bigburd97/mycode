#!/usr/bin/env python3

import psutil
import netifaces
import subprocess
from tabulate import tabulate

def get_ip_info():
    """Get IP address information for each network interface."""
    ip_info = []

    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addrs:
            ip_address = addrs[netifaces.AF_INET][0]["addr"]
            ip_info.append([
                interface,
                ip_address
            ])

    return ip_info

def get_routing_statistics():
    """Get routing statistics including packet loss."""
    routing_stats = []
    try:
        routing_info = subprocess.run(["netstat", "-s"], capture_output=True, text=True).stdout
        lines = routing_info.split("\n")
        for line in lines:
            if "packet receive errors" in line:
                packet_loss = line.split()[0]
                routing_stats.append([
                    "Packet Loss",
                    packet_loss
                ])
    except FileNotFoundError:
        pass
    return routing_stats

def get_network_traffic():
    """Get network traffic information for each network interface."""
    network_traffic = []
    for interface, stats in psutil.net_io_counters(pernic=True).items():
        received = f"{stats.bytes_recv / (1024 ** 2):.2f} MB"
        sent = f"{stats.bytes_sent / (1024 ** 2):.2f} MB"
        network_traffic.append([
            interface,
            received,
            sent
        ])
    return network_traffic

def main():
    """Main function to display comprehensive system information."""
    print("System Information:")

    # Display IP information in a table
    ip_info = get_ip_info()
    ip_headers = ["Interface", "IP Address"]
    print(tabulate(ip_info, headers=ip_headers, tablefmt="pretty"))

    # Display routing statistics in a table
    routing_stats = get_routing_statistics()
    routing_headers = ["Metric", "Value"]
    print(tabulate(routing_stats, headers=routing_headers, tablefmt="pretty"))

    # Display network traffic in a table
    network_traffic = get_network_traffic()
    network_traffic_headers = ["Interface", "Received", "Sent"]
    print(tabulate(network_traffic, headers=network_traffic_headers, tablefmt="pretty"))

if __name__ == "__main__":
    main()

