from django.test import TestCase
from rest_framework.test import APIClient

from .models import Company, Price, Product


class CompanyTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_product(self):
        response = self.client.get("/product/products/")
        self.assertEqual(response.status_code, 200)

    def test_add_product(self):
        company = Company.objects.create(
            nit="1234567890",
            name="Company",
            phone="1234567",
            direction="Calle 123",
        )
        response = self.client.post(
            "/product/products/",
            {
                "code": 1234567890,
                "name": "Product",
                "characteristics": "Characteristics",
                "company": company.nit,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_update_product(self):
        company = Company.objects.create(
            nit="1234567890",
            name="Company",
            phone="1234567",
            direction="Calle 123",
        )
        product = Product.objects.create(
            code=1234567890,
            name="Product",
            characteristics="Characteristics",
            company=company,
        )
        response = self.client.put(
            f"/product/products/{product.code}/",
            {
                "code": 1234567890,
                "name": "Product",
                "characteristics": "Characteristics",
                "company": company.nit,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        company = Company.objects.create(
            nit="1234567890",
            name="Company",
            phone="1234567",
            direction="Calle 123",
        )
        product = Product.objects.create(
            code=1234567890,
            name="Product",
            characteristics="Characteristics",
            company=company,
        )
        response = self.client.delete(f"/product/products/{product.code}/")
        self.assertEqual(response.status_code, 204)

    def test_get_price(self):
        response = self.client.get("/product/prices/")
        self.assertEqual(response.status_code, 200)

    def test_add_price(self):
        company = Company.objects.create(
            nit="1234567890",
            name="Company",
            phone="1234567",
            direction="Calle 123",
        )
        product = Product.objects.create(
            code=1234567890,
            name="Product",
            characteristics="Characteristics",
            company=company,
        )
        response = self.client.post(
            "/product/prices/",
            {
                "price": 1000,
                "code": 1,
                "product": product.code,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_update_price(self):
        company = Company.objects.create(
            nit="1234567890",
            name="Company",
            phone="1234567",
            direction="Calle 123",
        )
        product = Product.objects.create(
            code=1234567890,
            name="Product",
            characteristics="Characteristics",
            company=company,
        )
        price = Price.objects.create(
            price=1000,
            code=1,
            product=product,
        )
        response = self.client.put(
            f"/product/prices/{price.id}/",
            {
                "price": 1000,
                "code": 1,
                "product": product.code,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_price(self):
        company = Company.objects.create(
            nit="1234567890",
            name="Company",
            phone="1234567",
            direction="Calle 123",
        )
        product = Product.objects.create(
            code=1234567890,
            name="Product",
            characteristics="Characteristics",
            company=company,
        )
        price = Price.objects.create(
            price=1000,
            code=1,
            product=product,
        )
        response = self.client.delete(f"/product/prices/{price.id}/")
        self.assertEqual(response.status_code, 204)
