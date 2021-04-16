from pycoingecko import CoinGeckoAPI

def get_btc():
    cg = CoinGeckoAPI()
    eth = cg.get_price(ids='ethereum', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    btc = cg.get_price(ids='bitcoin', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    lite = cg.get_price(ids='litecoin', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    usdt = cg.get_price(ids='tether', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    dash = cg.get_price(ids='dashcoin', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    xrp = cg.get_price(ids='ripple', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    tezos = cg.get_price(ids='tezos', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    doge = cg.get_price(ids='dogecoin', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    args = {
        'price': btc['bitcoin']['cad'],
        'change24': btc['bitcoin']['cad_24h_change'],
        'marketCap': btc['bitcoin'],
        'ethP': eth['ethereum']['cad'],
        'eth24': eth['ethereum']['cad_24h_change'],
        'liteP': lite['litecoin']['cad'],
        'lite24': lite['litecoin']['cad_24h_change'],
        'usdtP': usdt['tether']['cad'],
        'usdt24': usdt['tether']['cad_24h_change'],
        'dashP': dash['dashcoin']['cad'],
        'dash24': dash['dashcoin']['cad_24h_change'],
        'xrpP': xrp['ripple']['cad'],
        'xrp24': xrp['ripple']['cad_24h_change'],
        'tezosP': tezos['tezos']['cad'],
        'tezos24': tezos['tezos']['cad_24h_change'],
        'dogeP': doge['dogecoin']['cad'],
        'doge24': doge['dogecoin']['cad_24h_change']
    }
    return args