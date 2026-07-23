import re
import pdfplumber
from docx import Document
import spacy

nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = [
    "python",
    "django",
    "django rest framework",
    "drf",
    "flask",
    "fastapi",
    "html",
    "css",
    "bootstrap",
    "tailwind",
    "javascript",
    "typescript",
    "react",
    "next.js",
    "vue",
    "angular",
    "mysql",
    "postgresql",
    "sqlite",
    "mongodb",
    "git",
    "github",
    "docker",
    "linux",
    "aws",
    "azure",
    "postman",
]
def extract_skills(text):

    found = []

    lower_text = text.lower()

    for skill in COMMON_SKILLS:

        if skill in lower_text:
            found.append(skill.title())

    return sorted(list(set(found)))
def extract_text(file_path):

    if file_path.lower().endswith(".pdf"):

        text = ""

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    elif file_path.lower().endswith(".docx"):

        doc = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

    return ""


def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text,
    )

    return match.group() if match else None


def extract_phone(text):

    match = re.search(
        r"(\+91[\s-]?)?[6-9]\d{9}",
        text,
    )

    return match.group() if match else None


def parse_resume(file_path):

    text = extract_text(file_path)

    return {
        "text": text,
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
    }
    
    
def extract_name(text):

    lines = text.splitlines()

    ignore = {
        "python",
        "django",
        "rest",
        "framework",
        "developer",
        "engineer",
        "resume",
        "curriculum vitae",
        "cv",
        "email",
        "phone",
        "skills",
    }

    for line in lines[:15]:

        line = line.strip()

        if not line:
            continue

        lower = line.lower()

        if any(word in lower for word in ignore):
            continue

        if len(line.split()) < 2:
            continue

        if len(line) > 40:
            continue

        if re.search(r"[0-9@]", line):
            continue

        return line.title()

    return None