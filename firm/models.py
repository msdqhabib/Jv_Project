from django.db import models
from users.models import User


class Firm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_ntn = models.CharField(max_length=255, blank=True, null=True)
    company_email = models.EmailField(unique=True)
    business_type = models.CharField(max_length=255)
    company_website = models.CharField(max_length=255, blank=True, null=True)
    company_phone_no = models.CharField(max_length=255)

    owner_name = models.CharField(max_length=255)
    owner_cnic = models.CharField(max_length=255)
    owner_nationality = models.CharField(max_length=255, blank=True, null=True)
    owner_phone_no = models.CharField(max_length=255, blank=True, null=True)
    owner_address = models.TextField(null=True, blank=True)
    owner_email = models.EmailField(unique=True)


    poc_name = models.CharField(max_length=255, blank=True, null=True)
    poc_phone_no = models.CharField(max_length=255, blank=True, null=True)
    poc_email = models.EmailField(unique=True)
    poc_address = models.TextField(blank=True, null=True)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved by DHA', 'Approved by DHA'),
        ('Approved by Admin', 'Approved by Admin'),
    )

    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default='Pending', blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
