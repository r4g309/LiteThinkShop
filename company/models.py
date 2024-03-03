import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


def validate_nit(nit: str) -> None:
    valid_formats = [r"^\d{9}-\d$", r"^\d{10}$", r"^\d{8}$"]
    parsed_nit = normalize_nit(nit)
    if not any(re.match(regex_exp, parsed_nit) for regex_exp in valid_formats):
        raise ValidationError("Invalid NIT format")


def normalize_nit(nit: str) -> str:
    return re.sub(r"[. ]", "", nit)


def normalize_phone(phone: str) -> str:
    return re.sub(r"[+. ]", "", phone)


class Company(models.Model):
    nit = models.CharField(validators=[validate_nit], primary_key=True)
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=20)
    phone = models.CharField(validators=[RegexValidator(r"^\+?\d{7,12}$", message="Invalid Phone Number")])

    def clean(self):
        self.nit = normalize_nit(self.nit)
        self.phone = normalize_phone(self.phone)
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nit} {self.name}"
