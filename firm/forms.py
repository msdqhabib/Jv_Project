from django import forms
from .models import Firm

class FirmRegistrationForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields = ['company_name', 'company_ntn', 'company_email', 'business_type', 'company_website', 'company_phone_no',
                  'owner_name', 'owner_cnic', 'owner_nationality', 'owner_phone_no','owner_address','owner_email',
                  'poc_name', 'poc_phone_no', 'poc_email', 'poc_address', 'status']
