from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

# class User(AbstractUser):
#     age = models.IntegerField()

class ExerciseUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=(('M','male'), ('F','female')), default = 'male')

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)
    def __str__(self):
        return '%s' % self.exercise_name
class ExerciseCard(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.user_id, self.exercise_id)


class ExerciseSet(models.Model):
    exercise_card_id = models.ForeignKey(ExerciseCard, on_delete=models.CASCADE)
    set_number = models.IntegerField()
    exercise_number = models.IntegerField()
    exercise_weight = models.IntegerField()
    exercise_break_time = models.IntegerField()