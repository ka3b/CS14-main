import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_services_server.settings')

import django
django.setup()

import datetime
from main.models import DataAnalyst, Journey
from django.contrib.auth.models import User
from django.core.files import File

def populate():

    #need unique identifier for journeys
    journeys = [
        {
            'date' : datetime.date.today,
            'driver' : "Chris",
            'destination' : "Vet School",
            'purpose' : "Supplies",
            'no_of_pass' : "2",
            'start_time' : datetime.time(hour=1, minute=1),
            'end_time' : datetime.time(hour=2, minute=10),
            'speedo_start': 12000,
            'speedo_finish' : 12004
        },
        {           
            'date' : datetime.date(2020, 6, 11),
            'driver' : "Joe",
            'destination' : "Vet School",
            'purpose' : "Travel People",
            'no_of_pass' : "0",
            'start_time' : datetime.time(hour=10, minute=15),
            'end_time' : datetime.time(hour=11, minute=00),
            'speedo_start': 12004,
            'speedo_finish' : 12010
        },
        {           
            'date' : datetime.date(2021, 4, 22),
            'driver' : "Vet School",
            'destination' : "Vet School",
            'purpose' : "Supplies",
            'no_of_pass' : "1",
            'start_time' : datetime.time(hour=20, minute=0),
            'end_time' : datetime.time(hour=21, minute=0),
            'speedo_start': 16010,
            'speedo_finish' : 16042
        },
        {           
            'date' : datetime.date(2020, 5, 24),
            'driver' : "Olivia",
            'destination' : "Main",
            'purpose' : "Supplies",
            'no_of_pass' : "4",
            'start_time' : datetime.time(hour=12, minute=00),
            'end_time' : datetime.time(hour=12, minute=45),
            'speedo_start': 100400,
            'speedo_finish' : 100402
        }
    ]

    data_analysts = [
        {
            'name' : "John Smith",
            'username' : "JohnSmith4"
        },
        {
            'name' : "Barry Pete",
            'username' : "BigBarry"
        },
        {
            'name' : "Mohammed",
            'username' : "CoolMan123"
        }
    ]


    for p in data_analysts:
        add_analyst(p["username"], p["name"])

    for p in journeys:
        add_journey(p["driver"])


def add_analyst(username, name):
    analyst = DataAnalyst.objects.get_or_create(username=username, name=name)[0]
    analyst.save()
    return analyst

def add_journey(driver):
    journey = Journey.objects.get_or_create(driver=driver)[0]
    journey.save()
    return journey


if __name__ == '__main__':
    print("Starting population script...")
    populate()
