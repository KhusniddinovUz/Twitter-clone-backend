from django.db import models
from accounts.models import Accounts
from django.conf import settings


# Tweet Model
class TweetModel(models.Model):
    text = models.TextField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    username = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.username}: {self.text[0:15]}'


# Comment Model
class Comment(models.Model):
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE, related_name='comment')
    username = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Accounts, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ('created', 'username')

    def __str__(self):
        return f'{self.username}: {self.body[0:15]}'
