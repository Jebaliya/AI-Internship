# backend/routes/auth_routes.py
from flask import Blueprint, request, jsonify, send_file
from controllers.user_controller import find_user_by_email, save_user
from resume_parser import parse_resume
from models.user import make_user
import bcrypt
import jwt
import os
import tempfile

auth_bp = Blueprint("auth", __name__)
JWT_SECRET = os.environ.get("JWT_SECRET", "supersecretkey")

@auth_bp.route("/api/register", methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")
    confirm = request.form.get("confirm")
    if not email or not password or password != confirm:
        return jsonify({"error": "Invalid registration"}), 400
    if find_user_by_email(email):
        return jsonify({"error": "Email already registered"}), 400

    # Resume upload and parsing
    resume_file = request.files.get("resume")
    resume_data = {}
    resume_path = ""
    if resume_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(resume_file.filename)[1]) as tmp:
            resume_file.save(tmp.name)
            resume_data = parse_resume(tmp.name)
            resume_path = tmp.name

    # Prepare user data
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user_data = {
        "email": email,
        "password_hash": password_hash,
        "name": resume_data.get("name", ""),
        "education": resume_data.get("education", ""),
        "skills": resume_data.get("skills", []),
        "interests": resume_data.get("interests", []),
        "preferred_locations": [resume_data.get("location", "")] if resume_data.get("location") else [],
        "resume": resume_path,
    }
    user = make_user(user_data)
    save_user(user)
    return jsonify({"status": "registered"})

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.json or {}
    email = data.get("email")
    password = data.get("password")
    user = find_user_by_email(email)
    if not user or not bcrypt.checkpw(password.encode(), user["password_hash"].encode()):
        return jsonify({"error": "Invalid credentials"}), 401
    token = jwt.encode({"email": email}, JWT_SECRET, algorithm="HS256")
    return jsonify({"token": token, "user": {
        "email": user["email"],
        "name": user.get("name", ""),
        "education": user.get("education", ""),
        "skills": user.get("skills", []),
        "interests": user.get("interests", []),
        "preferred_locations": user.get("preferred_locations", []),
    }})

@auth_bp.route("/api/me", methods=["GET"])
def get_me():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing token"}), 401
    token = auth_header.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = find_user_by_email(payload["email"])
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"user": {
            "email": user["email"],
            "name": user.get("name", ""),
            "education": user.get("education", ""),
            "skills": user.get("skills", []),
            "interests": user.get("interests", []),
            "preferred_locations": user.get("preferred_locations", []),
        }})
    except Exception:
        return jsonify({"error": "Invalid token"}), 401

@auth_bp.route("/api/resume/<email>", methods=["GET"])
def get_resume(email):
    user = find_user_by_email(email)
    if not user or not user.get("resume"):
        return jsonify({"error": "Resume not found"}), 404
    return send_file(user["resume"], mimetype="application/pdf")
