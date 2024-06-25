from django.contrib import admin
from core.models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['phase', 'sector', 'dha_location','type_of_land']
admin.site.register(Property, PropertyAdmin)