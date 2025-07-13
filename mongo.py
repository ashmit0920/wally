from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

DB_NAME = "userdata"
COLLECTION_NAME = "userdata"

client = MongoClient(MONGO_URI)

db = client[DB_NAME]
collection = db[COLLECTION_NAME]


def find_userdata(name: str):
    doc = collection.find_one({"name": name})
    return doc
