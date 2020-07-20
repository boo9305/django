from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import ExerciseUser, Exercise, ExerciseCard, ExerciseSet

from .serializers import ExerciseUserSerializer, UserSerializer, ExerciseSerializer, ExerciseCardSerializer, ExerciseSetSerializer

from .models import ExerciseUser

from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExerciseUserViewSet(viewsets.ModelViewSet):
    queryset = ExerciseUser.objects.all()
    serializer_class = ExerciseUserSerializer
    
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    
class ExerciseCardViewSet(viewsets.ModelViewSet):
    queryset = ExerciseCard.objects.all()
    serializer_class = ExerciseCardSerializer
    

class ExerciseSetViewSet(viewsets.ModelViewSet):
    queryset = ExerciseSet.objects.all()
    serializer_class = ExerciseSetSerializer
    
