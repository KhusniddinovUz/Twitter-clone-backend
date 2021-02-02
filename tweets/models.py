from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Tweet Model
class TweetModel(models.Model):
    text = models.TextField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    username = models.CharField(max_length=100, blank=True)
