from django.conf import settings
from django.core.mail import send_mail


def send_otp_email(user, otp):

    subject = "Verify Your Email - KEVORIX Hire"

    message = f"""
Hi {user.first_name},

Welcome to KEVORIX Hire!

Your Email Verification OTP is:

{otp}

This OTP is valid for 5 minutes.

If you did not create this account, please ignore this email.

Thanks,
KEVORIX Hire Team
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )