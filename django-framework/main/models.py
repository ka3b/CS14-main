from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=20, unique=False)
    plate_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.plate_number


class Journey(models.Model):
    start_date = models.DateField(auto_now=False, auto_now_add=False, default=None, blank=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False, default=None, blank=False)
    driver = models.CharField(max_length=128, unique=False, blank=False)
    plate_number = models.CharField(max_length=20, unique=False, blank=False)
    start_location = models.CharField(max_length=256, null=True, blank=False)
    destinations1 = models.CharField(max_length=256, null=True, blank=False)
    destinations2 = models.CharField(max_length=256, null=True, blank=True)
    destinations3 = models.CharField(max_length=256, null=True, blank=True)
    purpose = models.CharField(max_length=50, unique=False, blank=False)
    no_of_pass = models.IntegerField(blank=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    mileage_start = models.IntegerField(blank=False)
    mileage_finish = models.IntegerField(blank=False)
    approved = models.BooleanField(default=False)
    round_trip = models.BooleanField(default=False)
    vehicle_type = models.CharField(null=True, blank=True, max_length=50)
    total_miles = models.IntegerField(blank=True, null=True)

    #class Meta:
    #    unique_together = ((date_of_journey, driver), )

    def miles(self):
        self.total_miles = self.mileage_finish - self.mileage_start

    def __str__(self):
        return self.driver+self.destinations1

    def get_destinations(self):
        return destinations.split(" | ")

    def update_vehicle_type(self):
        if not Vehicle.objects.filter(plate_number=self.plate_number).exists():
            self.vehicle_type = "Unknown"
        else:
            vehicle = Vehicle.objects.get(plate_number=self.plate_number)
            self.vehicle_type = vehicle.vehicle_type 
