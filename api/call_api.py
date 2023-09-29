import requests
import time


def get_data():
    url = "https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-products"
    payload = {
        "includeEtf":"true"
        }

    headers = {
            'content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
                    }

    request_time = time.time()
    response = requests.get(url, headers=headers, params=payload)
    return response,request_time

    




