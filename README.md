# Trading API Project
Consume trading APIs and get prices and orders from the orderbook from various exchanges like Bitstamp, Bitfinex, Coinbase and Kraken. An API is an “application program interface”, usually provided for external access through RESTful Web Services, JSON-RPC or other communication protocols. It basically provides access to a company’s data. 

This example will use public data functions which Exchanges offer without having to register using their public APIs. 

## Requirements
* Ubuntu 16.04.3
* Python3

## Source Code
[TradingAPI](https://github.com/aenhsaihan/TradingAPI)

## Commands
```bash
$ python3 TradingAPI.py
```

## Exchange APIs
Get info from the [Bitstamp](https://www.bitstamp.net/api/ticker/) ticker. Here we use last and with the response, it will give us the last BTC price but you can experiment with other values, for example, volume will give you Last 24 hours volume.

Using similar logic, let’s get last prices from other exchanges like [Bitfinex](https://api.bitfinex.com/v1/ticker/), [Coinbase](https://coinbase.com/api/v2/prices/BTC-USD/buy) and [Kraken](https://api.kraken.com/0/public/Ticker).

Get some info from the Bitstamp order book. The difference is that in this case, the API returns a JSON dictionary with "bids" and "asks". Each is a list of open orders and each order is represented as a list holding the price and the amount. Implement code that gets price and quantity for last bid and ask orders.

Print the information in the console and update it in every 3 seconds. 

### Module
MI2: Module 4: E2
