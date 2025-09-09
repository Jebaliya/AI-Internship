# backend/controllers/user_controller.py
from db import users_coll
from models.user import make_user

def find_user_by_email(email):
    return users_coll.find_one({"email": email})

def save_user(user):
    users_coll.insert_one(user)