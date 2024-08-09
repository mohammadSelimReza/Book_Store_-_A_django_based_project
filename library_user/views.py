from django.shortcuts import render,redirect
from django.views import generic
from .forms import RegistrationForm,UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
# Create your views here.
class UserRegistrationView(UserPassesTestMixin,generic.FormView):
    template_name = 'user_form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user=form.save()
        messages.success(self.request,'Account has been created succesfully.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors,flush=True)
        return super().form_invalid(form)
    
    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return redirect('home')
    
    
class UserLoginView(UserPassesTestMixin,LoginView):
    template_name = 'user_login.html'
    form_class = AuthenticationForm
    def get_success_url(self):
        return reverse_lazy('home')
    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return redirect('home')
    
class UserLogoutView(LoginRequiredMixin,LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            messages.success(self.request,'Logged Out')
            logout(self.request)
        return reverse_lazy('home')
    
class UserProfileUpdate(LoginRequiredMixin, generic.View):
    form_class = UpdateUserForm
    template_name = 'user_profile.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = request.user
            user_details = user.account
            initial_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'gender': user_details.gender,
                'birth_date': user_details.birth_date,
                'address': user_details.address,
                'country': user_details.country,
                'account_no': user_details.account_no,
            }
            form = self.form_class(initial=initial_data)
            return render(request, self.template_name, {'form': form})
        return reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(self.request, self.template_name, {'form': form})