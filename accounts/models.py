from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    email_verified = models.BooleanField(default=False, blank=False)
