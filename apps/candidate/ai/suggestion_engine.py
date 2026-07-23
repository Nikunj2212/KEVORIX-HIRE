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


def get_resume_suggestions(profile):

    suggestions = []

    # Personal Information
    if not profile.user.first_name:
        suggestions.append("Add your first name.")

    if not profile.user.last_name:
        suggestions.append("Add your last name.")

    if not profile.city:
        suggestions.append("Add your city.")

    # Headline
    if not profile.headline:
        suggestions.append("Add a professional headline.")

    # About
    if not profile.about:
        suggestions.append("Complete your About section.")

    # Education
    if not Education.objects.filter(profile=profile).exists():
        suggestions.append("Add your education details.")

    # Experience
    if not Experience.objects.filter(profile=profile).exists():
        suggestions.append("Add work experience.")

    # Skills
    skill_count = Skill.objects.filter(profile=profile).count()

    if skill_count < 5:
        suggestions.append(
            f"Add at least {5 - skill_count} more skill(s)."
        )

    # Projects
    project_count = Project.objects.filter(profile=profile).count()

    if project_count < 2:
        suggestions.append(
            f"Add {2 - project_count} more project(s)."
        )

    # Certificates
    if not Certificate.objects.filter(profile=profile).exists():
        suggestions.append("Add certifications.")

    # Languages
    if not Language.objects.filter(profile=profile).exists():
        suggestions.append("Add languages.")

    # Social Links
    if not SocialLink.objects.filter(profile=profile).exists():
        suggestions.append("Add social links.")

    # Resume
    if not Resume.objects.filter(profile=profile).exists():
        suggestions.append("Upload your resume.")

    # Profile Photo
    if not profile.profile_photo:
        suggestions.append("Upload a profile photo.")

    # Cover Photo
    if not profile.cover_photo:
        suggestions.append("Generate an AI cover photo.")

    return suggestions