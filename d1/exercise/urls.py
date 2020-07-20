from . import views
from rest_framework import routers
from django.urls import path

urlpatterns = [

]

router = routers.DefaultRouter()
# router.register('user', views.UserViewSet)
router.register('user', views.ExerciseUserViewSet)
router.register('ex', views.ExerciseViewSet)
router.register('ex_set', views.ExerciseSetViewSet)
router.register('ex_card', views.ExerciseCardViewSet)
urlpatterns += router.urls