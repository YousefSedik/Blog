from rest_framework.serializers import ModelSerializer
from main.models import Post

class PostSerializers(ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'post_text', 'created_at', 'author', 'other_field']  # Add all relevant fields
