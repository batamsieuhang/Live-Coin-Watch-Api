from connect_DB import get_connection
from call_api import get_data
from api.convert_api import convert_api


def get_coin():
    db = get_connection()
    collection = db.coin
    response = get_data(1)[0]
    coin_list = convert_api(response)[1]
    for coin in coin_list:
        print(coin)
        collection.replace_one({"name":coin},{"name":coin},upsert=True)

