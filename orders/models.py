from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    currency_code = models.IntegerField(choices=[(1, "USD"), (2, "EUR"), (3, "COP")], default=3)

    def calculate_total(self):
        return sum(item.calculate_subtotal(self.currency_code) for item in self.order_items.all())

    def __str__(self):
        formatted_date = self.created_at.strftime("%d/%m/%Y")
        return f"{self.client.username} - {self.id} / {formatted_date} - {self.calculate_total()}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def calculate_subtotal(self, currency_code: int):
        price_in_currency = self.product.get_price_in_currency(currency_code)
        if price_in_currency is None:
            raise ValueError("Price not found")
        return price_in_currency * self.quantity

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
