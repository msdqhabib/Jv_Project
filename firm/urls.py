from django.urls import path
from . import views

urlpatterns = [
    path('register-firm/', views.FirmCreateView.as_view(), name='register-firm'),
    path('resend-verification/', views.resend_verification_email, name='resend_verification_email'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('faqs', views.faqs, name='faqs'),
]
