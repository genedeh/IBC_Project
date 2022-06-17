from django.contrib import admin
from .models import Book, BookListItem
# Register your models here.
admin.site.register(Book)
admin.site.register(BookListItem)