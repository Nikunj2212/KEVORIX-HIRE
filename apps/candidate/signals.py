from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from apps.candidate.models import (
    CandidateProfile,
    Education,
    Experience,
    Skill,
    Project,
    Certificate,
    Language,
    Resume,
)

from .services.profile_completion_service import ProfileCompletionService

User = get_user_model()


# ==========================================================
# Helper Function
# ==========================================================

def update_profile_completion(profile):
    ProfileCompletionService(profile).calculate()


# ==========================================================
# Create Candidate Profile
# ==========================================================

@receiver(post_save, sender=User)
def create_candidate_profile(sender, instance, created, **kwargs):
    if created and instance.role == "candidate":
        CandidateProfile.objects.create(user=instance)


# ==========================================================
# Candidate Profile
# ==========================================================

@receiver(post_save, sender=CandidateProfile)
def candidate_profile_saved(sender, instance, **kwargs):
    update_profile_completion(instance)


# ==========================================================
# Resume
# ==========================================================

@receiver([post_save, post_delete], sender=Resume)
def resume_changed(sender, instance, **kwargs):
    update_profile_completion(instance.profile)


# ==========================================================
# Education
# ==========================================================

@receiver([post_save, post_delete], sender=Education)
def education_changed(sender, instance, **kwargs):
    update_profile_completion(instance.profile)


# ==========================================================
# Experience
# ==========================================================

@receiver([post_save, post_delete], sender=Experience)
def experience_changed(sender, instance, **kwargs):
    update_profile_completion(instance.profile)


# ==========================================================
# Skill
# ==========================================================

@receiver([post_save, post_delete], sender=Skill)
def skill_changed(sender, instance, **kwargs):
    update_profile_completion(instance.profile)


# ==========================================================
# Project
# ==========================================================

@receiver([post_save, post_delete], sender=Project)
def project_changed(sender, instance, **kwargs):
    update_profile_completion(instance.profile)


# ==========================================================
# Certificate
# ==========================================================

@receiver([post_save, post_delete], sender=Certificate)
def certificate_changed(sender, instance, **kwargs):
    update_profile_completion(instance.profile)


# ==========================================================
# Language
# ==========================================================

@receiver([post_save, post_delete], sender=Language)
def language_changed(sender, instance, **kwargs):
    update_profile_completion(instance.profile)