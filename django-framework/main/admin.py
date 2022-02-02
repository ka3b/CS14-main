from django.contrib import admin
from .models import DataAnalyst, Journey

class DataAnalystAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'username')
    list_filter = ('username',)
    exclude = ('name', 'user')
admin.site.register(DataAnalyst, DataAnalystAdmin)

class JourneyAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'driver', 'start_location', 'destinations1', 'destinations2', 'destinations3', 'purpose', 'no_of_pass', 'start_time', 'end_time', 'mileage_start', 'mileage_finish', 'approved', 'round_trip')
    list_filter = ('driver', 'start_time', 'end_time', 'start_location', 'destinations1', 'destinations2', 'destinations3', 'purpose', 'no_of_pass', 'mileage_start', 'mileage_finish')
    exclude = ()
admin.site.register(Journey, JourneyAdmin)

class Vehicle(admin.ModelAdmin):
    list_display = ('vehicle_type', 'plate_number')
    list_filter = ('vehicle_type', 'plate_number')
    exclude = ()
admin.site.register(Vehicle, VehicleAdmin)
