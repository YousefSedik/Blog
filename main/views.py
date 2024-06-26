from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.views.defaults import page_not_found
import datetime
from dateutil.relativedelta import relativedelta
# Create your views here.


def delete_post(post_id):
    post = models.Post.objects.filter(id=post_id).first()
    post.delete()
     
     

def search(request, query):
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        if post_id:
            delete_post(post_id)

    if query is None:
        query = ''
        
        
    
    posts = models.Post.objects.search(query) 
    return render(request,'main/search.html', {'posts':posts}) 

def home(re):
    
    if re.method == 'POST': 
        post_id = re.POST.get('post-id')
        user_id = re.POST.get('user-id')
        query = re.POST.get('search_panel')
        
        print(post_id, user_id)
        if post_id:
            post = models.Post.objects.get(id=post_id)
            if (post.author == re.user or re.user.has_perm('main.delete_post')):
                delete_post(post_id) 
                
        elif user_id:
            user = User.objects.get(id=user_id)
            if re.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user) 
                    
                except:
                    pass
                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                    
                except:
                    pass
        
        elif query:
            return redirect(f"/search/{query}")
            
        
    all_posts = models.Post.objects.get_first(5)
    
    month_number = {'1':'Jan', '2':'Feb', '3':'Mar', '4':'Apr', 
                    '5':'May', '6':'Jun', '7':'Jul', '8':'Aug', '9':'Sep'
                    , '10':'Oct', '11':'Nov', '12': 'Dec'}

    for post in all_posts:
        post.created_at = f"{month_number[str(post.created_at.month)]} {post.created_at.day}, {post.created_at.year} |\
        {str(post.created_at.hour%12 +1).zfill(2)}:{str(post.created_at.minute).zfill(2)} "
        
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
@permission_required('main.add_post', login_url='/login', raise_exception=True)
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
    if re.method == 'POST':
        delete_post(re)
    context['username'] = username
    try:
        profile = models.User.objects.get(username=username)
        context['profile'] = profile
        profile_posts = models.Post.objects.filter(author=profile)
        context['posts'] = profile_posts
        
    except:
        return render(re, '404.html')
    
    return render(re, 'main/view_profile.html', context)

def edit_profile(request, username):
    if request.user.username == username:
        if request.method == 'GET':
            form = forms.CustomUserForm(instance = request.user) 
            return render(request, 'main/edit_profile.html', {'form':form})
        form = forms.CustomUserForm(request.POST or None, request.FILES, instance=request.user)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('/home/')
        return render(request, 'main/edit_profile.html', {'form':form})
    else:
        return redirect('/home/')
    
