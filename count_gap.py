from calculate_per import percentage

def count(price_coin,coin_name):
    result = {}
    result[coin_name] = {}
    result[coin_name]["increase"] =0
    result[coin_name]["decrease"] =0

    for i in range(len(price_coin[coin_name])-2):
        if (percentage(price_coin[coin_name][i]['price'],price_coin[coin_name][i+1]['price'])>0):
            result[coin_name]["increase"] +=1
        elif (percentage(price_coin[coin_name][i]['price'],price_coin[coin_name][i+1]['price'])<0):
            result[coin_name]["decrease"] +=1
    return result



