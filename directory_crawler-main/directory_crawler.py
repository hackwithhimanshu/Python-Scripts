import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "192.168.29.218/mutillidae/"

with open("files-and-dirs-wordlist.txt", "r") as dirs_file:
    for line in dirs_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)