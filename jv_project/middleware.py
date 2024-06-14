from django.shortcuts import redirect
from django.urls import reverse


class LogoutRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is authenticated
        if not request.user.is_authenticated and request.path != reverse('login') and request.path != reverse('register'):
            # Redirect to the login page if the user is not authenticated
            return redirect('login')

        return response
