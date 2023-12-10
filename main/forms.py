from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class CustomUserForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['avatar', 'username', 'email']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for field in ['avatar', 'username', 'email']:
            self.fields[field].help_text = "" 

        
    
class Register_form(CustomUserForm):
    
    class Meta:
        model = models.User
        fields = ['avatar', 'username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(Register_form, self).__init__(*args, **kwargs)
        # print(dir(self.fields))
        for field in ['username', 'email', 'password1', 'password2']:
            self.fields[field].help_text = "" 
                
    
class PostForm(forms.ModelForm):
    
    class Meta:
        
        model = models.Post
        fields = [
            'post_text'
            ]
        
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['post_text'].label = 'Post' 
        
    
        