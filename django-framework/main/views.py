from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import *
# Create your views here.
def index(request):
    return render(request, "main/index.html")

def report_journey(request):
    return render(request, "main/journey/report-journey.html")

def journey_details(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JourneyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cleaned_form = form.cleaned_data

            journey = Journey.objects.get_or_create(driver=cleaned_form['driver'], start_date=cleaned_form['start_date'],
            end_date=cleaned_form['end_date'],destinations=cleaned_form['destinations'],
            purpose=cleaned_form['purpose'], plate_number=cleaned_form['plate_number'],
            no_of_pass=cleaned_form['no_of_pass'],start_time=cleaned_form['start_time'],
            end_time=cleaned_form['end_time'], speedo_start=cleaned_form['mileage_start'],
            speedo_finish=cleaned_form['mileage_finish'], round_trip=cleaned_form['is_round_trip'])[0]

            journey.save()
            # redirect to a new URL:
            return HttpResponse('Thanks')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = JourneyForm()

    return render(request,"main/journey/journey-details.html", {'form': form})

def admin_login(request):
    return render(request,"main/analytics/admin-login.html")

def analysis(request):
    return render(request,"main/analytics/analysis.html")

def analytics(request):
    return render(request,"main/analytics/analytics.html")

def account_manager(request):
    return render(request,"main/analytics/account-manager.html")

def dashboard(request):
    return render(request,"main/analytics/dashboard.html")

def data_table(request):
    return render(request,"main/analytics/data-table.html")

def export_data(request):
    return render(request,"main/analytics/export-data.html")

def pending_data(request):
    return render(request,"main/analytics/pending-data.html")

def logout(request):
    return render(request,"main/analytics/logout.html")
