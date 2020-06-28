from . import views
from rest_framework import routers
from django.urls import path

urlpatterns = [
    
]

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'post', views.PostViewSet, basename='post')
router.register(r'comment', views.CommentViewSet)
urlpatterns += router.urls
