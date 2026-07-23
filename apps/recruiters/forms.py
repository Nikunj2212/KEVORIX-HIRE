from django import forms

from .models import Company, Recruiter

class CompanyForm(forms.ModelForm):

    class Meta:

        model = Company

        exclude = (
            "slug",
            "is_verified",
            "is_featured",
            "is_active",
            "created_at",
            "updated_at",
        )

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name",
            }),

            "tagline": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Tagline",
            }),

            "industry": forms.Select(attrs={
                "class": "form-control",
            }),

            "organization_type": forms.Select(attrs={
                "class": "form-control",
            }),

            "company_size": forms.Select(attrs={
                "class": "form-control",
            }),

            "founded_year": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Founded Year",
            }),

            "website": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "company@example.com",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "+91 9876543210",
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Company Address",
            }),

            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "City",
            }),

            "state": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "State",
            }),

            "country": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Country",
            }),

            "postal_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Postal Code",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Tell candidates about your company...",
            }),

            "logo": forms.FileInput(attrs={
                "class": "form-control",
            }),

            "cover_image": forms.FileInput(attrs={
                "class": "form-control",
            }),

            "linkedin": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "LinkedIn URL",
            }),

            "facebook": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Facebook URL",
            }),

            "twitter": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Twitter URL",
            }),

            "instagram": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Instagram URL",
            }),

            "youtube": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "YouTube URL",
            }),

        }
        
class RecruiterForm(forms.ModelForm):

    class Meta:

        model = Recruiter

        fields = (
            "designation",
            "department",
            "employee_id",
            "phone",
            "profile_photo",
        )

        widgets = {

            "designation": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Founder / HR Manager",
            }),

            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Human Resources",
            }),

            "employee_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Employee ID",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "+91 9876543210",
            }),

            "profile_photo": forms.FileInput(attrs={
                "class": "form-control",
            }),

        }