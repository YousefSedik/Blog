from django.urls import path
from . import view
urlpatterns = [
    path('', view.getRoutes), 
    path('po/', view.getPosts), 
]