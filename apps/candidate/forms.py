from django import forms
from apps.accounts.models import User
from .models import CandidateProfile

class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [

            "first_name",
            "last_name",
            "phone",

        ]
        
class CandidateProfileForm(forms.ModelForm):

    class Meta:

        model = CandidateProfile

        fields = [

            "headline",
            "about",
            "date_of_birth",
            "gender",
            "city",
            "state",
            "country",
            "nationality",
            "current_job_title",
            "profile_photo",
            "cover_photo",

        ]