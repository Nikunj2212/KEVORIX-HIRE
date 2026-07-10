from django import forms
from apps.accounts.models import User
from .models import CandidateProfile
from .models import Education
from .models import CandidateProfile, Education, Experience
from .models import CandidateProfile, Education, Experience, Skill


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
        
class PersonalInformationForm(forms.ModelForm):

    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter first name",
            }
        ),
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter last name",
            }
        ),
    )

    email = forms.EmailField(
        label="Email Address",
        disabled=True,
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    phone = forms.CharField(
        label="Phone Number",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }
        ),
    )

    class Meta:

        model = CandidateProfile

        fields = [
            "date_of_birth",
            "gender",
            "headline",
            "current_job_title",
        ]

        widgets = {

            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "gender": forms.Select(
                choices=[
                    ("", "Select Gender"),
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Other", "Other"),
                    ("Prefer not to say", "Prefer not to say"),
                ],
                attrs={
                    "class": "form-control",
                },
            ),

            "headline": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Python Django Developer",
                }
            ),

            "current_job_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Software Engineer",
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        user = kwargs.pop("user")

        super().__init__(*args, **kwargs)

        self.fields["first_name"].initial = user.first_name
        self.fields["last_name"].initial = user.last_name
        self.fields["email"].initial = user.email
        self.fields["phone"].initial = user.phone

    def clean_phone(self):

        phone = self.cleaned_data["phone"].strip()

        if len(phone) < 10:
            raise forms.ValidationError(
                "Phone number must be at least 10 digits."
            )

        return phone

    def save(self, commit=True):

        profile = super().save(commit=False)

        user = profile.user

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone = self.cleaned_data["phone"]

        if commit:

            user.save()
            profile.save()

        return profile

    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter first name",
            }
        ),
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter last name",
            }
        ),
    )

    email = forms.EmailField(
        label="Email Address",
        disabled=True,
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    phone = forms.CharField(
        label="Phone Number",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }
        ),
    )

    class Meta:

        model = CandidateProfile

        fields = [
            "date_of_birth",
            "gender",
            "headline",
            "current_job_title",
        ]

        widgets = {

            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "gender": forms.Select(
                choices=[
                    ("", "Select Gender"),
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Other", "Other"),
                    ("Prefer not to say", "Prefer not to say"),
                ],
                attrs={
                    "class": "form-control",
                },
            ),

            "headline": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Python Django Developer",
                }
            ),

            "current_job_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Software Engineer",
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        user = kwargs.pop("user")

        super().__init__(*args, **kwargs)

        self.fields["first_name"].initial = user.first_name
        self.fields["last_name"].initial = user.last_name
        self.fields["email"].initial = user.email
        self.fields["phone"].initial = user.phone

    def clean_phone(self):

        phone = self.cleaned_data["phone"].strip()

        if len(phone) < 10:
            raise forms.ValidationError(
                "Phone number must be at least 10 digits."
            )

        return phone

    def save(self, commit=True):

        profile = super().save(commit=False)

        user = profile.user

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone = self.cleaned_data["phone"]

        if commit:

            user.save()
            profile.save()

        return profile
    
class AboutForm(forms.ModelForm):

    class Meta:

        model = CandidateProfile

        fields = [

            "about",

        ]

        widgets = {

            "about": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 10,

                    "maxlength": 2000,

                    "placeholder": (
                        "Write a professional summary about yourself. "
                        "Mention your experience, skills, technologies, "
                        "achievements and career goals."
                    ),

                }

            )

        }

    def clean_about(self):

        about = self.cleaned_data["about"].strip()

        if len(about) < 20:

            raise forms.ValidationError(
                "About section must contain at least 20 characters."
            )

        return about
    
    
class EducationForm(forms.ModelForm):

    class Meta:

        model = Education

        fields = [

            "education_type",
            "institution_name",
            "degree",
            "field_of_study",
            "location",
            "start_date",
            "end_date",
            "currently_studying",
            "grade",
            "description",

        ]

        widgets = {

            "education_type": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "institution_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Institution Name",
                }
            ),

            "degree": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Degree",
                }
            ),

            "field_of_study": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Field of Study",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Location",
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "grade": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "CGPA / Grade",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe your education, achievements, activities...",
                }
            ),

        }

    def clean(self):

        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        currently_studying = cleaned_data.get("currently_studying")

        if not currently_studying:

            if end_date is None:

                raise forms.ValidationError(
                    "End date is required."
                )

        if start_date and end_date:

            if end_date < start_date:

                raise forms.ValidationError(
                    "End date cannot be earlier than start date."
                )

        return cleaned_data
    
    
class ExperienceForm(forms.ModelForm):

    class Meta:

        model = Experience

        fields = [

            "job_title",
            "company_name",
            "employment_type",
            "location",
            "start_date",
            "end_date",
            "currently_working",
            "description",

        ]

        widgets = {

            "job_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Job Title",
                }
            ),

            "company_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Company Name",
                }
            ),

            "employment_type": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Location",
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Describe your responsibilities, achievements, technologies used and key contributions.",
                }
            ),

        }

    def clean(self):

        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        currently_working = cleaned_data.get("currently_working")

        if not currently_working and not end_date:

            raise forms.ValidationError(
                "End date is required unless you are currently working."
            )

        if start_date and end_date:

            if end_date < start_date:

                raise forms.ValidationError(
                    "End date cannot be earlier than start date."
                )

        return cleaned_data
    
    
class SkillForm(forms.ModelForm):

    class Meta:

        model = Skill

        fields = [

            "name",
            "proficiency",

        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Skill Name (e.g. Python, Django, Docker)"
                }
            ),

            "proficiency": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

        }

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        return name.title()