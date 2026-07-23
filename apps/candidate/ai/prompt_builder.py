JOB_STYLES = {
    "python": "Python Developer",
    "django": "Python Django Developer",
    "developer": "Software Developer",
    "full stack": "Full Stack Developer",
    "fullstack": "Full Stack Developer",
    "frontend": "Frontend Developer",
    "backend": "Backend Developer",
    "react": "React Developer",
    "flutter": "Flutter Developer",
    "android": "Android Developer",
    "ai": "AI Engineer",
    "machine learning": "Machine Learning Engineer",
    "data": "Data Scientist",
    "designer": "UI UX Designer",
    "devops": "DevOps Engineer",
}


def build_cover_prompt(job_title, skills=None):

    title = (job_title or "").lower()

    profession = "Software Developer"

    for keyword, value in JOB_STYLES.items():
        if keyword in title:
            profession = value
            break

    skill_text = ""

    if skills:
        skill_text = ", ".join(skills)

    prompt = f"""
Create a premium LinkedIn cover banner.

Profession:
{profession}

Skills:
{skill_text}

Requirements:

Ultra modern.

Minimal.

Professional.

Dark futuristic workspace.

Purple and blue ambient lighting.

Coding setup.

No people.

No logos.

No readable text.

Wide banner.

16:9 ratio.

High quality.
"""

    return prompt.strip()