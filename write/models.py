from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Post(models.Model):

    class Categories(models.TextChoices):
        QUOTES = 'Q', 'Quotes'
        POEMS = 'P', 'Poems'

    OWNER = ((0, "My own WordArt"), (1, "Not my WordArt"), (2, ""))

    category = models.CharField(max_length=256, choices=Categories.choices)
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='write_post')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    ownership = models.IntegerField(choices=OWNER, default=2)
    creator = models.CharField(
        max_length=256, default="Original Author's name")
    likes = models.ManyToManyField(
        User, related_name='writepost_like', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', default='')
    name = models.CharField(max_length=256, default='name')
    email = models.EmailField(default='email address')
    comment = models.TextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    author_id = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.comment} by {self.name} on {self.created_date}"


class AddWordArt(ModelForm):
    class Meta:
        model = Post
        fields = [
            'category', 'title', 'author', 'content', 'ownership', 'creator']
