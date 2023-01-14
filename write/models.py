from django.db import models


class User(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256, unique=True)
    email = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    birthday = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True)
    admin = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return self.username


class Post(models.Model):

    class Categories(models.TextChoices):
        QUOTES = 'Q', 'Quotes'
        POEMS = 'P', 'Poems'

    category = models.CharField(max_length=256, choices=Categories.choices)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='write_post')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='writepost_like', blank=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.content} by {self.author}"

    def number_of_comments(self):
        return self.content.count()
