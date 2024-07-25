from scapy.all import sniff, IP

def handle_sniffed_packet(packet):
  """
  Prints a summary of the captured packet.

  Args:
    packet: The captured packet object.
  """
  # Limit output to avoid overwhelming the user
  if len(packet) > 100:
    return
  try:
    # Access protocol from the IP layer
    print(f"Protocol: {packet.layer(IP).proto}")
  except AttributeError:
    # Handle cases where the packet might not have an IP layer
    print("Non-IP packet detected")
  print(f"Source: {packet[0].src}")
  print(f"Destination: {packet[0].dst}")

def main():
  """
  Captures packets on the default interface.
  """
  sniff(iface="en0", prn=handle_sniffed_packet)  # Replace "en0" with your interface if needed

if __name__ == "__main__":
  main()