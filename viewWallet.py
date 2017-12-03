import json

# === READS PORTFOLIO FILE ===
with open('portfolio.json') as portfolio:
    jPortfolio = json.load(portfolio)

# === LAST UPDATE ===
lastUpdate = jPortfolio["lastupdate"]

# === PRICE PER CURRENCY ===
pBTC = jPortfolio["detail"]["BTC"]["price"]
pBCH = jPortfolio["detail"]["BCH"]["price"]
pETH = jPortfolio["detail"]["ETH"]["price"]
pDASH = jPortfolio["detail"]["DASH"]["price"]
pEOS = jPortfolio["detail"]["EOS"]["price"]

# === AMOUNT OF CURRENCY ===
aBTC = jPortfolio["detail"]["BTC"]["amount"]
aBCH = jPortfolio["detail"]["BCH"]["amount"]
aETH = jPortfolio["detail"]["ETH"]["amount"]
aDASH = jPortfolio["detail"]["DASH"]["amount"]
aEOS = jPortfolio["detail"]["EOS"]["amount"]

# === VALUE PER CURRENCY ===
vBTC = jPortfolio["detail"]["BTC"]["value"]
vBCH = jPortfolio["detail"]["BCH"]["value"]
vETH = jPortfolio["detail"]["ETH"]["value"]
vDASH = jPortfolio["detail"]["DASH"]["value"]
vEOS = jPortfolio["detail"]["EOS"]["value"]

# === VALUE OF PORTFOLIO ===
vPortfolio = jPortfolio["value"]

# === DISPLAY ===
print()
print("Last update: " + lastUpdate)
print()
print("BTC  | price: " + str(pBTC) + "€ | amount: " + str(aBTC) + " | value: " + str(vBTC) + "€")
print("BCH  | price: " + str(pBCH) + "€ | amount: " + str(aBCH) + " | value: " + str(vBCH) + "€")
print("ETH  | price: " + str(pETH) + "€ | amount: " + str(aETH) + " | value: " + str(vETH) + "€")
print("DASH | price: " + str(pDASH) + "€ | amount: " + str(aDASH) + " | value: " + str(vDASH) + "€")
print("EOS  | price: " + str(pEOS) + "€ | amount: " + str(aEOS) + " | value: " + str(vEOS) + "€")
print()
print("Portfolio: " + str(vPortfolio) + "€")


