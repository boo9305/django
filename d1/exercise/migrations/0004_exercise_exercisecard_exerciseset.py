# Generated by Django 3.0.8 on 2020-07-20 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercise', '0003_auto_20200720_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.Exercise')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.IntegerField()),
                ('exercise_number', models.IntegerField()),
                ('exercise_weight', models.IntegerField()),
                ('exercise_break_time', models.IntegerField()),
                ('exercise_card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.ExerciseCard')),
            ],
        ),
    ]
