import subprocess
import sys
import re
from termcolor import colored

def get_ip_address(interface):
    try:
        result = subprocess.run(['ip', 'addr', 'show', interface], capture_output=True, text=True, check=True)
        ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+)')
        match = ip_pattern.search(result.stdout)
        if match:
            return match.group(1)
        else:
            return "No IP address assigned."
    except subprocess.CalledProcessError:
        return "Failed to get IP address."

def change_ip_address(interface, new_ip):
    try:
        subprocess.run(['sudo', 'ip', 'addr', 'change', new_ip, 'dev', interface], check=True)
        print(colored(f"IP address changed to {new_ip} on {interface}.", "green"))
    except subprocess.CalledProcessError:
        print(colored("Failed to change IP address.", "red"))

def get_mac_address(interface):
    try:
        result = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "Failed to get MAC address."

def enable_interface(interface):
    try:
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], check=True)
        print(colored(f"Interface {interface} enabled.", "green"))
    except subprocess.CalledProcessError:
        print(colored(f"Failed to enable interface {interface}.", "red"))

def disable_interface(interface):
    try:
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'], check=True)
        print(colored(f"Interface {interface} disabled.", "green"))
    except subprocess.CalledProcessError:
        print(colored(f"Failed to disable interface {interface}.", "red"))

def show_menu():
    print(colored("\nNetwork Tool", "cyan", attrs=["bold"]))
    print(colored("1. View IP Address", "blue"))
    print(colored("2. Change IP Address", "blue"))
    print(colored("3. View MAC Address", "blue"))
    print(colored("4. Enable Network Interface", "blue"))
    print(colored("5. Disable Network Interface", "blue"))
    print(colored("6. Exit", "blue"))

def main():
    while True:
        show_menu()
        choice = input(colored("Choose an option: ", "yellow"))
        if choice == '1':
            interface = input(colored("Enter the network interface (e.g., eth0, wlan0): ", "yellow"))
            ip_address = get_ip_address(interface)
            print(colored(f"Current IP Address: {ip_address}", "green"))
        elif choice == '2':
            interface = input(colored("Enter the network interface (e.g., eth0, wlan0): ", "yellow"))
            new_ip = input(colored("Enter the new IP address (e.g., 192.168.1.10): ", "yellow"))
            change_ip_address(interface, new_ip)
        elif choice == '3':
            interface = input(colored("Enter the network interface (e.g., eth0, wlan0): ", "yellow"))
            mac_address = get_mac_address(interface)
            print(colored(f"MAC Address: {mac_address}", "green"))
        elif choice == '4':
            interface = input(colored("Enter the network interface to enable (e.g., eth0, wlan0): ", "yellow"))
            enable_interface(interface)
        elif choice == '5':
            interface = input(colored("Enter the network interface to disable (e.g., eth0, wlan0): ", "yellow"))
            disable_interface(interface)
        elif choice == '6':
            print(colored("Exiting...", "red"))
            sys.exit()
        else:
            print(colored("Invalid choice. Please try again.", "red"))

if __name__ == "__main__":
    main()
