#!/usr/bin/env python3

import psutil
import netifaces
from tabulate import tabulate

def get_storage_info():
    """Get storage information for each mounted partition."""
    disk_partitions = psutil.disk_partitions()
    storage_info = []

    for partition in disk_partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        storage_info.append([
            partition.mountpoint,
            f"{usage.total / (1024 ** 3):.2f} GB",
            f"{usage.used / (1024 ** 3):.2f} GB",
            f"{usage.free / (1024 ** 3):.2f} GB",
            partition.fstype
        ])

    return storage_info


def get_network_info():
    """Get network information for each network interface."""
    network_info = []

    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addrs:
            ip_address = addrs[netifaces.AF_INET][0]["addr"]
            network_info.append([
                interface,
                ip_address
            ])

    return network_info


def main():
    """Main function to display storage and network information."""
    print("Storage Information:")
    storage_info = get_storage_info()
    storage_headers = ["Mount Point", "Total Size", "Used", "Free", "File System"]
    print(tabulate(storage_info, headers=storage_headers, tablefmt="pretty"))

    print("\nNetwork Information:")
    network_info = get_network_info()
    network_headers = ["Interface", "IP Address"]
    print(tabulate(network_info, headers=network_headers, tablefmt="pretty"))


if __name__ == "__main__":
    main()

