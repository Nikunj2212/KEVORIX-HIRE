from django.conf import settings
from django.db import models
from django.utils.text import slugify

from apps.recruiters.models import Company

class JobCategory(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    icon = models.CharField(
        max_length=50,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Job Category"

        verbose_name_plural = "Job Categories"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name
    
class JobType(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Job Type"

        verbose_name_plural = "Job Types"

    def __str__(self):

        return self.name
class ExperienceLevel(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = ["id"]

        verbose_name = "Experience Level"

        verbose_name_plural = "Experience Levels"

    def __str__(self):

        return self.name
    
class JobSkill(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Job Skill"

        verbose_name_plural = "Job Skills"

    def __str__(self):

        return self.name


class SalaryType(models.TextChoices):

    YEAR = "YEAR", "Per Year"

    MONTH = "MONTH", "Per Month"

    WEEK = "WEEK", "Per Week"

    DAY = "DAY", "Per Day"

    HOUR = "HOUR", "Per Hour"


class WorkplaceType(models.TextChoices):

    ON_SITE = "ON_SITE", "On Site"

    REMOTE = "REMOTE", "Remote"

    HYBRID = "HYBRID", "Hybrid"


class JobStatus(models.TextChoices):

    DRAFT = "DRAFT", "Draft"

    PUBLISHED = "PUBLISHED", "Published"

    PAUSED = "PAUSED", "Paused"

    CLOSED = "CLOSED", "Closed"

    EXPIRED = "EXPIRED", "Expired"
    
class Job(models.Model):

    title = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs",
    )

    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posted_jobs",
    )

    category = models.ForeignKey(
        JobCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="jobs",
    )

    job_type = models.ForeignKey(
        JobType,
        on_delete=models.SET_NULL,
        null=True,
        related_name="jobs",
    )

    experience_level = models.ForeignKey(
        ExperienceLevel,
        on_delete=models.SET_NULL,
        null=True,
        related_name="jobs",
    )

    workplace_type = models.CharField(
        max_length=20,
        choices=WorkplaceType.choices,
        default=WorkplaceType.ON_SITE,
    )

    skills = models.ManyToManyField(
        JobSkill,
        blank=True,
        related_name="jobs",
    )

    vacancies = models.PositiveIntegerField(
        default=1,
    )

    minimum_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    maximum_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    salary_type = models.CharField(
        max_length=20,
        choices=SalaryType.choices,
        default=SalaryType.YEAR,
    )

    salary_negotiable = models.BooleanField(
        default=False,
    )

    hide_salary = models.BooleanField(
        default=False,
    )

    location = models.CharField(
        max_length=255,
    )

    address = models.TextField(
        blank=True,
    )

    responsibilities = models.TextField()

    requirements = models.TextField()

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=JobStatus.choices,
        default=JobStatus.DRAFT,
    )

    is_featured = models.BooleanField(
        default=False,
    )

    is_urgent = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    application_deadline = models.DateField(
        null=True,
        blank=True,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    total_views = models.PositiveIntegerField(
        default=0,
    )

    total_applications = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = [
            "-created_at",
        ]

        verbose_name = "Job"

        verbose_name_plural = "Jobs"
        
    def __str__(self):
            return self.title

    def save(self, *args, **kwargs):

            if not self.slug:
                base_slug = slugify(self.title)
                slug = base_slug
                counter = 1

                while Job.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1

                self.slug = slug

            super().save(*args, **kwargs)

    @property
    def salary_range(self):

            if self.hide_salary:
                return "Salary Not Disclosed"

            if self.salary_negotiable:
                return "Negotiable"

            if self.minimum_salary and self.maximum_salary:
                return (
                    f"₹{self.minimum_salary:,.0f} - "
                    f"₹{self.maximum_salary:,.0f} "
                    f"{self.get_salary_type_display()}"
                )

            if self.minimum_salary:
                return (
                    f"From ₹{self.minimum_salary:,.0f} "
                    f"{self.get_salary_type_display()}"
                )

            return "Not Specified"

    @property
    def is_open(self):
            return self.status == JobStatus.PUBLISHED

    @property
    def total_positions_left(self):
            return max(
                self.vacancies - self.total_applications,
                0,
            )
            
class JobBenefit(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="benefits",
    )

    title = models.CharField(
        max_length=150,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = ["id"]

        verbose_name = "Job Benefit"

        verbose_name_plural = "Job Benefits"

    def __str__(self):
        return self.title


class JobAttachment(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="attachments",
    )

    file = models.FileField(
        upload_to="jobs/attachments/",
    )

    title = models.CharField(
        max_length=255,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Job Attachment"

        verbose_name_plural = "Job Attachments"

    def __str__(self):

        if self.title:
            return self.title

        return self.file.name