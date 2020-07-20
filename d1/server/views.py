from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import UserSerializer
from .serializers import CommentSerializer ,CommentCreateSerializer
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer

# post viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        elif self.action == 'create':
            return PostCreateSerializer

        return PostListSerializer 

    def get_queryset(self):    
        return Post.objects.all()
    
    def retrieve(self, request, pk=None):
        post = self.get_object()
        post.increase_hit()
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def perform_create(self,serializer):
        print("k")
        serializer.save(author=self.request.user)
        

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_serializer_class(self):
        if self.action == "create" :
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self,serializer):
        print("k")
        serializer.save(author=self.request.user)
