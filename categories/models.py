from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
