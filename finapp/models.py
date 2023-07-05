from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

class TransactionsByUser(models.Model):
    @staticmethod
    def transactionsSum(user):
        amountSum = Transactions.objects.filter(user=user).aggregate(Sum('amount'))
        return amountSum['amount__sum'] or 0
    
    def userTransactions(user):
        userTransactions = Transactions.objects.filter(user=user)
        return userTransactions

class Transactions(models.Model):
    # Columns required for a transaction history + associated to specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    vendor = models.CharField(max_length=80)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.user)