from api.call_api import get_data
from api.convert_api import convert_api
from save_data.db_save_all import save_all_data
import time,json


while(True):
    response,request_time = get_data()
    print(response)
    try:
        data, coin_name = convert_api(response)
        save_all_data(data,coin_name,request_time)
    except json.decoder.JSONDecodeError as err:
        continue
    print(request_time)
    print("Waiting for 15s.....")
    time.sleep(15)