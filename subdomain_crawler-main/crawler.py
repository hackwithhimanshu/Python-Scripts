#!/usr/bin/env python


import requests

def request(url):
    try:
        return requests.get("http://" + url, timeout=3)
    except requests.exceptions.ConnectionError:
        pass

target_url = "google.com" #Enter your targer link

with open("subdomains-wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response and response.status_code == 200:
            print("[+] Discovered subdomain --> " + test_url)