import json

from django.core import serializers
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import *
from .models import Journey, Vehicle, Purpose
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.http import JsonResponse
import datetime
from django.db.models import Count
import csv
from django.contrib import messages

import matplotlib.pyplot as plt
import urllib
import base64
import io
import numpy as np

# Create your views here.

testMode = False
def returnTestMode(x):
    return testMode

def my_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    if testMode == False:
        actual_decorator = user_passes_test(
            lambda u: u.is_authenticated,
            login_url=login_url,
            redirect_field_name=redirect_field_name
        )
    else:
        actual_decorator = user_passes_test(
            returnTestMode,
            login_url=login_url,
            redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator



def index(request):
    return redirect('main/report-journey/journey-details')

@my_login_required
def analytics(request):


    current_date = datetime.date.today()
    week_ago_date = current_date - datetime.timedelta(days=6)
    cur_date = current_date.strftime("%b %d")
    week_ago = week_ago_date.strftime("%b %d")
    weeks_journeys = Journey.objects.filter(start_date__range=[week_ago_date, current_date], approved=True)

    average_miles = 0
    total_miles = 0
    for journey in weeks_journeys:
        journey.miles()
        total_miles += journey.total_miles
    if (weeks_journeys.count() > 0):
        average_miles = round(total_miles / weeks_journeys.count())


    x_freq = []
    y_freq = []
    x_purp = []
    y_purp = []
    x_dest = []
    y_dest = []
    x_mpurp = []
    y_mpurp = []

    for i in range(7):
        date = week_ago_date + datetime.timedelta(days=i+1)
        current_date = date
        x_freq.append(current_date.strftime("%b %d"))
        y_freq.append(weeks_journeys.filter(start_date=date).count())

    journeys_purpose = weeks_journeys.filter(approved=True).values_list('purpose').annotate(journey_count=Count('purpose')).order_by('-journey_count')
    if journeys_purpose.count() > 0:
        counter = 0
        other = 0
        for j in journeys_purpose:
            if counter < 3:
                counter+=1;
                x_purp.append(j[0])
                y_purp.append(j[1])
            else:
                other += j[1]
        x_purp.append("Other")
        y_purp.append(other)

    destinations = {}
    for journey in weeks_journeys:
        if not journey.destinations1 in destinations and journey.destinations1 != None:
            destinations[journey.destinations1] = 1
        elif journey.destinations1 != None:
            destinations[journey.destinations1] += 1

        if not journey.destinations2 in destinations and journey.destinations2 != None:
            destinations[journey.destinations2] = 1
        elif journey.destinations2 != None:
            destinations[journey.destinations2] += 1

        if not journey.destinations3 in destinations and journey.destinations3 != None:
            destinations[journey.destinations3] = 1
        elif journey.destinations3 != None:
            destinations[journey.destinations3] += 1

    larg_vals = sorted(destinations, key=destinations.get, reverse=True)[:5]
    destination = {}
    for val in larg_vals:
        destination[val] = destinations.get(val)

    vehicles_reg = {}
    vehicles = {}
    for journey in weeks_journeys:
        if not journey.plate_number in vehicles_reg:
            vehicles_reg[journey.plate_number] = 1
        else:
            vehicles_reg[journey.plate_number] += 1


    types = Vehicle.objects.all()
    for reg in vehicles_reg.keys():
        for type in types:
            if type.plate_number == reg:
                if not reg in vehicles.keys():
                    vehicles[type.vehicle_type] = vehicles_reg[reg]
                else:
                    vehicles[type.vehicle_type] += vehicles_reg[reg]

    if (len(vehicles.values()) > 0):
        max_value = max(vehicles.values())
        total_v_miles = sum(vehicles.values())
        vehs = list(vehicles.keys())[list(vehicles.values()).index(max_value)]
        percent = round(max_value/total_v_miles, 3) * 100
    else:
        vehs = "All vehicle"
        percent = 0


    miles = {}
    for journey in weeks_journeys:
        if not journey.purpose in miles:
            miles[journey.purpose] = journey.total_miles
        else:
            miles[journey.purpose] += journey.total_miles

    #Graph for frequency
    plt.figure(figsize=(8, 32))
    plt.subplot(5,1,1)
    plt.bar(x_freq,y_freq, color='lightgreen')
    plt.title('Journeys Per Day', fontsize=25, pad=20)
    plt.xlabel('Date')
    plt.ylabel('Number of visits')

    #Graph for purpose
    plt.subplot(5,1,2)
    plt.title('Journeys Per Purpose', fontsize=25, pad=20)
    plt.xlabel('Purpose')
    plt.ylabel('Number of journeys')
    plt.bar(x_purp,y_purp, color='lightblue')
    plt.xticks(x_purp)


    #Destinations
    x_dest = destination.keys()
    y_dest = destination.values()
    plt.subplot(5,1,3)
    plt.title('Visits To Each Destination', fontsize=25, pad=20)
    plt.xlabel('Destination')
    plt.ylabel('Number of visits')
    plt.bar(x_dest,y_dest, color='orange', alpha=0.5)
    


    #Miles for purpose
    x_mpurp = miles.keys()
    y_mpurp = miles.values()
    plt.subplot(5,1,4)
    plt.title('Miles Travelled Per Purpose', fontsize=25, pad=20)
    plt.xlabel('Purpose')
    plt.ylabel('Miles travelled')
    plt.bar(x_mpurp,y_mpurp, color='purple', alpha=0.5)


    #Vehicle types
    plt.subplot(5,1,5)
    plt.title('Vehicle Usage', fontsize=25, pad=20)
    x_type = vehicles.keys()
    y_type = vehicles.values()
    [float(i) for i in y_dest]
    explode = []
    [explode.append(0.1) for i in x_type]
    plt.pie(y_type, shadow=True, explode = explode)
    plt.legend(labels = x_type, loc="lower right", 
                          bbox_transform=plt.gcf().transFigure)



  

    fig = plt.gcf()

    buf = io.BytesIO()
    fig.patch.set_alpha(0)
    fig.subplots_adjust(hspace=.5)
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    dests = urllib.parse.quote(string)


    if (len(miles.values()) > 0):
        all_values = miles.values()
        max_value = max(all_values)
        purpose = list(miles.keys())[list(miles.values()).index(max_value)]
    else:
        max_value = 0
        purpose = "none"


    context_dict = {}
    context_dict['average_miles'] = average_miles
    context_dict['total_miles'] = total_miles
    context_dict['purpose_miles'] = max_value
    context_dict['purpose_purpose'] = purpose
    context_dict['percent'] = percent
    context_dict['vehs'] = vehs
    context_dict['graphs'] = dests

    return render(request,"main/analytics/analytics.html", context=context_dict)


def report_journey(request):
    return render(request, "main/journey/report-journey.html")


def journey_details(request):
    form = JourneyForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = JourneyForm(data=request.POST)
        print(form.errors)
        context_dict = {}
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cleaned_form = form.cleaned_data

            if not form.errors:
                journey = \
                Journey.objects.get_or_create(driver=cleaned_form['driver'], start_date=cleaned_form['start_date'],
                                              end_date=cleaned_form['end_date'],
                                              purpose=cleaned_form['purpose'],
                                              plate_number=cleaned_form['plate_number'],
                                              start_location=cleaned_form['start_location'],
                                              destinations1=cleaned_form['destinations1'],
                                              destinations2=cleaned_form['destinations2'],
                                              destinations3=cleaned_form['destinations3'],
                                              no_of_pass=cleaned_form['no_of_pass'],
                                              start_time=cleaned_form['start_time'],
                                              end_time=cleaned_form['end_time'],
                                              mileage_start=cleaned_form['mileage_start'],
                                              mileage_finish=cleaned_form['mileage_finish'],
                                              round_trip=cleaned_form['is_round_trip'])[0]
                journey.save()
                # redirect to a new URL:
                return redirect('main:report_journey')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = JourneyForm()

    return render(request, "main/journey/journey-details.html", {'form': form})

@my_login_required
def dashboard(request):
    pending = Journey.objects.filter(approved=False).count()
    current_date = datetime.date.today()
    week_ago_date = current_date - datetime.timedelta(days=6)
    cur_date = current_date.strftime("%b %d")
    week_ago = week_ago_date.strftime("%b %d")
    weeks_journeys = Journey.objects.filter(start_date__range=[week_ago_date, current_date], approved=True)
    reported_journeys = weeks_journeys.count()
    average_miles = 0
    common_purpose = None
    for journey in weeks_journeys:
        journey.miles()
        average_miles += journey.total_miles
    if (reported_journeys > 0):
        average_miles = round(average_miles / reported_journeys)
        common_purpose = Journey.objects.filter(approved=True).values_list('purpose').annotate(journey_count=Count('purpose')).order_by('-journey_count')[0][0]

    context_dict = {}
    context_dict['pending'] = pending
    context_dict['cur_date'] = cur_date
    context_dict['week_ago'] = week_ago
    context_dict['reported_journeys'] = reported_journeys
    context_dict['average_miles'] = average_miles
    context_dict['common_purpose'] = common_purpose
    return render(request, "main/analytics/dashboard.html", context=context_dict)


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                # Signs the user in with the details supllied once they create an account
                auth_login(request, user)
                return redirect(reverse("main:dashboard"))
            else:
                return HttpResponse("Your account has been disabled.")

        else:
            return HttpResponse("Incorrect username or password.")

    else:
        return render(request, 'main/admin/admin-login.html')

@my_login_required
def analysis(request):
    return render(request, "main/analytics/analysis.html")




# def account_manager(request):
#    return render(request,"main/analytics/account-manager.html")
@my_login_required
def data_table(request):
    order_by = request.GET.get('order_by', '-start_date')
    journeys = Journey.objects.filter(approved=True).order_by(order_by)
    context_dict = {}
    context_dict['journeys'] = journeys
    return render(request, "main/analytics/data-table.html", context=context_dict)

@my_login_required
def export_data(request):
    return render(request, "main/analytics/export-data.html")

@my_login_required
def export_data_file(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="TransportServices.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Start Date', 'End Date', 'Driver', 'Plate Number', 'Start Location', 'First Destination',
                     'Second Destination',
                     'Third Destination', 'Purpose', 'Number of Passengers', 'Start Time', 'End Time',
                     'Starting Mileage', 'Ending Mileage', 'Round Trip?'])

    journeys = Journey.objects.filter(approved=True)
    for journey in journeys:
        writer.writerow(
            [journey.start_date, journey.end_date, journey.driver, journey.plate_number, journey.start_location,
             journey.destinations1, journey.destinations2, journey.destinations3, journey.purpose, journey.no_of_pass,
             journey.start_time, journey.end_time, journey.mileage_start, journey.mileage_finish, journey.round_trip])

    return response

@my_login_required
def pending_data(request):
    order_by = request.GET.get('order_by', 'start_date')
    journeys = Journey.objects.filter(approved=False).order_by(order_by)
    for journey in journeys:
        journey.update_vehicle_type()
        journey.miles()
        journey.save()
    context_dict = {}
    context_dict['journeys'] = journeys
    return render(request, "main/analytics/pending-data.html", context=context_dict)

@my_login_required
def approve_journey(request):
    data = {'success': False}
    if request.method == 'POST':
        id = request.POST.get('id')
        journey = Journey.objects.get(id=id)
        journey.approved = True
        journey.save()
        data = {'success': True}

    return JsonResponse(data)

@my_login_required
def reject_journey(request):
    data = {'success': False}
    if request.method == 'POST':
        id = request.POST.get('id')
        Journey.objects.filter(id=id).delete()
        data = {'success': True}

    return JsonResponse(data)


@my_login_required
def logout(request):
    print(1)
    auth_logout(request)
    return render(request, "main/admin/admin-login.html")
