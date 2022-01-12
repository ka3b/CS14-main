from django.contrib import admin
from .models import DataAnalyst, Journey

class DataAnalystAdmin(admin.ModelAdmin):
    list_display = ('name', 'username')
    list_filter = ('username',)
    exclude = ('name',)
admin.site.register(DataAnalyst, DataAnalystAdmin)

class JourneyAdmin(admin.ModelAdmin):
    list_display = ('date', 'driver', 'get_destinations', 'purpose', 'no_of_pass', 'start_time', 'end_time', 'speedo_start', 'speedo_finish')
    list_filter = ('driver', 'start_time', 'end_time')
    exclude = ('get_destinations', 'purpose', 'no_of_pass', 'speedo_start', 'speedo_finish')
admin.site.register(Journey, JourneyAdmin)
