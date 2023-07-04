from database.connect_DB import get_connection
from calculate.count_gap import count

import time,sys

def get_streak(map_time):
    db = get_connection()
    collection = db.page_2
    map_time_value = {"1m": 1, "2m": 2, "3m": 3,
                    "4m": 4, "5m": 5, "10m": 10, "15m": 15, "20m": 20,"30m":30,"1h":60,"2h":120,"4h":240,"6h":360,"12h":720,"24h":1440}
    
    end_time = time.time()
    # 5 mins = 300 seconds
    start_time = end_time - (60*map_time_value[map_time])

    # query command between time
    query = {
        "_id": {
            "$gt": start_time,
            "$lt": end_time
        }
    }
    results = list(collection.find(query).sort("_id", 1))


    collection_coin = get_connection().coin
    coins = collection_coin.find()

    coin_data = {}
    final_result = []
    for coin in coins:
        list_coin = []
        for result in results:
            try:
                list_coin.append(result['data'][coin['name']])
            except KeyError:
                continue
        coin_data[coin['name']] = list_coin
        final_result.append(count(coin_data,coin['name']))
    sorted_data_positive = sorted(final_result, key=lambda x: x[list(x.keys())[0]]['streak_positive'], reverse=True)
    sorted_data_negative = sorted(final_result, key=lambda x: x[list(x.keys())[0]]['streak_negative'], reverse=True)
    print("-------------------------------------POSITVE--------------------------------------------------")
    for i in range(0,21):
        print(sorted_data_positive[i])
    print("\n")
    print("-------------------------------------NEGATIVE--------------------------------------------------")
    for i in range(0,21):
        print(sorted_data_negative[i])
    print("\n\n\n\n\n")


while(True):
    get_streak(sys.argv[1])
    time.sleep(10)

