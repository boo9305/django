from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UpLoadFile(models.Model):
    title = models.TextField(default="")
    file = models.FileField(null=True)

    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)
    contents = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    contents = models.TextField(max_length=300)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
