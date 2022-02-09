from django.test import TestCase
from django.urls import resolve



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
            