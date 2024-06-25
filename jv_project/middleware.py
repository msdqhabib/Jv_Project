from django.shortcuts import redirect
from django.urls import reverse

class LogoutRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Exclude certain paths from redirection
            excluded_paths = [reverse('login'), reverse('register-firm')]
            
            # Check if the current path is not in excluded paths and doesn't contain 'activate'
            if not any(request.path.startswith(path) for path in excluded_paths) and 'activate' not in request.path:
                # Redirect to the login page if the user is not authenticated
                return redirect('login')

        # Continue processing the request
        response = self.get_response(request)
        return response
