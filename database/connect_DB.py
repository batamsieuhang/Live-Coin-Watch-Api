from pymongo import MongoClient
from decouple import config
import urllib.parse
def get_connection():
    username = urllib.parse.quote_plus(config('MONGO_USER'))
    password = urllib.parse.quote_plus(config('MONGO_PASS'))
    CONNECTION_STRING = "mongodb://{username_mongo}:{password_mongo}@localhost:27017/test_mongo".format(username_mongo=username, password_mongo=password)
    client = MongoClient(CONNECTION_STRING)
    # auto return db
    return client['test_mongo']


# # sample connection
# db = get_connection()

# # users is a collection in db
# check = db.users

# print(check.find_one({"name":"Tu"}))sd

