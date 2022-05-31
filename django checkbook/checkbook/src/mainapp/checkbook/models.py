from django.db import models

# Create your models here.
class Account(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    startingBalance = models.DecimalField(max_digits=15, decimal_places=2, max_length=300)

    Accounts = models.Manager()

    def __str__(self):
        return self.firstName + ' ' + self.lastName

transactionTypes = {
    ('withdrawal', 'withdrawal'),
    ('deposit', 'deposit'),
}

class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=15, choices=transactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2, max_length=300)
    description = models.CharField(max_length=300)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()

