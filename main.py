from call_api import get_data
from connect_DB import get_connection
from convert_api import convert_api
import time,json


while(True):
    response,request_time = get_data(2)

    db = get_connection()

    collection = db.page_2
    collection.insert_one({"_id":request_time,"data":convert_api(response)})
    print(request_time)
    time.sleep(2)