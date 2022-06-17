from django.contrib import admin
from .models import Book, BookListItem, BookList
# Register your models here.
admin.site.register(Book)
admin.site.register(BookList)
admin.site.register(BookListItem)
