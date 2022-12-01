from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Subscription

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class ClockoutForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['user', 'name', 'billing_cycle', 'price', 'start_month',
        'start_day', 'start_year']