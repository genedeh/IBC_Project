from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Book, BookList
from .serializer import BookSerializer, BookListSerializer


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookListViewSet(ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        booklist = get_object_or_404(Book, pk=pk)
        booklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)