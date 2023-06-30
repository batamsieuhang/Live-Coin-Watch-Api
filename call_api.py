import requests
import time


def get_data(page):
    offset = {1:"0",2:"30",3:"60",4:"90",5:"120",6:"150",7:"180",8:"210",9:"240",10:"270"}
    url = "https://http-api.livecoinwatch.com/markets"
    payload = {
        "exchange": "binance",
        "sort": "depth",
        "order": "descending",
        "offset": offset[page],
        "limit": "30",
        "search": "usdt"
    }

    headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        'x-api-key': '58c9be28-962f-4177-b6a0-dec1f6968f7d'
    }

    request_time = time.time()
    response = requests.get(url, headers=headers, params=payload)
    return response,request_time

    




