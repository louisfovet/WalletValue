import requests

rBTCEUR = requests.get("https://api.cryptowat.ch/markets/kraken/btceur/price")
rBCHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/bcheur/price")
rETHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/etheur/price")
rDASHEUR = requests.get("https://api.cryptowat.ch/markets/kraken/dasheur/price")
rEOSETH = requests.get("https://api.cryptowat.ch/markets/kraken/eoseth/price")

pBTC = rBTCEUR.json()["result"]["price"]
pBCH = rBCHEUR.json()["result"]["price"]
pETH = rETHEUR.json()["result"]["price"]
pDASH = rDASHEUR.json()["result"]["price"]
pEOS = rEOSETH.json()["result"]["price"] * pETH

print("BTCEUR: " + str(pBTC) + "€")
print("BCHEUR: " + str(pBCH) + "€")
print("ETHEUR: " + str(pETH) + "€")
print("DASHEUR: " + str(pDASH) + "€")
print("EOSEUR: " + str(pEOS) + "€")





