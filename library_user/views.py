from django.shortcuts import render
from django.views import generic
from .forms import RegistrationForm
from django.urls import reverse_lazy
# Create your views here.
class UserRegistrationView(generic.FormView):
    template_name = 'user_form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self, form):
        user=form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors,flush=True)
        return super().form_invalid(form)