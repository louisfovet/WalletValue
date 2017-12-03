import requests
import json

# === READS PORTFOLIO FILE ===
with open('portfolio.json') as portfolio:
    jPortfolio = json.load(portfolio)

rBTCEUR = requests.get("https://api.cryptowat.ch/markets/kraken/btceur/price")
rBCHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/bcheur/price")
rETHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/etheur/price")
rDASHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/dasheur/price")
rEOSETH = requests.get("https://api.cryptowat.ch/markets/kraken/eoseth/price")

# === PRICE PER CURRENCY ===
pBTC = rBTCEUR.json()["result"]["price"]
pBCH = rBCHEUR.json()["result"]["price"]
pETH = rETHEUR.json()["result"]["price"]
pDASH = rDASHEUR.json()["result"]["price"]
pEOS = rEOSETH.json()["result"]["price"] * pETH

# === VALUE OF WALLET PER CURRENCY ===
vBTC = pBTC * jPortfolio["detail"]["BTC"]["amount"]
vBCH = pBCH * jPortfolio["detail"]["BCH"]["amount"]
vETH = pETH * jPortfolio["detail"]["ETH"]["amount"]
vDASH = pDASH * jPortfolio["detail"]["DASH"]["amount"]
vEOS = pEOS * jPortfolio["detail"]["EOS"]["amount"]


# === VALUE OF EACH CURRENCY ===
print("BTCEUR: " + str(pBTC) + "€")
print("BCHEUR: " + str(pBCH) + "€")
print("ETHEUR: " + str(pETH) + "€")
print("DASHEUR: " + str(pDASH) + "€")
print("EOSEUR: " + str(pEOS) + "€")

print("")
print("Portfolio:")

print("BTC: " + str(vBTC) + "€")
print("BCH: " + str(vBCH) + "€")
print("ETH: " + str(vETH) + "€")
print("DASH: " + str(vDASH) + "€")
print("EOS: " + str(vEOS) + "€")

print("")
print("TOTAL: " + str(vBTC + vBCH + vETH + vDASH + vEOS) + "€")