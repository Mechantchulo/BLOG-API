from django.urls import path  # Import the `path` function from Django's URL module to define URL patterns.
from .views import PostList, PostDetail  # Import the views `PostList` and `PostDetail` from the current app's views module.

urlpatterns = [  # Define a list of URL patterns for the application.
    path('<int:pk>/', PostDetail.as_view()),  # Map a URL with an integer parameter `pk` to the `PostDetail` view
    path('', PostList.as_view()),  # Map the root URL of the app to the `PostList` view.
]
