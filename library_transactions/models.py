from django.db import models
from library_user.models import UserDetailsModel
from .constrant import TRANSACTION_TYPE
class TransactionModel(models.Model):
    account = models.ForeignKey(UserDetailsModel, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Transaction {self.id}: {self.get_transaction_type_display()} of {self.amount} on {self.timestamp}"
