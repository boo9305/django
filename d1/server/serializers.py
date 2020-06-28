from rest_framework import serializers
from .models import Post, Comment, Board
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password')
        
###### Board Serializer
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('pk', 'name')
        
###### Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'author', 'post', 'contents')

###### Post Serializer
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'author', 'board', 'title', 'contents')

class PostCreateSerializer(serializers.ModelSerializer):
    #board = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ('pk', 'board', 'title', 'contents')

class PostDetailSerializer(serializers.ModelSerializer):
    #board = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('pk', 'author', 'board', 'hit', 'title', 'contents' , 'comments')
        
