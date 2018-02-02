import os
import time
import requests, json
from time import sleep
from datetime import datetime

def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        price = float(json.loads(r.text)['last'])
        return price
    except requests.ConnectionError:
        print("Error querying Bitstamp API", flush=True)

price = getBitcoinPrice()
priceStr = "$" + str(price) + " /BTC"
dt = datetime.now().strftime("%Y-%m-%d %H:%M:S")
print("Bitstamp price at %s: %s" % (dt, priceStr))

# print("HELLO")

# time.sleep(10)

# print("DONE")
