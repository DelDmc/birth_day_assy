from datetime import datetime

from decouple import config
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    f"mongodb+srv://{config('MONGO_LOGIN')}:{config('MONGO_PASSWORD')}"
    f"@sandbox.0ca4qre.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1'))

db = client.bday_db



# post = {"author": "Del",
#         "text": "My birth day",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.utcnow()}


if __name__ == '__main__':
    pass
    # posts = db.posts
    # post_id = posts.insert_one(post).inserted_id
    # print(post_id)
    # print(db.list_collection_names())
