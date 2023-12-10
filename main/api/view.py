from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Post
from .serializers import PostSerializers
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api', 
        'GET /api/profile', 
        'GET /api/profile/:username'
    ]
    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    
    posts = Post.objects.all()
    print(posts)
    serializers = PostSerializers(posts, many=True)
    print(serializers)
    return Response(serializers) 