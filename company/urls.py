from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views

router = routers.DefaultRouter()
router.register(r"company", views.CompanyViewSet, "company")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Company API")),
]
