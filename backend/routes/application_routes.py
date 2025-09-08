# backend/routes/application_routes.py
from flask import Blueprint, request, jsonify
from models.application import make_application
from controllers.application_controller import save_application
import datetime

application_bp = Blueprint("application", __name__)

@application_bp.route("/api/apply", methods=["POST"])
def apply():
    data = request.json or {}
    data["timestamp"] = datetime.datetime.utcnow()
    application = make_application(data)
    save_application(application)
    return jsonify({"status": "success"})