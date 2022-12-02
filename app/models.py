from django.contrib.auth.models import User
from django.db import models

# Create your models here.

cycle_choices = [
    ('Monthly','Monthly'), ('Yearly','Yearly')
]

month_choices = [
    ('Jan','Jan'), ('Feb','Feb'),
    ('March','Mar'), ('April','April'),
    ('May','May'), ('June','June'),
    ('July','July'), ('Aug','Aug'),
    ('Sept','Sept'), ('Oct','Oct'),
    ('Nov','Nov'), ('Dec','Dec'),
]






class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=20, blank=True)
    billing_cycle = models.CharField(max_length=20, choices=cycle_choices, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=4, blank=True)
    start_month = models.CharField(max_length=10, default="Jan", choices=month_choices, blank=True)
    start_day = models.CharField(max_length=10, default="1", blank=True)
    start_year = models.CharField(max_length=10, default="2022", blank=True)
    

    