from django.db import models
from django.utils import timezone


class post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    songname = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.songname
