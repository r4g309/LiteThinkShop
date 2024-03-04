from django.db import models

from categories.models import Category
from company.models import Company


# Create your models here.
class Product(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    characteristics = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="products")

    def __str__(self):
        return f"{self.company.name}: {self.name}"


class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.IntegerField(choices=[(1, "USD"), (2, "EUR"), (3, "COP")])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="prices")

    class Meta:
        unique_together = ("product", "code")

    def __str__(self):
        return f"{self.product.name}:{self.price}-{self.get_code_display()}"
