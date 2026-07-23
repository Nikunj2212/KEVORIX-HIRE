from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .constants import (
    ROLE_CANDIDATE,
    ROLE_COMPANY,
    ROLE_RECRUITER,
    ROLE_INTERVIEWER,
    ROLE_SUPER_ADMIN,
    LOGIN_URL,
)


def role_required(role):

    def decorator(view_func):

        @login_required(login_url=LOGIN_URL)
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if request.user.role != role:

                messages.error(
                    request,
                    "You are not authorized to access this page."
                )

                return redirect("accounts:access_denied")

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


candidate_required = role_required(ROLE_CANDIDATE)

company_required = role_required(ROLE_COMPANY)

recruiter_required = role_required(ROLE_RECRUITER)

interviewer_required = role_required(ROLE_INTERVIEWER)

super_admin_required = role_required(ROLE_SUPER_ADMIN)


def email_verified_required(view_func):

    @login_required(login_url=LOGIN_URL)
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_email_verified:

            messages.warning(
                request,
                "Please verify your email address."
            )

            return redirect("accounts:verify_otp")

        return view_func(request, *args, **kwargs)

    return wrapper


def profile_completed_required(view_func):

    @login_required(login_url=LOGIN_URL)
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.profile_completed:

            messages.warning(
                request,
                "Please complete your profile."
            )

            return redirect("candidate:profile")

        return view_func(request, *args, **kwargs)

    return wrapper