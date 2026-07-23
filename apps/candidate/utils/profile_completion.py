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

def calculate_profile_completion(profile):

    score = 0

    # Personal Information
    if profile.headline:
        score += 5

    if profile.about:
        score += 10

    if profile.current_job_title:
        score += 5

    if profile.city:
        score += 3

    if profile.country:
        score += 2

    if profile.profile_photo:
        score += 5

    if profile.cover_photo:
        score += 5

    # Profile Sections
    if Education.objects.filter(profile=profile).exists():
        score += 15

    if Experience.objects.filter(profile=profile).exists():
        score += 15

    if Skill.objects.filter(profile=profile).exists():
        score += 10

    if Project.objects.filter(profile=profile).exists():
        score += 10

    if Certificate.objects.filter(profile=profile).exists():
        score += 5

    if Language.objects.filter(profile=profile).exists():
        score += 5

    if SocialLink.objects.filter(profile=profile).exists():
        score += 5

    if Resume.objects.filter(profile=profile).exists():
        score += 15

    return min(score, 100)