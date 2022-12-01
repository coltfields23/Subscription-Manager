from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from .forms import NewUserForm
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from app.forms import *
# from .decorators import admin_only, customer_only
from .models import Subscription
from decimal import Decimal


# Auth views
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("subscribe")
    form = NewUserForm()
    return render(
        request=request, template_name="signup.html", context={"register_form": form}
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("subscription")
    form = AuthenticationForm()
    return render(
        request=request, template_name="login.html", context={"login_form": form}
    )

def logout_request(request):
    logout(request)
    return redirect("CreateTask")

def subscribe(request):
    form = SubscriptForm()
    if request.method == 'POST':
        form = SubscriptForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Subscription Saved!')
    return render(request, 'create.html', {'form':form})


def mysubscripts(request):
    my_subs = Subscription.objects.filter(user=request.user)
    total_monthly = 0
    for subs in my_subs:
        total_monthly += subs.price
    yearly_price = total_monthly * 12
    var = Subscription.objects.filter(user=request.user)
    for new_var in var:
        total = new_var.price * Decimal(yearly_price)
        grand_total = "{:.2f}".format(total)
        if new_var.billing_cycle == "Monthly":
            monthly_total = new_var.price
            monthly_total = "{:.2f}".format(monthly_total)
        elif new_var.billing_cycle == "Yearly":
            monthly_total = new_var.price / 12
            monthly_total = "{:.2f}".format(monthly_total)
    return render(request, "subscriptions.html", {'my_subs':my_subs,
    'monthly':total_monthly, 'yearly':yearly_price, 'grand':grand_total,
    'monthly_total':monthly_total,})
     
    

    


