from connect_DB import get_connection
from calculate.count_gap import count

import time

db = get_connection()
collection = db.page_2

n = time.time()
m = n - (60*5)
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
    list_coin.append(result['data']['AR'])
querry_coin['AR'] = list_coin

print(len(querry_coin["AR"]))



print(count(querry_coin,"AR"))