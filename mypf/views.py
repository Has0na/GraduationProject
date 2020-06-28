from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Contact
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
# Create your views here.

def logIn(request):
    if request.method == 'POST':
       return render(request, 'mypf/portfolio.html')

# Home/Index View
def index(request):
    # check post method and request type
    if request.method == 'POST'and request.is_ajax():
        # check for empty name field
        if request.POST['name'] == "":
            username = "Jane Doe"   # set default name
        else:
            username = request.POST['name']
        # check for select field
        if request.POST['gender'] == "Select":
            gender = "f"
        else:
            gender = request.POST['gender']
        # return name and gender to success in ajax call top update content
        return HttpResponse(json.dumps({'name': username, 'gender': gender}))
    else:
        return render(request, 'mypf/home.html')


# Portfolio View
def portfolio(request):
    return render(request, 'mypf/portfolio.html')


# Contact View
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(email=email, subject=subject, message=message)
        # Saving Form data to Database
        form.save()

        return render(request, 'mypf/contact.html')
    else:
        return render(request, 'mypf/contact.html')
