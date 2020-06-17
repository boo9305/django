from django.db import models

# Create your models here.


class UpLoadFile(models.Model):
    title = models.TextField(default="")
    file = models.FileField(null=True)

    
