from django.core.validators import MinValueValidator
from django.db import models
from User.models import User


# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    story = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    likes = models.IntegerField()

    def __str__(self):
        return self.title
