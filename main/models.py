from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save 
from django.urls import reverse
from django.db.models import Q
# Create your models here.

class PostManager(models.Manager):
    
    def search(self, query):
        query = query.strip()
        lookups = Q(post_text__contains = query)
        # posts = Post.objects.filter(lookups) 
        posts = self.get_queryset().filter(lookups)
        return posts
    
    def get_first(self, number):
        
        return Post.objects.all()[:min(Post.objects.all().count(), number)] 
    

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.TextField(max_length=200, unique_for_date='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    objects = PostManager()
    def __str__(self):
        return self.post_text
    
    def is_liked(self):
        return author in likes 
    class Meta:
        ordering  = ["-created_at"]
            
    def get_absolute_url(self):
        return reverse('view_profile:details', kwargs={'username':self.author.username})