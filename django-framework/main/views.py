from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def report_journey(request):
    return render(request, "main/report-journey.html")

def journey_details(request):
    return render(request,"main/journey-details.html")