from rest_framework import serializers  # Importing serializers from Django REST framework
from .models import Post  # Importing the Post model from the current directory's models module
from django.contrib.auth import get_user_model  # Importing the function to get the user model
# Defining a serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # Specifying the model to serialize
        fields = ('id', 'author', 'title', 'body', 'created_at',)  # Fields to include in the serialized output
        

# Defining a serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Getting the user model
        fields = ('id', 'username','email',) # fields to be included in the serialized output
    