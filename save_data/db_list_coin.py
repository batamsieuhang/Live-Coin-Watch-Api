from database.connect_DB import get_connection


def save_coin(coin_list):
    db = get_connection()
    collection = db.coin
    for coin in coin_list:
        collection.replace_one({"name":coin},{"name":coin},upsert=True)

