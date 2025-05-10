from django.urls import path  # Import the `path` function from Django's URL module to define URL patterns.
from .views import UserViewSet, PostViewSet  # Import the views `PostList` and `PostDetail` from the current app's views module.
from rest_framework.routers import SimpleRouter  # Import the `router` from Django REST framework to create a router for viewsets.

""" urlpatterns = [  # Define a list of URL patterns for the application.
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),  # Map a URL with an integer parameter `pk` to the `UserDetail` view
    path('posts/', PostList.as_view()),  # Map the URL 'posts/' to the `PostList` view.
    path('<int:pk>/', PostDetail.as_view()),  # Map a URL with an integer parameter `pk` to the `PostDetail` view
    path('', PostList.as_view()),  # Map the root URL of the app to the `PostList` view.
]
 """
 
 #let's use routers to create the urls with minimal code
 
router = SimpleRouter()
router.register('users', UserViewSet, basename = 'users')
router.register('posts', PostViewSet, basename = 'posts')
urlpatterns = router.urls
 