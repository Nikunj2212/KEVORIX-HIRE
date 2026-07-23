from django import forms

from .models import Job


class JobForm(forms.ModelForm):

    class Meta:

        model = Job

        exclude = (
            "slug",
            "company",
            "recruiter",
            "total_views",
            "total_applications",
            "created_at",
            "updated_at",
            "published_at",
        )

        widgets = {

            "application_deadline": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 6,
                }
            ),

            "responsibilities": forms.Textarea(
                attrs={
                    "rows": 6,
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),

            "skills": forms.CheckboxSelectMultiple(),

        }