# backend/app.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from db import internships_coll, profiles_coll, recommendations_coll
from recommender import recommend_topk
from resume_parser import parse_resume
from bson import ObjectId
import tempfile
from routes.application_routes import application_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(application_bp)

def serialize_internship(doc):
    doc["id"] = str(doc["_id"])
    doc.pop("_id", None)
    return doc

@app.route("/api/internships", methods=["GET"])
def list_internships():
    items = list(internships_coll.find({}))
    return jsonify([serialize_internship(i) for i in items])

@app.route("/api/upload-resume", methods=["POST"])
def upload_resume():
    f = request.files.get("file")
    if not f:
        return jsonify({"error":"no file"}), 400
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(f.filename)[1])
    f.save(tmp.name)
    parsed = parse_resume(tmp.name)
    os.unlink(tmp.name)
    return jsonify(parsed)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.json or {}
    skills = data.get("skills", [])
    education = data.get("education", "")
    interests = data.get("interests", [])
    preferred_locations = data.get("preferred_locations", [])

    # Build profile text for TF-IDF: combine skills + education + interests + preferred locations
    profile_parts = []
    if education:
        profile_parts.append(education)
    profile_parts.extend(skills)
    profile_parts.extend(interests)
    profile_parts.extend(preferred_locations)
    profile_text = " ".join(profile_parts) if profile_parts else ""

    internships = list(internships_coll.find({}))

    # Simple fallback: if no profile_text, still attempt by skills only
    recs = recommend_topk(profile_text, skills, internships, top_k=5)

    # convert ObjectId to string for JSON
    out = []
    for r in recs:
        it = r["internship"].copy()
        it["id"] = str(it["_id"])
        it.pop("_id", None)
        out.append({
            "internship": it,
            "score": r["score"],
            "matched_skills": r["matched_skills"]
        })

    # Optionally store recommendations (MVP)
    # recommendations_coll.insert_one({"profile": data, "results": out})

    return jsonify({"recommendations": out})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
