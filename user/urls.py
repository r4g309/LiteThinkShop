from django.urls import path

from user import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("logout", views.logout_user, name="logout"),
]
