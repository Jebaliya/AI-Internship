# backend/controllers/application_controller.py
from db import db

def save_application(application):
    applications_coll = db["applications"]
    applications_coll.insert_one(application)