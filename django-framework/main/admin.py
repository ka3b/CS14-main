from django.contrib import admin
from .models import DataAnalyst, Journey

class DataAnalystAdmin(admin.ModelAdmin):
    list_display = ('name', 'username')
    list_filter = ('username',)
    exclude = ('name',)
admin.site.register(DataAnalyst, DataAnalystAdmin)

class JourneyAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'driver', 'destinations', 'purpose', 'no_of_pass', 'start_time', 'end_time', 'mileage_start', 'mileage_finish')
    list_filter = ('driver', 'start_time', 'end_time')
    exclude = ('destinations', 'purpose', 'no_of_pass', 'mileage_start', 'mileage_finish')
admin.site.register(Journey, JourneyAdmin)
