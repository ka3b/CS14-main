from django.contrib import admin
from .models import Journey, Vehicle, Purpose

class JourneyAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'driver', 'plate_number', 'start_location', 'destinations1', 'destinations2', 'destinations3', 'purpose', 'no_of_pass', 'start_time', 'end_time', 'mileage_start', 'mileage_finish', 'approved', 'round_trip')
    list_filter = ('driver', 'start_time', 'end_time', 'plate_number', 'start_location', 'destinations1', 'destinations2', 'destinations3', 'purpose', 'no_of_pass', 'mileage_start', 'mileage_finish')
    exclude = ()
admin.site.register(Journey, JourneyAdmin)

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'plate_number')
    list_filter = ('vehicle_type', 'plate_number')
    exclude = ()
admin.site.register(Vehicle, VehicleAdmin)

class PurposeAdmin(admin.ModelAdmin):
    list_display = ('purpose',)
    list_filter = ('purpose',)
    exclude = ()
admin.site.register(Purpose, PurposeAdmin)
