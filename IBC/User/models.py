from django.db import models


# Create your models here.
class User(models.Model):
    RANK_BOOK_WORM = 'BW'
    RANK_GOLD_BOOK_WORM = 'GBW'
    RANK_PLATINUM_BOOK_WORM = 'PBW'
    RANK_LIST = [
        (RANK_BOOK_WORM, 'Bookworm'),
        (RANK_GOLD_BOOK_WORM, 'Gold Bookworm'),
        (RANK_PLATINUM_BOOK_WORM, 'Platinum Bookworm')
    ]
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=8, unique=True)
    email = models.EmailField(unique=True)
    is_writer = models.BooleanField()
    rank = models.CharField(max_length=3, choices=RANK_LIST)
    bio = models.TextField(max_length=500, help_text="MAX LENGTH OF 500")

    def __str__(self):
        return self.username
