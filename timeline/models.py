from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    songname = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author_ipaddress = models.TextField()
    author_city = models.TextField()

    def __str__(self):
        return self.songname
