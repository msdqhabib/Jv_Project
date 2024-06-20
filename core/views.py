from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


@login_required
def dashboard(request):
    role_name = request.user.role.role_name
    # Default to 'base.html' if no layout is specified
    
    if role_name == 'admin':
        return admin_dashboard(request)
    elif role_name == 'lister':
        return lister_dashboard(request)
    elif role_name == 'firm':
        return firm_dashboard(request)
    else:
        return render(request, 'base.html')

def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

def lister_dashboard(request):
    return render(request, 'lister_dashboard.html')

def firm_dashboard(request):
    return render(request, 'firm_dashboard.html')


