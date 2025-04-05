import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

def set_tor_proxy():
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return proxies

def crawl_onion_site(url):
    try:
        proxies = set_tor_proxy()
        response = requests.get(url, proxies=proxies, timeout=20)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print("Crawler Error:", e)
    return None
