from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #Anatomy of a URL route: (<pattern to watch for>, <method to call>, <shortcut name>)
    #When the "name" parameter is called it knows to go to views and get the function (e.g. views.details), which will change the url to the appripriate page
    path('', views.home, name="index"),
    path('create/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction'),
]