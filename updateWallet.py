import requests
import json
import datetime

# === READS PORTFOLIO FILE ===
with open('portfolio.json') as portfolio:
    jPortfolio = json.load(portfolio)

# === REQUESTS CRYPTOWACH API ===
rBTCEUR = requests.get("https://api.cryptowat.ch/markets/kraken/btceur/price")
rBCHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/bcheur/price")
rETHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/etheur/price")
rDASHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/dasheur/price")
rEOSETH = requests.get("https://api.cryptowat.ch/markets/kraken/eoseth/price")

# === PRICE PER CURRENCY ===
jPortfolio["detail"]["BTC"]["price"] = rBTCEUR.json()["result"]["price"]
jPortfolio["detail"]["BCH"]["price"] = rBCHEUR.json()["result"]["price"]
jPortfolio["detail"]["ETH"]["price"] = rETHEUR.json()["result"]["price"]
jPortfolio["detail"]["DASH"]["price"] = rDASHEUR.json()["result"]["price"]
jPortfolio["detail"]["EOS"]["price"] = rEOSETH.json()["result"]["price"] * rETHEUR.json()["result"]["price"]

# === COMPUTES NEW VALUES ===
jPortfolio["detail"]["BTC"]["value"] = jPortfolio["detail"]["BTC"]["amount"] * jPortfolio["detail"]["BTC"]["price"]
jPortfolio["detail"]["BCH"]["value"] = jPortfolio["detail"]["BCH"]["amount"] * jPortfolio["detail"]["BCH"]["price"]
jPortfolio["detail"]["ETH"]["value"] = jPortfolio["detail"]["ETH"]["amount"] * jPortfolio["detail"]["ETH"]["price"]
jPortfolio["detail"]["DASH"]["value"] = jPortfolio["detail"]["DASH"]["amount"] * jPortfolio["detail"]["DASH"]["price"]
jPortfolio["detail"]["EOS"]["value"] = jPortfolio["detail"]["EOS"]["amount"] * jPortfolio["detail"]["EOS"]["price"]

# === COMPUTES PORTFOLIO VALUE ===
jPortfolio["value"] = jPortfolio["detail"]["BTC"]["value"] + jPortfolio["detail"]["BCH"]["value"] \
                      + jPortfolio["detail"]["ETH"]["value"] + jPortfolio["detail"]["DASH"]["value"] \
                      + jPortfolio["detail"]["EOS"]["value"]

# === LAST UPDATED TIME IN FILE ===
jPortfolio["lastupdate"] = str(datetime.datetime.now()).split('.')[0]


# === UPDATE JSON FILE ===
with open('portfolio.json', 'w') as portfolio:
    json.dump(jPortfolio, portfolio)