from django.urls import path 
from .views import * 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name = 'home'),
    path('home/', home, name = 'home'), 
    path('sign_up/', sign_up , name = 'sign_up'),
    path('profile/<str:username>', view_profile, name = 'view_profile'),
    path('Post', create_post, name='create_post'),
    path('search/<str:query>', search, name='search'),
    path('edit_profile/<str:username>', edit_profile, name= 'edit_profile'),    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

