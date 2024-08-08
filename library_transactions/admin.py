from django.contrib import admin
from .models import TransactionModel,BorrowedBooksModel
# Register your models here.
admin.site.register(TransactionModel)
admin.site.register(BorrowedBooksModel)