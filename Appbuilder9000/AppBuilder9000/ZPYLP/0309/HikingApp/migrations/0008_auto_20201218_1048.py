# Generated by Django 2.2.5 on 2020-12-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikingApp', '0007_trails_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trails',
            name='image',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]
