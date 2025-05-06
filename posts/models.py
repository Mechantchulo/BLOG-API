from django.db import models
# Importing the models module from Django to define database models.

from django.contrib.auth.models import User
# Importing the built-in User model from Django's authentication system.

class Post(models.Model):
    # Defining a Post model that inherits from Django's base Model class.

    # A foreign key relationship to the User model. If the user is deleted, all their posts will also be deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # A character field to store the title of the post, with a maximum length of 100 characters.
    title = models.CharField(max_length=100)

    # A text field to store the body/content of the post. (Note: There is a typo here; it should be `TextField`.)
    body = models.TextField()

    # A datetime field that automatically sets the current timestamp when a post is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A datetime field that automatically updates the timestamp whenever the post is modified.
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        # A string representation of the Post object, returning its title.
        return self.title