from django.test import TestCase
from rest_framework.test import APIClient

from .models import Category


# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(
            name="test",
            description="test",
        )

    def test_get_category(self):
        response = self.client.get("/category/")
        self.assertEqual(response.status_code, 200)

    def test_create_category(self):
        response = self.client.post(
            "/category/",
            {
                "name": "test1",
                "description": "test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_update_category(self):
        response = self.client.put(
            f"/category/{self.category.name}/",
            {
                "name": "test",
                "description": "test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_category(self):
        response = self.client.delete(f"/category/{self.category.name}/")
        self.assertEqual(response.status_code, 204)
