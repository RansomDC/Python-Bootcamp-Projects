# Generated by Django 2.2.5 on 2021-07-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBAstats', '0004_auto_20210722_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerDatabase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('playerName', models.CharField(max_length=60)),
                ('defRebs', models.IntegerField(default=0)),
                ('steals', models.IntegerField(default=0)),
                ('blocks', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
    ]
