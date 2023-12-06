from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
class Register_form(UserCreationForm):
    
    email = forms.EmailField(required=True)
    # username = forms.CharField(widget=forms.TextInput(attrs={''}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
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
        
    
        