from api.call_api import get_data
from api.convert_api import convert_api
from database.connect_DB import get_connection
import json,time



db = get_connection()
collection = db.per_coin
time_request_list = []
for i in range(0,3):
    
    data = {}
    request_time = time.time()
    time_request_list.append(request_time)
    for i in range(1,11):
        response= get_data(i)[0]
        print(response)
        print(request_time)
        try:
            update_coin, coin_name = convert_api(response)
            data.update(update_coin)
        except json.decoder.JSONDecodeError as err:
            continue
    collection.insert_one({"_id":request_time,"data":data})
    time.sleep(60)
        
print(time_request_list)




