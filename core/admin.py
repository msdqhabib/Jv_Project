from django.contrib import admin
from core.models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['phase', 'sector', 'dha_location', 'land_type']


admin.site.register(Property, PropertyAdmin)
