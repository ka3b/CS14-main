from django.db import models
from django.contrib.auth.models import User

class DataAnalyst(models.Model):
    name = models.CharField(max_length=128, unique=False)
    username = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

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
    destinations = models.CharField(max_length=256, null=True, blank=False)
    purpose = models.CharField(max_length=50, unique=False, blank=False)
    no_of_pass = models.IntegerField(blank=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    mileage_start = models.IntegerField(blank=False)
    mileage_finish = models.IntegerField(blank=False)
    approved = models.BooleanField(default=False)
    round_trip = models.BooleanField(default=False)

    #class Meta:
    #    unique_together = ((date_of_journey, driver), )

    def miles(self):
        return self.mileage_finish - self.mileage_start

    def __str__(self):
        return self.driver, self.destination

    def get_destinations(self):
        return destinations.split(" | ")



#class Admin(models.Model):
