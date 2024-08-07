from django.shortcuts import render,redirect
from django.views import generic
from .forms import RegistrationForm,UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
class UserRegistrationView(generic.FormView):
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
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    form_class = AuthenticationForm
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            messages.success(self.request,'Logged Out')
            logout(self.request)
        return reverse_lazy('home')
    
class UserProfileUpdate(generic.View):
    form_class = UpdateUserForm
    template_name = 'user_profile.html'
    
    def get(self,request,*args, **kwargs):
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
        return render(request,self.template_name,{'form':form})
    
    def post(self,requet,*args, **kwargs):
        form=self.form_class(requet.POST,instance=requet.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(self.request, self.template_name, {'form': form}) 