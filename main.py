from api.call_api import get_data
from api.convert_api import convert_api
from save_data.db_save_all import save_all_data
import time,json


while(True):
    for i in range(1,11):
        response,request_time = get_data(i)
        print(response)
        try:
            data, coin_name = convert_api(response)
        except json.decoder.JSONDecodeError as err:
            continue
        print(request_time)
    time.sleep(5)