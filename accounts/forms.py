from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'id':"exampleInputEmail",
        'class':"form-control form-control-user", 
        'placeholder':"Enter Email Address..."
    }))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'id':"username",
        'class':"form-control form-control-user", 
        'placeholder':"Enter Username"
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'id':"exampleInputPassword",
        'class':"form-control form-control-user", 
        'placeholder':"Enter Password"
    }))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={
        'id':"exampleInputPassword2",
        'class':"form-control form-control-user", 
        'placeholder':"Repeat Password"
    }))
    class Meta:
        model = get_user_model()
        fields = ('email','username', 'password1', 'password2')
        # fields = ('email','password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'id':"exampleInputEmail",
        'class':"form-control form-control-user", 
        'placeholder':"Enter Email Address..."
    }))
