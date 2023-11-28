from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save 
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    def __str__(self):
        return self.title +'\n' + self.description
    
    
    class Meta:
        ordering  = ["-created_at"]
    
    
def pre_save_(*args, **kwargs):
    print("pre save:",args, kwargs)
        
def post_save_(*args, **kwargs):
    print("post save:",args, kwargs)
        
        
pre_save.connect(pre_save_, sender=Post)
post_save.connect(post_save_, sender=Post)

