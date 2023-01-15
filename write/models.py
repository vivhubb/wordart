from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     slug = models.SlugField(unique=True)
#     first_name = models.CharField(max_length=256)
#     last_name = models.CharField(max_length=256)
#     username = models.CharField(max_length=256, unique=True)
#     email = models.CharField(max_length=256, unique=True)
#     password = models.CharField(max_length=256)       #characters not hidden
#     birthday = models.DateTimeField()
#     date_joined = models.DateTimeField(auto_now_add=True)
#     admin = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['-date_joined']

#     def __str__(self):
#         return self.username


class Post(models.Model):

    class Categories(models.TextChoices):
        QUOTES = 'Q', 'Quotes'
        POEMS = 'P', 'Poems'

    category = models.CharField(max_length=256, choices=Categories.choices)
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='write_post')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='writepost_like', blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.content} by {self.author} on {self.created_date}"

    def number_of_comments(self):
        return self.content.count()
