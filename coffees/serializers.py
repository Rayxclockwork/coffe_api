from rest_framework import serializers
from .models import Post

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Post
