from .models import Post, Comment
from django import forms
from django.forms import ModelForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class WordArtForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'category', 'title', 'content', 'ownership', 'creator')
