from django.db import models
from django.contrib.auth.models import User

class DataAnalyst(models.Model):
    name = models.CharField(max_length=128, unique=False)
    username = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Journey(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    driver = models.CharField(max_length=128, unique=False)
    destination = models.CharField(max_length=128, unique=False)
    purpose = models.CharField(max_length=50, unique=False)
    no_of_pass = models.IntegerField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    speedo_start = models.IntegerField()
    speedo_finish = models.IntegerField()

    #class Meta:
    #    unique_together = ((date_of_journey, driver), )

    def miles(self):
        return self.speedo_finish - self.speedo_start

    def __str__(self):
        return self.driver, self.destination


#class Admin(models.Model):
    
