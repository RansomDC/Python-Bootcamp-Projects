# Generated by Django 2.1.5 on 2022-05-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220523_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Ms.', 'Ms.'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Sirmaam', 'Sirmaam')], max_length=10),
        ),
    ]