from database.connect_DB import get_connection

def save_data_coin(data,request_time ):
    db = get_connection()
    collection = db.page_2
    collection.insert_one({"_id":request_time,"data":data})
    