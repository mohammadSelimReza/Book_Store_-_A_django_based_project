from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, View
from django.db import models
from .models import TransactionModel
from .forms import DepositForm, WithdrawForm
from .constrant import DEPOSIT,WITHDRAWAL
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
from django.urls import reverse_lazy
from library_user.models import UserDetailsModel
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transaction_form.html'
    model = TransactionModel
    title = ''
    success_url = reverse_lazy('home')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account,
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })
        return context
        
class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = "Deposit"

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        print("Form is valid")
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        print(f"Initial Balance: {account.balance}")
        print(f"Deposit Amount: {amount}")
        account.balance += amount
        print(f"Updated Balance: {account.balance}")
        account.save(update_fields=['balance'])
        messages.success(self.request, f"{amount}$ was deposited to your account successfully.")
        mail_subject = "Deposit Message"
        message = render_to_string('email_msg.html',{
            'user': self.request.user,
            'amount': amount,
        })
        to_email = self.request.user.email
        send_email = EmailMessage(mail_subject,message,to=[to_email])
        send_email.send()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = "Withdraw"
    
    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        total_balance = UserDetailsModel.objects.aggregate(total_balance=models.Sum('balance'))['total_balance']
        if total_balance is None or total_balance < amount:
            messages.error(self.request,f"The bank is bankrupt")
            return redirect('homePage')
        
        account.balance -= amount
        account.save(update_fields=['balance'])
        messages.success(self.request, f"{amount}$ was withdrawn from your account successfully.")
        return super().form_valid(form)
