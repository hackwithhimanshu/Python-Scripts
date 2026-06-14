import requests 
import re
from urllib.parse import urlparse, urljoin


target_url = "http://192.168.29.218/mutillidae/"
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall(b'(?:href=")(.*?)"', response.content)

def crawler(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = link.decode(errors="ignore")
        link = urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawler(link)

crawler(target_url)