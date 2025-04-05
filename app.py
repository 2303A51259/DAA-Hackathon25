from flask import Flask, request, render_template
from tor_crawler import crawl_onion_site
from pii_extractor import extract_pii
from bitcoin_tracer import check_wallet
from osint_stylometry import run_osint

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    btc_data = []
    risk = None

    if request.method == "POST":
        url = request.form.get("url")
        html = crawl_onion_site(url)
        if html:
            data = extract_pii(html)
            if data["btc_wallets"]:
                btc_data = [check_wallet(wallet) for wallet in data["btc_wallets"]]
            if data["ips"]:
                risk = run_osint(data["ips"][0])
    return render_template("index.html", data=data, btc_data=btc_data, risk=risk)

if __name__ == "__main__":
    app.run(debug=True)
