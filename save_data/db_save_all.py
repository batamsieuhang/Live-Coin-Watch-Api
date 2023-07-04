from save_data.db_list_coin import save_coin
from save_data.db_coin_data import save_data_coin

def save_all_data(data,coin_name,request_time):
    save_coin(coin_name)
    save_data_coin(data,request_time)