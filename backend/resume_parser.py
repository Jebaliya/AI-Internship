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
            return line.strip()
    return ""

def extract_interests(text):
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
    education = extract_education(text)
    interests = extract_interests(text)
    location = extract_location(text)
    return {
        "text": text,
        "skills": skills,
        "name": name,
        "education": education,
        "interests": interests,
        "location": location
    }
