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
    content = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        related_name='posts'
    )
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField()
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_at', 'author']

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class PostLike(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='post_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user} likes {self.post}'

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_comments')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('comment', 'user')

    def __str__(self):
        return f'{self.user.username} likes "{self.comment.content}"'