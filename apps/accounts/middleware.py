from django.shortcuts import redirect

from .constants import (
    ROLE_URL_PREFIX,
)
from .redirects import get_dashboard_url


class RoleAccessMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:
            

            allowed_prefix = ROLE_URL_PREFIX.get(request.user.role)

            protected_prefixes = tuple(ROLE_URL_PREFIX.values())

            current_path = request.path
            
            if current_path.startswith(protected_prefixes):

                if not current_path.startswith(allowed_prefix):

                    return redirect(get_dashboard_url(request.user))

        response = self.get_response(request)

        return response