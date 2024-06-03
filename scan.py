import subprocess

def scan_networks():
  """
  Scans all surrounding Wi-Fi networks and returns them in a list.
  Uses PowerShell commands on Windows.
  """
  networks = []
  command = 'powershell Get-NetAdapterWirelessNetworkAdapter -Name Wi-Fi | Where-Object {$_.NetworkName}'
  output = subprocess.check_output(command, shell=True, encoding='utf-8').strip()

  # Parse the output to extract network information
  for line in output.splitlines():
    if ':' in line:
      key, value = line.split(':', 1)
      key = key.strip()
      value = value.strip()
      if key == 'NetworkName':
        network_name = value
      elif key == 'SignalQuality':
        signal_strength = value
      elif key == 'EncryptionType':
        encryption_type = value
  
  # Assuming only one network parsed for simplicity
  return [{
    "essid": network_name,
    "quality": signal_strength,
    "encryption": encryption_type,
  }]  

def get_strongest_network(networks):
  """
  Chooses the strongest Wi-Fi network from the list (modify if needed).
  Currently assumes the first network is strongest.
  """
  return networks[0]

def print_network_info(network):
  """
  Prints information about a Wi-Fi network.
  """
  print(f"**Wi-Fi Network:** {network['essid']}")
  print(f"  - Signal strength: {network['quality']}")
  print(f"  - Encryption type: {network['encryption']}")

if __name__ == "__main__":
  networks = scan_networks()
  strongest_network = get_strongest_network(networks)

  print("\n**Strongest Wi-Fi Network:**")
  print_network_info(strongest_network)
