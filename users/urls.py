from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthenticationForm


urlpatterns = [

    # path('', HomePageView.as_view(), name='home'),
    # path('', auth_views.LoginView.as_view(
    #     template_name='users/login.html', authentication_form=CustomAuthenticationForm), name='login'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    
    # path('users/', UserListView.as_view(), name='user_list'),

    # # return clicked user details
    # path('user-detail/<int:user_id>/',
    #      UserDetailView.as_view(), name='user-detail'),
    # path('user-update/',
    #      UserUpdateView.as_view(), name='user-update'),


    # path('profile/', ProfileView.as_view(), name='profile'),
]
