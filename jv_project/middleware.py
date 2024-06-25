# jv_project/middleware.py

from django.shortcuts import redirect
from django.urls import reverse_lazy


class LogoutRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path != reverse_lazy('login') and request.path != reverse_lazy('register-firm'):
            return redirect('login')
        response = self.get_response(request)
        return response
