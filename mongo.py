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
    return doc if doc else "User not found"


def find_previously_bought(name: str):
    doc = collection.find_one({"name": name})
    prev = doc['previously_bought']

    return prev if prev else "No previously bought items found."


def find_cart_items(name: str):
    doc = collection.find_one({"name": name})
    cart_items = doc['cart_items']

    return cart_items if cart_items else "Cart is empty."
