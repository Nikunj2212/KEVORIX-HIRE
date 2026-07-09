from django.db import models
from django.conf import settings


class CandidateProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="candidate_profile"
    )

    headline = models.CharField(max_length=150, blank=True)

    profile_photo = models.ImageField(
        upload_to="candidate/profile/",
        blank=True,
        null=True
    )

    cover_photo = models.ImageField(
        upload_to="candidate/cover/",
        blank=True,
        null=True
    )

    about = models.TextField(blank=True)

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=20,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        blank=True
    )

    nationality = models.CharField(
        max_length=100,
        blank=True
    )

    current_job_title = models.CharField(
        max_length=150,
        blank=True
    )

    years_of_experience = models.PositiveIntegerField(
        default=0
    )

    website = models.URLField(blank=True)

    profile_completion = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.email