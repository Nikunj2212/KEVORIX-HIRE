from django.contrib import admin
from .models import User
from .models import User, EmailVerificationToken, EmailOTP


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "role",
        "is_active",
        "is_staff",
        "date_joined",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
        "is_email_verified",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
    )

    ordering = ("-date_joined",)
    
@admin.register(EmailVerificationToken)
class EmailVerificationTokenAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "token",
        "created_at",
        "expires_at",
    )

    search_fields = (
        "user__email",
        "token",
    )

    readonly_fields = (
        "token",
        "created_at",
        "expires_at",
    )
    
@admin.register(EmailOTP)
class EmailOTPAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "otp",
        "created_at",
        "expires_at",
        "attempts",
    )

    search_fields = (
        "user__email",
        "otp",
    )