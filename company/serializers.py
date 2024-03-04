from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Company
        fields = ("nit", "name", "phone", "direction", "products")
