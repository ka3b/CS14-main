from django.urls import resolve
import os
import re
import datetime
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from main.models import *
from main import form

from django.contrib.auth.models import User
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}MGG TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class UrlMappingTest(TestCase):

    def test_all_url_are_present(self):
        test_urls = [
            '/main/report-journey/',
            '/main/report-journey/journey-details/',
            '/main/admin-login/analysis/',
            '/main/admin-login/analysis/dashboard/',
            '/main/admin-login/analysis/pending-data/',
            '/main/admin-login/analysis/analytics/',
            '/main/admin-login/analysis/data-table/',
            '/main/admin-login/analysis/export-data/',
            '/main/admin-login/'
        ]
        test_resolvers = [
            'report_journey',
            'journey_details',
            'analysis',
            'dashboard',
            'pending_data',
            'analytics',
            'data_table',
            'export_data',
            'admin_login'
            ]
        for url in test_urls:

                response = self.client.get(url)
                self.assertEqual(response.status_code, 200, msg=url)

                import os


class ProjectStructureTests(TestCase):
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.main_templates_dir = os.path.join(self.templates_dir, 'main')
        self.main_dir = os.path.join(self.project_base_dir, 'main')
        self.project_dir = os.path.join(self.project_base_dir, 'transport_services_server')

    def test_directories_exists(self):
        directory_exists = os.path.isdir(self.templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Template directory does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isdir(self.main_templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Templates folder does not contain folder main.{FAILURE_FOOTER}")
        directory_exists = os.path.isdir(self.main_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Project folder transport_services_server does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isdir(self.project_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Application folder main does not exist.{FAILURE_FOOTER}")

    def test_app_files_exist(self):
        directory_exists = os.path.isfile(os.path.join(self.main_dir, 'admin.py'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}admin.py file does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_dir, 'form.py'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}form.py file does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_dir, 'models.py'))        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}models.py file does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_dir, 'urls.py'))      
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}urls.py file does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_dir, 'views.py'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}views.py file does not exist.{FAILURE_FOOTER}")

    def test_templates_files_exist(self):
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'base.html'))      
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}base.html page does not exist.{FAILURE_FOOTER}")

    def test_admin_templates_files_exist(self):
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'admin/admin-login.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}admin-login.html page does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'admin/base.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}base.html page does not exist.{FAILURE_FOOTER}")

    def test_analytics_templates_files_exist(self):
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'analytics/dashboard.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}dashboard.html page does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'analytics/account-manager.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}account-manager.html page does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'analytics/analysis.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}analysis.html page does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'analytics/base.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}base.html page does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'analytics/data-table.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}data-table.html page does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'analytics/export-data.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}export-data.html page does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'analytics/pending-data.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}pending-data.html page does not exist.{FAILURE_FOOTER}")

    def test_journey_templates_files_exist(self):
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'journey/journey-details.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}journey-details.html page does not exist.{FAILURE_FOOTER}")
        directory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'journey/base.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}base.html page does not exist.{FAILURE_FOOTER}")
        irectory_exists = os.path.isfile(os.path.join(self.main_templates_dir, 'journey/report-journey.html'))     
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}report-journey.html page does not exist.{FAILURE_FOOTER}")


    def test_main_has_urls_module(self):
        module_exists = os.path.isfile(os.path.join(self.project_dir, 'urls.py'))
        self.assertTrue(module_exists, f"{FAILURE_HEADER}The app's urls.py module is missing. You need two urls.py modules.{FAILURE_FOOTER}")
        

class DashboardViewsTests(TestCase):
    def setUp(self):
        self.main_module = importlib.import_module('main.views')
        self.main_module_listing = dir(self.main_module) 
        self.project_urls_module = importlib.import_module('transport_services_server.urls')
        self.response = self.client.get(reverse('main:dashboard'))

    def test_dashboard_view_exists(self):
        name_exists = 'dashboard' in self.main_module_listing
        is_callable = callable(self.main_module.dashboard)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}The dashboard() view does not exist.{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}The dashboard view cannot be called.{FAILURE_FOOTER}")

    def test_mappings_exists(self):
        self.assertEquals(reverse('main:dashboard'), '/main/admin-login/analysis/dashboard/', f"{FAILURE_HEADER}The dashboard URL lookup failed.{FAILURE_FOOTER}")

    def test_response(self):
        self.assertEqual(self.response.status_code, 200, f"{FAILURE_HEADER}Requesting the dashboard page failed.{FAILURE_FOOTER}")
        self.assertContains(self.response, 'dashboard', msg_prefix=f"{FAILURE_HEADER}The dashboard view does not return the expected response.{FAILURE_FOOTER}")

    def test_dashboard_uses_template(self):
        self.assertTemplateUsed(self.response, 'main/analytics/dashboard.html', f"{FAILURE_HEADER}Your dashboard() view does not use the expected dashboard.html template.{FAILURE_FOOTER}")
        self.assertTemplateUsed(self.response, 'main/analytics/base.html', f"{FAILURE_HEADER}Your dashboard() view does not use the expected dashboard.html template.{FAILURE_FOOTER}")

    def test_dashboard_starts_with_doctype(self):
        self.assertTrue(self.response.content.decode().startswith('<!DOCTYPE html>'), f"{FAILURE_HEADER}dashboard.html template does not start with <!DOCTYPE html>.{FAILURE_FOOTER}")


class JourneyDetailsViewsTests(TestCase):
    def setUp(self):
        self.main_module = importlib.import_module('main.views')
        self.main_module_listing = dir(self.main_module) 
        self.project_urls_module = importlib.import_module('transport_services_server.urls')
        self.response = self.client.get(reverse('main:journey_details'))

    def test_journey_details_view_exists(self):
        name_exists = 'journey_details' in self.main_module_listing
        is_callable = callable(self.main_module.journey_details)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}The journey_details() view does not exist.{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}The journey_details view cannot be called.{FAILURE_FOOTER}")

    def test_mappings_exists(self):
        self.assertEquals(reverse('main:journey_details'), '/main/report-journey/journey-details/', f"{FAILURE_HEADER}The journey_details URL lookup failed.{FAILURE_FOOTER}")

    def test_response(self):
        self.assertEqual(self.response.status_code, 200, f"{FAILURE_HEADER}Requesting the journey_details page failed.{FAILURE_FOOTER}")
        self.assertContains(self.response, 'journey-details', msg_prefix=f"{FAILURE_HEADER}The journey-details view does not return the expected response.{FAILURE_FOOTER}")

    def test_journey_details_uses_template(self):
        self.assertTemplateUsed(self.response, 'main/journey/journey-details.html', f"{FAILURE_HEADER}Your journey-details() view does not use the expected journey_details.html template.{FAILURE_FOOTER}")
        self.assertTemplateUsed(self.response, 'main/journey/base.html', f"{FAILURE_HEADER}Your journey-details() view does not use the expected journey_details.html template.{FAILURE_FOOTER}")

    def test_journey_details_starts_with_doctype(self):
        self.assertTrue(self.response.content.decode().startswith('<!DOCTYPE html>'), f"{FAILURE_HEADER}journey_details.html template does not start with <!DOCTYPE html>.{FAILURE_FOOTER}")



class TransportServicesModelsTests(TestCase):
    def setUp(self):  
        user = User.objects.get_or_create(username='Grantt',password='CS14')

        Journey.objects.get_or_create(start_date=datetime.date.today(),
                                        end_date=datetime.date.today(),
                                        driver="Joe",
                                        start_location="Uni",
                                        destinations1="Shops",
                                        destinations2="City centre",
                                        destinations3=None,
                                        purpose="Travel People",
                                        plate_number="AB70DHD",
                                        no_of_pass=0,
                                        start_time=datetime.time(hour=10, minute=15),
                                        end_time=datetime.time(hour=11, minute=00),
                                        mileage_start=12004,
                                        mileage_finish=12010,
                                        approved=False,
                                        round_trip=True)

        Vehicle.objects.get_or_create(vehicle_type="Car", plate_number="AB70DHD")
        
    def test_Journey_model(self):
        j = Journey.objects.get(mileage_start='12004', plate_number='AB70DHD')
        self.assertEqual(j.start_date, datetime.date.today(), f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.end_date, datetime.date.today(), f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.driver, 'Joe', f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.start_location, 'Uni', f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.destinations1, 'Shops', f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.destinations2, 'City centre', f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.destinations3, None, f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.purpose, 'Travel People', f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.no_of_pass, 0, f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.start_time, datetime.time(hour=10, minute=15), f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.end_time, datetime.time(hour=11, minute=00), f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.mileage_finish, 12010, f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.approved, False, f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")
        self.assertEqual(j.round_trip, True, f"{FAILURE_HEADER}Tests on the Journey model failed.{FAILURE_FOOTER}")

    def test_Vehicle_model(self):
        v = Vehicle.objects.get(plate_number="AB70DHD")
        self.assertEqual(v.vehicle_type, "Car", f"{FAILURE_HEADER}Tests on the vehicle model failed.{FAILURE_FOOTER}")
        self.assertEqual(v.plate_number, "AB70DHD", f"{FAILURE_HEADER}Tests on the vehicle model failed.{FAILURE_FOOTER}")



class test_population_script(TestCase):
    def setUp(self):
        try:
            import population_script
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}Could not import the population script. Check it's in the right location.{FAILURE_FOOTER}")         
        if 'populate' not in dir(population_script):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist.{FAILURE_FOOTER}")         
        population_script.populate()    

    def test_journeys_instances(self):
        journeys = Journey.objects.filter()
        journeys_len = len(journeys)
        journeys_purp = Journey.objects.filter(purpose="Supplies")
        self.assertEqual(journeys_len, 6, f"{FAILURE_HEADER}Expecting 6 journeys in the population script; found {journeys_len}.{FAILURE_FOOTER}")
        self.assertTrue(journeys_purp.count()>0, f"{FAILURE_HEADER}No instance of a journey with 'Supplies' as the purpose exists{FAILURE_FOOTER}")        