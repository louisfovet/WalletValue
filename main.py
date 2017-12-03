import requests

rBTCEUR = requests.get("https://api.cryptowat.ch/markets/kraken/btceur/price")
rBCHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/bcheur/price")
rETHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/etheur/price")
rDASHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/dasheur/price")
rEOSETH = requests.get("https://api.cryptowat.ch/markets/kraken/eoseth/price")

# === PRICE FROM CRYPTOWATCH ===
pBTC = rBTCEUR.json()["result"]["price"]
pBCH = rBCHEUR.json()["result"]["price"]
pETH = rETHEUR.json()["result"]["price"]
pDASH = rDASHEUR.json()["result"]["price"]
pEOS = rEOSETH.json()["result"]["price"] * pETH

# === VALUE OF WALLET PER CURRENCY ===
vBTC = pBTC * 0.29751
vBCH = pBCH * 1.80237
vETH = pETH * 6.45911
vDASH = pDASH * 1.70867
vEOS = pEOS * 80.45374

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




