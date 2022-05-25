from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views
from .models import Profiles
from .views import home

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()