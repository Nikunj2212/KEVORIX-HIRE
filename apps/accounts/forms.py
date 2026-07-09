from django import forms
from .models import User


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password"
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password"
            }
        )
    )

    class Meta:

        model = User

        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "password",
        )

    def clean_email(self):

        email = self.cleaned_data["email"].lower()

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError(
                "Email already exists."
            )

        return email

    def clean_phone(self):

        phone = self.cleaned_data["phone"]

        if User.objects.filter(phone=phone).exists():

            raise forms.ValidationError(
                "Phone number already exists."
            )

        return phone

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")

        confirm = cleaned_data.get("confirm_password")

        if password != confirm:

            raise forms.ValidationError(
                "Passwords do not match."
            )

        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:

            user.save()

        return user
    
class LoginForm(forms.Form):

    email_or_phone = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Email or Phone"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password"
            }
        )
    )