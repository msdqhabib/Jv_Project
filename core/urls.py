from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('lister_dashboard/', views.lister_dashboard, name='lister_dashboard'),
    path('firm_dashboard/', views.firm_dashboard, name='firm_dashboard'),

    # properties routes
    path('properties', views.PropertyListView.as_view(), name='property-list'),
    path('property/<int:pk>/', views.PropertyDetailView.as_view(), name='property-detail'),
    path('property/new/', views.PropertyCreateView.as_view(), name='property-create'),
    path('property/<int:pk>/edit/', views.PropertyUpdateView.as_view(), name='property-edit'),
    path('property/<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='property-delete'),

    # Meetings
    path('meetings/', views.MeetingListView.as_view(), name='meeting-list'),

    
    

]



