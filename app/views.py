from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
# from .forms import NewUserForm
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
    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect("subscribe")
    # form = NewUserForm()
    # return render(
    #     request=request, template_name="signup.html", context={"register_form": form}
    # )

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # group = Group.objects.get(name='not_admin')
            # user.groups.add(group)
            return redirect('login')
    return render(request, 'signup.html', {'form':form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("subscriptions")
    form = AuthenticationForm()
    return render(
        request=request, template_name="login.html", context={"login_form": form}
    )

def logout_request(request):
    logout(request)
    return redirect("subscribe")

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
    if len(my_subs) == 0:
        monthly_total = 0
        yearly_total = 0
        return render(request, "subscriptions.html", 
        {"monthly":monthly_total, 'yearly':yearly_total})
    else:
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

def delete_subscriptions(request, id):
    delete_object = Subscription.objects.get(id=id)
    current_user = request.user
    if current_user == delete_object.user:
        Subscription.objects.get(id=id).delete()
        return HttpResponseRedirect("/subscriptions/")


@login_required
def edit_subscription(request, id):
    form = SubscriptForm()
    edit_object = Subscription.objects.get(id=id)
    current_user = request.user
    if request.method == "POST":
        form = SubscriptForm(request.POST)
        if form.is_valid():
            billing_cycle = form.cleaned_data['billing_cycle']
            price = form.cleaned_data['price']

            edit_object.billing_cycle = billing_cycle
            edit_object.price = price
            edit_object.save()
            return redirect('subscriptions') 
    return render(request, 'edit.html', {'form':form})




def home(request):
    
    return render(request, 'home.html')








     
    

    


