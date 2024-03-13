import ccxt

ex = ccxt.binance()
r = ex.fetch_ticker('BTC/USDT')
print(r)