from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    billing_cycle = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    start_month = models.CharField(max_length=10, default="January")
    start_day = models.CharField(max_length=10, default="1")
    start_year = models.CharField(max_length=10, default="2022")