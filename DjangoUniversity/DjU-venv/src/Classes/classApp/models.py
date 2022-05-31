from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title =  (models.CharField(max_length=60, default='', blank=True, null=False))
    courseNumber = (models.IntegerField(max_length=20, blank=True, null=False))
    Instructor = (models.CharField(max_length=60, default='', blank=True, null=False))
    Duration = (models.FloatField(max_length=60, blank=True, null=False))

    objects = models.Manager()

