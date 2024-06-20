from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.ForeignKey('UserRole', on_delete=models.SET_NULL, null=True, blank=True)

class UserRole(models.Model):
    role_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.role_name
        
