from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username="test",
            email="b@mail.com",
            password="test",
            first_name="test",
            last_name="test",
        )

    def test_create_user(self):
        response = self.client.post(
            "/register",
            {
                "username": "rage",
                "email": "b@mail.com",
                "password": "1234",
                "first_name": "Brayan",
                "last_name": "Cortes",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        response = self.client.post(
            "/register",
            {
                "username": "user10",
                "email": "b@mail.com",
                "password": "1234",
                "first_name": "User",
                "last_name": "Test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            "/login",
            {
                "username": "user10",
                "password": "1234",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.client.post(
            "/register",
            {
                "username": "user10",
                "email": "b@mail.com",
                "password": "1234",
                "first_name": "User",
                "last_name": "Test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        user_tk = response.data.get("token")
        response = self.client.get("/profile", headers={"Authorization": f"Token {user_tk}"})
        self.assertEqual(response.status_code, 200)

    #
    def test_logout_user(self):
        response = self.client.post(
            "/register",
            {
                "username": "user10",
                "email": "b@mail.com",
                "password": "1234",
                "first_name": "User",
                "last_name": "Test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        user_tk = response.data.get("token")
        response = self.client.get("/logout", headers={"Authorization": f"Token {user_tk}"})
        self.assertEqual(response.status_code, 200)
