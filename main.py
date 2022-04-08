import time
import requests



while(True):
    r = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC')
    r.status_code
    print(r.json()['data']['rates']['EUR'])
    time.sleep(20)
