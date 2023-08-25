#!/bin/env python3

import psutil

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    print("Disk Usage:")
    print(f"Total: {disk_info.total} bytes")
    print(f"Used: {disk_info.used} bytes")
    print(f"Free: {disk_info.free} bytes")
    print(f"Usage Percentage: {disk_info.percent}%")

def main():
    print("System Administrator Tool")
    print("------------------------")
    print("1. Check Disk Usage")
    choice = input("Enter your choice: ")

    if choice == '1':
        check_disk_usage()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

