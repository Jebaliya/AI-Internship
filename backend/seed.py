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
    # Web related
    {
        "title": "Backend Developer Intern",
        "org": "TechNest",
        "description": "Work on server-side logic using Node.js and Express.",
        "required_skills": ["nodejs", "express", "mongodb"],
        "sector": "IT",
        "location": "Delhi",
        "stipend": "9000",
        "duration": "2 months",
    },
    {
        "title": "Full Stack Web Intern",
        "org": "WebWorks",
        "description": "Develop full stack web apps using Django and React.",
        "required_skills": ["django", "react", "javascript", "python"],
        "sector": "IT",
        "location": "Hyderabad",
        "stipend": "11000",
        "duration": "3 months",
    },
    {
        "title": "WordPress Developer Intern",
        "org": "Creative Minds",
        "description": "Build and customize WordPress sites.",
        "required_skills": ["wordpress", "php", "css", "javascript"],
        "sector": "IT",
        "location": "Pune",
        "stipend": "7000",
        "duration": "2 months",
    },
    # Data related
    {
        "title": "Business Intelligence Intern",
        "org": "Insight Analytics",
        "description": "Create BI dashboards using Power BI and SQL.",
        "required_skills": ["powerbi", "sql", "excel"],
        "sector": "Data",
        "location": "Chennai",
        "stipend": "10000",
        "duration": "3 months",
    },
    {
        "title": "Machine Learning Intern",
        "org": "ML Labs",
        "description": "Build ML models with scikit-learn and Python.",
        "required_skills": ["python", "scikit-learn", "ml"],
        "sector": "Data",
        "location": "Kolkata",
        "stipend": "13000",
        "duration": "3 months",
    },
    {
        "title": "Data Engineering Intern",
        "org": "DataStream",
        "description": "ETL pipelines using Python and Apache Spark.",
        "required_skills": ["python", "spark", "etl"],
        "sector": "Data",
        "location": "Noida",
        "stipend": "12000",
        "duration": "2 months",
    },
    # UI/UX
    {
        "title": "UI Designer Intern",
        "org": "DesignHub",
        "description": "Design user interfaces using Figma and Adobe XD.",
        "required_skills": ["figma", "adobe xd", "ui design"],
        "sector": "Design",
        "location": "Bangalore",
        "stipend": "9000",
        "duration": "2 months",
    },
    {
        "title": "UX Research Intern",
        "org": "UserFirst",
        "description": "Conduct user research and usability testing.",
        "required_skills": ["ux research", "usability testing", "interviews"],
        "sector": "Design",
        "location": "Mumbai",
        "stipend": "8500",
        "duration": "3 months",
    },
    {
        "title": "Product Design Intern",
        "org": "Innovate Studio",
        "description": "Work on product design and prototyping.",
        "required_skills": ["prototyping", "figma", "product design"],
        "sector": "Design",
        "location": "Delhi",
        "stipend": "9500",
        "duration": "2 months",
    },
    # Cyber Security
    {
        "title": "Cyber Security Analyst Intern",
        "org": "SecureIT",
        "description": "Monitor network security and analyze threats.",
        "required_skills": ["network security", "threat analysis", "python"],
        "sector": "Cyber Security",
        "location": "Hyderabad",
        "stipend": "12000",
        "duration": "3 months",
    },
    {
        "title": "Penetration Testing Intern",
        "org": "CyberSafe",
        "description": "Perform penetration testing and vulnerability assessment.",
        "required_skills": ["penetration testing", "vulnerability assessment", "linux"],
        "sector": "Cyber Security",
        "location": "Pune",
        "stipend": "11000",
        "duration": "2 months",
    },
    {
        "title": "Security Operations Intern",
        "org": "DefendTech",
        "description": "Assist in SOC operations and incident response.",
        "required_skills": ["soc", "incident response", "siem"],
        "sector": "Cyber Security",
        "location": "Chennai",
        "stipend": "10000",
        "duration": "3 months",
    },
]

# insert if not exists
if internships_coll.count_documents({}) == 0:
    internships_coll.insert_many(sample)
    print("Seeded internships.")
else:
    print("Internships collection already has data.")


