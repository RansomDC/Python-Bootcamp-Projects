# Generated by Django 2.1.5 on 2022-05-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20220523_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Mr.', 'Mr.'), ('Sirmaam', 'Sirmaam')], max_length=10),
        ),
    ]
