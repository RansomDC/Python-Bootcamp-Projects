from django.shortcuts import render
from django.http import HttpResponse

#This allows us to use Profiles from the models app
from . import views
from .models import Profiles


def home(request):
    users = Profiles.objects.all()
    print("hello")
    return render(request, "home.html", {'user': users})

