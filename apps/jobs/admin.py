from django.contrib import admin

from .models import (ExperienceLevel,Job,JobAttachment,JobBenefit,JobCategory,JobSkill,JobType,)


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }
    
@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
    )

    search_fields = (
        "name",
    )
    
@admin.register(ExperienceLevel)
class ExperienceLevelAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
    )

    search_fields = (
        "name",
    )
    
@admin.register(JobSkill)
class JobSkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
    )

    search_fields = (
        "name",
    )
    
class JobBenefitInline(admin.TabularInline):

    model = JobBenefit

    extra = 1


class JobAttachmentInline(admin.TabularInline):

    model = JobAttachment

    extra = 1


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "company",
        "job_type",
        "experience_level",
        "status",
        "is_featured",
        "is_active",
        "created_at",
    )

    list_filter = (
        "status",
        "job_type",
        "experience_level",
        "workplace_type",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "company__company_name",
        "location",
    )

    readonly_fields = (
        "slug",
        "total_views",
        "total_applications",
        "created_at",
        "updated_at",
    )

    filter_horizontal = (
        "skills",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    inlines = [
        JobBenefitInline,
        JobAttachmentInline,
    ]


@admin.register(JobBenefit)
class JobBenefitAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "job",
    )

    search_fields = (
        "title",
    )


@admin.register(JobAttachment)
class JobAttachmentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "job",
        "created_at",
    )

    search_fields = (
        "title",
    )