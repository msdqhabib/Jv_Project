from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('lister_dashboard/', views.lister_dashboard, name='lister_dashboard'),
    path('firm_dashboard/', views.firm_dashboard, name='firm_dashboard'),
]
