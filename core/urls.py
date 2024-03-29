"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

from utils.generate_pdf import download_pdf, send_mail_pdf

urlpatterns = [
    path("admin/", admin.site.urls),
    path("company/", include("company.urls")),
    path("product/", include("products.urls")),
    path("category/", include("categories.urls")),
    path("order/", include("orders.urls")),
    path("docs/", include_docs_urls(title="Company API")),
    path("generate_pdf/", download_pdf),
    path("send_mail/<str:email>", send_mail_pdf),
    path("", include("user.urls")),
]
