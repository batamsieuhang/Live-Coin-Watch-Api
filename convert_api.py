import json

def convert_api(response):
    data_coin = json.loads(response.text)['data']
    finally_data = {}
    for data in data_coin:
        finally_data[data['base']] = {"price":data['price'],"depth":data['depth'],"volume":data['volume']}
    return finally_data

    