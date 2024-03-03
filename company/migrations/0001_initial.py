# Generated by Django 5.0.2 on 2024-03-03 22:54

import django.core.validators
from django.db import migrations, models

import company.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "nit",
                    models.CharField(
                        primary_key=True,
                        serialize=False,
                        validators=[company.models.validate_nit],
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("direction", models.CharField(max_length=20)),
                (
                    "phone",
                    models.CharField(
                        validators=[
                            django.core.validators.RegexValidator("^\\+?\\d{7,12}$", message="Invalid Phone Number")
                        ]
                    ),
                ),
            ],
        ),
    ]