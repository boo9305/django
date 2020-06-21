from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User
from .models import Post, Comment, PostTest
from .serializers import UserSerializer, PostSerializer, CommentSerializer,PostTestSerializer

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


# post viewsets
class PostTestViewSet(viewsets.ModelViewSet):
    queryset = PostTest.objects.all()
    serializer_class = PostTestSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
  
# post viewsets
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
