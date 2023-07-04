from api.call_api import get_data
from api.convert_api import convert_api
from database.connect_DB import get_connection
import time


while(True):
    db = get_connection()
    response,request_time = get_data(1)
    data, coin_name = convert_api(response)
    collection = db.page_2
    collection.insert_one({"_id":request_time,"data":data})
    print(request_time)
    time.sleep(2)
    