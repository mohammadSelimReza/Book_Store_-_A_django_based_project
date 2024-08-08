from django.db import models
from library_user.models import UserDetailsModel
from .constrant import TRANSACTION_TYPE
from django.contrib.auth.models import User
from library_book.models import BookModel
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
    
class BorrowedBooksModel(models.Model):
    user=models.ForeignKey(User,related_name='borrowed_books',on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,related_name='borrowed_books',on_delete=models.CASCADE)
    borrowed_date=models.DateTimeField(auto_now_add=True)
    is_borrow = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
    