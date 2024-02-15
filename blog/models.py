from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


# Unsure if category is going to be utilized
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
        )
    link = models.URLField(blank=True, null=True)  # potential link for sharing
    content = models.TextField(blank=True)
    posted_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='posts'
        )
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
