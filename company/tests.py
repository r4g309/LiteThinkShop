from django.test import TestCase
from rest_framework.test import APIClient


class CompanyTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_company(self):
        response = self.client.get("/api/v1/company/")
        self.assertEqual(response.status_code, 200)

    def test_add_company(self):
        response = self.client.post(
            "/api/v1/company/",
            {
                "nit": "1234567890",
                "name": "Company",
                "phone": "1234567",
                "direction": "Calle 123",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_update_company(self):
        response = self.client.put(
            "/api/v1/company/1234567890/",
            {
                "nit": "1234567890",
                "name": "Company",
                "phone": "1234567",
                "direction": "Calle 123",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_company(self):
        response = self.client.delete("/api/v1/company/1234567890/")
        self.assertEqual(response.status_code, 204)
