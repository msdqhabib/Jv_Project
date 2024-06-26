from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, authenticate
from django.views import View
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse
from .models import User, UserRole
from firm.models import Firm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/login.html')

    def post(self, request, *args, **kwargs):
        try:
            email = request.POST.get('email').strip()
            password = request.POST.get('password').strip()
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the dashboard page after successful login
                return redirect('dashboard')

            else:
                # Handle invalid login credentials
                messages.error(request, 'Invalid Username or Password')
                return redirect("login")

        except Exception as e:
            messages.error(request, 'Invalid Username or Passworddd')
            return redirect("login")


class CustomLogoutView(auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect('login')  # Redirect to 'login' URL after logout
