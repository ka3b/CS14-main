from django.contrib import admin
from main.models import DataAnalyst, Journey

class JourneyAdmin(admin.ModelAdmin):
    list_display = ('name', 'username')
    list_filter = ('username',)
    exclude = ('name',)
admin.site.register(Journey, JourneyAdmin)

class DataAnalystAdmin(admin.ModelAdmin):
    list_display = ('date', 'driver', 'destination', 'purpose', 'no_of_pass', 'start_time', 'end_time', 'speedo_start', 'speedo_finish')
    list_filter = ('driver', 'start_time', 'end_time')
    exclude = ('destination', 'purpose', 'no_of_pass', 'speedo_start', 'speedo_finish')
admin.site.register(DataAnalyst, DataAnalystAdmin)
