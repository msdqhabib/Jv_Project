from django.contrib import admin
from .models import User,UserRole

admin.site.register(User)


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['role_name']

admin.site.register(UserRole, UserRoleAdmin)