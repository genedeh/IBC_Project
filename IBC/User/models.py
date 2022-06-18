from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    RANK_BOOK_WORM = 'BW'
    RANK_GOLD_BOOK_WORM = 'GBW'
    RANK_PLATINUM_BOOK_WORM = 'PBW'
    RANK_LIST = [
        (RANK_BOOK_WORM, 'Bookworm'),
        (RANK_GOLD_BOOK_WORM, 'Gold Bookworm'),
        (RANK_PLATINUM_BOOK_WORM, 'Platinum Bookworm')
    ]
    email = models.EmailField(unique=True)
    is_writer = models.BooleanField(default=False)
    rank = models.CharField(max_length=3, choices=RANK_LIST, default=RANK_BOOK_WORM)
    bio = models.TextField(max_length=500, help_text="MAX LENGTH OF 500", default="NO BIO")

    def __str__(self):
        return self.username
