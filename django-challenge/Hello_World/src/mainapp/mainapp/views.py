#Allows us to use the render function which will send the data from our view to the webpage
from django.shortcuts import render
from django.http import HttpResponse


#This allows us to use Profiles from the models app
from . import views
from profiles.views import Profiles



def home(request):
    users = Profiles.objects.all()
    print(users)
    for user in users:
        print(user)
    return render(request, "home.html", {'user': users})
