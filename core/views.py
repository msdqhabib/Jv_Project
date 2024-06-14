from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    role_name = request.user.role.role_name
    # Default to 'base.html' if no layout is specified
    layout = request.GET.get('layout', 'base.html')  
    
    if role_name == 'admin':
        return admin_dashboard(request, layout)
    elif role_name == 'lister':
        return lister_dashboard(request, layout)
    elif role_name == 'firm':
        return firm_dashboard(request, layout)
    else:
        return render(request, 'base.html')

def admin_dashboard(request, layout):
    # Admin-specific logic here
    return render(request, 'core/admin_dashboard.html', {'layout': layout})

def lister_dashboard(request, layout):
    # Lister-specific logic here
    return render(request, 'lister_dashboard.html', {'layout': layout})

def firm_dashboard(request, layout):
    # Firm-specific logic here
    return render(request, 'firm_dashboard.html', {'layout': layout})
