# backend/routes/application_routes.py
from flask import Blueprint, request, jsonify
from models.application import make_application
from controllers.application_controller import save_application
from db import db, internships_coll
import datetime
import jwt
import os

application_bp = Blueprint("application", __name__)
JWT_SECRET = os.environ.get("JWT_SECRET", "supersecretkey")

def is_admin_request(request):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return False
    token = auth_header.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        from controllers.user_controller import find_user_by_email
        user = find_user_by_email(payload["email"])
        return user and user.get("is_admin", False)
    except Exception:
        return False

@application_bp.route("/api/apply", methods=["POST"])
def apply():
    data = request.json or {}
    # Extract user_id from request (e.g., from JWT or request data)
    user_id = data.get("user_id")  # Make sure frontend sends user_id, or decode from JWT
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    data["user_id"] = user_id
    data["timestamp"] = datetime.datetime.utcnow()
    application = make_application(data)
    save_application(application)
    return jsonify({"status": "success"})

@application_bp.route("/api/admin/internships", methods=["GET", "POST"])
def admin_internships():
    if not is_admin_request(request):
        return jsonify({"error": "Admin only"}), 403
    if request.method == "GET":
        items = list(internships_coll.find({}))
        for i in items:
            i["id"] = str(i["_id"])
            i.pop("_id", None)
        return jsonify(items)
    elif request.method == "POST":
        data = request.json or {}
        internships_coll.insert_one(data)
        return jsonify({"status": "added"})

@application_bp.route("/api/admin/internships/<iid>", methods=["PUT", "DELETE"])
def admin_update_delete_internship(iid):
    if not is_admin_request(request):
        return jsonify({"error": "Admin only"}), 403
    from bson import ObjectId
    if request.method == "PUT":
        data = request.json or {}
        internships_coll.update_one({"_id": ObjectId(iid)}, {"$set": data})
        return jsonify({"status": "updated"})
    elif request.method == "DELETE":
        internships_coll.delete_one({"_id": ObjectId(iid)})
        return jsonify({"status": "deleted"})

@application_bp.route("/api/admin/applications", methods=["GET"])
def admin_applications():
    if not is_admin_request(request):
        return jsonify({"error": "Admin only"}), 403
    applications_coll = db["applications"]
    items = list(applications_coll.find({}))
    for i in items:
        i["id"] = str(i["_id"])
        i.pop("_id", None)
    return jsonify(items)