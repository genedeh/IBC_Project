from rest_framework import routers
from . import views

# URLConf
router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='user')
urlpatterns = router.urls
