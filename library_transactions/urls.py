from django.urls import path
from .views import DepositMoneyView,WithdrawMoneyView,BorrowBook,BorrowBookView,ReturnBookView

urlpatterns = [
    path('deposit/',DepositMoneyView.as_view(),name='deposit_money'),
    path('withdraw/',WithdrawMoneyView.as_view(),name='withdraw_view'),
    path('borrow/book/<int:book_id>/', BorrowBook, name='borrow_book'),
    path('borrowed-books/', BorrowBookView.as_view(), name='borrowed_books'),
    path('return-book/<int:borrowed_book_id>/',ReturnBookView,name='return_book'),
]