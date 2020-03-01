import time, json, requests

# get tickets from various exchanges
def btstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()['last'] # experiment replace last with other values

def btStamp():
    bitStampHI= requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampHI.json()['high']

def bt_stamp():
    bitStampETH = requests.get('https://www.bitstamp.net/api/v2/ticker/ethbtc/')
    return bitStampETH.json()['last']

def bitfinex():
    bitFinexTick = requests.get('https://api.bitfinex.com/v1/ticker/btcusd')
    return bitFinexTick.json()['last_price']

def bit_finex():
    bitFinexETH = requests.get('https://api.bitfinex.com/v1/ticker/ethbtc')
    return bitFinexETH.json()['last_price']

def coinbase():
    coinBaseTick = requests.get('https://coinbase.com/api/v2/prices/BTC-USD/buy')
    return coinBaseTick.json()['data']['amount']

def coin_base():
    coinBaseETH = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy')
    return coinBaseETH.json()['data']['amount']

def kraken():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker', data=json.dumps({"pair":"XXBTZUSD"}),
                              headers={'content-type':'application/json'})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]

# get last btcusd bid and ask orders from bitstamp orderbook
#bid
def btstampOrderBookLastBidPrice():
    bitStampOrderBookLastBidPrice = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampOrderBookLastBidPrice.json()['bids'][0][0]

def btstampOrderBookLastBidQuantity():
    bitstampOrderBookLastBidQuantity = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitstampOrderBookLastBidQuantity.json()['bids'][0][1]

#ask
def btstampOrderBookLastAskPrice():
    bitStampOrderBookLastAskPrice = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampOrderBookLastAskPrice.json()['bids'][1][0]

def btstampOrderBookLastAskQuantity():
    bitstampOrderBookLastAskQuantity = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitstampOrderBookLastAskQuantity.json()['bids'][1][1]

while True:
    btstampUSDLive = float(btstamp())
    btstampUSD_Hi_Live = float(btStamp())
    coinbUSDLive = float(coinbase())
    krakenUSDLive = float(kraken())
    bitfinexUSDLive = float(bitfinex())
    btstampETHLive = float(bt_stamp())
    bitfinexETHLive = float(bit_finex())
    coinbETHLive = float(coin_base())

    print (" --- ticker --- ")
    print ("Bitstamp Price in USD = ", btstampUSDLive)
    print ("Coinbase Price in USD = ", coinbUSDLive)
    print ("Kraken Price in USD = ", krakenUSDLive)
    print ("Bitfinex Price in USD = ", bitfinexUSDLive)
    print (" -- ")
    print ("Bitstamp Highest Price of the Day in USD = ", btstampUSD_Hi_Live)
    print (" -- ")
    print ("Bitstamp Price in ETH = ", (1 / btstampETHLive))
    print ("Bitfinex Price in ETH = ", (1 / bitfinexETHLive))
    print ("Coinbase Price in ETH = ", (btstampUSDLive / coinbETHLive))
    print (" ")

    btstampOrderBookLastBidP = float(btstampOrderBookLastBidPrice())
    btstampOrderBookLastBidQ = float(btstampOrderBookLastBidQuantity())
    btstampOrderBookLastAskP = float(btstampOrderBookLastAskPrice())
    btstampOrderBookLastAskQ = float(btstampOrderBookLastAskQuantity())

    print (" --- bitstamp BTCUSD orders --- ")
    print ("last bid: ")
    print ("        price = ", btstampOrderBookLastBidP)
    print ("        quantity = ", btstampOrderBookLastBidQ)
    print ("last ask: ")
    print ("        price = ", btstampOrderBookLastAskP)
    print ("        quantity = ", btstampOrderBookLastAskQ)
    print (" ")
    print (" ")
    print (" ")
    time.sleep(3) # 120 equals two minutes
