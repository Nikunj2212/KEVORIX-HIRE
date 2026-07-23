from django.contrib import admin

from .models import Company, Recruiter


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "industry",
        "organization_type",
        "company_size",
        "is_verified",
        "is_active",
    )

    list_filter = (
        "industry",
        "organization_type",
        "company_size",
        "is_verified",
        "is_active",
    )

    search_fields = (
        "name",
        "email",
        "website",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "company",
        "designation",
        "is_primary",
        "is_admin",
        "is_active",
    )

    list_filter = (
        "is_primary",
        "is_admin",
        "is_active",
        "company",
    )

    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "company__name",
    )

    autocomplete_fields = (
        "user",
        "company",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )