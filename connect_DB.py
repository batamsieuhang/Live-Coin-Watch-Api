from pymongo import MongoClient
from decouple import config
def get_connection():
    CONNECTION_STRING = "mongodb://{username}:{password}@localhost:27017/test_mongo".format(username=config('MONGO_USER'), password=config('MONGO_PASS'))
    client = MongoClient(CONNECTION_STRING)
    # auto return db
    return client['test_mongo']


# sample connection
db = get_connection()

# users is a collection in db
check = db.users

print(check.find_one({"name":"Tu"}))

