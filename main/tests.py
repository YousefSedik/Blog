from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User 

from django.contrib.auth import get_user_model 
User = get_user_model()
