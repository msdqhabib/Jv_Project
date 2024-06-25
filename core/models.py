# models.py
from django.db import models


class Property(models.Model):
    phase = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    dha_location = models.CharField(max_length=500)

    map_lat = models.DecimalField(max_digits=9, decimal_places=6)
    map_long = models.DecimalField(max_digits=9, decimal_places=6)

    LAND_TYPE_CHOICES = (
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Semi Commercial', 'Semi Commercial'),
    )

    land_type = models.CharField(max_length=250, choices=LAND_TYPE_CHOICES)

    detail_of_project = models.TextField()
    total_land = models.DecimalField(max_digits=10, decimal_places=2)
    land_unit = models.CharField(max_length=100)
    percentage_shareholding = models.DecimalField(
        max_digits=5, decimal_places=2)
    feasibility_of_project = models.TextField()
    land_price_to_be_paid_to_dha = models.DecimalField(
        max_digits=10, decimal_places=2)
    project_monitoring_team = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phase
