from django.shortcuts import render
from django.http import HttpResponse
#test fixed or not
# Create your views here.
def index(request):
    return render(request, "main/index.html")

def report_journey(request):
    return render(request, "main/report-journey.html")

def journey_details(request):
    return render(request,"main/journey-details.html")

def admin_login(request):
    return render(request,"main/admin-login.html")

def analysis(request):
    return render(request,"main/analysis.html")

def analytics(request):
    return render(request,"main/analytics.html")

def account_manager(request):
    return render(request,"main/account-manager.html")

def dashboard(request):
    return render(request,"main/dashboard.html")

def data_table(request):
    return render(request,"main/data-table.html")

def export_data(request):
    return render(request,"main/export-data.html")

def pending_data(request):
    return render(request,"main/pending-data.html")

def logout(request):
    return render(request,"main/admin-login.html")