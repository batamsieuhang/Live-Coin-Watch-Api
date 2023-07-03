from connect_DB import get_connection
from convert_api import convert_api
from call_api import get_data
import time

db = get_connection()
collection = db.page_2

page_2 = collection.find_one({"_id":1688355584.587282})
# print(page_2['data'])
n = time.time()
m = n -60
query = {
    "_id": {
        "$gt": m,
        "$lt": n
    }
}
test_result = collection.find(query).sort("_id", 1)

querry_coin = []
for result in test_result:
    print(result['data']['MTL'])
    print("\n")


response,request_time = get_data(2)
data, coin_name = convert_api(response)



