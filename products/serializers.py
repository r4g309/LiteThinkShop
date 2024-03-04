from rest_framework import serializers

from .models import Price, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("code", "name", "characteristics", "company")


class PriceSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["code"] = instance.get_code_display()
        return data

    class Meta:
        model = Price
        fields = ("code", "price", "product")
