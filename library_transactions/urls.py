from django.urls import path
from .views import DepositMoneyView,WithdrawMoneyView

urlpatterns = [
    path('deposit/',DepositMoneyView.as_view(),name='deposit_money'),
    path('withdraw/',WithdrawMoneyView.as_view(),name='withdraw_view'),
]