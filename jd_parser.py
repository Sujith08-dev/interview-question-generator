import re

SKILLS = [
    "python", "java", "sql", "flask", "django",
    "aws", "rest api", "data structures",
    "machine learning", "html", "css", "javascript"
]

def extract_skills(jd_text):
    jd_text = jd_text.lower()
    found = []

    for skill in SKILLS:
        if re.search(rf"\b{skill}\b", jd_text):
            found.append(skill)

    return found
