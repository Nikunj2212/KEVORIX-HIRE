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
    
    
class Education(models.Model):

    profile = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name="educations"
    )

    EDUCATION_TYPES = [

        ("school", "School"),

        ("diploma", "Diploma"),

        ("bachelor", "Bachelor"),

        ("master", "Master"),

        ("phd", "PhD"),

        ("certification", "Certification"),

        ("other", "Other"),

    ]

    education_type = models.CharField(
        max_length=30,
        choices=EDUCATION_TYPES,
    )

    institution_name = models.CharField(
        max_length=255
    )

    degree = models.CharField(
        max_length=255
    )

    field_of_study = models.CharField(
        max_length=255,
        blank=True
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    currently_studying = models.BooleanField(
        default=False
    )

    grade = models.CharField(
        max_length=50,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["-start_date"]

        verbose_name = "Education"

        verbose_name_plural = "Educations"

    def __str__(self):

        return f"{self.degree} - {self.institution_name}"
    
    
class Experience(models.Model):

    profile = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name="experiences"
    )

    EMPLOYMENT_TYPES = [

        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("internship", "Internship"),
        ("freelance", "Freelance"),
        ("contract", "Contract"),
        ("temporary", "Temporary"),
        ("volunteer", "Volunteer"),

    ]

    job_title = models.CharField(
        max_length=200
    )

    company_name = models.CharField(
        max_length=255
    )

    employment_type = models.CharField(
        max_length=30,
        choices=EMPLOYMENT_TYPES
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    currently_working = models.BooleanField(
        default=False
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["-start_date"]

        verbose_name = "Experience"

        verbose_name_plural = "Experiences"

    def __str__(self):

        return f"{self.job_title} - {self.company_name}"
    
    
class Skill(models.Model):

    profile = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    name = models.CharField(
        max_length=100
    )

    proficiency = models.CharField(
        max_length=20,
        choices=[
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
            ("expert", "Expert"),
        ],
        default="intermediate"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["name"]

        unique_together = ("profile", "name")

        verbose_name = "Skill"

        verbose_name_plural = "Skills"

    def __str__(self):

        return self.name
    
    
class Project(models.Model):

    profile = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(
        max_length=200
    )

    short_description = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    technologies = models.CharField(
        max_length=255,
        help_text="Example: Python, Django, DRF, MySQL"
    )

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    thumbnail = models.ImageField(
        upload_to="candidate/projects/",
        blank=True,
        null=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    currently_working = models.BooleanField(
        default=False
    )

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["-featured", "-start_date"]

        verbose_name = "Project"

        verbose_name_plural = "Projects"

    def __str__(self):

        return self.title