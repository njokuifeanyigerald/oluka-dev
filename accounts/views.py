from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import logout


from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    # def post(self,*args,**kwargs):
    #     # messages.info(self.request, "Logged in successfully!")
    #     return redirect("student:Home")

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    # messages.info(request, "Registered successfully!")
    success_url = reverse_lazy('login')

def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect("Home")

