# backend/resume_parser.py
from pdfminer.high_level import extract_text
from docx import Document
import os

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

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = parse_pdf(file_path)
    elif ext in [".docx", ".doc"]:
        text = parse_docx(file_path)
    else:
        text = ""
    skills = extract_skills_from_text(text)
    return {"text": text, "skills": skills}
