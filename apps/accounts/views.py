from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from .models import User
from .forms import LoginForm
from .models import EmailOTP
from .models import generate_otp
from .email import send_otp_email
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import timedelta
from .email import send_otp_email
from .models import EmailOTP
from .models import generate_otp
from django.contrib.auth import logout

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            otp = generate_otp()

            EmailOTP.objects.update_or_create(
                user=user,
                defaults={"otp": otp}
            )

            send_otp_email(user, otp)
            request.session["verify_email"] = user.email

            messages.success(
                request,
                "OTP has been sent to your email."
            )
            
            request.session["verify_email"] = user.email
            
            return redirect("accounts:verify_otp")

        else:

            print(form.errors)

            messages.error(request, form.errors.as_text())

            return render(
                request,
                "accounts/register.html",
                {"form": form}
            )

    else:

        form = RegisterForm()

    return render(request,"accounts/register.html",{"form": form})
    
def login_view(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            email_or_phone = form.cleaned_data["email_or_phone"]
            password = form.cleaned_data["password"]

            # Find user using email or phone

            try:

                if "@" in email_or_phone:

                    user_obj = User.objects.get(
                        email=email_or_phone.lower()
                    )

                else:

                    user_obj = User.objects.get(
                        phone=email_or_phone
                    )

            except User.DoesNotExist:

                messages.error(
                    request,
                    "Invalid email/phone."
                )

                return render(
                    request,
                    "accounts/login.html",
                    {
                        "form": form
                    }
                )

            user = authenticate(
                request,
                email=user_obj.email,
                password=password
            )

            if user is not None:

                if not user.is_email_verified:

                    messages.error(
                        request,
                        "Please verify your email before logging in."
                    )

                    return redirect("accounts:login")

                login(request, user)

                messages.success(
                    request,
                    f"Welcome back, {user.first_name}!"
                )

                return redirect("home")

            else:

                messages.error(
                    request,
                    "Invalid password."
                )

    else:

        form = LoginForm()

    return render(request,"accounts/login.html",{"form": form})


def verify_otp(request):

    if request.method == "POST":

        email = request.session.get("verify_email")

        otp = request.POST.get("otp")

        if not email:

            messages.error(
                request,
                "Session expired. Please register again."
            )

            return redirect("accounts:register")

        user = get_object_or_404(
            User,
            email=email
        )

        try:

            email_otp = EmailOTP.objects.get(
                user=user
            )

        except EmailOTP.DoesNotExist:

            messages.error(
                request,
                "OTP not found."
            )

            return redirect("accounts:register")

        if email_otp.expires_at < timezone.now():

            email_otp.delete()

            messages.error(
                request,
                "OTP expired."
            )

            return redirect("accounts:register")

        if email_otp.otp != otp:

            email_otp.attempts += 1

            email_otp.save()

            messages.error(
                request,
                "Invalid OTP."
            )

            return redirect("accounts:verify_otp")

        user.is_email_verified = True

        user.save()

        email_otp.delete()

        request.session.pop(
            "verify_email",
            None
        )

        messages.success(
            request,
            "Email verified successfully."
        )

        return redirect("accounts:login")

    return render(request,"accounts/verify_otp.html",
    {
        "email": request.session.get("verify_email")
    }
)
    
def resend_otp(request):

    email = request.session.get("verify_email")

    if not email:

        messages.error(request, "Session expired. Please register again.")

        return redirect("accounts:register")

    user = get_object_or_404(User, email=email)

    otp = generate_otp()

    EmailOTP.objects.update_or_create(

        user=user,

        defaults={

            "otp": otp,

            "expires_at": timezone.now() + timedelta(minutes=5),

            "attempts": 0,

        }

    )

    send_otp_email(user, otp)

    messages.success(request, "A new OTP has been sent to your email.")

    return redirect("accounts:verify_otp")



def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get("email").lower()

        try:

            user = User.objects.get(
                email=email
            )

        except User.DoesNotExist:

            messages.error(
                request,
                "No account found with this email."
            )

            return redirect("accounts:forgot_password")

        otp = generate_otp()

        EmailOTP.objects.update_or_create(

            user=user,

            defaults={

                "otp": otp,

                "expires_at": timezone.now() + timedelta(minutes=5),

                "attempts": 0,

            }

        )

        send_otp_email(
            user,
            otp
        )

        request.session["reset_email"] = user.email

        messages.success(
            request,
            "OTP has been sent to your email."
        )

        return redirect(
            "accounts:forgot_password_verify_otp"
        )

    return render(
        request,
        "accounts/forgot_password.html"
    )


def forgot_password_verify_otp(request):

    if request.method == "POST":

        email = request.session.get("reset_email")

        otp = request.POST.get("otp")

        if not email:

            messages.error(
                request,
                "Session expired. Please try again."
            )

            return redirect("accounts:forgot_password")

        user = get_object_or_404(
            User,
            email=email
        )

        try:

            email_otp = EmailOTP.objects.get(
                user=user
            )

        except EmailOTP.DoesNotExist:

            messages.error(
                request,
                "OTP not found."
            )

            return redirect("accounts:forgot_password")

        if email_otp.expires_at < timezone.now():

            email_otp.delete()

            messages.error(
                request,
                "OTP has expired."
            )

            return redirect("accounts:forgot_password")

        if email_otp.otp != otp:

            email_otp.attempts += 1

            email_otp.save()

            messages.error(
                request,
                "Invalid OTP."
            )

            return redirect("accounts:forgot_password_verify_otp")

        email_otp.delete()

        request.session["password_reset_verified"] = True

        return redirect("accounts:reset_password")

    return render(
        request,
        "accounts/verify_otp.html",
        {
            "email": request.session.get("reset_email")
        }
    )


def reset_password(request):

    if not request.session.get("password_reset_verified"):

        return redirect("accounts:forgot_password")

    if request.method == "POST":

        password = request.POST.get("password")

        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("accounts:reset_password")

        user = get_object_or_404(
            User,
            email=request.session.get("reset_email")
        )

        user.set_password(password)

        user.save()

        request.session.pop(
            "reset_email",
            None
        )

        request.session.pop(
            "password_reset_verified",
            None
        )

        messages.success(
            request,
            "Password reset successfully. Please login."
        )

        return redirect("accounts:login")

    return render(
        request,
        "accounts/reset_password.html"
    )
    
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("accounts:login")