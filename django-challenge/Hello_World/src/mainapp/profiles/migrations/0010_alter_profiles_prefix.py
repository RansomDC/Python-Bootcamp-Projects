# Generated by Django 4.0.4 on 2022-05-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20220524_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Sirmaam', 'Sirmaam'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Mr.', 'Mr.')], max_length=10),
        ),
    ]