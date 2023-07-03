from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transactions(models.Model):
    #Column as required for a transaction history + associated to specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()
    vendor = models.CharField(max_length=80)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    amountSum = TransactionsSum()

    def __str__(self):
        return self.user

class TransactionsSum(models.Model):
    def transactionsSum(self, user):
        amountSum = Transactions.user
        return amountSum