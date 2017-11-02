from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    email = models.EmailField()
    text = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)
    send_status = models.TextField(default='ok')

    def __str__(self):
        return self.email
