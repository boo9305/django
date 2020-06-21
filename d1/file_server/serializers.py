from rest_framework import serializers
from .models import Post, Comment, PostTest
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password')

    def create(self, validated_data):
         user = User(username=validated_data['username'])
         user.set_password(validated_data['password'])
         user.save()
         return user


class PostTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTest
        fields = ( 'title', 'contents')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'contents')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'author', 'post', 'contents')
