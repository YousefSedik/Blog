from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.views.defaults import page_not_found
# Create your views here.

# @login_required(login_url='/login')
def home(re):
    if re.method == 'POST':
        post_id = re.POST.get('post-id')
        post = models.Post.objects.filter(id=post_id).first()
        if post and post.author == re.user:
            post.delete()
            
    all_posts = models.Post.objects.all() 
    return render(re, 'main/home.html', {'posts': all_posts} )


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

@login_required(login_url='login/')
def create_post(re):
    if re.method == 'POST':
        form = forms.PostForm(re.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = re.user 
            post.save()
        return redirect('/home')
    else:
        
        form = forms.PostForm()
        return render(re, 'main/create_post.html', context = {'form': form})
    
    
def view_profile(re, username):
    context = {}
    
    try:
        profile = User.objects.get(username=username)
        context['profile'] = profile
        
    except:
        return render(re, '404.html')
    
    return render(re, 'main/view_profile.html', context)

