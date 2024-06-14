from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from users.models import User


class UserRegistrationForm(UserCreationForm):
    phone = forms.CharField(required=True, max_length=50)
    city = forms.CharField(required=True, max_length=250)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Remove help text for username
        
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].help_text = None
        self.fields['password2'].label = 'Confirm Password'


        # Set username as required and change the label
        self.fields['username'].help_text = None
        self.fields['username'].label = 'Username'
        self.fields['username'].required = True


        # Set first_name as required and change the label
        self.fields['first_name'].label = 'First Name'
        self.fields['first_name'].required = True
        

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email Address", widget=forms.EmailInput)

