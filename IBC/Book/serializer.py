from rest_framework import serializers
from User.models import User
from .models import Book, BookList, BookListItem


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'slug', 'author', 'story', 'price', 'likes']


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = ['id', 'name', 'books', 'user']
