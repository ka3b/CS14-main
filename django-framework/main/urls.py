from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('report-journey/',views.report_journey,name='report_journey'),
    path('report-journey/journey-details/',views.journey_details,name='journey_details'),
    path('admin-login/',views.admin_login,name='admin_login'),
    path('admin-login/analysis/',views.analysis,name='analysis'),
    path('admin-login/analysis/dashboard/',views.dashboard,name='dashboard'),
    path('admin-login/analysis/pending-data/',views.pending_data,name='pending_data'),
    path('admin-login/analysis/pending-data/approve/', views.approve_journey, name='approve_journey'),
    path('admin-login/analysis/pending-data/reject/', views.reject_journey, name='reject_journey'), 
    path('admin-login/analysis/analytics/',views.analytics,name='analytics'),
    path('admin-login/analysis/data-table/',views.data_table,name='data_table'),
    path('admin-login/analysis/export-data/',views.export_data,name='export_data'),
    path('admin-login/analysis/account-manager/',views.account_manager,name='account_manager'),
    path('admin-login/',views.logout,name='logout'),

]
