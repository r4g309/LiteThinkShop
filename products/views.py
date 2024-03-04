from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Price, Product
from .serializers import PriceSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [AllowAny()]
        elif self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return super().get_permissions()


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [AllowAny()]
        elif self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return super().get_permissions()
