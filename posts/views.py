from django.contrib.auth import get_user_model  # Import the function to get the user model.
from django.shortcuts import render  # Import the render function from Django's shortcuts module (not used in this code).
from rest_framework import generics,permissions, viewsets # Import generic views from Django REST framework.
from .models import Post  # Import the Post model from the current app's models.
from .serializers import PostSerializer, UserSerializer  # Import the PostSerializer from the current app's serializers.
from .permissions import IsAuthorOrReadOnly

# Create your views here.

""" class PostList(generics.ListCreateAPIView):  # Define a view for listing and creating Post objects.
    '''permission_classes = (permissions.IsAuthenticated,)'''#this is a view-level permission
    queryset = Post.objects.all()  # Specify the queryset to retrieve all Post objects from the database.
    serializer_class = PostSerializer  # Specify the serializer class to handle serialization and deserialization.

class PostDetail(generics.RetrieveUpdateDestroyAPIView):  # Define a view for retrieving, updating, and deleting a single Post object.
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()  # Specify the queryset to retrieve all Post objects from the database.
    serializer_class = PostSerializer  # Specify the serializer class to handle serialization and deserialization.


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer """
    
    
#Let's use viewsets to create the views with minimal code

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer