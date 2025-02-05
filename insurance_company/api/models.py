from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


def validate_expiry_date(value):
    if value < date.today():
        raise ValidationError("Expiry date cannot be in the past.")

class Policy(models.Model):
    POLICY_TYPES = [
       ('auto', 'Auto'),
       ('home', 'Home'),
    ]
    policy_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    policy_type = models.CharField(max_length=10, choices=POLICY_TYPES)
    expiry_date = models.DateField(validators=[validate_expiry_date])

    def __str__(self):
       return f"{self.customer_name} - {self.policy_type}"