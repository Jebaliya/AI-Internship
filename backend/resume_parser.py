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
            return line.strip()
    return ""

def extract_interests(text):
    # Look for a line starting with 'Interests' or similar
    for line in text.splitlines():
        if "interest" in line.lower():
            return line.split(":", 1)[-1].strip()
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
    gmail = extract_email(text)
    education = extract_education(text)
    interests = extract_interests(text)
    return {
        "text": text,
        "skills": skills,
        "name": name,
        "gmail": gmail,
        "education": education,
        "interests": interests
    }
