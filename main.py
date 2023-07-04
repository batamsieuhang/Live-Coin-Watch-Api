from api.call_api import get_data
from api.convert_api import convert_api
from database.connect_DB import get_connection
from save_data.db_list_coin import save_coin
from save_data.db_coin_data import save_data_coin
import time


while(True):
    db = get_connection()
    response,request_time = get_data(1)
    data, coin_name = convert_api(response)
    save_coin(coin_name)
    save_data_coin(data,request_time)
    print(request_time)
    time.sleep(2)
    