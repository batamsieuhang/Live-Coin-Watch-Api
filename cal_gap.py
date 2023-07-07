from api.call_api import get_data
from api.convert_api import convert_api
from database.connect_DB import get_connection
from calculate.get_per import get_per
import json,time,sys



def count_per(per_limit_positive,per_limit_negative):
    db = get_connection()
    collection = db.per_coin
    time_request_list = []
    index = 0
    for i in range(0,3):
        print(str(i+1)+"...")
        time.sleep(1)
    for i in range(0,3):
        data = {}
        request_time = time.time()
        time_request_list.append(request_time)
        if (index == 0):
                print("Wating for 2 min...") 
        for i in range(1,11):
            response= get_data(i)[0]
            try:
                update_coin, coin_name = convert_api(response)
                data.update(update_coin)
            except json.decoder.JSONDecodeError as err:
                continue
        collection.insert_one({"_id":request_time,"data":data})
        if (index==1):
            print("---------------------------------LAP1-----------NEGATIVE-----------------------------------")
            negative, positive = get_per(time_request_list[0:2])
            for coin in negative:
                try:
                    if abs(coin[1]["negative"]) >  per_limit_negative:
                        print(coin)
                except KeyError:
                    continue
            print("---------------------------------LAP1--------------POSITIVE---------------------------------")
            for coin in positive:
                try:
                    if coin[1]["positive"] >  per_limit_positive:
                        print(coin)
                except KeyError:
                    continue
            print("---------------------------------LAP1--------------END---------------------------------")
        if (index==2):
            print("---------------------------------LAP2-----------NEGATIVE-----------------------------------")
            negative, positive = get_per(time_request_list[1:3])
            for coin in negative:
                try:
                    if abs(coin[1]["negative"]) >  per_limit_negative:
                        print(coin)
                except KeyError:
                    continue
            print("---------------------------------LAP2--------------POSITIVE---------------------------------")
            for coin in positive:
                try:
                    if abs(coin[1]["positive"]) >  per_limit_positive:
                        print(coin)
                except KeyError:
                    continue
            print("---------------------------------LAP2--------------END---------------------------------")
        index+=1
        print("Waiting for 1 minute...")
        time.sleep(40) 

     
while(True):
    count_per(float(sys.argv[1]),float(sys.argv[2]))

        
        


