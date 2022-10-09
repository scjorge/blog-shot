from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    bio = models.TextField()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
