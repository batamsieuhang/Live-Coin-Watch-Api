import json

def convert_api(response):
    data_coin = json.loads(response.text)['data']
    coins = {}
    coin_name = []
    for data in data_coin:
        coins[data['base']] = {"price":data['price'],"depth":data['depth'],"volume":data['volume']}
        coin_name.append(data['base'])
    return coins, coin_name