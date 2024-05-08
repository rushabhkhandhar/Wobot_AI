# database.py

from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb+srv://user1:abcd@user1.jmfnfbr.mongodb.net/todolist")
db = client["todolist"]
todos_collection = db["task"]
