import re

def extract_pii(html):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
    ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", html)
    btc_wallets = re.findall(r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b", html)
    return {
        "emails": list(set(emails)),
        "ips": list(set(ips)),
        "btc_wallets": list(set(btc_wallets))
    }
