from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# models imports
from firm.models import Firm
from users.models import User
from core.models import Property


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
    return render(request, 'core/lister_dashboard.html')

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


# Properties View Logic
class PropertyListView(ListView):
    model = Property
    template_name = 'core/property_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_value = self.request.GET.get('filter')
        if filter_value and filter_value != 'all':
            queryset = queryset.filter(dha_location=filter_value)
        # else:
        return queryset

    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            properties = self.get_queryset().values('type_of_land', 'phase', 'total_land', 'land_unit', 'percentage_shareholding', 'id')
            return JsonResponse(list(properties), safe=False)
        return super().get(request, *args, **kwargs)

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'core/property_detail.html'

class PropertyCreateView(CreateView):
    model = Property
    fields = '__all__'
    template_name = 'core/property_form.html'
    success_url = reverse_lazy('property-list')

class PropertyUpdateView(UpdateView):
    model = Property
    fields = '__all__'
    template_name = 'core/property_form.html'
    success_url = reverse_lazy('property-list')

class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'core/property_confirm_delete.html'
    success_url = reverse_lazy('property-list')


# Meetins View
class MeetingListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/meetings.html')
