from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Book, BookList, BookListItem
from .serializer import BookSerializer, BookListSerializer, BookListItemSerializer


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
    permission_classes = []

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        booklist = get_object_or_404(BookList, pk=pk)
        booklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookListItemViewSet(ModelViewSet):
    queryset = BookListItem.objects.all()
    serializer_class = BookListItemSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        booklistitem = get_object_or_404(BookListItem, pk=pk)
        booklistitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
