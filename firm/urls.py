from django.urls import path
from . import views

urlpatterns = [
    path('register-firm/', views.FirmCreateView.as_view(), name='register-firm'),
]
