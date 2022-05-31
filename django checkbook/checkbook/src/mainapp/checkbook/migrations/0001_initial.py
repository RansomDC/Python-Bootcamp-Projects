# Generated by Django 4.0.4 on 2022-05-31 00:33

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('startingBalance', models.DecimalField(decimal_places=2, max_digits=15, max_length=300)),
            ],
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default='')),
                ('type', models.CharField(choices=[('desposit', 'deposit'), ('withdrawal', 'withdrawal')], max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkbook.account')),
            ],
            managers=[
                ('Transactions', django.db.models.manager.Manager()),
            ],
        ),
    ]
