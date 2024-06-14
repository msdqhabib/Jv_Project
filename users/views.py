from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.views import View
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse
from .models import User




class RegisterView(View):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully. You can now log in.')
            return redirect('login')
        else:
            # If form data is invalid, display error messages
            messages.error(
                request, f'Failed to create account. Please enter correct details')
            return render(request, self.template_name, {'form': form})

