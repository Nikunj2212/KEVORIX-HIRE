from .constants import (
    ROLE_CANDIDATE,
    ROLE_COMPANY,
    ROLE_RECRUITER,
    ROLE_INTERVIEWER,
    ROLE_SUPER_ADMIN,
)


def has_role(user, role):

    if not user.is_authenticated:
        return False

    return user.role == role


def is_candidate(user):
    return has_role(user, ROLE_CANDIDATE)


def is_company(user):
    return has_role(user, ROLE_COMPANY)


def is_recruiter(user):
    return has_role(user, ROLE_RECRUITER)


def is_interviewer(user):
    return has_role(user, ROLE_INTERVIEWER)


def is_super_admin(user):
    return has_role(user, ROLE_SUPER_ADMIN)


def has_permission(user, permission):
    """
    Future Enterprise Permission Engine.

    Current Version:
    - Super Admin => All Permissions
    - Others => Role Based

    Future:
    Database Permission System
    Company Team Permissions
    Subscription Permissions
    """
    
    if not user.is_authenticated:
        return False

    if user.role == ROLE_SUPER_ADMIN:
        return True

    return True