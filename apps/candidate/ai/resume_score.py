from apps.candidate.models import (
    Education,
    Experience,
    Skill,
    Project,
    Certificate,
    Language,
    SocialLink,
    Resume,
)


def calculate_resume_score(profile):

    score = 0

    # -------------------------
    # Personal Information (10)
    # -------------------------
    if profile.user.first_name:
        score += 2

    if profile.user.last_name:
        score += 2

    if profile.user.email:
        score += 2

    if profile.user.phone:
        score += 2

    if profile.city:
        score += 2

    # -------------------------
    # Headline (10)
    # -------------------------
    if profile.headline:
        score += 10

    # -------------------------
    # About (10)
    # -------------------------
    if profile.about:
        score += 10

    # -------------------------
    # Education (10)
    # -------------------------
    if Education.objects.filter(profile=profile).exists():
        score += 10

    # -------------------------
    # Experience (15)
    # -------------------------
    if Experience.objects.filter(profile=profile).exists():
        score += 15

    # -------------------------
    # Skills (15)
    # -------------------------
    skills = Skill.objects.filter(profile=profile).count()

    score += min(skills * 3, 15)

    # -------------------------
    # Projects (10)
    # -------------------------
    projects = Project.objects.filter(profile=profile).count()

    score += min(projects * 5, 10)

    # -------------------------
    # Certificates (5)
    # -------------------------
    if Certificate.objects.filter(profile=profile).exists():
        score += 5

    # -------------------------
    # Languages (5)
    # -------------------------
    if Language.objects.filter(profile=profile).exists():
        score += 5

    # -------------------------
    # Social Links (5)
    # -------------------------
    if SocialLink.objects.filter(profile=profile).exists():
        score += 5

    # -------------------------
    # Resume (5)
    # -------------------------
    if Resume.objects.filter(profile=profile).exists():
        score += 5

    # -------------------------
    # Profile Photo (5)
    # -------------------------
    if profile.profile_photo:
        score += 5

    # -------------------------
    # Cover Photo (5)
    # -------------------------
    if profile.cover_photo:
        score += 5

    return min(score, 100)