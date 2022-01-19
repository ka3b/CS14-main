from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import *
from .models import DataAnalyst, Journey
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "main/index.html")

def report_journey(request):
    return render(request, "main/journey/report-journey.html")

def journey_details(request):

    form = JourneyForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = JourneyForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cleaned_form = form.cleaned_data

            journey = Journey.objects.get_or_create(driver=cleaned_form['driver'], start_date=cleaned_form['start_date'],
            end_date=cleaned_form['end_date'],destinations=cleaned_form['destinations'],
            purpose=cleaned_form['purpose'], plate_number=cleaned_form['plate_number'],
            no_of_pass=cleaned_form['no_of_pass'],start_time=cleaned_form['start_time'],
            end_time=cleaned_form['end_time'], mileage_start=cleaned_form['mileage_start'],
            mileage_finish=cleaned_form['mileage_finish'], round_trip=cleaned_form['is_round_trip'])[0]

            journey.save()
            # redirect to a new URL:
            return HttpResponse('Successfully reported your journey!')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = JourneyForm()

    return render(request,"main/journey/journey-details.html", {'form': form})

def admin_login(request):
    if request.method == 'POST':       
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:          

            if user.is_active:   
                #Signs the user in with the details supllied once they create an account             
                auth_login(request, user)
                return render(request,'main/analytics/dashboard.html')
            else:             
                return HttpResponse("Your account is disabled.")

        else:          
            return HttpResponse("Incorrect username or password.")
        
    else:
        return render(request, 'main/analytics/admin-login.html')

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
