from django.contrib import admin
from .models import Firm


class FirmAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_ntn', 'company_email', 'business_type', 'company_website','poc_name','status']

admin.site.register(Firm, FirmAdmin)