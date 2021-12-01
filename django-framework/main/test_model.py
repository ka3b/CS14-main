from django.test import TestCase
from django.urls import resolve



class UrlMappingTest(TestCase):

    def test_all_url_are_present(self):
        test_urls = [
            '/main/report-journey/',
            '/main/report-journey/journey-details/',
            '/main/admin-login/analysis/',
            '/main/admin-login/dashboard/',
            '/main/admin-login/pending-data/',
            '/main/admin-login/analytics/',
            '/main/admin-login/data-table/',
            '/main/admin-login/export-data/',
            '/main/admin-login/account-manager/',
            '/main/admin-login/logout/',
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
            'account_manager',
            'logout',
            'admin_login'
            ]
        for url in test_urls:
                self.assertEqual()
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
            