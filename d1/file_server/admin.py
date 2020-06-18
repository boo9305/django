from django.contrib import admin
from .models import UpLoadFile
from .models import  Post, Comment
# Register your models here.
admin.site.register(UpLoadFile)
admin.site.register(Post)
admin.site.register(Comment)