from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title =  (models.CharField(max_length=60, default='', blank=True, null=False))
    courseNumber = (models.CharField(max_length=20, default='', blank=True, null=False))
    Instructor = (models.CharField(max_length=60, default='', blank=True, null=False))
    Duration = (models.CharField(max_length=60, default='', blank=True, null=False))

    objects = models.Manager()

