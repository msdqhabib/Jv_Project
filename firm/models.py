from django.db import models
from users.models import User
from django.utils import timezone
from datetime import datetime


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
        ('Verified', 'Verified'),
        ('Approved_by_DHA', 'Approved_by_DHA'),
        ('Approved_by_GHQ', 'Approved_by_GHQ'),
    )

    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default='Pending', blank=True)
    status_history = models.JSONField(default=list, null=True, blank=True)

    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    
    def firm_status_change(self, status):
        timestamp = datetime.now()
        timestamp = timestamp.strftime('%d:%m:%Y %H:%M:%S')

        # Check if status already exists in property_status_history
        status_exists = any(
            entry['status'] == status for entry in self.status_history)

        if not status_exists:
            self.status_history.append({'status': status,
                                                'timestamp': timestamp})
            self.save()

