# backend/db.py
import os
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["internship_recommender"]
internships_coll = db["internships"]
profiles_coll = db["profiles"]
recommendations_coll = db["recommendations"]
