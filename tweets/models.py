from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Tweet Model
class TweetModel(models.Model):
    text = models.TextField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    username = models.CharField(max_length=100, blank=True)


class Comment(models.Model):
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE, related_name='comment')
    username = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created', 'username')

    def __str__(self):
        return f'Comment by {self.username} to {self.tweet.owner}'
