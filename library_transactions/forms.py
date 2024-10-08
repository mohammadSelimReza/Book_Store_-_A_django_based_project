from typing import Any
from django import forms
from .models import TransactionModel
from library_user.models import UserDetailsModel
class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['amount','transaction_type']
        
    def __init__(self,*args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()
        
    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
    
    
class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data["amount"]
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount}$'
            )
        
        return amount
    
class WithdrawForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance
        amount = self.cleaned_data["amount"]
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f"You have to withdraw at least {min_withdraw_amount}$"
            )
        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f"You can not withdraw more that {max_withdraw_amount}$ at a time."
            )
        if amount > balance:
            raise forms.ValidationError(
                f"You have {balance}$ in your account."
            )
        return amount
