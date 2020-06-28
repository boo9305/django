from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name;

    def __unicode__(self):
        return "%s" % self.name;

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)
    contents = models.TextField()

    hit = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    def increase_hit(self):
        self.hit = self.hit + 1

    class Meta:
        unique_together = ['author', 'board']
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    contents = models.TextField(max_length=300)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.contents
    
