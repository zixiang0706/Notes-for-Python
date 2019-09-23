import requests
import pandas as pd

pd.set_option('expand_frame_repr', False)

BASE_URL = 'https://api.binance.com'

kline = '/api/v1/klines'
#
kline_url = BASE_URL + kline + '?' + 'symbol=BTCUSDT&interval=1h&limit=1000'
print(kline_url)
resp = requests.get(kline_url)
# print(resp.json())
df = pd.DataFrame(resp.json())
print(df)

