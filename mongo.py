from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

DB_NAME = "userdata"
USER_COLLECTION_NAME = "userdata"
PRODUCT_COLLECTION_NAME = "products"

client = MongoClient(MONGO_URI)

db = client[DB_NAME]
collection = db[USER_COLLECTION_NAME]
product_collection = db[PRODUCT_COLLECTION_NAME]


def find_userdata(name: str) -> dict:
    doc = collection.find_one({"name": name.lower()})
    return doc if doc else {"name": "User not found"}


def find_previously_bought(name: str):
    doc = collection.find_one({"name": name.lower()})
    prev = doc['previously_bought']

    return prev if prev else "No previously bought items found."


def find_cart_items(name: str):
    doc = collection.find_one({"name": name.lower()})
    cart_items = doc['cart_items']

    return cart_items if cart_items else "Cart is empty."


def find_budget(name: str):
    doc = collection.find_one({"name": name.lower()})
    budget = doc['budget']

    return budget if budget else "No budget set."


def find_products(product_name: str) -> str:
    query = {"name": {"$regex": re.escape(product_name), "$options": "i"}}
    # result = product_collection.find(query)
    # products = []
    # for doc in result:
    #     products.append(doc)

    def serialize_doc(doc):
        doc["_id"] = str(doc["_id"])  # convert ObjectId to string
        return doc

    products = [serialize_doc(doc) for doc in product_collection.find(query)]

    return products
