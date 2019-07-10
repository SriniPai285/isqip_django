from django.db import models
from django.conf import settings


# Create your models here.

class TimeStampMode(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Category(TimeStampMode):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Post(TimeStampMode):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name="posts")

    def __str__(self):
        return self.title