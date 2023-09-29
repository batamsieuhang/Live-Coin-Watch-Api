from database.connect_DB import get_connection



def get_per_vol_price(time_request):
    
    db = get_connection()
    collection = db.per_coin
    data = []

    for i in range(0,2):
        for coin in collection.find({"_id":time_request[i]}):
            data.append(coin['data'])


    collection_coin = db.coin

    coins = collection_coin.find()

    dict_price_coin = {}

    for coin in coins:    
        try:
            dict_price_coin[coin["name"]] = {}
            after_vol_price=float(data[1][coin["name"]]["volume"])/float(data[1][coin["name"]]["price"])
            pre_vol_price = float(data[0][coin["name"]]["volume"])/float(data[0][coin["name"]]["price"])
            per_cal = (after_vol_price/pre_vol_price-1)*100
            if(per_cal > 0):
                dict_price_coin[coin["name"]]["positive"] = per_cal
                dict_price_coin[coin["name"]]["negative"] = 0
            elif(per_cal < 0):
                dict_price_coin[coin["name"]]["positive"] = 0
                dict_price_coin[coin["name"]]["negative"] = per_cal
            else:
                dict_price_coin[coin["name"]]["positive"] = per_cal
                dict_price_coin[coin["name"]]["negative"] = per_cal
        except KeyError:
            continue
    sorted_data_negative = sorted(dict_price_coin.items(), key=lambda x: x[1].get('negative', float('inf')))

    sorted_data_positive = sorted(dict_price_coin.items(), key=lambda x: x[1].get('positive', 0), reverse=True)
    return sorted_data_negative, sorted_data_positive


