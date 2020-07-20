from rest_framework import serializers
from .models import ExerciseUser, Exercise, ExerciseCard, ExerciseSet

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
class ExerciseUserSerializer(serializers.Serializer):
    user = UserSerializer()
    gender = serializers.CharField()
    age = serializers.IntegerField()

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['exercise_name']
    
class ExerciseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCard
        fields = ['user_id', 'exercise_id', 'create_at']
    
class ExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSet
        fields = ["exercise_card_id", 'exercise_number', 'exercise_weight', 'exercise_break_time']
        
    def create(self, validated_data):
        validated_data['set_number'] = ExerciseSet,objects.count()
        instance = super().create(validated_data)
    
    def to_representation(self, instsance):
        ret = super().to_representation(instance)
        ret['set_number'] = instance.set_number
        return ret
    