import requests

def check_wallet(wallet):
    url = f"https://blockchain.info/rawaddr/{wallet}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            total_received = data['total_received'] / 1e8
            return {"wallet": wallet, "received_btc": total_received}
    except Exception as e:
        print(f"Error tracing wallet {wallet}:", e)
    return {"wallet": wallet, "received_btc": 0}
