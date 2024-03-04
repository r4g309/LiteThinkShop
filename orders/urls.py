from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"main-order", views.OrderViewSet, "order-main")
router.register(r"item-order", views.OrderItemViewSet, "order-item")

urlpatterns = [path("", include(router.urls))]
