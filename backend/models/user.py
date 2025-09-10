# backend/models/user.py
def make_user(data):
    return {
        "email": data.get("email"),
        "password_hash": data.get("password_hash"),
        "name": data.get("name", ""),
        "education": data.get("education", ""),
        "skills": data.get("skills", []),
        "interests": data.get("interests", []),
        "preferred_locations": data.get("preferred_locations", []),
        "resume": data.get("resume", ""),
        "is_admin": data.get("is_admin", False),  # <-- Add this line
    }