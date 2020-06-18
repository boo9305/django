from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)
urlpatterns = router.urls
