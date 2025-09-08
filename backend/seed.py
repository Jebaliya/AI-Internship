# backend/seed.py
from db import internships_coll

sample = [
    {
        "title": "AI Research Intern",
        "org": "NATPAC",
        "description": "Assist with travel survey data, ML pipelines, Python and SQL.",
        "required_skills": ["python", "ml", "sql"],
        "sector": "Transport",
        "location": "Gujarat",
        "stipend": "8000",
        "duration": "3 months",
    },
    {
        "title": "Web Developer Intern",
        "org": "Startup X",
        "description": "Frontend development with HTML, CSS, JS and React.",
        "required_skills": ["html", "css", "javascript", "react"],
        "sector": "IT",
        "location": "Mumbai",
        "stipend": "10000",
        "duration": "2 months",
    },
    {
        "title": "Data Analyst Intern",
        "org": "DataCorp",
        "description": "Analyze datasets using Python, pandas and Excel.",
        "required_skills": ["python", "pandas", "excel"],
        "sector": "Data",
        "location": "Bangalore",
        "stipend": "12000",
        "duration": "3 months",
    },
]

# insert if not exists
if internships_coll.count_documents({}) == 0:
    internships_coll.insert_many(sample)
    print("Seeded internships.")
else:
    print("Internships collection already has data.")
