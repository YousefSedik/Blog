from django.urls import path 
from .views import * 

urlpatterns = [
    path('', home, name = 'home'),
    path('home/', home, name = 'home'), 
    path('sign_up/', sign_up , name = 'sign_up'),
    path('profile/<str:username>', view_profile, name = 'view_profile'),
    path('Post', create_post, name='create_post'),
    path('search/<str:query>', search, name='search'),
    path('like/<int:post_id>', add_like, name= 'like')
]

