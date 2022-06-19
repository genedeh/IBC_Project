from rest_framework import routers
from . import views


# URLConf
router = routers.DefaultRouter()
router.register('books', views.BookViewSet, basename='book')
urlpatterns = router.urls