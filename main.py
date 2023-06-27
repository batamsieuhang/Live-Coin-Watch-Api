import requests
import json

url = "https://http-api.livecoinwatch.com/markets"

payload = json.dumps({
    "exchange": "binance",
    "sort": "depth",
    "order": "descending",
    "offset": 0,
    "limit": 30,
    "search": "usdt"
})
headers = {
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
    'x-api-key': '58c9be28-962f-4177-b6a0-dec1f6968f7d'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
