#Allows us to use the render function which will send the data from our view to the webpage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


#This allows us to use Profiles from the models app
from . import views
from profiles.views import Profiles
from .forms import ProfileForm



def home(request):
    users = Profiles.objects.all()
#    print(users)
#    for user in users:
#        print(user)
    return render(request, "home.html", {'users': users})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profiles, pk=pk)
    form = ProfileForm(data=request.POST or None, instance = item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form. save(commit=False)
            form2.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        return render(request, 'present_profile.html', {'form': form})

def addProfile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print(form.errors)
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'addProfile.html', context)

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profiles, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    context = {"item": item,}
    return render(request, "confirmDelete.html", context)

def confirmed(request):
    if request.method == 'POST':
        #creates a form instance and binds data to it
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('home')
    else:
        return redirect('home')