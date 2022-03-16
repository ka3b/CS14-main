import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_services_server.settings')

import django
django.setup()

import datetime
from main.models import Journey, Vehicle
from django.contrib.auth.models import User
from django.core.files import File

def populate():

    if not User.objects.filter(username='Viola').exists():
        user=User.objects.create_user('Viola', password='63JsRy')
        user.is_superuser=True
        user.is_staff=True
        user.save()

    if not User.objects.filter(username='Grant').exists():
        user=User.objects.create_user('Grant', password='QhR7Lu')
        user.is_superuser=True
        user.is_staff=True
        user.save()

    if not User.objects.filter(username='Jennifer').exists():
        user=User.objects.create_user('Jennifer', password='j29wUg')
        user.is_superuser=True
        user.is_staff=True
        user.save()


if __name__ == '__main__':
    print("Starting setup script...")
    populate()
    print("Finished populating")
