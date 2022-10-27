from django.db import models
from apps.user.models import UserProfile


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(Base):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title()


class Category(Base):
    title = models.CharField(max_length=100)
    post = models.ManyToManyField(to="Post", related_name="category")
