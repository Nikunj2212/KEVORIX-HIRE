from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from .managers import CustomUserManager
import random
from datetime import timedelta
from django.utils import timezone


def email_verification_expiry():
        return timezone.now() + timedelta(hours=24)

class UserRole(models.TextChoices):

    CANDIDATE = "candidate", "Candidate"

    RECRUITER = "recruiter", "Recruiter"

    COMPANY = "company", "Company"

    INTERVIEWER = "interviewer", "Interviewer"

    SUPER_ADMIN = "super_admin", "Super Admin"
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
    max_length=100,
    blank=True,
    null=True
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
    max_length=20,
    unique=True
    )
    
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CANDIDATE
    )
    is_email_verified = models.BooleanField(
        default=False
    )

    is_phone_verified = models.BooleanField(
        default=False
    )

    profile_completed = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "phone",
        "first_name"
    ]
    
    def get_full_name(self):

        return f"{self.first_name} {self.last_name or ''}".strip()
    
    def __str__(self):
        return self.get_full_name()


    class Meta:
        db_table = "users"
        ordering = ["-date_joined"]
        verbose_name = "User"
        verbose_name_plural = "Users"

class EmailVerificationToken(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="email_verification_token"
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True)

    expires_at = models.DateTimeField(
        default=email_verification_expiry
    )

    def __str__(self):
        return f"{self.user.email}"
    
    
def otp_expiry():
    return timezone.now() + timedelta(minutes=5)

def generate_otp():
    return str(random.randint(100000, 999999))

class EmailOTP(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="email_otp"
    )

    otp = models.CharField(
        max_length=6,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    expires_at = models.DateTimeField(
        default=otp_expiry
    )

    attempts = models.PositiveSmallIntegerField(
        default=0
    )
    is_used = models.BooleanField(
    default=False
    )

    def __str__(self):
        return f"{self.user.email} - {self.otp}"