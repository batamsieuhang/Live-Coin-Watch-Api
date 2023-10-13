from database.connect_DB import get_connection
from api.call_api import get_data
from api.convert_api import convert_api
from calculate.get_per_vol_v import get_per_vol_price
import time,sys,json

def cal_gap(per_limit_positive,per_limit_negative,time_value):
    map_time_value = {"1s":1,"5s":5,"10s":10,"20s":20,"30s":30,"1m": 60, "2m": 120, "3m": 180,
                    "4m": 240, "5m": 300, "10m": 600, "15m": 900, "20m": 1200,"30m":1800,"1h":3600,"2h":7200,"3h":10800,"4h":14400,"6h":21600,"12h":43200,"24h":86400}
    db = get_connection()
    collection = db.per_coin
    time_request_list = []
    time_pre = time.time()
    time_after = time.time()
    index = 0
    count_coin = {}
    db_coin = get_connection()
    coins = db_coin.coin.find()
    for coin in coins:
        count_coin[coin["name"]] = {}
        count_coin[coin["name"]]["increase"] = 0
        count_coin[coin["name"]]["decrease"] = 0
        count_coin[coin["name"]]["streak_decrease"] = 0
        count_coin[coin["name"]]["streak_increase"] = 0

    while(True):
        data = {}
        request_time = time.time()
        
        time_request_list.append(request_time)
        response= get_data()[0]
        try:
            update_coin, coin_name = convert_api(response)
            data.update(update_coin)
        except json.decoder.JSONDecodeError as err:
            continue
        collection.insert_one({"_id":request_time,"data":data})
        if index==0:
            index+=1
            time_pre=request_time
            continue
        else:
            time_after=request_time
            negative, positive,count_coin = get_per_vol_price([time_pre,time_after],count_coin)
            print("--------------------------------------------NEGATIVE-cal_gap_vol_price----------------------------------")
            
            for coin in negative:
                try:
                    if abs(coin[1]["negative"]) >  per_limit_negative:
                        print(coin," so lan giam: ",count_coin[coin[0]]["decrease"]," chuoi giam: ",count_coin[coin[0]]["streak_decrease"])
                except KeyError:
                    continue
            print("-----------------------------------------------POSITIVE-cal_gap_vol_price--------------------------------")
            for coin in positive:
                try:
                    if coin[1]["positive"] >  per_limit_positive:
                        print(coin," so lan tang: ",count_coin[coin[0]]["increase"]," chuoi tang: ", count_coin[coin[0]]["streak_increase"])
                except KeyError:
                    continue
        print("Waiting for {time_show} ...".format(time_show=time_value))
        time_pre=time_after

        time.sleep(map_time_value[time_value])

cal_gap(float(sys.argv[1]),float(sys.argv[2]),sys.argv[3])