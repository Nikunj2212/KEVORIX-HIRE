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


class ProfileCompletionService:

    def __init__(self, profile):
        self.profile = profile

    def calculate(self):
        """
        Calculate profile completion percentage.
        """

        score = 0

        # -------------------------------
        # Basic Profile
        # -------------------------------

        basic_fields = [
            self.profile.user.first_name,
            self.profile.user.email,
            self.profile.user.phone,
            self.profile.current_job_title,
            self.profile.city,
            self.profile.country,
        ]

        if all(basic_fields):
            score += 15

        # -------------------------------
        # About
        # -------------------------------

        if self.profile.about:
            score += 10

        # -------------------------------
        # Profile Photo
        # -------------------------------

        if self.profile.profile_photo:
            score += 10

        # -------------------------------
        # Resume
        # -------------------------------

        if Resume.objects.filter(profile=self.profile).exists():
            score += 10

        # -------------------------------
        # Education
        # -------------------------------

        if Education.objects.filter(profile=self.profile).exists():
            score += 15

        # -------------------------------
        # Experience
        # -------------------------------

        if Experience.objects.filter(profile=self.profile).exists():
            score += 15

        # -------------------------------
        # Skills
        # -------------------------------

        if Skill.objects.filter(profile=self.profile).exists():
            score += 10

        # -------------------------------
        # Projects
        # -------------------------------

        if Project.objects.filter(profile=self.profile).exists():
            score += 5

        # -------------------------------
        # Certificates
        # -------------------------------

        if Certificate.objects.filter(profile=self.profile).exists():
            score += 5

        # -------------------------------
        # Languages
        # -------------------------------

        if Language.objects.filter(profile=self.profile).exists():
            score += 5

        # Final Score
        score = min(score, 100)

        # Update without triggering post_save signal
        CandidateProfile.objects.filter(
            pk=self.profile.pk
        ).update(
            profile_completion=score
        )

        # Update current object
        self.profile.profile_completion = score

        return score