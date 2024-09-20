from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() # Retrieve the auth_user model being used by django

# Post model allowing users to create posts
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') 

# comment model for users to add comment to post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
