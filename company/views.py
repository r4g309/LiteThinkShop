from rest_framework import permissions, viewsets

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    # TODO: Update permissions to allow only authenticated users
    permission_classes = [permissions.AllowAny]
