# backend/models/application.py

def make_application(data):
    return {
        "name": data.get("name"),
        "education": data.get("education"),
        "skills": data.get("skills", []),
        "interests": data.get("interests", []),
        "preferred_locations": data.get("preferred_locations", []),
        "internship_id": data.get("internship_id"),
        "user_id": data.get("user_id"),  # <-- Add this line
        "timestamp": data.get("timestamp"),
    }