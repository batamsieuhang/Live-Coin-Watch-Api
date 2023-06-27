import requests
import json

url = "https://api.livecoinwatch.com/coins/list"

payload = json.dumps({
    "currency": "USD",
    "sort": "rank",
    "order": "ascending",
    "offset": 0,
    "limit": 100,
    "meta": False
})
headers = {
    'content-type': 'application/json',
    'x-api-key': '58c9be28-962f-4177-b6a0-dec1f6968f7d'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
