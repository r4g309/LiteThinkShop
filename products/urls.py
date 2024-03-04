from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"products", views.ProductViewSet, "company")
router.register(r"prices", views.PriceViewSet, "price")

urlpatterns = [path("", include(router.urls))]
