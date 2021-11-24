from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('report-journey/',views.report_journey,name='report_journey'),
    path('journey-details/',views.journey_details,name='journey-details')
]