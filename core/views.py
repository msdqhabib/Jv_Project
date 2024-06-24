from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# models imports
from firm.models import Firm
from users.models import User


@login_required
def dashboard(request):
    role_name = request.user.role.role_name
    # Default to 'base.html' if no layout is specified
    print(role_name)
    if role_name == 'admin':
        return admin_dashboard(request)
    elif role_name == 'Listers':
        return lister_dashboard(request)
    elif role_name == 'Firms':
        return firm_dashboard(request)
    else:
        return render(request, 'base.html')

def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

def lister_dashboard(request):
    return render(request, 'lister_dashboard.html')

def firm_dashboard(request):
    user = User.objects.get(username=request.user.username)
    firm_instance = Firm.objects.filter(user=user).last()
    status_history = firm_instance.status_history
    
    # Create a dictionary of statuses with their timestamps
    status_history = {entry['status'].replace('-', '_'): entry['timestamp']
        for entry in firm_instance.status_history}

    context = {
        'firm': firm_instance,
        'status_history': status_history,
    }
    return render(request, 'firm/firm_dashboard.html', context)


