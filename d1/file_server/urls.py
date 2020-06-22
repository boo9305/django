from . import views
from rest_framework import routers
from django.urls import path

urlpatterns = [
    path(r'postlist/', views.PostListView.as_view(), name='post-list'),
]

router = routers.DefaultRouter()
# router.register(r'user', views.UserViewSet)
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)
urlpatterns += router.urls
