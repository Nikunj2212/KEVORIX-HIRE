from django.urls import reverse

from .constants import (
    ROLE_CANDIDATE,
    ROLE_COMPANY,
    ROLE_RECRUITER,
    ROLE_INTERVIEWER,
    ROLE_SUPER_ADMIN,
    CANDIDATE_DASHBOARD,
    COMPANY_DASHBOARD,
    RECRUITER_DASHBOARD,
    INTERVIEWER_DASHBOARD,
    SUPER_ADMIN_DASHBOARD,
    LOGIN_URL,
)


ROLE_DASHBOARD_MAP = {
    ROLE_CANDIDATE: CANDIDATE_DASHBOARD,
    ROLE_COMPANY: COMPANY_DASHBOARD,
    ROLE_RECRUITER: RECRUITER_DASHBOARD,
    ROLE_INTERVIEWER: INTERVIEWER_DASHBOARD,
    ROLE_SUPER_ADMIN: SUPER_ADMIN_DASHBOARD,
}


def get_dashboard_url(user):

    if not user.is_authenticated:
        return LOGIN_URL

    return ROLE_DASHBOARD_MAP.get(
        user.role,
        LOGIN_URL,
    )


def get_dashboard_redirect(user):

    return reverse(
        get_dashboard_url(user)
    )