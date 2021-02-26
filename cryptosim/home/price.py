from pycoingecko import CoinGeckoAPI

def get_btc():
    cg = CoinGeckoAPI()
    api = cg.get_price(ids='bitcoin', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    args = {
        'price': api['bitcoin']['cad'],
        'change24': api['bitcoin']['cad_24h_change']
    }
    return args