import pywifi
from pywifi import const
import time

def scan_networks():
    """
    Scans all surrounding Wi-Fi networks and returns them in a list.
    """
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)  # Wait for the scan to complete
    scan_results = iface.scan_results()
    
    networks = []
    for network in scan_results:
        networks.append({
            "essid": network.ssid,
            "quality": network.signal,
            "bssid": network.bssid,
            "encryption": network.akm[0] if network.akm else "Unknown"
        })
    return networks

def get_strongest_network(networks):
    """
    Chooses the strongest Wi-Fi network from the list of networks.
    """
    strongest_network = None
    for network in networks:
        if not strongest_network or network["quality"] > strongest_network["quality"]:
            strongest_network = network
    return strongest_network

def print_network_info(network):
    """
    Prints information about a Wi-Fi network.
    """
    print(f"**Wi-Fi Network:** {network['essid']}")
    print(f"  - Signal strength: {network['quality']}")
    print(f"  - BSSID: {network['bssid']}")
    print(f"  - Encryption type: {network['encryption']}")

if __name__ == "__main__":
    networks = scan_networks()
    if networks:
        strongest_network = get_strongest_network(networks)

        print("\n**Strongest Wi-Fi Network:**")
        print_network_info(strongest_network)
    else:
        print("No Wi-Fi networks found.")
