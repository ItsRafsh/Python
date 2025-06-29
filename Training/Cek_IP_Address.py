# aku menulis catatan ini di 25-4-2025
# dari grup ka Ozan

import ipaddress

def subnetting(ip_input):
    try:
        network = ipaddress.ip_network(ip_input, strict=False)

        print(f"IP Address       : {ip_input.split('/')[0]}")
        print(f"Subnet Mask      : {network.netmask}")
        print(f"Network Address  : {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Total Hosts      : {network.num_addresses - 2}")  # -2: for network & broadcast
        hosts = list(network.hosts())
        if hosts:
            print(f"IP Range         : {hosts[0]} - {hosts[-1]}")
        else:
            print("IP Range         : No usable host (maybe /31 or /32)")
    
    except ValueError as e:
        print(f"Error: {e}")

ip_cidr = input("Masukkan IP dan subnet (contoh: 192.168.1.0/24): ")
subnetting(ip_cidr)