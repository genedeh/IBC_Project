from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializer import BookSerializer
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_context(self):
        return {"request": self.request}