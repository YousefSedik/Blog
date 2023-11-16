from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
# Create your views here.

# @login_required(login_url='/login')
def home(re):
    return render(re, 'main/home.html' ) 


def sign_up(re):
    if re.method == 'POST':
        form = forms.Register_form(re.POST) 
        if form.is_valid():
            user = form.save() 
            login(re, user)
            return redirect('/home')

    else:
        form = forms.Register_form() 
    form = forms.Register_form()
        
    return render(re, 'registration/sign_up.html', {'form':form})


