from rest_framework import serializers  # Importing serializers from Django REST framework
from .models import Post  # Importing the Post model from the current directory's models module

# Defining a serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # Specifying the model to serialize
        fields = ('id', 'author', 'title', 'body', 'created_at',)  # Fields to include in the serialized output