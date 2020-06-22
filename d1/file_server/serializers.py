from rest_framework import serializers
from .models import Post, Comment
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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'author', 'post', 'contents')

class PostDetailSerializer(serializers.Serializer):
    comments = CommentSerializer(read_only=True, many=True)
    title = serializers.CharField(max_length=300)
    contents = serializers.CharField()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'contents')

   #def create(self, validated_data):
    #    print(self.context.get("request").user)
    #    post = Post(title=validated_data['title'])
   #     return post;
