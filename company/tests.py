from django.test import TestCase
from rest_framework.test import APIClient

from .models import Company


class CompanyTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_company(self):
        response = self.client.get("/company/")
        self.assertEqual(response.status_code, 200)

    def test_add_company(self):
        response = self.client.post(
            "/company/",
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

        company = Company.objects.create(
            nit="1234567890",
            name="Existing Company",
            phone="1234567",
            direction="Calle 123",
        )
        response = self.client.put(
            f"/company/{company.nit}/",
            {
                "nit": "1234567890",
                "name": "Company",
                "phone": "1234567",
                "direction": "Calle 123",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)

    #
    def test_delete_company(self):
        company = Company.objects.create(
            nit="1234567890",
            name="Existing Company",
            phone="1234567",
            direction="Calle 123",
        )
        response = self.client.delete(f"/company/{company.nit}/")
        self.assertEqual(response.status_code, 204)
