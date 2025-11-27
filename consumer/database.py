from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017/bookdb")

client = MongoClient(MONGO_URL)
db = client.get_default_database()
books_collection = db["books"]