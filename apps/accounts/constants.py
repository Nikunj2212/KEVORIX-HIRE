from .models import UserRole


# ==========================
# USER ROLES
# ==========================

ROLE_CANDIDATE = UserRole.CANDIDATE.value
ROLE_COMPANY = UserRole.COMPANY.value
ROLE_RECRUITER = UserRole.RECRUITER.value
ROLE_INTERVIEWER = UserRole.INTERVIEWER.value
ROLE_SUPER_ADMIN = UserRole.SUPER_ADMIN.value


# ==========================
# DASHBOARD URLS
# ==========================

CANDIDATE_DASHBOARD = "candidate:dashboard"

COMPANY_DASHBOARD = "company:dashboard"

RECRUITER_DASHBOARD = "recruiters:dashboard"

INTERVIEWER_DASHBOARD = "interviewer:dashboard"

SUPER_ADMIN_DASHBOARD = "super_admin:dashboard"


# ==========================
# AUTH URLS
# ==========================

LOGIN_URL = "accounts:login"

LOGOUT_URL = "accounts:logout"

ACCESS_DENIED_URL = "accounts:access_denied"

# ==========================
# PERMISSION KEYS
# ==========================

JOB_CREATE = "jobs.create"

JOB_EDIT = "jobs.edit"

JOB_DELETE = "jobs.delete"

JOB_VIEW = "jobs.view"

CANDIDATE_VIEW = "candidate.view"

CANDIDATE_UPDATE = "candidate.update"

COMPANY_MANAGE = "company.manage"

COMPANY_TEAM = "company.team"

INTERVIEW_MANAGE = "interview.manage"

PLATFORM_MANAGE = "platform.manage"


# ==========================
# ROLE URL PREFIXES
# ==========================

ROLE_URL_PREFIX = {
    ROLE_CANDIDATE: "/candidate/",
    ROLE_COMPANY: "/companies/",
    ROLE_RECRUITER: "/recruiters/",
    ROLE_INTERVIEWER: "/interviewer/",
    ROLE_SUPER_ADMIN: "/super-admin/",
}