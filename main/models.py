from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    created_at_time = models.TimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    updated_at_time = models.TimeField(auto_now=True)
    def __str__(self):
        return self.title +'\n' + self.description
    
    
    class Meta:
        ordering  = ["-created_at", '-created_at_time']
    
        
    