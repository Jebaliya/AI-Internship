# backend/resume_parser.py
from pdfminer.high_level import extract_text
from docx import Document
import os
import re

COMMON_SKILLS = [
    'python','java','c++','ml','machine learning','data analysis',
    'sql','excel','r','javascript','react','node','django','flask',
    'html','css','aws','docker','pandas','tensorflow','scikit-learn'
]

def parse_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def parse_pdf(path):
    try:
        return extract_text(path)
    except Exception as e:
        print("pdf parse error:", e)
        return ""

def extract_skills_from_text(text):
    text_low = text.lower()
    found = [s for s in COMMON_SKILLS if s in text_low]
    return sorted(set(found))

<<<<<<< HEAD
def extract_name(text):
    # Try to find a line that looks like a name (first non-empty line)
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if line and len(line.split()) >= 2 and not any(c.isdigit() for c in line):
            return line
    return ""

def extract_education(text):
    # Look for education keywords
    edu_keywords = ["b.tech", "bachelor", "bsc", "msc", "m.tech", "be", "phd", "engineering", "computer", "science"]
    for line in text.splitlines():
        l = line.lower()
        if any(k in l for k in edu_keywords):
=======
def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else ""

def extract_name(text):
    # Simple heuristic: first non-empty line
    for line in text.splitlines():
        if line.strip() and "@" not in line:
            return line.strip()
    return ""

def extract_education(text):
    # Look for lines containing common degrees
    for line in text.splitlines():
        if any(degree in line.lower() for degree in ["b.tech", "bachelor", "m.tech", "master", "phd", "engineer"]):
>>>>>>> 751384f569368c10763a8b14adb12d713507917f
            return line.strip()
    return ""

def extract_interests(text):
<<<<<<< HEAD
    # Look for 'interests' section
    match = re.search(r"interests[:\-]?\s*(.*)", text, re.IGNORECASE)
    if match:
        interests = match.group(1)
        return [i.strip() for i in re.split(r",|;", interests) if i.strip()]
    return []

def extract_location(text):
    # Look for 'location' or common Indian cities/states
    loc_keywords = ["location", "gujarat", "mumbai", "delhi", "bangalore", "pune", "hyderabad", "chennai", "kolkata", "noida"]
    for line in text.splitlines():
        l = line.lower()
        for k in loc_keywords:
            if k in l:
                return line.strip()
=======
    # Look for a line starting with 'Interests' or similar
    for line in text.splitlines():
        if "interest" in line.lower():
            return line.split(":", 1)[-1].strip()
>>>>>>> 751384f569368c10763a8b14adb12d713507917f
    return ""

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = parse_pdf(file_path)
    elif ext in [".docx", ".doc"]:
        text = parse_docx(file_path)
    else:
        text = ""
    skills = extract_skills_from_text(text)
    name = extract_name(text)
<<<<<<< HEAD
    education = extract_education(text)
    interests = extract_interests(text)
    location = extract_location(text)
=======
    gmail = extract_email(text)
    education = extract_education(text)
    interests = extract_interests(text)
>>>>>>> 751384f569368c10763a8b14adb12d713507917f
    return {
        "text": text,
        "skills": skills,
        "name": name,
<<<<<<< HEAD
        "education": education,
        "interests": interests,
        "location": location
=======
        "gmail": gmail,
        "education": education,
        "interests": interests
>>>>>>> 751384f569368c10763a8b14adb12d713507917f
    }
