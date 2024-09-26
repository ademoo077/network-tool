import subprocess
import sys
import re
from termcolor import colored

def display_hacker_art():
    """Affiche un dessin ASCII de style hacker avec le nom 'hezil'."""
    hacker_art = r"""
    
  _    _          _ _   _                _    
 | |  | |        (_) | | |              | |   
 | |__| | ___ _____| | | |__   __ _  ___| | __
 |  __  |/ _ \_  / | | | '_ \ / _` |/ __| |/ /
 | |  | |  __// /| | | | | | | (_| | (__|   < 
 |_|  |_|\___/___|_|_| |_| |_|\__,_|\___|_|\_\
                                              
                                              

    """
    print(colored(hacker_art, "green", attrs=["bold"]))

def run_command(command):
    """Execute a shell command and return the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return colored(f"Error: {e}", "red")

def get_ip_address(interface):
    """Get the current IP address of the specified network interface."""
    command = ['ip', 'addr', 'show', interface]
    output = run_command(command)
    ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+)')
    match = ip_pattern.search(output)
    return match.group(1) if match else "No IP address assigned."

def change_ip_address(interface, new_ip):
    """Change the IP address of the specified network interface."""
    command = ['sudo', 'ip', 'addr', 'change', new_ip, 'dev', interface]
    output = run_command(command)
    if "Error" in output:
        print(output)
    else:
        print(colored(f"IP address changed to {new_ip} on {interface}.", "green"))

def get_mac_address(interface):
    """Get the MAC address of the specified network interface."""
    command = ['cat', f'/sys/class/net/{interface}/address']
    return run_command(command)

def enable_interface(interface):
    """Enable the specified network interface."""
    command = ['sudo', 'ip', 'link', 'set', interface, 'up']
    output = run_command(command)
    print(colored(f"Interface {interface} enabled.", "green") if "Error" not in output else output)

def disable_interface(interface):
    """Disable the specified network interface."""
    command = ['sudo', 'ip', 'link', 'set', interface, 'down']
    output = run_command(command)
    print(colored(f"Interface {interface} disabled.", "green") if "Error" not in output else output)

def show_interface_details(interface):
    """Display detailed information about the specified network interface."""
    command = ['ip', 'addr', 'show', interface]
    return run_command(command)

def list_interfaces():
    """List all available network interfaces."""
    command = ['ip', 'link', 'show']
    return run_command(command)

def show_menu():
    """Display the main menu options."""
    print(colored("\n🛠️ Network Tool", "cyan", attrs=["bold"]))
    print(colored("1. View IP Address", "blue"))
    print(colored("2. Change IP Address", "blue"))
    print(colored("3. View MAC Address", "blue"))
    print(colored("4. Enable Network Interface", "blue"))
    print(colored("5. Disable Network Interface", "blue"))
    print(colored("6. Show Interface Details", "blue"))
    print(colored("7. List All Interfaces", "blue"))
    print(colored("8. Exit", "blue"))

def main():
    display_hacker_art()  # Afficher le dessin ASCII
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
            interface = input(colored("Enter the network interface to show details (e.g., eth0, wlan0): ", "yellow"))
            details = show_interface_details(interface)
            print(colored(details, "cyan"))
        elif choice == '7':
            interfaces = list_interfaces()
            print(colored(interfaces, "cyan"))
        elif choice == '8':
            print(colored("Exiting...", "red"))
            sys.exit()
        else:
            print(colored("Invalid choice. Please try again.", "red"))

if __name__ == "__main__":
    main()
