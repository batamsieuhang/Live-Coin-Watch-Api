from api.call_api import get_data
from api.convert_api import convert_api
from database.connect_DB import get_connection
from calculate.get_per_price_vol import get_per_vol_price
import json,time,sys



def count_per(per_limit_positive,per_limit_negative,time_value):
    map_time_value = {"1s":1,"5s":5,"10s":10,"20s":20,"30s":30,"1m": 60, "2m": 120, "3m": 180,
                    "4m": 240, "5m": 300, "10m": 600, "15m": 900, "20m": 1200,"30m":1800,"1h":3600,"2h":7200,"3h":10800,"4h":14400,"6h":21600,"12h":43200,"24h":86400}
    db = get_connection()
    collection = db.per_coin
    time_request_list = []
    index = 0
    for i in range(0,3):
        data = {}
        request_time = time.time()
        time_request_list.append(request_time)
        if (index == 0):
                print("Waiting for {time_show} ...".format(time_show=time_value)) 
        response= get_data()[0]
        try:
            update_coin, coin_name = convert_api(response)
            data.update(update_coin)
        except json.decoder.JSONDecodeError as err:
            continue
        collection.insert_one({"_id":request_time,"data":data})
        if (index==1):
            print("---------------------------------LAP1-----------NEGATIVE-cal_gap_vol_price----------------------------------")
            negative, positive = get_per_vol_price(time_request_list[0:2])
            for coin in negative:
                try:
                    if abs(coin[1]["negative"]) >  per_limit_negative:
                        print(coin)
                except KeyError:
                    continue
            print("---------------------------------LAP1--------------POSITIVE-cal_gap_vol_price--------------------------------")
            for coin in positive:
                try:
                    if coin[1]["positive"] >  per_limit_positive:
                        print(coin)
                except KeyError:
                    continue
            print("---------------------------------LAP1--------------END---------------------------------")
        if (index==2):
            print("---------------------------------LAP2-----------NEGATIVE-cal_gap_vol_price----------------------------------")
            negative, positive = get_per_vol_price(time_request_list[1:3])
            for coin in negative:
                try:
                    if abs(coin[1]["negative"]) >  per_limit_negative:
                        print(coin)
                except KeyError:
                    continue
            print("---------------------------------LAP2--------------POSITIVE-cal_gap_vol_price--------------------------------")
            for coin in positive:
                try:
                    if abs(coin[1]["positive"]) >  per_limit_positive:
                        print(coin)
                except KeyError:
                    continue
            print("---------------------------------LAP2--------------END---------------------------------")
        index+=1
        if (index ==1 or index ==2):
            print("Waiting for {time_show} ...".format(time_show=time_value))
            time.sleep(map_time_value[time_value])
        elif(index ==3):
            print("Waiting for 30s ...")
            time.sleep(30)


while(True):
    count_per(float(sys.argv[1]),float(sys.argv[2]),sys.argv[3])

        
        


