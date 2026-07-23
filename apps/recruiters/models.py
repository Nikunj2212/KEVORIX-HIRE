from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
import os


# ==========================================================
# Upload Paths
# ==========================================================

def company_logo_upload_path(instance, filename):
    extension = filename.split(".")[-1]
    filename = f"logo_{uuid.uuid4().hex}.{extension}"
    return os.path.join("company", "logos", filename)


def company_cover_upload_path(instance, filename):
    extension = filename.split(".")[-1]
    filename = f"cover_{uuid.uuid4().hex}.{extension}"
    return os.path.join("company", "covers", filename)


# ==========================================================
# Company Choices
# ==========================================================

class IndustryChoices(models.TextChoices):

    SOFTWARE = "software", "Software"
    INFORMATION_TECHNOLOGY = "information_technology", "Information Technology"
    FINTECH = "fintech", "FinTech"
    HEALTHCARE = "healthcare", "Healthcare"
    EDUCATION = "education", "Education"
    ECOMMERCE = "ecommerce", "E-Commerce"
    TELECOM = "telecom", "Telecommunication"
    MANUFACTURING = "manufacturing", "Manufacturing"
    BANKING = "banking", "Banking"
    AUTOMOBILE = "automobile", "Automobile"
    MEDIA = "media", "Media"
    REAL_ESTATE = "real_estate", "Real Estate"
    LOGISTICS = "logistics", "Logistics"
    CONSULTING = "consulting", "Consulting"
    OTHER = "other", "Other"


class OrganizationType(models.TextChoices):

    PRIVATE = "private", "Private"
    PUBLIC = "public", "Public"
    GOVERNMENT = "government", "Government"
    STARTUP = "startup", "Startup"
    NON_PROFIT = "non_profit", "Non Profit"


class CompanySize(models.TextChoices):

    SIZE_1_10 = "1-10", "1 - 10 Employees"
    SIZE_11_50 = "11-50", "11 - 50 Employees"
    SIZE_51_200 = "51-200", "51 - 200 Employees"
    SIZE_201_500 = "201-500", "201 - 500 Employees"
    SIZE_501_1000 = "501-1000", "501 - 1000 Employees"
    SIZE_1001_5000 = "1001-5000", "1001 - 5000 Employees"
    SIZE_5000_PLUS = "5000+", "5000+ Employees"
    
    
    
# ==========================================================
# Company Model
# ==========================================================

class Company(models.Model):

    name = models.CharField(
        max_length=200,
        unique=True
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    tagline = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    industry = models.CharField(
        max_length=50,
        choices=IndustryChoices.choices,
        default=IndustryChoices.SOFTWARE
    )

    organization_type = models.CharField(
        max_length=30,
        choices=OrganizationType.choices,
        default=OrganizationType.PRIVATE
    )

    company_size = models.CharField(
        max_length=20,
        choices=CompanySize.choices,
        default=CompanySize.SIZE_1_10
    )

    founded_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2100),
        ],
        null=True,
        blank=True
    )

    logo = models.ImageField(
        upload_to=company_logo_upload_path,
        blank=True,
        null=True
    )

    cover_image = models.ImageField(
        upload_to=company_cover_upload_path,
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )
    
    address = models.TextField(
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
        default="India"
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    facebook = models.URLField(
        blank=True
    )

    twitter = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    youtube = models.URLField(
        blank=True
    )

    is_verified = models.BooleanField(
        default=False
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Company"

        verbose_name_plural = "Companies"

    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Company.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    
    
# ==========================================================
# Recruiter Model
# ==========================================================

class Recruiter(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recruiter_profile"
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="recruiters"
    )

    designation = models.CharField(
        max_length=150
    )

    department = models.CharField(
        max_length=150,
        blank=True
    )

    employee_id = models.CharField(
        max_length=50,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    profile_photo = models.ImageField(
        upload_to="recruiters/profile/",
        blank=True,
        null=True
    )

    is_primary = models.BooleanField(
        default=False
    )

    is_admin = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["company", "user"]

        verbose_name = "Recruiter"

        verbose_name_plural = "Recruiters"

    def __str__(self):

        return f"{self.user.get_full_name()} - {self.company.name}" 