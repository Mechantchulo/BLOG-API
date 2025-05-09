from django.test import TestCase
from django.contrib.auth.models import User

# Import the Post model from the current app
from .models import Post

# Define a test case class for the blog
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        
        # Create a test blog post associated with the test user
        test_post = Post.objects.create(
            author=testuser1, title='Blog title', body='Body content...')
        test_post.save()
        
    # Define a test method to check the content of the blog post
    def test_blog_content(self):
        # Retrieve the blog post with ID 1
        post = Post.objects.get(id=1)
        
        # Get the string representation of the author, title, and body
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        
        # Assert that the author, title, and body match the expected values
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')