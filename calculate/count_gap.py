from calculate.calculate_per import percentage

def count(price_coin,coin_name):
    result = {}
    result[coin_name] = {}
    result[coin_name]["increase"] =0
    result[coin_name]["decrease"] =0
    result[coin_name]["streak_positive"] =0
    result[coin_name]["streak_negative"] =0
    streak_positive = 0
    streak_negative =0 

    for i in range(len(price_coin[coin_name])-2):

        if (percentage(price_coin[coin_name][i]['price'],price_coin[coin_name][i+1]['price'])>0):
            streak_negative =0
            streak_positive +=1
            if streak_positive >= result[coin_name]["streak_positive"]:
                result[coin_name]["streak_positive"] = streak_positive
            result[coin_name]["increase"] +=1
            
            
        elif (percentage(price_coin[coin_name][i]['price'],price_coin[coin_name][i+1]['price'])<0):
            streak_positive = 0
            streak_negative +=1
            if streak_negative >= result[coin_name]["streak_negative"]:
                result[coin_name]["streak_negative"] = streak_negative
            result[coin_name]["decrease"] +=1
    
    return result



