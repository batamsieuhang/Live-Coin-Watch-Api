from connect_DB import get_connection
from convert_api import convert_api
from call_api import get_data
from calculate_per import percentage
from count_gap import count

import time

db = get_connection()
collection = db.page_2

page_2 = collection.find_one({"_id":1688355584.587282})
n = 1688432797.0976057
m = n -60
query = {
    "_id": {
        "$gt": m,
        "$lt": n
    }
}
test_result = collection.find(query).sort("_id", 1)

querry_coin = {}
list_coin = []
for result in test_result:
    list_coin.append(result['data']['____PEPE'])
querry_coin['____PEPE'] = list_coin

print(len(querry_coin["____PEPE"]))



print(count(querry_coin,"____PEPE"))