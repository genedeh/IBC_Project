from rest_framework import routers
from . import views

# URLConf
router = routers.DefaultRouter()
router.register('books', views.BookViewSet, basename='book')
router.register('booklists', views.BookListViewSet, basename='booklist')
router.register('booklistitems', views.BookListItemViewSet, basename='booklistitem')
urlpatterns = router.urls
