from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save 
from django.urls import reverse
from django.db.models import Q
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(default = 'p.jpg', null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

class PostManager(models.Manager):
    
    def search(self, query):
        query = query.strip()
        lookups = Q(post_text__contains = query)
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
    
    class Meta:
        ordering  = ["-created_at"]
            
    def get_absolute_url(self):
        return reverse('view_profile', kwargs={'username':self.author.username})
    
    
    