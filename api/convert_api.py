import json

def convert_api(response):
    data_coin = response.json()['data']
    coins = {}
    coin_name = []
    for data in data_coin:
        if data['q'] == "USDT":
            coins[data['s']] = {"price":data['c'],"depth":0,"volume":data['qv']}
            coin_name.append(data['s'])
    return coins, coin_name